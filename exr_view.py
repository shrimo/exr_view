import OpenEXR
from PIL import Image, ImageDraw 
import sys, array

print 'PyExrView v0.1a'

exrfile=sys.argv[1]
print 'open',exrfile

import convert_srgb
_RGB_size_=convert_srgb.Put_Exr_Data(exrfile)

print convert_srgb.format(OpenEXR.InputFile(exrfile).header())

print 'start convert srgb'
convert_srgb.ConvertSRGB(_RGB_size_[0],_RGB_size_[1],_RGB_size_[2])
print 'finale'
    
rgbf = [Image.fromstring("F", _RGB_size_[3], _RGB_size_[0].tostring())]
rgbf.append(Image.fromstring("F", _RGB_size_[3], _RGB_size_[1].tostring()))
rgbf.append(Image.fromstring("F", _RGB_size_[3], _RGB_size_[2].tostring()))

rgb8 = [im.convert("L") for im in rgbf]

exrimage = Image.merge("RGB", rgb8)
print 'draw'
draw = ImageDraw.Draw(exrimage)
draw.text((0, 0),exrfile,(255,255,255))
print 'view'
exrimage.show()
