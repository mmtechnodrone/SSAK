import sys
import os
import getopt
'''
definitions
'''
space = " "
tab = chr(9)
terminator = tab*4

def addToLineX(line, s, x):
    '''
    adds s to line x times
    '''
    return line.rstrip()+(s*x)

def writeOctalBits(lines, messageInt):
    '''
    takes an iterator(lines) and an integer in octal(message int) and writes that integer into the next three lines.  It then prints those three lines, unless there are fewer than 3 lines left.  
    '''
    try:
        o = oct(messageInt)
        outLines = []
        # 1 or 2 tabs for first octal digit
        outLines.append(addToLineX(lines.next(), tab, int(o[1])+1))
       # second and third octal digits
        outLines.append(addToLineX(lines.next(), space, (int(o[2]))))
        outLines.append(addToLineX(lines.next(), space, (int(o[3]))))
        for l in outLines:
            print l
    except StopIteration:
        print outLines
        
def writeMessageToLines(dataLines, message, outfile):
    '''
    takes a list of strings, each string being a line 
    of the original file.
    prints new file with encoded message
    '''
    numLines = len(dataLines)
    # message can only be as long as number of lines in file
    truncated_message = message[:(numLines/3)-1]
    iterLines = iter(dataLines) 
    messageInts = [ord(m) for m in truncated_message]
    
    for mi in messageInts:
        writeOctalBits(iterLines, mi)
    #add message terminator and print rest of message
    print addToLineX(iterLines.next(), tab, 4)
    while True:
        try:
            print addToLineX(iterLines.next(), '', 0)
        except StopIteration:
            break
def trailing_whitespace(string):
    return string[len(string.rstrip()):]

def readOctalBit(lines):
    l1 = lines.next()
    w = trailing_whitespace(l1)
    if w == terminator:
        return None
    else:
        bits = [w[1:], 
                trailing_whitespace(lines.next()),
                trailing_whitespace(lines.next())]
        #print bits
        bits = map(len, bits)
        #print bits
        return chr(int("".join(map(str,bits)),8))    
                   
def readMessageFromLines(dataLines):
    '''
    takes a list of strings, each string being a line of the original file.
    prints the message encoded in the file
    '''
    if dataLines[0].rfind == -1:
        print "no stegText encoded message"
        exit
    else:
        outStr = []
        iterLines = iter(dataLines)
        while True:
            c = readOctalBit(iterLines)
            #print c
            if c == None:
                print "".join(outStr)
                break     
            else:
                outStr.append(c)
        
def usage():
        print "usage: \n [encrypt] Stegtext.py -e hidden_message covertext \n [decrypt] -d Stegtext.py -d covert_message"
def main():
    decrypt = False
    try:
        options, remainder = getopt.getopt(sys.argv[1:], "e:d")
    except getopt.GetoptError, err:
        usage()
        exit
        
    for opt, arg in options:
        if opt in ('-d'):
            decrypt = True
        elif opt in ('-e'):
            message = arg
        else:
            usage()
            exit
            
    plaintext = remainder[0]
    #print options, remainder
       
    if os.path.exists(plaintext):
        with open(plaintext, 'r') as f:
            data = f.readlines()
        if not decrypt:
            writeMessageToLines(data, message, sys.stdout)
        else:
            readMessageFromLines([l.rstrip('\n') for l in data])

if __name__ == "__main__":
    main()
