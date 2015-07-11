from PIL import Image, ImageStat, ImageMath
def diffs(list):
    evens = [(x,y) for (x,y) in list if x%2 == 0]
    odds = [(x,y) for (x,y) in list if x%2 == 1]
    z = zip([y for (x,y) in evens], [y for (x,y) in odds])
    return [abs(x-y) for (x,y) in z]
def reds(filename):
    return Image.open(filename).histogram()[:256]
    
