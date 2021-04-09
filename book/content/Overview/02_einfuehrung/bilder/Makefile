FILES = uebersicht_themen.png

all: $(FILES)

%.png: %.tex
	pdflatex -shell-escape $<
	rm $(basename $<).aux $(basename $<).log

clean:
	rm $(FILES)
