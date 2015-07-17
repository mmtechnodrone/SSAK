import os, pwd, sys, re, urlparse, time, fcntl, struct
from gi.repository import Gtk, GObject
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

arch = str(8 * struct.calcsize("P"))

class steghide:
	
	def stegembed(self, widget):
		checkcompress = self.builder.get_object("checkbutton14")
		compress = ("OFF", "ON")[checkcompress.get_active()]
		checksum = self.builder.get_object("checkbutton15")
		sumit = ("OFF", "ON")[checksum.get_active()]
		checkname = self.builder.get_object("checkbutton16")
		nameit = ("OFF", "ON")[checkname.get_active()]
		self.enctype = self.builder.get_object("comboboxtext3")
		self.enc = (self.enctype.get_active_text())
		self.steghpass = self.builder.get_object("entry8")
		self.hpass = self.steghpass.get_text()
		self.steghchooser = self.builder.get_object("filechooserbutton5")
		self.steghidefile = str(self.steghchooser.get_filename())
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		options = " -f "
		if compress == "OFF":
			options += " -Z "
		if sumit == "OFF":
			options += " -K "
		if nameit == "OFF":
			options += " -N "
		encryption = ""
		if self.steghidefile != "None" and self.sfile != "":
			if self.enc == "none":
				encryption = " -e none"
			else:
				if self.enc == "wake" or self.enc == "arcfour" or self.enc == "enigma":
					encryption = " -e " + self.enc + " stream "
				else:
					encryption = " -e " + self.enc + " cbc "
			head, tail = os.path.split(self.sfile)
			outdir = home + tail + '/steghide'
			self.outfile2 = outdir + '/' + tail
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			cmd = re.escape(execdir) + "/programs/" + arch + "/steghide --embed -ef " + self.steghidefile + options + encryption + " -cf " + re.escape(self.sfile) + " -sf " + re.escape(self.outfile2) + " -p '" + self.hpass + "'"
			proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
			line = str(proc.communicate()[1])
			self.buffer1.set_text(line)
			self.showdiag()
		else:
			self.buffer1.set_text("You must select a cover file from the file menu and a message file")
			self.showdiag()
