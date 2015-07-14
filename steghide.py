import os, pwd, sys, re, urlparse, time, fcntl
from gi.repository import Gtk, GObject
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

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
		if self.steghidefile != "None" and self.sfile != "" and self.hpass != "":
			if self.enc == "none":
				encryption = " -e none -p " + self.hpass + " "
			else:
				if self.enc == "wake" or self.enc == "arcfour" or self.enc == "enigma":
					encryption = " -e " + self.enc + " stream -p " + self.hpass + " "
				else:
					encryption = " -e " + self.enc + " cbc -p " + self.hpass + " "
			head, tail = os.path.split(self.sfile)
			outdir = home + tail + '/steghide'
			self.outfile2 = outdir + '/' + tail
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			cmd = re.escape(execdir) + "/programs/steghide --embed -ef " + self.steghidefile + options + encryption + " -cf " + self.sfile + " -sf " + self.outfile2
			print cmd
			proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
			line = str(proc.communicate()[1])
			self.buffer1.set_text(line)
			self.showdiag()
		else:
			self.buffer1.set_text("You must select a cover file from the file menu, a message file and a passphrase!")
			self.showdiag()
