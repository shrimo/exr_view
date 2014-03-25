import OpenEXR
import Imath
from PIL import Image
import sys, array
import os

exrf=sys.argv[1]

def exrToJpgGamma(exrfile):
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

    def EncodeToSRGB(v):
        if (v <= 0.0031308):
            return (v * 12.92) * 255.0
        else:
            return (1.055*(v**(1.0/2.2))-0.055) * 255.0

    for I in range(len(Red)):
        Red[I] = EncodeToSRGB(Red[I])

    for I in range(len(Green)):
        Green[I] = EncodeToSRGB(Green[I])

    for I in range(len(Blue)):
        Blue[I] = EncodeToSRGB(Blue[I])

    rgbf = [Image.fromstring("F", size, Red.tostring())]
    rgbf.append(Image.fromstring("F", size, Green.tostring()))
    rgbf.append(Image.fromstring("F", size, Blue.tostring()))

    rgb8 = [im.convert("L") for im in rgbf]
    myqimage = Image.merge("RGB", rgb8)
    return myqimage.show()

exrToJpgGamma(exrf)



