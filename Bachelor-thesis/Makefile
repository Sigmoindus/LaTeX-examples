LATEXMK = latexmk
LATEX = xelatex
OUT_DIR = output
MAIN = main
CLEAN_EXTENSIONS = aux log out toc bbl blg synctex.gz run.xml bcf pdf sta

LATEXMK_OPTS = -pdfxe -output-directory=$(OUT_DIR)
LATEXMK_NO_BIBER_OPTS = -pdfxe -output-directory=$(OUT_DIR) -bibtex-

.PHONY: all quick clean final

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

all: $(OUT_DIR)
	$(LATEXMK) $(LATEXMK_OPTS) $(MAIN).tex

quick: $(OUT_DIR)
	$(LATEX) -output-directory=$(OUT_DIR) $(MAIN).tex

clean:
	rm -rf $(OUT_DIR)/* $(MAIN).$(CLEAN_EXTENSIONS)

final: clean all
