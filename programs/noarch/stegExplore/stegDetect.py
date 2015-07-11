from PIL import Image, ImageStat, ImageMath
from math import *
import stegPNG

def isPair(color1, color2):
    li = [abs(x-y)<=1 for (x,y) in zip(color1, color2)]
    return not False in li

def numPairs(colorList):
    n = 0
    for x in colorList:
        for y in colorList[1:]:
            if isPair(x,y):
                n = n+1
    return n
    
def combination(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def ratio(colorList):
    # takes in output of Image.getcolors()
    colorList = [y for (x,y) in colorList if x >2]
    return float(numPairs(colorList))/combination(len(colorList), 2)

def cropTop(im, height):
    return im.crop((0, 0, im.size[0], height if height <= im.size[1] else im.size[1]))

def testRatio(im1):
    im = Image.open(im1)
    #because messages are put in the first few lines, should work.
    im = cropTop(im, 200)
    im.load()
    colors = im.getcolors(im.size[0]*im.size[1])
    print "Image Ratio: " + str(ratio(colors))
    imTest = stegPNG.encode(im, "01"*20000)
    colors = imTest.getcolors(imTest.size[0]*imTest.size[1])
    print "IfMessage Ratio " + str(ratio(colors))

def testRatioTwo(im1, im2):
    testRatio(im1)
    testRatio(im2)

def usage():
    print "Usage: stegDetect.py filename"
    sys.exit()

def main():
    if len(sys.argv) <= 1:
        usage()
    fileName = sys.argv[1]
    image = Image.open(fileName)
    testRatio(image)
    
