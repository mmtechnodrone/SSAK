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
		out1 = ("OFF", "ON")[extractpassbox.get_active()]
		outguessver = self.builder.get_object("checkbutton22")
		out2 = ("OFF", "ON")[outguessver.get_active()]
		pass2 = self.ogpass2.get_text()
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.fileinfo = self.builder.get_object("entry3")
		self.info = self.fileinfo.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		head, tail = os.path.split(self.sfile)
		cmd = ''
		outdir = home + tail + '/outguessextract'
		if out2 == "ON":
			prog = re.escape(execdir) + "/programs/" + arch + "/outguess_0.13"
		else:
			prog = re.escape(execdir) + "/programs/" + arch + "/outguess_0.2"
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		if self.sfile != '':
			if 'JPEG' or 'JPG' or 'PNM' or 'PPM' in self.info:
				if out1 == "ON":
					if str.strip(pass2) == '':	
						self.buffer1.set_text("You must enter a password if the password box is checked!")	
						self.showdiag()		
					else:
						cmd = prog + " -r -k " + re.escape(pass2) + " " + re.escape(self.sfile) + " " + re.escape(outdir) + "/outguessoutput"
						proc = Popen(cmd, shell = True,stdout=PIPE)
						self.buffer1.set_text("Output should be at " + outdir + "/outguessoutput")
						self.showdiag()
				else:
					cmd = prog + " -r " + re.escape(self.sfile) + " " + re.escape(outdir) + "/outguessoutput"
					print cmd
					proc = Popen(cmd, shell = True,stdout=PIPE)
					self.buffer1.set_text("Output should be at " + outdir + "/outguessoutput")
					self.showdiag()
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()
