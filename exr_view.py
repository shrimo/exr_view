from PIL import Image, ImageDraw
import sys, array

print 'PyExrView v0.1a\nexr_view.py (exr file) (channels)\n'

try:
    exrfile=sys.argv[1]
except:
    print '->Error. No Exr File'
    sys.exit (0)
try:
    chanName=sys.argv[2]
except:
    chanName='RGB'

#exrfile='test_c.exr'#sys.argv[1]
print 'open',exrfile,'\nchannels',chanName

import exr_handler
# 0-Red, 1-Green, 2-Blue, 3-Size, 4-Header data
_EXR_data_=exr_handler.Put_Exr_Data(exrfile,chanName)

print '\n',exr_handler.format(_EXR_data_[4])

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
