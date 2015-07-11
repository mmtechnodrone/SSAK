The stegExplore package is available at http://dl.dropbox.com/u/10783341/stegExplore.tar.gz

    Pre-requisite for all programs: Python 2.5 or greater available at http://www.python.org/download/

StegText.py:
    to encode string hidden_message in a text file  text:
        Python stegText.py -e hidden_message text
    The new stego-text prints to standard output
    to decode a message hidden in a text file text:
        python stegText.py -d text
    The message prints to standard output

StegPNG, stegDetect, and stegDetectPNG require the Python Imaging Library available at http://www.pythonware.com/products/pil/
    To encode a message stored in a text file message.txt in a 24-bit png file cover.png to save in out.png::
        python stegPNG.py -e message.txt -o out.png cover.png
    To decode a message from image cover.png:
        python stegPNG.py cover.png
    The message prints to standard output
    You can also import  it as  a module.  The methods of interest are encode(Image, String) and decode(Image).
    To detect the presence of an ascii message in an image image.png:
        python stegDetectPNG.py image.png
    This prints the percentage of unusual characters and its judgement on the likelihood of the image carrying a message
    To detect the ratio of color pairs in an image image.png:
        python stegDetect.py image.png
    To compare the ratio of two images, load the stegDetect.py and use the testRatioTwo() method.  
