#!/usr/bin/python
import numpy as np 
from PIL import Image
import sys


def gamma_correct(mat, gamma, scale):

	# 1D
	if len(mat.shape) == 1:
		mat[:] = scale * np.divide(mat[:], scale) ** gamma

	# 2D
	if len(mat.shape) == 2:
		mat[:,:] = scale * np.divide(mat[:,:], scale) ** gamma
	# 3D
	if len(mat.shape) == 3:
		mat[:,:,:] = scale * np.divide(mat[:,:,:], scale) ** gamma
	return mat


file = sys.argv[1]
gamma = float(sys.argv[2])
outfile = sys.argv[3]

im = Image.open(file)
mat = np.array(im)
scale = float(np.max(mat))
mat = gamma_correct(mat, gamma, scale)
im = Image.fromarray(mat)
im.save(outfile)




