import numpy

def drawRectangleFill(ndarray, p1x, p1y, p2x, p2y, r, g, b):
	ndarray[p1x:p2x, p1y:p2y] = [r,g,b,255]

def drawRectangle(ndarray, p1x, p1y, p2x, p2y, width, r, g, b):
	drawRectangleFill(ndarray, p1x, p1y, p2x, p2y, 255, 255, 255)
	drawRectangleFill(ndarray, p1x+width, p1y+width, p2x-width, p2y-width, r, g, b)
