import os, pwd, sys, pexpect, re, urlparse
from gi.repository import Gtk
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

class stegdetect:

	def showdiag(self):
		def hidedialog(widget):
			self.nofiledialog.hide()
		self.nofiledialog = self.builder.get_object("dialog1")
		self.nofiledialogbutton = self.builder.get_object("button5")
		self.nofiledialogbutton.connect("clicked",hidedialog)
		self.nofiledialog.show()

	def stegdet(self, widget):
		checkbuttonjs = self.builder.get_object("checkbutton5")
		jsteg = ("OFF", "ON")[checkbuttonjs.get_active()]
		checkbuttonog = self.builder.get_object("checkbutton6")
		outguess = ("OFF", "ON")[checkbuttonog.get_active()]
		checkbuttonjph = self.builder.get_object("checkbutton7")
		jphide = ("OFF", "ON")[checkbuttonjph.get_active()]
		checkbuttoninv = self.builder.get_object("checkbutton8")
		invisible = ("OFF", "ON")[checkbuttoninv.get_active()]
		checkbuttonf5 = self.builder.get_object("checkbutton9")
		f5 = ("OFF", "ON")[checkbuttonf5.get_active()]
		checkbuttonca = self.builder.get_object("checkbutton10")
		camapp = ("OFF", "ON")[checkbuttonca.get_active()]
		self.buffer1 = self.builder.get_object("textbuffer3")
		tests = "-t "
		if jsteg == "ON":
			tests += "j"
		if outguess == "ON":
			tests += "o"
		if jphide == "ON":
			tests += "p"
		if invisible == "ON":
			tests += "i"
		if f5 == "ON":
			tests += "F"
		if camapp == "ON":
			tests += "a"
		sensitivity = self.builder.get_object("spinbutton1")
		size = sensitivity.get_value_as_int()
		self.buffer = self.builder.get_object("textbuffer5")
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		checkdir = self.builder.get_object("checkbutton4")
		wholedir = ("OFF", "ON")[checkdir.get_active()]
		if wholedir == "ON" or self.sfile != "":
			self.dircheck = self.builder.get_object("filechooserbutton3")
			directory = self.dircheck.get_uri()
			if wholedir == "ON" and directory == None:
				self.buffer1.set_text("You need to select a directory")
				self.showdiag()
			elif wholedir == "OFF":
				cmd = re.escape(execdir) + "/programs/stegdetect " + tests + " -s " + str(size) + " " + self.sfile
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				line = str(proc.communicate()[0])
				self.buffer1.set_text(line)
				self.showdiag()
			elif wholedir == "ON":
				cdir = urlparse.urlparse(directory).path
				cmd = re.escape(execdir) + "/programs/stegdetect " + tests + " -s " + str(size) + " " + re.escape(cdir) + "/*.jpg " + re.escape(cdir) + "/*.jpeg"
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				line = str(proc.communicate()[0])
				if line == "":
					self.buffer1.set_text("No jpg or jpeg images in that directory")
					self.showdiag()
				else:
					self.buffer1.set_text(line)
					self.showdiag()
		else:
			self.buffer1.set_text("You must select a file or directory")
			self.showdiag()

		
