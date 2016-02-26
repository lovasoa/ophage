#!/usr/bin/env python3

import sys
import os
from pdfrw.pdfrw import PdfReader, PdfWriter, PdfDict, PdfArray, PdfObject, PdfName

if len(sys.argv)<3:
    print("""Usage: %s file.pdf page_number
            Will create renumbered.file.pdf in the current directory,
            with the page numbers shifted by page_number.""" % sys.argv[0])
    sys.exit(1)

infile     = sys.argv[1]
outfile    = "renumbered." + os.path.basename(infile)
startpage = int(sys.argv[2])

labels = PdfDict(Type=PdfName("Catalog"),
                 Nums = PdfArray([
                            PdfObject(0),
                            PdfDict(S=PdfName('r')),
                        ])
                )

if(startpage>0):
    labels.Nums.append(PdfObject(startpage-1))
    labels.Nums.append(PdfDict(S=PdfName('D')))
else:
    labels.Nums[1] = PdfDict(S=PdfName('D'), St=PdfObject(-startpage))

reader = PdfReader(infile)
reader.Root.PageLabels = labels

writer = PdfWriter()
writer.trailer = reader
writer.write(outfile)
