import os, pwd, sys, re, urlparse, time, fcntl
from gi.repository import Gtk, GObject
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

class stegdetect:

	def showdiag(self):
		def hidedialog(widget):
			self.nofiledialog.hide()
		self.nofiledialog = self.builder.get_object("dialog1")
		self.nofiledialogbutton = self.builder.get_object("button5")
		self.nofiledialogbutton.connect("clicked",hidedialog)
		self.nofiledialog.show()

	def showprogress(self):
		def hideprogress(widget):
			os.system("kill " + str(self.pid))
			self.showstatus.hide()
		self.showstatus = self.builder.get_object("dialog2")
		self.statusbutton = self.builder.get_object("button12")
		self.statusbutton.connect("clicked",hideprogress)
		self.showstatus.show()

	def stegdet(self, widget):
		checkbuttonjs = self.builder.get_object("checkbutton5")
		jsteg = ("OFF", "ON")[checkbuttonjs.get_active()]
		checkbuttonog = self.builder.get_object("checkbutton6")
		outguess = ("OFF", "ON")[checkbuttonog.get_active()]
		checkbuttonjph = self.builder.get_object("checkbutton7")
		jphide = ("OFF", "ON")[checkbuttonjph.get_active()]
		checkbuttoninv = self.builder.get_object("checkbutton8")
		invisible = ("OFF", "ON")[checkbuttoninv.get_active()]
		checkbuttonf5 = self.builder.get_object("checkbutton9")
		f5 = ("OFF", "ON")[checkbuttonf5.get_active()]
		checkbuttonca = self.builder.get_object("checkbutton10")
		camapp = ("OFF", "ON")[checkbuttonca.get_active()]
		self.buffer1 = self.builder.get_object("textbuffer3")
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
		sensitivity = self.builder.get_object("spinbutton1")
		size = sensitivity.get_value_as_int()
		self.buffer = self.builder.get_object("textbuffer5")
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		checkdir = self.builder.get_object("checkbutton4")
		wholedir = ("OFF", "ON")[checkdir.get_active()]
		if wholedir == "ON" or self.sfile != "":
			self.dircheck = self.builder.get_object("filechooserbutton3")
			directory = self.dircheck.get_uri()
			if wholedir == "ON" and directory == None:
				self.buffer1.set_text("You need to select a directory")
				self.showdiag()
			elif wholedir == "OFF":
				cmd = re.escape(execdir) + "/programs/stegdetect " + tests + " -s " + str(size) + " " + re.escape(self.sfile)
				proc = Popen(cmd, shell = True, stderr=PIPE, stdout=PIPE)
				line = str(proc.communicate()[0])
				self.buffer1.set_text(line)
				self.showdiag()
			elif wholedir == "ON":
				cdir = urlparse.urlparse(directory).path
				cmd = re.escape(execdir) + "/programs/stegdetect " + tests + " -s " + str(size) + " " + re.escape(cdir) + "/*.jpg " + re.escape(cdir) + "/*.jpeg"
				proc = Popen(cmd, shell = True, stdout=PIPE)
				line = ''
				for append in proc.stdout:
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
		self.buffer1 = self.builder.get_object("textbuffer6")
		checkoutguess = self.builder.get_object("checkbutton11")
		outguess = ("OFF", "ON")[checkoutguess.get_active()]
		checkjph = self.builder.get_object("checkbutton12")
		jphide = ("OFF", "ON")[checkjph.get_active()]
		checkjsteg = self.builder.get_object("checkbutton13")
		jsteg = ("OFF", "ON")[checkjsteg.get_active()]
		self.dict = self.builder.get_object("filechooserbutton4")
		dictionary = self.dict.get_filename()
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.tw = self.builder.get_object("textview7")
		self.sw = self.builder.get_object("scrolledwindow6")
		tests = " -t "
		if outguess == "ON":
			tests += "o"
		if jphide == "ON":
			tests += "p"
		if jsteg == "ON":
			tests += "j"

		if self.sfile != '' and dictionary != None:
			self.buffer1.set_text("Please Wait \n")
			cmd = re.escape(execdir) + "/programs/stegbreak " + tests + " -r " + re.escape(execdir) + "/programs/noarch/rules.ini -f " + re.escape(dictionary) + " " + self.sfile
			print cmd
			self.showprogress()
			p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
			fd = p.stdout.fileno()
			file_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
			fcntl.fcntl(fd, fcntl.F_SETFL, file_flags | os.O_NDELAY)
			self.pid = p.pid
			def test_io_watch(f, cond):
				out = f.readline()
				if out == '':
					return False
				end_iter = self.buffer1.get_end_iter()
				self.buffer1.insert(end_iter, out)
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
			newbuff = self.builder.get_object("textbuffer3")
			newbuff.set_text("You must select a stego file and a dictionary file.")
			self.showdiag()





		
