pandoc --filter pandoc-citeproc $1.md --standalone --to latex --latex-engine xelatex --output $1.pdf
