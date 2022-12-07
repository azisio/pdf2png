import fitz
import os
import sys
from pathlib import Path

args = sys.argv

if len(args) >= 3:
    pdfFile = Path(args[1])
    outputPath = args[2]
elif len(args) >= 2:
    pdfFile = Path(args[1])
    outputPath = "output"
else:
    sys.exit()

os.makedirs(outputPath, exist_ok=True)

fileName = pdfFile.stem

pages = fitz.open(pdfFile)

for page in pages:
    pix = page.get_pixmap()
    pix.save("%s\\%s_%i.png" % (outputPath,fileName, page.number+1))