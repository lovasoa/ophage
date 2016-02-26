#!/usr/bin/env python3

import sys
import os
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfArray, PdfObject, PdfName

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
