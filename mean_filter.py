#!/usr/bin/python
import numpy as np
from PIL import Image
from scipy.signal import convolve2d
import sys

def meanFilter(mat,n):
	ones = np.ones((n,n))
	avg = ones / float(n**2)
	mean = convolve2d(mat,avg,mode='same')
	return mean



file = sys.argv[1]
n = int(sys.argv[2])
outfile = sys.argv[3]


im = Image.open(file)
if im.mode != "L":
	im = im.convert("L")
mat = np.array(im)
mat = meanFilter(mat, n)
im = Image.fromarray(mat)
im.save(outfile)

