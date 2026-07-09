#!/usr/bin/env python3
import sys
from pathlib import Path

# Paths
ars_dir = Path(__file__).resolve().parent.parent
panel_reports_file = ars_dir / "05_Reviewer_Panel_Reports.md"

files = [
    ("Editor-in-Chief (EIC)", ars_dir / "05_EIC_Report.md"),
    ("Peer Reviewer 1 (Methodology)", ars_dir / "05_Methodology_Report.md"),
    ("Peer Reviewer 2 (Domain)", ars_dir / "05_Domain_Report.md"),
    ("Peer Reviewer 3 (Perspective)", ars_dir / "05_Perspective_Report.md"),
    ("Devil's Advocate", ars_dir / "05_Devils_Advocate_Report.md")
]

def main():
    print("[*] Consolidating reports...")
    consolidated_content = "# Consolidated Peer Review Reports\n\n"
    
    for label, path in files:
        if path.exists():
            print(f"  [+] Reading {path.name}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            consolidated_content += f"## {label} Report\n\n{content}\n\n---\n\n"
        else:
            print(f"  [!] Warning: {path.name} not found.")
            
    with open(panel_reports_file, "w", encoding="utf-8") as f:
        f.write(consolidated_content)
    print(f"[+] Consolidated reports saved to {panel_reports_file}")

if __name__ == "__main__":
    main()
