LATEX_FLAGS=-interaction=nonstopmode

all: default requirements_traceability_matrix.pdf

requirements_traceability_matrix.pdf : requirements_traceability_matrix.tex requirements_traceability_matrix.bib intro.tex ../../version.tex ../sdd/ravenDepAndLimitations.tex
	pdflatex $(LATEX_FLAGS) requirements_traceability_matrix.tex
	pdflatex $(LATEX_FLAGS) requirements_traceability_matrix.tex
	pdflatex $(LATEX_FLAGS) requirements_traceability_matrix.tex

../../version.tex : *.tex
	git log -1 --format="%H %an %aD" .. > ../../version.tex

default: *.tex
	python $(RAVEN_DIR)/scripts/library_handler.py manual > dependencies.tex
	python $(RAVEN_DIR)/developer_tools/createSQAtracebilityMatrix.py -i ../srs/requirements_list.xml -o traceability_matrix.tex
	git log -1 --format="%H %an %aD" .. > ../../version.tex

.PHONY: clean

clean:
	@rm -f *~ *.aux *.bbl *.blg *.log *.out *.toc *.lot *.lof requirements_traceability_matrix.pdf dependencies.tex traceability_matrix.tex
