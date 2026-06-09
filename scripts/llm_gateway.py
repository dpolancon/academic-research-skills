#!/usr/bin/env python3
"""Unified LLM Gateway for ARS.

Supports Together AI (OpenAI-compatible) and Google Gemini APIs,
including structured function/tool calling and multi-turn chat.
"""

from __future__ import annotations

import os
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Any, Union

# Ensure dependencies are available
try:
    from openai import OpenAI
except ImportError:
    print("Warning: 'openai' package not found. Run 'pip install openai' to enable Together AI support.", file=sys.stderr)
    OpenAI = None

try:
    import google.generativeai as genai
except ImportError:
    print("Warning: 'google-generativeai' package not found. Run 'pip install google-generativeai' to enable Google Gemini support.", file=sys.stderr)
    genai = None


class LLMGateway:
    """Gateway for routing agent queries to Qwen (Together AI) and Gemini."""

    def __init__(
        self,
        config_path: Union[str, Path] = None,
        default_model: str = None,
        default_provider: str = None,
        base_url: str = None
    ):
        if config_path is None:
            # Look in repository root
            config_path = Path(__file__).resolve().parent.parent / "agent_config.yaml"
        
        self.config_path = Path(config_path)
        self.config = {}
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = yaml.safe_load(f) or {}

        # Resolve priority order:
        # 1. Constructor arguments (highest priority, from CLI/Env resolved in runner)
        # 2. Config file settings (agent_config.yaml global settings)
        # 3. Environment variables (DEFAULT_MODEL, DEFAULT_PROVIDER)
        # 4. Hardcoded defaults (lowest priority)
        
        self.default_provider = (
            default_provider or 
            self.config.get("global_settings", {}).get("default_provider") or
            os.getenv("DEFAULT_PROVIDER") or
            "together"
        )
        
        self.default_model = (
            default_model or 
            self.config.get("global_settings", {}).get("default_model") or
            os.getenv("DEFAULT_MODEL") or
            "Qwen/Qwen3.5-9B"
        )
        
        self.base_url = (
            base_url or 
            self.config.get("providers", {}).get("together", {}).get("base_url") or
            "https://api.together.ai/v1"
        )
        
        self.together_client = None
        self._init_clients()

    def _init_clients(self):
        """Initializes API clients based on environment keys and configs."""
        providers = self.config.get("providers", {})
        
        # Initialize Together AI Client (via OpenAI-compatible endpoint)
        together_cfg = providers.get("together", {})
        together_api_key = os.getenv(together_cfg.get("api_key_env", "TOGETHER_API_KEY"))
        
        # Fallback check for docs file if key is missing from env
        if not together_api_key:
            doc_path = Path(__file__).resolve().parent.parent / "docs" / "together_AI_baseURL_APIKEY.txt"
            if doc_path.exists():
                try:
                    with open(doc_path, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            # Parse KEY=VALUE format
                            if line and not line.startswith("#") and "=" in line:
                                key, value = line.split("=", 1)
                                key = key.strip()
                                value = value.strip()
                                if key == "TOGETHER_API_KEY":
                                    together_api_key = value
                                elif key == "TOGETHER_BASE_URL" and not self.base_url:
                                    self.base_url = value
                except Exception:
                    pass

        if together_api_key and OpenAI:
            self.together_client = OpenAI(api_key=together_api_key, base_url=self.base_url)

        # Initialize Google Gemini SDK Client
        gemini_cfg = providers.get("gemini", {})
        gemini_api_key = os.getenv(gemini_cfg.get("api_key_env", "GEMINI_API_KEY"))
        if gemini_api_key and genai:
            genai.configure(api_key=gemini_api_key)

    def generate(
        self,
        agent_name: str,
        system_prompt: str,
        user_prompt: str,
        tools: List[Dict[str, Any]] = None,
        override_provider: str = None,
        override_model: str = None
    ) -> Dict[str, Any]:
        """Runs a single-turn generation query."""
        messages = [{"role": "user", "content": user_prompt}]
        return self.chat(
            agent_name=agent_name,
            system_prompt=system_prompt,
            messages=messages,
            tools=tools,
            override_provider=override_provider,
            override_model=override_model
        )

    def chat(
        self,
        agent_name: str,
        system_prompt: str,
        messages: List[Dict[str, Any]],
        tools: List[Dict[str, Any]] = None,
        override_provider: str = None,
        override_model: str = None
    ) -> Dict[str, Any]:
        """Runs a multi-turn chat generation query."""
        provider = override_provider or self.default_provider
        model = override_model or self.default_model

        if provider == "together":
            if not self.together_client:
                raise RuntimeError("Together AI Client not initialized. Check TOGETHER_API_KEY or docs file.")
            
            # Map system prompt into messages if not already present
            formatted_messages = []
            if system_prompt:
                formatted_messages.append({"role": "system", "content": system_prompt})
            
            for msg in messages:
                role = msg["role"]
                content = msg.get("content")
                formatted_msg = {"role": role, "content": content}
                
                if role == "assistant" and "tool_calls" in msg:
                    formatted_msg["tool_calls"] = []
                    for tc in msg["tool_calls"]:
                        formatted_msg["tool_calls"].append({
                            "id": tc.get("id"),
                            "type": "function",
                            "function": {
                                "name": tc["name"],
                                "arguments": tc["arguments"]
                            }
                        })
                if role == "tool":
                    formatted_msg["tool_call_id"] = msg.get("tool_call_id")
                    
                formatted_messages.append(formatted_msg)

            openai_tools = tools if tools else None
            response = self.together_client.chat.completions.create(
                model=model,
                messages=formatted_messages,
                tools=openai_tools,
                temperature=0.1
            )
            message = response.choices[0].message
            
            tool_calls = []
            if message.tool_calls:
                for tc in message.tool_calls:
                    tool_calls.append({
                        "id": tc.id,
                        "name": tc.function.name,
                        "arguments": tc.function.arguments
                    })
            
            return {
                "content": message.content,
                "tool_calls": tool_calls
            }

        elif provider == "gemini":
            if not genai:
                raise RuntimeError("Google Gemini SDK package not found or not initialized.")
            
            # Map tools to Gemini format
            gemini_tools = None
            if tools:
                functions = []
                for tool in tools:
                    if tool.get("type") == "function":
                        func = tool["function"]
                        functions.append({
                            "name": func["name"],
                            "description": func.get("description", ""),
                            "parameters": func.get("parameters", {})
                        })
                if functions:
                    gemini_tools = [{"function_declarations": functions}]

            # Initialize model
            model_client = genai.GenerativeModel(
                model_name=model,
                system_instruction=system_prompt,
                tools=gemini_tools
            )

            # Map messages to Gemini history structure
            gemini_history = []
            for msg in messages:
                role = msg["role"]
                if role == "system":
                    continue
                
                mapped_role = "user" if role in ("user", "tool") else "model"
                parts = []
                
                if role == "tool":
                    parts.append({
                        "function_response": {
                            "name": msg.get("name"),
                            "response": {"result": msg.get("content")}
                        }
                    })
                elif role == "assistant" and "tool_calls" in msg and msg["tool_calls"]:
                    for tc in msg["tool_calls"]:
                        parts.append({
                            "function_call": {
                                "name": tc["name"],
                                "args": yaml.safe_load(tc["arguments"]) if isinstance(tc["arguments"], str) else tc["arguments"]
                            }
                        })
                else:
                    parts.append({"text": msg.get("content", "")})

                gemini_history.append({
                    "role": mapped_role,
                    "parts": parts
                })

            # Start chat session
            chat_session = model_client.start_chat(history=gemini_history[:-1])
            
            # Send the last message in history
            last_msg = gemini_history[-1]
            last_parts = last_msg["parts"]
            
            response = chat_session.send_message(last_parts)
            
            # Parse responses
            tool_calls = []
            try:
                candidate = response.candidates[0]
                if candidate.content and candidate.content.parts:
                    for part in candidate.content.parts:
                        if part.function_call:
                            tool_calls.append({
                                "id": None,
                                "name": part.function_call.name,
                                "arguments": dict(part.function_call.args)
                            })
            except (IndexError, AttributeError):
                pass
            
            content = None
            try:
                content = response.text
            except Exception:
                pass

            return {
                "content": content,
                "tool_calls": tool_calls
            }

        else:
            raise ValueError(f"Unsupported provider: {provider}")


if __name__ == "__main__":
    print("✅ LLMGateway modules loaded successfully.")