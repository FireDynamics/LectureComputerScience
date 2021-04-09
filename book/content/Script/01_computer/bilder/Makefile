FILES = zahlendarstellung_float.svg \
	zahlendarstellung_integer32.svg \
	zahlendarstellung_integer08.svg \
	zahlendarstellung_integer08_5.svg \
	zahlendarstellung_integer08_107.svg \
	algorithmus.svg \
	alg_findmax.svg \
	alg_selsort.svg \
	alg_bubblesort.svg \
	storage_hierachy.svg

all: $(FILES)

%.svg: %.tex
	pdflatex -shell-escape $<
	rm $(basename $<).aux $(basename $<).log

clean:
	rm $(FILES)
