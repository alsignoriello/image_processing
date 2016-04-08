#!/usr/bin/python
import numpy as np 
from PIL import Image
import sys



file = sys.argv[1]
thresh = float(sys.argv[2])
outfile = sys.argv[3]


im = Image.open(file)

if im.mode != "L":
	im = im.convert("L")

mat = np.array(im)
mat[mat < thresh] = 0
mat[mat != 0] = np.max(mat)
im = Image.fromarray(mat)
im.save(outfile)

