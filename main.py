import imageio
from PIL import Image
import numpy as np
import progressbar
import mathExt
import draw
import math 
from functools import lru_cache
from pygifsicle import optimize

height = 400
width  = 400
halfHeight = int(height/2)
halfWidth = int(width/2)

FPS = 60
totalFrames = FPS*10
frameOffset = 0
scale = 1

debug = False
drawTimeBar = False
mirror = False

xOffset = -200
yOffset = -200

if(mirror):
    height *=2
    width *= 2

fileName = "test2"
fileEnding = ".gif"

def main():
    print("Creating File:'{0}{1}' with {2} FPS and total Frames of {5} (Offset: {6}) and a size of {3}x{4}".format(fileName, fileEnding, FPS, width, height, totalFrames, frameOffset))
    with imageio.get_writer('./out/{0}{1}'.format(fileName, fileEnding), mode='I', fps=FPS) as writer:
        if(debug):
            d = np.fromfunction(np.vectorize(equation), [height, width])
            print(d)
            print(d*frameOffset)
        for framecnt in progressbar.progressbar(range(1 + frameOffset, totalFrames + frameOffset + 1)):
            image = np.array(Image.new('RGBA', (width, height)))
            for y in range(0, halfHeight if mirror else height, 1):
                for x in range(0, halfWidth if mirror else width, 1):
                    bitsize = 8
                    col = hextoRGBA(int(equation(abs(x + xOffset), abs(y + yOffset)) * framecnt * scale), bitsize)
                    image[y,x] = [val*255/((1 << bitsize)-1) for val in col]

            if(mirror):
                image[halfHeight:height,0:halfWidth] = np.flipud(image[0:halfHeight,0:halfWidth])
                image[0:height,halfWidth:width] = np.fliplr(image[0:height,0:halfWidth])

#           Draw Progressbar
            if(drawTimeBar):
                draw.drawRectangleWithBoarder(image, 0, 0, 10, width, 2, 0, 0, 0)
                barWidth = int(mathExt.remap(framecnt - frameOffset, 0, totalFrames - 1, 0, width))
                draw.drawRectangleWithBoarder(image, 0, 0, 10, barWidth, 2, 255, 0, 128)

            writer.append_data(image)
    print(equation.cache_info())
    if(fileEnding == ".gif"):
        draw.optimizeGIF('./out/{0}{1}'.format(fileName, fileEnding), 'C:\\Users\\Nutzer\\Documents\\Python\\out\\{0}opt{1}'.format(fileName, fileEnding))
@lru_cache(maxsize=None)   
def equation(x, y):
    ret = math.tan(x)*math.sin(y)
    return abs(ret)

def valueToColor(val):
    return hextoRGBA(abs(val), 8)

def hextoRGBA(d, bitsize = 8):
    bitmask = (1<<bitsize)-1
    return [(bitmask & (d)), (bitmask & (d >> bitsize)), (bitmask & (d >> bitsize*2)), bitmask]

if __name__ == '__main__':
    main()
