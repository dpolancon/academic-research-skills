#!/usr/bin/env python3
"""Cross-Model API Client for ARS.

Decouples the inline shell/curl commands inside agent prompts into first-class
Python wrappers. Supports factual reference verification with bibliographic index
search tools, and devil's advocate critiques.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any

# Adjust path so we can resolve sister modules in scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent))

from llm_gateway import LLMGateway

# Import bibliographic clients from scripts/ folder
try:
    from crossref_client import CrossrefClient, CrossrefUnavailable
except ImportError:
    CrossrefClient, CrossrefUnavailable = None, None

try:
    from openalex_client import OpenAlexClient, OpenAlexUnavailable
except ImportError:
    OpenAlexClient, OpenAlexUnavailable = None, None

try:
    from arxiv_client import ArxivClient, ArxivUnavailable
except ImportError:
    ArxivClient, ArxivUnavailable = None, None

try:
    from semantic_scholar_client import SemanticScholarClient
except ImportError:
    SemanticScholarClient = None


# Define the verification search tool schema (OpenAI format)
VERIFICATION_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_bibliographic_indexes",
            "description": "Searches online bibliographic indexes (Crossref, OpenAlex, Semantic Scholar, arXiv) for a given paper citation or title query. Returns matching metadata if found.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The paper title, author, year, or citation string to search for."
                    }
                },
                "required": ["query"]
            }
        }
    }
]


def search_bibliographic_indexes(query: str) -> str:
    """Executes programmatic searches across all available local API clients."""
    print(f"[*] Executing search for: {query!r}...")
    results = {}

    # 1. Semantic Scholar Search
    if SemanticScholarClient:
        try:
            client = SemanticScholarClient()
            # _lookup_by_title matches title-search semantics
            s2_res = client._lookup_by_title(query, None)
            if s2_res:
                results["semantic_scholar"] = {
                    "title": s2_res.get("title"),
                    "year": s2_res.get("year"),
                    "authors": [a.get("name") for a in s2_res.get("authors", [])],
                    "doi": s2_res.get("externalIds", {}).get("DOI"),
                    "url": s2_res.get("url")
                }
        except Exception as e:
            results["semantic_scholar"] = f"Unavailable: {e}"
    
    # 2. Crossref Search
    if CrossrefClient:
        try:
            client = CrossrefClient()
            cr_res = client.title_search(query)
            if cr_res:
                results["crossref"] = cr_res
        except Exception as e:
            results["crossref"] = f"Unavailable: {e}"

    # 3. OpenAlex Search
    if OpenAlexClient:
        try:
            client = OpenAlexClient()
            oa_res = client.title_search(query)
            if oa_res:
                results["openalex"] = oa_res
        except Exception as e:
            results["openalex"] = f"Unavailable: {e}"

    # 4. arXiv Search
    if ArxivClient:
        try:
            client = ArxivClient()
            ax_res = client.title_search(query)
            if ax_res:
                results["arxiv"] = ax_res
        except Exception as e:
            results["arxiv"] = f"Unavailable: {e}"

    # Format output for LLM consumption
    return json.dumps(results, indent=2, ensure_ascii=False)


def run_reference_verification(
    reference: str,
    context: str,
    override_provider: str = None,
    override_model: str = None
) -> Dict[str, Any]:
    """Runs verification on a single reference using LLM-as-a-judge and search tools."""
    gateway = LLMGateway()

    system_prompt = (
        "You are an academic citation-verification assistant. Your task is to verify if the provided reference "
        "exists and matches its details. You MUST search the bibliographic indexes using the "
        "`search_bibliographic_indexes` tool before declaring a final verdict. DO NOT answer from memory.\n\n"
        "You must respond with exactly one of these verdicts, followed by a one-sentence rationale:\n"
        "- VERIFIED  — found online and metadata matches\n"
        "- MISMATCH  — found, but fields (author, year, title, journal, etc.) are wrong\n"
        "- NOT_FOUND — searched, but no matching record exists\n"
        "- NOT_SEARCHED — you could not search for the reference\n\n"
        "If you conclude VERIFIED, you MUST list the URL or DOI of the paper you found in the search results."
    )

    user_prompt = f"Reference: {reference}\nContext: {context}"

    # Multi-turn conversation messages list
    messages = [{"role": "user", "content": user_prompt}]

    # Step 1: Request initial model completion with tools
    print("[*] Requesting verification from gateway model...")
    response = gateway.chat(
        agent_name="integrity_verification_agent",
        system_prompt=system_prompt,
        messages=messages,
        tools=VERIFICATION_TOOLS,
        override_provider=override_provider,
        override_model=override_model
    )

    # Step 2: Tool execution loop
    if response.get("tool_calls"):
        tool_calls = response["tool_calls"]
        # Add assistant's message to messages history
        messages.append({
            "role": "assistant",
            "content": response.get("content"),
            "tool_calls": tool_calls
        })

        for tc in tool_calls:
            if tc["name"] == "search_bibliographic_indexes":
                args = tc["arguments"]
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except Exception:
                        args = {"query": query}
                
                query = args.get("query", reference)
                
                # Execute Python search
                search_data = search_bibliographic_indexes(query)
                
                # Append tool result to history
                messages.append({
                    "role": "tool",
                    "name": "search_bibliographic_indexes",
                    "tool_call_id": tc.get("id"),
                    "content": search_data
                })

        # Request final model decision with tool results in context
        print("[*] Submitting search results to model for final verdict...")
        response = gateway.chat(
            agent_name="integrity_verification_agent",
            system_prompt=system_prompt,
            messages=messages,
            tools=None, # Disable tool calls in final turn
            override_provider=override_provider,
            override_model=override_model
        )

    return response


def run_devil_advocate_critique(
    material: str,
    override_provider: str = None,
    override_model: str = None
) -> str:
    """Generates an independent devil's advocate critique on the research/paper draft."""
    gateway = LLMGateway()

    system_prompt = (
        "You are a devil's advocate reviewing this research draft or outline. "
        "Find the 3 most serious weaknesses. For each weakness, state:\n"
        "1. What the weakness is\n"
        "2. Why it matters\n"
        "3. What the strongest counter-argument would be"
    )

    print("[*] Generating Devil's Advocate critique...")
    response = gateway.generate(
        agent_name="devils_advocate",
        system_prompt=system_prompt,
        user_prompt=material,
        override_provider=override_provider,
        override_model=override_model
    )
    return response.get("content", "No critique generated.")


