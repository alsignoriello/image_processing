#!/usr/bin/python
import numpy as np
from PIL import Image
from scipy.signal import convolve2d
import sys


def normalize(mat,n):
	ones = np.ones((n,n))
	avg = ones / float(n ** 2)
	mean = convolve2d(mat,avg,mode='same')
	s = convolve2d(mat**2,avg,mode='same')
	sigma = np.fabs(s-mean**2) ** (0.5)
	sigma[sigma == 0] = 1
	mat = ((mat - mean) / (sigma))
	mat[mat < 0] = 0
	return mat 


file = sys.argv[1]
n = int(sys.argv[2])
outfile = sys.argv[3]


im = Image.open(file)
if im.mode != "L":
	im = im.convert("L")
mat = np.array(im)
mat = normalize(mat, n)
mat = mat**(0.2)
mat[mat > 0.1] = 255
mat[mat <= 0.1] = 0
print mat
im = Image.fromarray(mat)
im.save(outfile)




