import os, pwd, sys, re, urlparse, time, fcntl, struct
from gi.repository import Gtk, GObject
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

class stegdetect:

	def showprogress(self):
		def hideprogress(widget):
			os.system("kill " + str(self.pid))
			self.showstatus.hide()
		self.statusbutton.connect("clicked",hideprogress)
		self.showstatus.show()

	def stegdet(self, widget):
		jsteg = ("OFF", "ON")[self.checkbuttonjs.get_active()]
		outguess = ("OFF", "ON")[self.checkbuttonog.get_active()]
		jphide = ("OFF", "ON")[self.checkbuttonjph.get_active()]
		invisible = ("OFF", "ON")[self.checkbuttoninv.get_active()]
		f5 = ("OFF", "ON")[self.checkbuttonf5.get_active()]
		camapp = ("OFF", "ON")[self.checkbuttonca.get_active()]
		tests = "-t "
		if jsteg == "ON":
			tests += "j"
		if outguess == "ON":
			tests += "o"
		if jphide == "ON":
			tests += "p"
		if invisible == "ON":
			tests += "i"
		if f5 == "ON":
			tests += "F"
		if camapp == "ON":
			tests += "a"
		size = self.sensitivity.get_value_as_int()
		self.sfile = self.file.get_text()
		wholedir = ("OFF", "ON")[self.checkdir.get_active()]
		if wholedir == "ON" or self.sfile != "":
			directory = self.dircheck.get_uri()
			if wholedir == "ON" and directory == None:
				self.buffer1.set_text("You need to select a directory")
				self.showdiag()
			elif wholedir == "OFF":
				cmd = re.escape(execdir) + "/programs/" + self.arch + "/stegdetect " + tests + " -s " + str(size) + " " + re.escape(self.sfile)
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				line = ''
				for append in proc.stdout:
					line += append
				for append in proc.stderr:
					line += append
				self.buffer1.set_text(line)
				self.showdiag()
			elif wholedir == "ON":
				cdir = urlparse.urlparse(directory).path
				cmd = re.escape(execdir) + "/programs/" + self.arch + "/stegdetect " + tests + " -s " + str(size) + " " + re.escape(cdir) + "/*.jpg " + re.escape(cdir) + "/*.jpeg"
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				line = ''
				for append in proc.stdout:
					line += append
				for append in proc.stderr:
					line += append
				if line == "":
					self.buffer1.set_text("No jpg or jpeg images in that directory")
					self.showdiag()
				else:
					self.buffer1.set_text(line)
					self.showdiag()
		else:
			self.buffer1.set_text("You must select a file or directory")
			self.showdiag()

	def stegcrack(self, widget):
		outguess = ("OFF", "ON")[self.checkoutguess.get_active()]
		jphide = ("OFF", "ON")[self.checkjph.get_active()]
		jsteg = ("OFF", "ON")[self.checkjsteg.get_active()]
		dictionary = self.dict.get_filename()
		self.sfile = self.file.get_text()
		tests = " -t "
		if outguess == "ON":
			tests += "o"
		if jphide == "ON":
			tests += "p"
		if jsteg == "ON":
			tests += "j"

		if self.sfile != '' and dictionary != None:
			self.buffer3.set_text("Please Wait \n")
			cmd = re.escape(execdir) + "/programs/" + self.arch + "/stegbreak " + tests + " -r " + re.escape(execdir) + "/programs/noarch/rules.ini -f " + re.escape(dictionary) + " " + self.sfile
			self.showprogress()
			p = Popen("exec " + cmd, shell=True, stdout=PIPE, stderr=PIPE)
			self.pid = p.pid
			def test_io_watch(f, cond):
				out = f.readline()
				if out == '':
					return False
				end_iter = self.buffer3.get_end_iter()
				self.buffer3.insert(end_iter, out)
				adj = self.sw.get_vadjustment()
				adj.set_value(adj.get_upper() - adj.get_page_size())
				return True
			def tester():
				if p.poll() is None:
					time.sleep(5)
					GObject.timeout_add(2000, update)
					return True			
			GObject.io_add_watch(p.stderr, GObject.IO_IN | GObject.IO_HUP, test_io_watch)
			GObject.io_add_watch(p.stdout, GObject.IO_IN | GObject.IO_HUP, test_io_watch)
			def update():
				os.system("kill -s 2 " + str(self.pid))
			GObject.idle_add(tester)
		else:
			self.buffer1.set_text("You must select a stego file and a dictionary file.")
			self.showdiag()





		
