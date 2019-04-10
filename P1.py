## used package : numpy, Pillow
from PIL import Image
import os, numpy
from osgeo import gdal

#ds1 = gdal.Open('17.10.tif')
#ds2 = gdal.Open('18.05.tif')

r1 = numpy.array(ds1.ReadAsArray())
r2 = numpy.array(ds2.ReadAsArray())

d = numpy.array_equal(r1,r2)

if d == False:
    print("They differ")
else:
    print("They are the same")
