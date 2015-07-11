from PIL import Image
import getopt
import sys
import os
import binascii
import itertools

# globals:

encode = False
payload = ""
outImage_name = ""
coverImage_name = ""



def modifyPixel(pixel, iterb, i, j):
    out = []
    for p in pixel:
        try:
            i = iterb.next()
            if (p % 2) == 0:
                if i=='1':
                    out.append(p+1)
                else:
                    out.append(p)
            else:
                if i=='0':
                    out.append(p-1)
                else:
                    out.append(p)
        except StopIteration:
            out.append(p)
            
    #print out
    return tuple(out)

def readPixel (pixel):
    return [(p%2) for p in pixel]

def usage():
    print "usage: stegPNG.py -e payload -o outImage image"
        
def readInput(inputs):
    global outImage_name
    global coverImage_name
    global payload
    global encode

    try:
        options, remainder = getopt.getopt(inputs, "e:o:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)

#    print (options, remainder)
    for opt, arg in options:
        # encoding: set payload
        if opt in ('-e'):
            encode = True
            if os.path.exists(arg):
                with open(arg, 'r') as f:
                     payload = f.read()
            else:
                usage()
                sys.exit(2)
        if opt in ('-o'):
            outImage_name = arg
            
    if (len(remainder) != 1):
        usage()
        sys.exit(2)
    else:
        coverImage_name = remainder[0]
#        print coverImage_name

def main():
    readInput(sys.argv[1:])
    coverImage = Image.open(coverImage_name)
    coverImage = coverImage.convert("RGB")

    if encode:
        coverImage = encode(coverImage, payload)
        coverImage.save(outImage_name, 'PNG')
        
    #decoding
    else:        
        decode(coverImage)

def encode(coverImage, payload):

    #set up limits, counts, bits
        pixels = coverImage.load()#2-d pixel array
        pwidth, pheight = coverImage.size
        #print(pwidth, pheight)
        
        payload_bits = [bin(ord(x))[2:] for x in payload]
        payload_bits = [x.rjust(7, '0') for x in payload_bits]        
        payload_bits = ''.join(payload_bits)
        payload_bits += "0000000"
        #print payload_bits
        i_bytes = iter(payload_bits)        
        num_bits = len(payload_bits)
        total_rows = (num_bits/(pwidth*3))+1 #total number of rows of image needed to store all bits
        #print num_bits
        #print total_rows
        if total_rows > pheight:
            print "message too long"
            exit(2)
        
    #main writing loop
        #pixel[x, y]
        for y in range(total_rows):
            for x in range(pwidth):
                #print (x,y)
                rgb = pixels[x,y]
                pixels[x,y] = modifyPixel(list(rgb), i_bytes, x, y)
        return coverImage

def decode(coverImage):
    pwidth, pheight = coverImage.size
    #print(pwidth, pheight)
    pixels = list(coverImage.getdata())
    pixels = [readPixel(x) for x in pixels]
    pixels = list(itertools.chain.from_iterable(pixels))
    pixels = split_7(pixels)
    pixels = list(pixels)
    pixels = [ chr(int("".join([str(x) for x in li]), 2)) for li in pixels]
    pixels = pixels[:pixels.index('\x00')]
    #print pixels
    print "".join([x for x in pixels])
def split_7(l):
    for i in xrange(0, len(l), 7):
        yield l[i:i+7]

def encodeLoremIpsum(image, bytes):
    import pypsum
    text, stuff = pypsum.get_lipsum(bytes, 'bytes', 'no')
    return encode(image, text)

if __name__ == "__main__":
    main()
