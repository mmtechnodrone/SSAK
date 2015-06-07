#!/usr/bin/env python

import sys, pygtk, gi, os, re, pwd, pexpect, time
from subprocess import Popen, PIPE
from gi.repository import Gtk

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

try: 
	os.stat(home)
except:
	os.mkdir(home)
fileselected = ''

class SSAK:

	def fileselect(self, widget):
		self.file = self.builder.get_object("entry1")
		chooser = Gtk.FileChooserDialog("Select file to Analyze", None, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_SAVE,Gtk.ResponseType.OK))
#	chooser.set_icon_from_file(file_name)
		response = chooser.run()
		if response == Gtk.ResponseType.OK:
			self.filename = str(chooser.get_filename())
			self.file.set_text(self.filename)
			head, tail = os.path.split(self.filename)
			fileselected = tail
			if not os.path.isdir(home + fileselected):
				os.mkdir(home + fileselected)
			cmd = 'file -b ' + self.filename
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.fileinfo = self.builder.get_object("entry3")
			self.fileinfo.set_text(str(proc.communicate()[0]))
			chooser.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			chooser.destroy()

	def exif(self, widget):
		self.file = self.builder.get_object("entry1")
		sfile = self.file.get_text()
		if sfile != '':
			self.textview2 = self.builder.get_object("textview2")
			self.textbuffer = self.builder.get_object("textbuffer2")
			sfile = self.file.get_text()
			cmd = 'metadata-extractor2 ' + sfile
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()[0]))
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def strings(self, widget):
		self.file = self.builder.get_object("entry1")
		sfile = self.file.get_text()
		if sfile != '':
			# runs strings command on input file and 
			# outputs the result into textbuffer for display
			self.textview = self.builder.get_object("textview1")
			self.textbuffer = self.builder.get_object("textbuffer1")
			sfile = self.file.get_text()
			cmd = 'strings ' + sfile
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()[0]))
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def strings2(self, widget):
		self.file = self.builder.get_object("entry1")
		sfile = self.file.get_text()
		if sfile != '':
			# runs strings command on input file and 
			# outputs the result into textbuffer for display
			self.file = self.builder.get_object("entry1")
			self.textview = self.builder.get_object("textview1")
			self.textbuffer = self.builder.get_object("textbuffer1")
			sfile = self.file.get_text()
			cmd = 'strings ' + sfile
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()))
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def carveit2(self, widget):
		self.file = self.builder.get_object("entry1")
		sfile = self.file.get_text()
		if sfile != '':
			head, tail = os.path.split(sfile)
			outdir = home + tail + '/scalpel'
			os.mkdir(outdir)
			cmd = 'scalpel -c /etc/scalpel.conf -o ' + outdir + ' ' + sfile
			proc = Popen(cmd, shell = True)
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def jphideit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry5")
		self.spass = self.password.get_text()
		self.fchooser = self.builder.get_object("filechooserbutton1")
		self.hidefile = self.fchooser.get_filename()
		if self.sfile != '' and self.password != '' and self.hidefile != None:
			head, tail = os.path.split(self.sfile)
			outdir = home + tail + '/jphide'
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			self.outfile = outdir + '/' +tail
			if os.path.isfile(self.outfile):
				os.remove(self.outfile)
			child = pexpect.spawn(execdir + '/programs/jphide.sh', [self.sfile, self.outfile, self.hidefile, execdir])
			child.expect('Passphrase:', timeout=2)
			child.sendline(self.spass)
			child.expect('Re-enter  :', timeout=2)
			child.sendline(self.spass)
			child.expect(pexpect.EOF)
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def jpseekit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry4")
		self.spass = self.password.get_text()
		if self.sfile != '' and self.password != '':
			head, tail = os.path.split(self.sfile)
			outdir = home + tail + '/jpseek'
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			self.outfile = outdir + '/' + tail + '.txt'
			if os.path.isfile(self.outfile):
				os.remove(self.outfile)
			child = pexpect.spawn(execdir + '/programs/jpseek.sh', [self.sfile, self.outfile, execdir])
			child.expect('Passphrase:', timeout=2)
			child.sendline(self.spass)
			child.expect(pexpect.EOF)
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def __init__(self):
		gladefile = "SSAK.glade"
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


SSAK=SSAK()
Gtk.main()
