import imageio
from PIL import Image
import numpy as np
import progressbar
import mathExt
import draw
import math 
from functools import lru_cache

height = 400
width  = 400
halfHeight = int(height/2)
halfWidth = int(width/2)

FPS = 24
totalFrames = FPS*5
frameOffset = 0

drawTimeBar = False
mirror = False

xOffset = -200
yOffset = -200

if(mirror):
    height *=2
    width *= 2

fileName = "debug"
fileEnding = ".gif"

def main():
    print("Creating File:'{0}{1}' with {2} FPS and total Frames of {5} and a size of {3}x{4}".format(fileName, fileEnding, FPS, width, height, totalFrames))
    with imageio.get_writer('./out/{0}{1}'.format(fileName, fileEnding), mode='I', fps=FPS) as writer:
        for framecnt in progressbar.progressbar(range(1 + frameOffset, totalFrames + frameOffset + 1)):
            image = np.array(Image.new('RGBA', (width, height)))
            for y in range(0, halfHeight if mirror else height, 1):
                for x in range(0, halfWidth if mirror else width, 1):
                    col = int(equation(abs(x + xOffset), abs(y + yOffset)) * framecnt)
                    ret = hextoRGBA(col, 4)

                    image[y,x] = [mathExt.remap(val, 0, 15, 0, 255) for val in ret]

            if(mirror):
                image[halfHeight:height,0:halfWidth] = np.flipud(image[0:halfHeight,0:halfWidth])
                image[0:height,halfWidth:width] = np.fliplr(image[0:height,0:halfWidth])

#           Draw Progressbar
            if(drawTimeBar):
                draw.drawRectangle(image, 0, 0, 10, width, 2, 0, 0, 0)
                barWidth = int(mathExt.remap(framecnt - frameOffset, 0, totalFrames - 1, 0, width))
                draw.drawRectangle(image, 0, 0, 10, barWidth, 2, 255, 0, 128)

            writer.append_data(image)
    print(equation.cache_info())

@lru_cache(maxsize=None)   
def equation(x, y):
    ret = (math.sqrt(x)*math.sqrt(y))
    return ret

def hextoRGBA(d, bitsize = 8):
    bitmask = (1<<bitsize)-1
    return [(bitmask & (d)), (bitmask & (d >> bitsize)), (bitmask & (d >> bitsize*2)), bitmask]

if __name__ == '__main__':
    main()