def main():
    parser = argparse.ArgumentParser(description="ARS Cross-Model API Client.")
    subparsers = parser.add_subparsers(dest="command", help="API commands")

    # verify subparser
    verify_parser = subparsers.add_parser("verify", help="Verify academic citation")
    verify_parser.add_argument("--reference", required=True, help="Full reference text")
    verify_parser.add_argument("--context", required=True, help="The sentence context where it is cited")
    verify_parser.add_argument("--override-provider", help="API provider to use")
    verify_parser.add_argument("--override-model", help="API model ID to use")

    # critique subparser
    critique_parser = subparsers.add_parser("critique", help="Run devil's advocate critique")
    critique_parser.add_argument("--material", required=True, help="The draft text or outline to critique")
    critique_parser.add_argument("--override-provider", help="API provider to use")
    critique_parser.add_argument("--override-model", help="API model ID to use")

    args = parser.parse_args()

    if args.command == "verify":
        try:
            res = run_reference_verification(
                reference=args.reference,
                context=args.context,
                override_provider=args.override_provider,
                override_model=args.override_model
            )
            print("\n=== VERIFICATION RESULT ===")
            print(res.get("content"))
        except Exception as e:
            print(f"Error executing verification: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "critique":
        try:
            res = run_devil_advocate_critique(
                material=args.material,
                override_provider=args.override_provider,
                override_model=args.override_model
            )
            print("\n=== DEVIL'S ADVOCATE CRITIQUE ===")
            print(res)
        except Exception as e:
            print(f"Error executing critique: {e}", file=sys.stderr)
            sys.exit(1)
            
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
