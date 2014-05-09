import OpenEXR
import Imath
from PIL import Image
import sys, array
import os

exrfile=sys.argv[1]

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
convert_srgb.ConvertSRGB(Red,Green,Blue)
    
rgbf = [Image.fromstring("F", size, Red.tostring())]
rgbf.append(Image.fromstring("F", size, Green.tostring()))
rgbf.append(Image.fromstring("F", size, Blue.tostring()))

rgb8 = [im.convert("L") for im in rgbf]

myqimage = Image.merge("RGB", rgb8)

myqimage.show()





