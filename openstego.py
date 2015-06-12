import os, pwd, sys, pexpect
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))
stegprog = 'java -jar ' + execdir + '/programs/openstego.jar '

class openstego:

	def togglepass(self, widget, data=None):
		value=''
		self.pass2 = self.builder.get_object("entry7")
		value = ("OFF", "ON")[widget.get_active()]
		if value == "OFF":
			self.pass2.set_property("editable", False)
		if value == "ON":
			self.pass2.set_property("editable", True)

	def showerr(self):
		def hidedialog(widget):
			self.nofiledialog.hide()
		self.nofiledialog = self.builder.get_object("dialog1")
		self.nofiledialogbutton = self.builder.get_object("button5")
		self.nofiledialogbutton.connect("clicked",hidedialog)
		self.nofiledialog.show()
		
	def embed(self):
		checkbutton3 = self.builder.get_object("checkbutton3")
		value = ("OFF", "ON")[checkbutton3.get_active()]
		checkbutton2 = self.builder.get_object("checkbutton2")
		value2 = ("OFF", "ON")[checkbutton2.get_active()]
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/openstegembed'
		self.outfile2 = outdir + '/' + tail + '.png'
		if os.path.isfile(self.outfile2):
			os.remove(self.outfile2)
		cmd = stegprog + ' --embed --algorithm ' + self.algorithm2 + ' --messagefile ' + self.hidefile2 + ' --coverfile ' + self.sfile + ' --stegofile ' + self.outfile2
		if value2 == "ON":
			cmd += ' --compress '
		elif value2 == "OFF":
			cmd += ' --nocompress '
		if value == "ON":
			cmd += ' --encrypt --password ' + self.spass
		elif value == "OFF":
			cmd += ' --noencrypt'
		print cmd
		proc = Popen(cmd, shell = True)

	def ostegembed2(self, widget):
		checkbutton3 = self.builder.get_object("checkbutton3")
		value = ("OFF", "ON")[checkbutton3.get_active()]
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
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		self.outfile2 = outdir + '/' + tail + '.png'
		if self.hidefile2 != "None" and self.sfile != '' and self.outfile2 != '':
			if value =="ON" and self.spass == '':
				self.showerr()
			else:			
				self.embed()
		else:
			self.showerr()		

			













