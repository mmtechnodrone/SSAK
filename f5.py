import os, pwd, sys, re, struct, time
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))
stegprog = 'java -jar ' + re.escape(execdir) + '/programs/noarch/f5.jar '

arch = str(8 * struct.calcsize("P"))

class f5:

	def f5embed(self, widget):
		f5embedf = self.builder.get_object("filechooserbutton9")
		f5embedfile = str(f5embedf.get_filename())
		getf5quality = self.builder.get_object("spinbutton3")
		f5quality = getf5quality.get_value_as_int()
		self.getf5pass = self.builder.get_object("entry14")
		f5pass = self.getf5pass.get_text()
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.fileinfo = self.builder.get_object("entry3")
		filetype = self.fileinfo.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		getusecomment = self.builder.get_object("checkbutton21")
		getcomment = self.builder.get_object("entry12")
		usecomment = ("OFF", "ON")[getusecomment.get_active()]
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/f5embed'
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		outfile = outdir + '/'+ tail
		if self.sfile != '' and str.strip(f5pass) != '' and f5embedfile != None:
			if "JPEG" in filetype:
				insertcomment = ''
				if usecomment =="ON" and getcomment.get_text() != "":
					insertcomment = ' -c ' + re.escape(getcomment.get_text())
				if usecomment == "ON" and getcomment.get_text() == "":
					self.buffer1.set_text("If comment box checked you must enter a comment!")
					self.showdiag()	
				else:
					cmd = stegprog + 'e -e ' + re.escape(f5embedfile) + ' -p ' + re.escape(f5pass) + ' -q ' + str(f5quality) + ' ' + insertcomment + ' ' + re.escape(self.sfile) + ' ' + re.escape(outfile)
					print cmd
					proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
					pid = proc.pid
					pid2 = int(proc.pid) + 1
					print pid2
					time.sleep(2)
					os.system("kill " + str(pid) + ' ' + str(pid2))
					print pid
					self.buffer1.set_text("If successful the output file should exist here: \n" + outfile)
					self.showdiag()
			else:
				self.buffer1.set_text("Input file must be jpeg!")
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid input JPEG input file, a valid hide file and a password")
			self.showdiag()

	def f5extract(self, widget):
		self.buffer1 = self.builder.get_object("textbuffer3")
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.f5extpass = self.builder.get_object("entry13")
		extpass = self.f5extpass.get_text()
		self.fileinfo = self.builder.get_object("entry3")
		filetype = self.fileinfo.get_text()
		head, tail = os.path.split(self.sfile)
		outdir = home + tail + '/f5extract'
		outfile = outdir + '/' + tail
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		if self.sfile != '' and str.strip(extpass):
			if "JPEG" in filetype:
				cmd = stegprog + 'x -p ' + re.escape(extpass) + ' -e ' + re.escape(outfile) + ' ' + re.escape(self.sfile)
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				self.buffer1.set_text("If successful the output file should exist here: \n" + outfile)
				self.showdiag()
			else:
				self.buffer1.set_text("Input file must be jpeg!")
				self.showdiag()
		else:
			self.buffer1.set_text("You must inputa valid JPEG input file and a password")
			self.showdiag()

