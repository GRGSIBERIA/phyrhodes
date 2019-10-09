rem platex --kanji=utf8
platex main.tex
pbibtex main
platex main.tex
dvipdfm main.dvi

del *.log
del *.bmc
del *.pbm
del *.aux