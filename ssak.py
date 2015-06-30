#!/usr/bin/env python

import sys, pygtk, gi, os, re, pwd
from gi.repository import Gtk
from openstego import openstego
from jphs import jphs
from fileops import fileops
from stegdetect import stegdetect

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

try: 
	os.stat(home)
except:
	os.mkdir(home)
fileselected = ''

class SSAK(openstego, jphs, fileops, stegdetect):

	def __init__(self):
		gladefile = execdir + "/SSAK.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladefile)
		self.window = self.builder.get_object("window1")
		self.window.set_title("SSAK - Steganography Swiss Army Knife")
		self.window.show_all()

		# exit on windows x button
		self.window.connect("delete_event", Gtk.main_quit)

		# exit on file menu quit button
		self.exit = self.builder.get_object("imagemenuitem3")
		self.exit.connect("activate", Gtk.main_quit)

		#select file from file menu
		self.selectfile = self.builder.get_object("imagemenuitem1")
		self.selectfile.connect("activate", self.fileselect)

		# call strings functions when readstring button pressed
		self.readstrings = self.builder.get_object("button1")
		self.readstrings.connect("clicked", self.strings)

		self.readstrings = self.builder.get_object("button3")
		self.readstrings.connect("clicked", self.strings2)
	
		# call exif function when get metadata button pressed
		self.readexif = self.builder.get_object("button2")
		self.readexif.connect("clicked", self.exif)
	
		# call carve function when carve menu item selected
		self.carveit = self.builder.get_object("imagemenuitem2")
		self.carveit.connect("activate", self.carveit2) 

		# jphide
		self.jphideit = self.builder.get_object("button6")
		self.jphideit.connect("clicked", self.jphideit2)

		# jpseek
		self.jpseekit = self.builder.get_object("button9")
		self.jpseekit.connect("clicked", self.jpseekit2)

		# openstegembed
		self.ostegembed = self.builder.get_object("button8")
		self.ostegembed.connect("clicked", self.ostegembed2)
		checkbutton3 = self.builder.get_object("checkbutton3")
		checkbutton3.connect("toggled", self.togglepass)

		# openstegextract
		self.ostegextract = self.builder.get_object("button7")
		self.ostegextract.connect("clicked", self.ostegextract2)
		checkbutton4 = self.builder.get_object("checkbutton1")
		checkbutton4.connect("toggled", self.togglepass2)

		# stegdetect
		self.steg = self.builder.get_object("button11")
		self.steg.connect("clicked", self.stegdet)

		#stegbreak
		self.stegc = self.builder.get_object("button10")
		self.stegc.connect("clicked", self.stegcrack)

SSAK=SSAK()
Gtk.main()
