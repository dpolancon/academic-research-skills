#!/usr/bin/env python3
import os
import tempfile
import json
import pytest
from check_jargon_leakage import check_file, load_blocklist

def test_jargon_leakage_detection():
    # 1. Create a temporary blocklist file
    blocklist_data = {
      "project_jargon": [
        {
          "term": "empirical object",
          "alternatives": ["coefficient", "estimate"]
        },
        {
          "term": "system-admissibility gates",
          "alternatives": ["VECM rank checks"]
        }
      ]
    }
    
    with tempfile.NamedTemporaryFile(suffix=".json", mode="w+", delete=False, encoding="utf-8") as f_block:
        json.dump(blocklist_data, f_block)
        blocklist_path = f_block.name
        
    try:
        # 2. Load the blocklist
        blocklist = load_blocklist(blocklist_path)
        assert len(blocklist) == 2
        
        # 3. Create a temporary mock LaTeX file with violations and comments
        latex_content = """
        \\documentclass{article}
        \\begin{document}
        % This is a comment containing empirical object which should be ignored.
        The empirical object is analyzed on line 5.
        Our model satisfies the system-admissibility gates.
        \\end{document}
        """
        
        with tempfile.NamedTemporaryFile(suffix=".tex", mode="w+", delete=False, encoding="utf-8") as f_latex:
            f_latex.write(latex_content)
            latex_path = f_latex.name
            
        try:
            # 4. Check the file
            violations = check_file(latex_path, blocklist)
            
            # 5. Assertions
            # We expect 2 violations (the one in the comment on line 4 should be ignored)
            assert len(violations) == 2
            
            # Check first violation (line 5 in latex_content)
            # The line numbers are 1-based.
            # Line 1: \documentclass{article}
            # Line 2: \begin{document}
            # Line 3: % This is a comment... (ignored comment, but still a line)
            # Line 4: The empirical object... (violating line)
            # Line 5: Our model satisfies... (violating line)
            
            # Let's check the terms found
            found_terms = [v["term"] for v in violations]
            assert "empirical object" in found_terms
            assert "system-admissibility gates" in found_terms
            
        finally:
            os.remove(latex_path)
    finally:
        os.remove(blocklist_path)
