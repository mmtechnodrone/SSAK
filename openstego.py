import os, pwd, sys, pexpect, gi, re
from gi.repository import Gtk
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))
stegprog = 'java -jar ' + re.escape(execdir) + '/programs/noarch/openstego.jar '

class openstego:

	def togglepass(self, widget, data=None):
		value=''
		self.pass2 = self.builder.get_object("entry7")
		value = ("OFF", "ON")[widget.get_active()]
		if value == "OFF":
			self.pass2.set_property("editable", False)
		if value == "ON":
			self.pass2.set_property("editable", True)

	def togglepass2(self, widget, data=None):
		value=''
		self.pass4 = self.builder.get_object("entry6")
		value = ("OFF", "ON")[widget.get_active()]
		if value == "OFF":
			self.pass4.set_property("editable", False)
		if value == "ON":
			self.pass4.set_property("editable", True)

	def ostegembed2(self, widget):
		checkbutton3 = self.builder.get_object("checkbutton3")
		value = ("OFF", "ON")[checkbutton3.get_active()]
		checkbutton2 = self.builder.get_object("checkbutton2")
		value2 = ("OFF", "ON")[checkbutton2.get_active()]
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.pass2 = self.builder.get_object("entry7")
		self.spass = self.pass2.get_text()
		self.algorithm = self.builder.get_object("comboboxtext2")
		self.alg = (self.algorithm.get_active())
		if self.alg == 0:
			self.algorithm2 = "RandomLSB"
		elif self.alg == 1:
			self.algorithm2 = "LSB"
		self.fchooser2 = self.builder.get_object("filechooserbutton2")
		self.hidefile2 = str(self.fchooser2.get_filename())
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/openstegembed'
		self.outfile2 = outdir + '/' + tail + '.png'
		self.buffer1 = self.builder.get_object("textbuffer3")
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		self.outfile2 = outdir + '/' + tail + '.png'
		if os.path.isfile(self.outfile2):
			os.remove(self.outfile2)
		if self.hidefile2 != "None" and self.sfile != '':
			if value =="ON" and str.strip(self.spass) == '':
				self.buffer1.set_text("If you select the password option you must fill in the password entry!")
				self.showdiag()
			else:			
				cmd = stegprog + ' --embed --algorithm ' + self.algorithm2 + ' --messagefile ' + re.escape(self.hidefile2) + ' --coverfile ' + re.escape(self.sfile) + ' --stegofile ' + re.escape(self.outfile2)
				if value2 == "ON":
					cmd += ' --compress '
				elif value2 == "OFF":
					cmd += ' --nocompress '
				if value == "ON":
					cmd += ' --encrypt --password ' + self.spass
				elif value == "OFF":
					cmd += ' --noencrypt'
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				line = str(proc.communicate()[1])
				if str.strip(line) == '':
					self.buffer1.set_text("Output file should exist here: " + self.outfile2)
				else:
					self.buffer1.set_text(line)
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid image file and a file to be hidden.")
			self.showdiag()	

	def ostegextract2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		checkbutton4 = self.builder.get_object("checkbutton1")
		value3 = ("OFF", "ON")[checkbutton4.get_active()]
		self.algorithm2 = self.builder.get_object("comboboxtext1")
		self.pass3 = self.builder.get_object("entry6") 
		self.spass = self.pass3.get_text()
		self.alg2 = (self.algorithm2.get_active())	
		self.fileinfo = self.builder.get_object("entry3")
		self.info = self.fileinfo.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		if self.alg2 == 0:
			self.algorithm3 = "RandomLSB"
		elif self.alg2 == 1:
			self.algorithm3 = "LSB"
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/openstegextract'
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		if self.sfile != '' and "PNG" in self.info:
			if value3 == "ON" and str.strip(self.spass) == '':
				self.buffer1.set_text("If you select the password option you must fill in the password entry!")
				self.showdiag()
			else:
				cmd = stegprog + ' extract --algorithm=' + self.algorithm3 + ' --stegofile=' + re.escape(self.sfile) + ' --extractdir=' + re.escape(outdir)
				if value3 == "ON":
					cmd += ' --password=' + self.spass
				proc = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
				line = str(proc.communicate()[1])
				self.buffer1.set_text(line)
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid PNG file before performing any operations. Please select a valid PNG file using the file menu!")
			self.showdiag()
			




	








