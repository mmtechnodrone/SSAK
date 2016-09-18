# SSAK
GUI front end for file identification, data carving, hexdump and steganography programs

Programs include stegdetect, stegbreak, steghide, openstego, jsteg, f5, foremost, outguess, exif, stegspy, bmppacker and diit

This program was developed due to the difficulty and finding these applications in a functional condition. For example due to compile options that need to be modified stegbreak segfaults on most distro's that actually have it available in repositories. The stegbreak in this package does not segfault. These tools are bundled into this program in what should be an easy to use interface. There are some dependencies which can be found in the dependencies.txt file. 

Output files are stored in the users home directory under a folder named SSAK. Subfolders are created under this folder named according to the program used and whether it has been embedded or extracted. For example if you embed a file with jphide (the linux version) it be in ~/SSAK/jphidelin. If you use the Windows version it will be in ~/SSAK/jphidewin. If you extract a file will be in ~/SSAK/jpseeklin or ~/SSAK/jpseekwin. 

It is important to note if you are testing the program and embed a file, to extract you must go back to file a select the output file.

Information about the selected file will appear at the bottom of the program. The file program is used to show the format and does depend on file extension.

Work has been attempted to integrate jstegshell with WINE winearch=win32 wineprefix=, but this has not yet been successful. Please post an issue on the github page if you have any insight into making this work.

Work is in progress to perform a dependency check on launch (or from the tools menu) but has not yet been implemented. If something isn't working first check that you have everything in the dependencies.txt file. If you have all the dependencies post an issue on the github page.
