import OpenEXR
import Imath
from PIL import Image, ImageDraw 
import sys, array

exrfile=sys.argv[1]

print 'PyExrView v0.1a'
print 'open',exrfile

file = OpenEXR.InputFile(exrfile)
pt = Imath.PixelType(Imath.PixelType.FLOAT)
dw = file.header()['dataWindow']
size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)

RedStr = file.channel('R', pt)
GreenStr = file.channel('G', pt)
BlueStr = file.channel('B', pt)

Red = array.array('f', RedStr)
Green = array.array('f', GreenStr)
Blue = array.array('f', BlueStr)


import convert_srgb
print convert_srgb.format(OpenEXR.InputFile(exrfile).header())

print 'start convert srgb'
convert_srgb.ConvertSRGB(Red,Green,Blue)
print 'finale'

    
rgbf = [Image.fromstring("F", size, Red.tostring())]
rgbf.append(Image.fromstring("F", size, Green.tostring()))
rgbf.append(Image.fromstring("F", size, Blue.tostring()))

rgb8 = [im.convert("L") for im in rgbf]

exrimage = Image.merge("RGB", rgb8)
print 'draw'
draw = ImageDraw.Draw(exrimage)
draw.text((0, 0),exrfile,(255,255,255))
print 'view'
exrimage.show()
