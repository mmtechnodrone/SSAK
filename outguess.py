import os, pwd, sys, re, struct
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

arch = str(8 * struct.calcsize("P"))

class outguess:

	def embedguess(self, widget):
		self.ogpass = self.builder.get_object("entry10")
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()


	def extractguess(self, widget):
		self.ogpass2 = self.builder.get_object("entry11")
		extractpassbox = self.builder.get_object("checkbutton24")
		pass2 = self.ogpass2.get_text()
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.fileinfo = self.builder.get_object("entry3")
		self.info = self.fileinfo.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/outguessextract'
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		if self.sfile != '':
			if 'JPEG' or 'JPG' or 'PNM' or 'PPM' in self.info:
				cmd = re.escape(execdir) + "/programs/" + arch + "/outguess_0.13 -r -k " + re.escape(pass2) + " " + re.escape(self.sfile) + " " + re.escape(outdir) + "/outguessoutput"
				proc = Popen(cmd, shell = True,stdout=PIPE)
				self.buffer1.set_text("Output should be at " + outdir + "/outguessoutput")
				self.showdiag()
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()
