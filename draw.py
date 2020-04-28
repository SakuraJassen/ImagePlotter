import numpy
from pygifsicle import optimize

def drawRectangleFill(ndarray, p1x, p1y, p2x, p2y, r, g, b):
	ndarray[p1y:p2y, p1x:p2x] = [r,g,b,255]

def drawRectangleWithBoarder(ndarray, p1x, p1y, p2x, p2y, bWidth, r, g, b):
	drawRectangleFill(ndarray, p1x, p1y, p2x, p2y, 255, 255, 255)
	drawRectangleFill(ndarray, p1x + bWidth, p1y + bWidth, p2x - bWidth, p2y - bWidth, r, g, b)

def optimizeGIF(path, out):
    print("Optimizing GIF...")
    if path[-4:] == '.gif':
    	optimize(path, out) 
