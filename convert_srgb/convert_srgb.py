def EncodeToSRGB(v):
    if (v <= 0.0031308):
        return (v * 12.92) * 255.0
    else:
        return (1.055*(v**(1.0/2.2))-0.055) * 255.0

def ConvertSRGB(Red,Green,Blue):
    rgb_size=range(len(Red))
    for I in rgb_size:
        Red[I] = EncodeToSRGB(Red[I])
        Green[I] = EncodeToSRGB(Green[I])
        Blue[I] = EncodeToSRGB(Blue[I])
    return Red,Green,Blue
