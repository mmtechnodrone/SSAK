import os, pwd, sys, pexpect, re, struct

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

arch = str(8 * struct.calcsize("P"))

class jphs:

	def jphideit2(self, widget):
		os.environ["WINEDEBUG"] = "warn-all,-heap,-relay,err-all,fixme-all,trace-all"
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry5")
		self.spass = self.password.get_text()
		self.fchooser = self.builder.get_object("filechooserbutton1")
		self.hidefile = self.fchooser.get_filename()
		self.buffer1 = self.builder.get_object("textbuffer3")
		checkwin = self.builder.get_object("checkbutton18")
		self.fileinfo = self.builder.get_object("entry3")
		filetype = self.fileinfo.get_text()
		if self.sfile != '' and str.strip(self.spass) != '' and self.hidefile != None:
			if "JPEG" in filetype:
				head, tail = os.path.split(self.sfile)
				needwin = ("OFF", "ON")[checkwin.get_active()]
				if needwin == "ON":
					outdir = home + tail + '/jphidewin'
					progcmd = "/usr/bin/wine " + re.escape(execdir) + "/programs/Win/jphide.exe " 
				else:
					outdir = home + tail + '/jphidelin'
					progcmd = execdir + "/programs/" + arch + "/jphide "
				if not os.path.isdir(outdir):
					os.mkdir(outdir)
				self.outfile = outdir + '/' +tail
				if os.path.isfile(self.outfile):
					os.remove(self.outfile)
				cmd = progcmd + re.escape(self.sfile) + " " + re.escape(self.outfile) + " " + re.escape(self.hidefile)
				child = pexpect.spawn(cmd)
				child.expect('Passphrase:')
				child.sendline(self.spass)
				child.expect('Re-enter  :')
				child.sendline(self.spass)
				child.expect(pexpect.EOF)
				self.buffer1.set_text("Output file should be located here: " + self.outfile + "!")
				self.showdiag()
			else:
				self.buffer1.set_text("Input file must be jpeg!")
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid input JPEG input file, a valid hide file and a password")
			self.showdiag()

	def jpseekit2(self, widget):
		os.environ["WINEDEBUG"] = "warn-all,-heap,-relay,err-all,fixme-all,trace-all"
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry4")
		self.spass = self.password.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		self.fileinfo = self.builder.get_object("entry3")
		checkwin = self.builder.get_object("checkbutton19")
		filetype = self.fileinfo.get_text()
		if self.sfile != '' and self.spass != '':
			if "JPEG" in filetype:
				head, tail = os.path.split(self.sfile)
				needwin = ("OFF", "ON")[checkwin.get_active()]
				if needwin == "ON":
					outdir = home + tail + '/jpseekwin'
					progcmd = "/usr/bin/wine " + re.escape(execdir) + "/programs/Win/jpseek.exe " 
				else:
					outdir = home + tail + '/jpseeklin'
					progcmd = execdir + "/programs/" + arch + "/jpseek "
				if not os.path.isdir(outdir):
					os.mkdir(outdir)
				self.outfile = outdir + '/' + tail + '.txt'
				if os.path.isfile(self.outfile):
					os.remove(self.outfile)
				cmd = progcmd + re.escape(self.sfile) + " " + re.escape(self.outfile)
				child = pexpect.spawn(cmd)
				child.expect('Passphrase:')
				child.sendline(self.spass)
				child.expect(pexpect.EOF)
				self.buffer1.set_text("Output file should be located here: " + self.outfile + "!")
				self.showdiag()
				os.chmod(self.outfile, 0o600)
			else:
				self.buffer1.set_text("Input file must be jpeg!")
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid file, and insert a password")
			self.showdiag()

