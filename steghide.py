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
			outdir = home + tail + '/steghide_embed'
			self.outfile2 = outdir + '/' + tail
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			cmd = re.escape(execdir) + "/programs/" + arch +"/steghide --embed -ef " + self.steghidefile + options + encryption + " -cf " + re.escape(self.sfile) + " -sf " + self.outfile2 + " -p '" + self.hpass + "'"
			proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
			line = str(proc.communicate()[1])
			self.buffer1.set_text(line)
			self.showdiag()
		else:
			self.buffer1.set_text("You must select a cover file from the file menu and a message file")
			self.showdiag()

	def steghcrackstatus(self):
		def hidestatus(widget):
			os.system("kill " + str(self.pid))
			self.dontshow = "yes"
			self.progresswindow.hide()
		self.quitbutton = self.builder.get_object("button15")
		self.quitbutton.connect("clicked", hidestatus)
		self.progresswindow.show()

	def stegextract(self, widget):
		self.stegxpass = self.builder.get_object("entry9")
		self.xpass = self.stegxpass.get_text()
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/steghide_extract'
		self.outfile2 = outdir + '/' + tail
		self.stegxchooser = self.builder.get_object("filechooserbutton6")
		self.stegpassfile = str(self.stegxchooser.get_filename())
		self.buffer1 = self.builder.get_object("textbuffer3")
		self.progressbar = self.builder.get_object("progressbar1")
		self.progresswindow = self.builder.get_object("window2")
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		self.dontshow = "no"
		if self.sfile == "":
			self.buffer1.set_text("You must select a steg file to analyze/extract")
			self.showdiag()
		elif "button1" in self.activeradio:
			if self.stegpassfile == "None":
				self.buffer1.set_text("You must select a password dictionary to perform a password attack!")				
				self.showdiag()
			else:
				self.line = ''
				cmd = re.escape(execdir) + "/programs/" + arch + "/steghide extract -sf " + re.escape(self.sfile) + " -f -pf " + re.escape(self.stegpassfile) + " -xf " + re.escape(self.outfile2)
				self.steghcrackstatus()			
				proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
				self.pid = proc.pid
				def test_io_watch(f, cond):
					out = f.readline()
					if out == '':
						return False
					self.line += out
					return True
				def tester():
					if proc.poll() is None:
						self.progressbar.set_pulse_step(.25)
						self.progressbar.pulse()
						time.sleep(.5)
						return True	
					else:
						self.progresswindow.hide()
						self.buffer1.set_text(self.line)
						if not "yes" in self.dontshow:					
							self.showdiag()
				GObject.io_add_watch(proc.stderr, GObject.IO_IN | GObject.IO_HUP, test_io_watch)
				GObject.io_add_watch(proc.stdout, GObject.IO_IN | GObject.IO_HUP, test_io_watch)
				GObject.idle_add(tester)
		elif "button2" in self.activeradio:
			cmd = re.escape(execdir) + "/programs/" + arch + "/steghide extract -sf " + re.escape(self.sfile) + " -p " + self.xpass + " -f -xf " + re.escape(self.outfile2)
			proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
			line = ''
			for append in proc.stdout:
				line += append
			for append in proc.stderr:
				line += append
			self.buffer1.set_text(line)
			self.showdiag()
		elif "button3" in self.activeradio:
			cmd = re.escape(execdir) + "/programs/" + arch + "/steghide info " + re.escape(self.sfile) + " -p " + self.xpass + "''"
			proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
			line = ''
			for append in proc.stdout:
				line += append
			for append in proc.stderr:
				line += append
			self.buffer1.set_text(line)
			self.showdiag()
