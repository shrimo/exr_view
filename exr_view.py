from PIL import Image, ImageDraw 
import sys, array

print 'PyExrView v0.1a'

exrfile=sys.argv[1]
print 'open',exrfile

import exr_handler
_EXR_data_=exr_handler.Put_Exr_Data(exrfile)

print exr_handler.format(_EXR_data_[4])

print 'start convert srgb'
exr_handler.ConvertSRGB(_EXR_data_[0],_EXR_data_[1],_EXR_data_[2])
print 'finale'
    
rgbf = [Image.fromstring("F", _EXR_data_[3], _EXR_data_[0].tostring())]
rgbf.append(Image.fromstring("F", _EXR_data_[3], _EXR_data_[1].tostring()))
rgbf.append(Image.fromstring("F", _EXR_data_[3], _EXR_data_[2].tostring()))

rgb8 = [im.convert("L") for im in rgbf]

exrimage = Image.merge("RGB", rgb8)
print 'draw'
draw = ImageDraw.Draw(exrimage)
draw.text((0, 0),exrfile,(255,255,255))
print 'view'
exrimage.show()
