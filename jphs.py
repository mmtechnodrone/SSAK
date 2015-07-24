import os, pwd, sys, pexpect, re, struct

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

arch = str(8 * struct.calcsize("P"))

class jphs:

	def jphideit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry5")
		self.spass = self.password.get_text()
		self.fchooser = self.builder.get_object("filechooserbutton1")
		self.hidefile = self.fchooser.get_filename()
		self.buffer1 = self.builder.get_object("textbuffer3")
		self.fileinfo = self.builder.get_object("entry3")
		filetype = self.fileinfo.get_text()
		if self.sfile != '' and str.strip(self.spass) != '' and self.hidefile != None:
			if "JPEG" in filetype:
				head, tail = os.path.split(self.sfile)
				outdir = home + tail + '/jphide'
				if not os.path.isdir(outdir):
					os.mkdir(outdir)
				self.outfile = outdir + '/' +tail
				if os.path.isfile(self.outfile):
					os.remove(self.outfile)
				bashfile = open(execdir + "/programs/" + arch + "/jphide.sh", "w")
				bashfile.write("#!/bin/bash \n \n")
				bashfile.write("cd " + re.escape(execdir) + "/programs/" + arch + " \n")
				bashfile.write(execdir + "/programs/" + arch + "/jphide " + re.escape(self.sfile) + " " + re.escape(self.outfile) + " " + re.escape(self.hidefile))
				bashfile.close()
				mode = os.stat(execdir + "/programs/" + arch + "/jphide.sh").st_mode
				mode |= (mode &0o444) >> 2
				os.chmod(execdir + "/programs/" + arch + "/jphide.sh", mode)
				child = pexpect.spawn(execdir + '/programs/' + arch + '/jphide.sh')
				child.expect('Passphrase:', timeout=2)
				child.sendline(self.spass)
				child.expect('Re-enter  :', timeout=2)
				child.sendline(self.spass)
				child.expect(pexpect.EOF)
				self.buffer1.set_text("Output file should be located here: " + self.outfile + "!")
				self.showdiag()
				os.remove(execdir + "/programs/" + arch + "/jphide.sh")
			else:
				self.buffer1.set_text("Input file must be jpeg!")
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid input JPEG input file, a valid hide file and a password")
			self.showdiag()

	def jpseekit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry4")
		self.spass = self.password.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		self.fileinfo = self.builder.get_object("entry3")
		filetype = self.fileinfo.get_text()
		if self.sfile != '' and self.spass != '':
			if "JPEG" in filetype:
				head, tail = os.path.split(self.sfile)
				outdir = home + tail + '/jpseek'
				if not os.path.isdir(outdir):
					os.mkdir(outdir)
				self.outfile = outdir + '/' + tail + '.txt'
				if os.path.isfile(self.outfile):
					os.remove(self.outfile)
				bashfile = open(execdir + "/programs/" + arch + "/jpseek.sh", "w")
				bashfile.write("#!/bin/bash \n \n")
				bashfile.write("cd " + re.escape(execdir) + "/programs/" + arch + " \n")
				bashfile.write(execdir + "/programs/" + arch + "/jpseek " + re.escape(self.sfile) + " " + re.escape(self.outfile))
				bashfile.close()
				mode = os.stat(execdir + "/programs/" + arch + "/jpseek.sh").st_mode
				mode |= (mode &0o444) >> 2
				os.chmod(execdir + "/programs/" + arch + "/jpseek.sh", mode)
				child = pexpect.spawn(execdir + '/programs/' + arch + '/jpseek.sh')
				child.expect('Passphrase:', timeout=2)
				child.sendline(self.spass)
				child.expect(pexpect.EOF)
				self.buffer1.set_text("Output file should be located here: " + self.outfile + "!")
				self.showdiag()
				os.remove(execdir + "/programs/" + arch + "/jpseek.sh")
				os.chmod(self.outfile, 0o600)
			else:
				self.buffer1.set_text("Input file must be jpeg!")
				self.showdiag()
		else:
			self.buffer1.set_text("You must select a valid file, and insert a password")
			self.showdiag()
