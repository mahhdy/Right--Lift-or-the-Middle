## Audit Summary (edits performed)

| File | Issues Found | Issues Fixed |
|---|---:|---:|
| `Main.tex` | TOC anchor & pagebreaks; missing `pdfencoding` in `hypersetup`; inconsistent color-name aliases; TOC syntax error | 4 |
| `chapters/ch11-.tex` | undefined color names; emoji in tcolorbox title | 2 |
| `chapters/ch12-.tex` | undefined color names in tcolorbox | 1 |
| `chapters/ch13-.tex` | undefined color names in tcolorbox | 1 |
| `chapters/ch14-.tex` | undefined color names in tcolorbox | 1 |
| `chapters/ch15-.tex` | undefined color names in tcolorbox | 1 |
| `chapters/ch16-.tex` | undefined color names in tcolorbox | 1 |
| `chapters/ch17-.tex` | undefined color names; emoji in tcolorbox title; TikZ color-case mismatch | 4 |
| `appendices/annx01-timeline.tex` | lowercase color names used in many TikZ nodes | 5 |
| Other chapters | checked for top-level `\documentclass`/`\begin{document}` and Latin labels — OK | 0 |

**Total files inspected:** 1 main + 17 chapters + 9 appendices (listed) — core issues fixed in the files above.

**Preamble Warnings:**
- Compile twice with XeLaTeX to regenerate TOC and resolve references: `xelatex -interaction=nonstopmode Main.tex` (run twice).
- If TOC is still empty after two runs, confirm that chapters compile individually and contain `\chapter{}` commands (they do in inspected files).
- Some color names in older fragments used lowercase variants; instead of editing every fragment, I added color aliases in `Main.tex` (`\colorlet{leftred}{LeftRed}` etc.) to maintain original content while preventing compilation errors.

If you want, I can now:
- Normalize all remaining lowercase color tokens across appendices (explicit replacements),
- Remove or relocate `\frontmatter` if you prefer the titlepage to be strictly first page,
- Run a quick syntactic balance check for environments (tcolorbox/TikZ) with a Python script.
