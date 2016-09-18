#!/usr/bin/env python

import sys, pygtk, gi, os, re, pwd, struct
from gi.repository import Gtk, GLib, Vte
from openstego import openstego
from jphs import jphs
from fileops import fileops
from stegdetect import stegdetect
from steghide import steghide
from outguess import outguess
from f5 import f5
from gtkvars import gtkvars
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

try: 
	os.stat(home)
except:
	os.mkdir(home)

class SSAK(gtkvars, openstego, jphs, fileops, stegdetect, steghide, outguess, f5):

	def spy(self, widget):
		os.environ["WINEDEBUG"] = "warn-all,-heap,-relay,err-all,fixme-all,trace-all"
		cmd = "WINEPREFIX=" + re.escape(home) + "wineprefix /usr/bin/wine " + re.escape(execdir) + "/programs/Win/StegSpy2.1.exe"
		Popen(cmd, shell=True)

	def diitrun(self, widget):
		cmd2 = "java -jar " + re.escape(execdir) + "/programs/noarch/diit-1.5.jar"
		Popen(cmd2, shell=True)

	def bmppackerrun(self, widget):
		os.environ["WINEDEBUG"] = "warn-all,-heap,-relay,err-all,fixme-all,trace-all"
		cmd3 = "WINEPREFIX=" + re.escape(home) + "wineprefix /usr/bin/wine " + re.escape(execdir) + "/programs/Win/bmpPacker.exe"
		Popen(cmd3, shell=True)

	def launchterm(self, widget):
		windowvte = Gtk.Window()
		v = Vte.Terminal ()
		windowvte.add(v)
		termdir = execdir + "/programs"
		try: 
			v.spawn_sync(Vte.PtyFlags.DEFAULT, termdir, ["/bin/bash"], [], GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None, )
		except:
			v.fork_command_full(Vte.PtyFlags.DEFAULT, termdir, ["/bin/sh"], [], GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None, )
		windowvte.connect('delete-event', lambda window, event: windowvte.hide() or True)
		windowvte.show_all()

	def showdiag(self):
		def hidedialog(widget):
			self.nofiledialog.hide()
		self.nofiledialogbutton.connect("clicked",hidedialog)
		self.nofiledialog.show()
		self.nofiledialog.connect("delete-event", lambda window, event: self.nofiledialog.hide() or True)

	def __init__(self):
		if (os.path.isdir(home + "wineprefix")) == False:
			os.environ["WINEDEBUG"] = "warn-all,-heap,-relay,err-all,fixme-all,trace-all"
			os.environ["WINEPREFIX"] = home + "/wineprefix"
			cmd = re.escape(execdir) + "/programs/noarch/winetricks.sh vb6run"
			Popen(cmd, shell=True)
		gladefile = execdir + "/SSAK.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladefile)
		self.setvars()
		self.window.set_title("SSAK - Steganography Swiss Army Knife")
		self.window.show_all()

		# exit on windows x button
		self.window.connect("delete_event", Gtk.main_quit)

		# exit on file menu quit button
		self.exit.connect("activate", Gtk.main_quit)

		#select file from file menu
		self.selectfile.connect("activate", self.fileselect)

		#show about dialog
		def about(widget):
			self.aboutwin.set_title("About SSAK")
			self.aboutwin.connect("delete-event", lambda window, event: self.aboutwin.hide() or True)
			def hideabout(widget):
				self.aboutwin.hide()
			self.aboutclose.connect("clicked",hideabout)
			self.aboutwin.show()		
		self.about.connect("activate", about)

		# call strings functions when readstring button pressed
		self.readstrings1.connect("clicked", self.strings)
		self.readstrings2.connect("clicked", self.strings2)
	
		# call exif function when get metadata button pressed
		self.readexif.connect("clicked", self.exif)
	
		# call carve function when carve menu item selected
		self.carveit.connect("activate", self.carveit2) 

		# call function to start StegSpy
		self.stegspy.connect("activate", self.spy) 

		# call function to start DIIT
		self.diit.connect("activate", self.diitrun)

		# call function to start BMPPacker
		self.bmppacker.connect("activate", self.bmppackerrun)

		# call function to launch terminal
		self.terminal.connect("activate", self.launchterm)

		# jphide
		self.jphideit.connect("clicked", self.jphideit2)

		# jpseek
		self.jpseekit.connect("clicked", self.jpseekit2)

		# openstegembed
		self.ostegembed.connect("clicked", self.ostegembed2)
		self.checkbutton3.connect("toggled", self.togglepass)

		# openstegextract
		self.ostegextract.connect("clicked", self.ostegextract2)
		self.checkbutton4.connect("toggled", self.togglepass2)

		# outguessembed
		self.outembed.connect("clicked", self.embedguess)

		# outguessextract
		self.outextract.connect("clicked", self.extractguess)

		# f5 embed
		self.f5embedit.connect("clicked", self.f5embed)

		# f5 extract
		self.f5extractit.connect("clicked", self.f5extract)

		# stegdetect
		self.steg.connect("clicked", self.stegdet)

		#stegbreak
		self.stegc.connect("clicked", self.stegcrack)

		#steghide
		self.stegh.connect("clicked", self.stegembed)

		#steghextract
		def radiocall(widget, data=None):
			if "ON" in (data, ("OFF","ON")[widget.get_active()]):
				self.activeradio = data
		self.stegx.connect("clicked", self.stegextract)
		self.stegradio1.connect("toggled", radiocall, "button1")
		self.stegradio2.connect("toggled", radiocall, "button2")		
		self.stegradio3.connect("toggled", radiocall, "button3")
		self.stegradio3.set_active("ON")

SSAK=SSAK()
Gtk.main()
