#!/usr/bin/python
import numpy as np
from PIL import Image
import sys




file = sys.argv[1]
outfile = sys.argv[2]


im = Image.open(file)
if im.mode != "L":
	im = im.convert("L")

mat = np.array(im)
grad = np.asarray(np.gradient(mat))
print grad.shape
im = Image.fromarray(grad[0,:,:]+grad[1,:,:])
im.save(outfile)