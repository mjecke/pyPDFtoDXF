# pyPDFtoDXF
Quick and dirty script to pull vector graphics from a PDF and export to DXF drawing files.  

System Requirements:
inkscape
pdf2svg

Python:

pip install PyPDF2

!!!! Requires 'inkscape' and 'pdf2svg' to be in system path !!!!

Script is just gluing together pdf2svg to make a svg, and then inkscape processes the svg to a dxf. 
Saves the svg in output folder along with dxf.
Note that this can be slow if your PDF has many, many pages to go thru as the inscape process has to be called once-per-page.
Better to extract just a single page instead if that is all you need.

Also this method has trouble with converting certain types of text in PDFs into DXF.  
It works mainly for polys and other vectors, e.g. drawings that were originally CAD and saved into PDF.  

Usage:

python pdftodxf.py input.pdf output


