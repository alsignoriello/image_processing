#!/usr/bin/python
from PIL import Image
import sys

"""

properties.py - lists properties of an Image

[image]


"""



file = sys.argv[1]


im = Image.open(file)

print "Image size = (%d,%d)" % (im.size[0], im.size[1])
print "Image mode = %s" % im.mode
