---
name: latex-compilation
description: Guidelines, protocols, and workflows for isolating LaTeX compilations, gitignoring source and output files entirely, compiling documents, and generating markdown backups.
---

# LaTeX Dedicated Workspace & Compilation Protocol

Use this skill when initializing a LaTeX document compilation workspace, managing drafts, or converting LaTeX documents to markdown backups.

## 1. Directory Setup & Git Isolation Protocol

To keep code repositories clean and avoid checking private drafts, unfinished manuscripts, or large binary PDFs into public version control, follow this structural protocol:

### A. Clear Folder Signaling
Always isolate LaTeX documents inside a dedicated subdirectory with a clear suffix or prefix that signals its purpose. Recommended folder names:
- `Chapter3_WriteUp/`
- `paper_draft/`
- `latex_manuscript/`

### B. Strict Gitignore Exclusion
To ensure the `.tex` files, figure sources, and compilation byproducts remain strictly local and do not sync with the online GitHub repository, immediately add the entire folder path to the repository's root `.gitignore`:

```gitignore
# Prevent sync of LaTeX source drafts and byproducts
/Chapter3_WriteUp/
/paper_draft/
/latex_manuscript/
```

*Note: By adding the leading slash (e.g., `/Chapter3_WriteUp/`), you target the specific folder at the root level of the workspace.*

---

## 2. LaTeX compilation Command Reference

Once the directory is created, compile locally using `latexmk` or manual `pdflatex` compilation:

### Option A: Automated (latexmk) - Recommended
`latexmk` automatically handles bibliographies and multiple passes:
```bash
latexmk -pdf -interaction=nonstopmode -synctex=1 Chapter3_Paper.tex
```

### Option B: Manual Multi-pass (Fallback)
```bash
pdflatex -interaction=nonstopmode Chapter3_Paper.tex
bibtex Chapter3_Paper.aux
pdflatex -interaction=nonstopmode Chapter3_Paper.tex
pdflatex -interaction=nonstopmode Chapter3_Paper.tex
```

---

## 3. Markdown Backup Generation (.md)

To create readable backups, analyze word counts, or generate clean previews of your sections, you can convert your LaTeX files to Markdown.

### Method A: Pandoc Conversion (Recommended)
If `pandoc` is installed, convert individual files or the full document:
```bash
# Convert a single section to markdown
pandoc -f latex -t gfm sections/01_introduction.tex -o backups/01_introduction.md

# Convert the master document (resolving inputs)
pandoc -f latex -t gfm Chapter3_Paper.tex -o backups/Chapter3_Paper.md --wrap=none
```

### Method B: Lightweight Backup Script
If pandoc is not available, you can run a simple Python script to merge `\input` lines and strip basic LaTeX wrappers to generate a consolidated `.md` text copy:

```python
import re
from pathlib import Path

def generate_md_backup(master_tex_path, output_md_path):
    master_path = Path(master_tex_path)
    output_path = Path(output_md_path)
    base_dir = master_path.parent
    
    with open(master_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all \input{path} patterns
    inputs = re.findall(r'\\input\{([^}]+)\}', content)
    
    consolidated_text = []
    for imp in inputs:
        imp_path = base_dir / (imp if imp.endswith('.tex') else f"{imp}.tex")
        if imp_path.exists():
            with open(imp_path, 'r', encoding='utf-8') as sf:
                consolidated_text.append(f"## Section: {imp}\n\n" + sf.read())
                
    # Basic cleanup of LaTeX commands (optional)
    full_text = "\n\n".join(consolidated_text)
    # Strip simple tags
    full_text = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', full_text)
    full_text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', full_text)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(full_text)
    print(f"Backup created at: {output_path}")
```
