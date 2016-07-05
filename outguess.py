import os, pwd, sys, re, struct
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

class outguess:

	def embedguess(self, widget):
		pass1 = self.ogpass.get_text()
		out1 = ("OFF", "ON")[self.extractpassbox.get_active()]
		hidefile2 = str(self.hidefile.get_filename())
		self.sfile = self.file.get_text()
		head, tail = os.path.split(self.sfile)
		self.info = self.fileinfo.get_text()
		out2 = ("OFF", "ON")[self.outguessver.get_active()]
		self.format = (self.getformat.get_active_text())
		quality = self.getquality.get_value_as_int()
		outdir = home + tail + '/outguessembed'
		if out2 == "ON":
			prog = re.escape(execdir) + "/programs/" + self.arch + "/outguess_0.13"
		else:
			prog = re.escape(execdir) + "/programs/" + self.arch + "/outguess_0.2"
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		cmd = ''
		if out2 == "ON":
			prog = re.escape(execdir) + "/programs/" + self.arch + "/outguess_0.13"
		else:
			prog = re.escape(execdir) + "/programs/" + self.arch + "/outguess_0.2"
		if self.sfile != '':
			if hidefile2 != "None":		
				if 'JPEG' or 'JPG' or 'PNM' or 'PPM' in self.info:
					if out1 == "ON":
						if str.strip(pass1) == '':	
							self.buffer1.set_text("You must enter a password if the password box is checked!")	
							self.showdiag()		
						else:
							cmd = prog + ' -p ' + str(quality) + ' -k ' + re.escape(pass1) + ' -d ' + re.escape(hidefile2) + ' ' + re.escape(self.sfile) + ' ' + re.escape(outdir) + '/outguessoutput.jpg'
							proc = Popen(cmd, shell = True,stdout=PIPE)
							self.buffer1.set_text("Output should be at " + outdir + "/outguessoutput")
							self.showdiag()
					else:
						cmd = prog + ' -p ' + str(quality) + ' -d ' + re.escape(hidefile2) + ' ' + re.escape(self.sfile) + ' ' + re.escape(outdir) + '/outguessoutput.jpg'
						proc = Popen(cmd, shell = True,stdout=PIPE)
						self.buffer1.set_text("Output should be at " + outdir + "/outguessoutput")
						self.showdiag()
			else:
				self.buffer1.set_text("Please select a file to embed!")
				self.showdiag()
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()			

	def extractguess(self, widget):
		out1 = ("OFF", "ON")[self.extractpassbox2.get_active()]
		out2 = ("OFF", "ON")[self.outguessver2.get_active()]
		pass2 = self.ogpass2.get_text()
		self.sfile = self.file.get_text()
		self.info = self.fileinfo.get_text()
		head, tail = os.path.split(self.sfile)
		cmd = ''
		outdir = home + tail + '/outguessextract'
		if out2 == "ON":
			prog = re.escape(execdir) + "/programs/" + self.arch + "/outguess_0.13"
		else:
			prog = re.escape(execdir) + "/programs/" + self.arch + "/outguess_0.2"
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
					proc = Popen(cmd, shell = True,stdout=PIPE)
					self.buffer1.set_text("Output should be at " + outdir + "/outguessoutput")
					self.showdiag()
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()
