#!/usr/bin/env python3
import os
import sys
import json
import re
import argparse

def load_blocklist(blocklist_path):
    if not os.path.exists(blocklist_path):
        print(f"Error: Blocklist path '{blocklist_path}' not found.")
        sys.exit(1)
    with open(blocklist_path, 'r', encoding='utf-8') as f:
        return json.load(f).get("project_jargon", [])

def check_file(file_path, blocklist):
    if not os.path.exists(file_path):
        print(f"Error: Target file '{file_path}' not found.")
        sys.exit(1)
        
    violations = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line_idx, line in enumerate(lines, start=1):
        # Ignore comments in LaTeX
        if line.strip().startswith('%'):
            continue
            
        for entry in blocklist:
            term = entry["term"]
            # Look for word bounds or raw string match
            match = re.search(r'\b' + re.escape(term) + r'\b', line, re.IGNORECASE)
            if match:
                violations.append({
                    "line": line_idx,
                    "term": term,
                    "snippet": line.strip(),
                    "alternatives": entry["alternatives"]
                })
    return violations

def generate_report(violations, format_type='markdown'):
    if not violations:
        return "SUCCESS: No jargon leakage detected."
        
    if format_type == 'markdown':
        report = ["# Prose Register Audit Report\n", f"Found **{len(violations)}** instances of leaked internal jargon:\n"]
        report.append("| Line | Found Term | Violating Snippet | Preferred Alternatives |")
        report.append("|---|---|---|---|")
        for v in violations:
            alts = ", ".join(f"`{a}`" for a in v["alternatives"])
            report.append(f"| {v['line']} | **{v['term']}** | *\"{v['snippet']}\"* | {alts} |")
        return "\n".join(report)
    else:
        return json.dumps(violations, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Check LaTeX/Markdown files for leaked editing jargon.")
    parser.add_argument("target_file", help="File path to check (e.g., main.tex)")
    parser.add_argument("--blocklist", default="academic-paper/references/jargon_leak_blocklist.json", help="Path to blocklist JSON")
    parser.add_argument("--json", action="store_true", help="Output report as JSON")
    args = parser.parse_args()
    
    blocklist = load_blocklist(args.blocklist)
    violations = check_file(args.target_file, blocklist)
    
    if violations:
        print(generate_report(violations, format_type='json' if args.json else 'markdown'))
        sys.exit(1) # Return failure status if violations found
    else:
        print("Success: No jargon leakage detected.")
        sys.exit(0)

if __name__ == "__main__":
    main()
