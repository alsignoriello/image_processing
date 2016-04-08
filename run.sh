#!/usr/bin/bash

file=$1

# python properties.py $file
# python gamma_correction.py $file 0.5 gamma.tif
# python threshold.py $file 100 thresh.tif
# python mean_filter.py $file 5 mean.tif
python normal_filter.py $file 5 norm.tif

