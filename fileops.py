import os, pwd, sys, gi, time, re
from subprocess import Popen, PIPE
from gi.repository import Gtk

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

class fileops:

	def showerr(self):
		def hidedialog(widget):
			self.nofiledialog.hide()
		self.nofiledialog = self.builder.get_object("dialog1")
		self.nofiledialogbutton = self.builder.get_object("button5")
		self.nofiledialogbutton.connect("clicked",hidedialog)
		self.nofiledialog.show()

	def fileselect(self, widget):
		self.file = self.builder.get_object("entry1")
		chooser = Gtk.FileChooserDialog("Select file to Analyze", None, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_SAVE,Gtk.ResponseType.OK))
		response = chooser.run()
		if response == Gtk.ResponseType.OK:
			self.filename = str(chooser.get_filename())
			self.file.set_text(self.filename)
			head, tail = os.path.split(self.filename)
			fileselected = tail
			if not os.path.isdir(home + fileselected):
				os.mkdir(home + fileselected)
			cmd = 'file -b ' + re.escape(self.filename)
			proc = Popen(cmd, shell = True,stdout=PIPE).communicate()[0]
			self.fileinfo = self.builder.get_object("entry3")
			for cake in proc.splitlines():
				self.fileinfo.set_text(cake)
			chooser.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			chooser.destroy()

	def exif(self, widget):
		self.file = self.builder.get_object("entry1")
		self.fileinfo = self.builder.get_object("entry3")
		filetype = self.fileinfo.get_text()
		self.textbuffer = self.builder.get_object("textbuffer2")
		self.buffer1 = self.builder.get_object("textbuffer3")
		sfile = self.file.get_text()
		if sfile != '':
			if "JPEG" in filetype:
				self.textview2 = self.builder.get_object("textview2")
				cmd = 'java -cp ' + re.escape(execdir) + '/programs/metadata-extractor2-2.jar:' + re.escape(execdir) + '/programs/xmpcore.jar com.drew.imaging.ImageMetadataReader ' + re.escape(sfile)			
				proc = Popen(cmd, shell = True,stdout=PIPE)
				self.textbuffer.set_text(str(proc.communicate()[0]))
			else:
				self.textbuffer.set_text("File must be jpeg/jpg!!!")	
		else:	
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showerr()
						
	def strings(self, widget):
		self.file = self.builder.get_object("entry1")
		sfile = self.file.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		if sfile != '':
			# runs strings command on input file and 
			# outputs the result into textbuffer for display
			self.textview = self.builder.get_object("textview1")
			self.textbuffer = self.builder.get_object("textbuffer1")
			sfile = self.file.get_text()
			cmd = re.escape(execdir) + '/programs/strings ' + re.escape(sfile)
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()[0]))
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showerr()

	def strings2(self, widget):
		self.file = self.builder.get_object("entry1")
		sfile = self.file.get_text()
		self.buffer1 = self.builder.get_object("textbuffer3")
		if sfile != '':
			# runs strings command on input file and 
			# outputs the result into textbuffer for display
			self.file = self.builder.get_object("entry1")
			self.textview = self.builder.get_object("textview1")
			self.textbuffer = self.builder.get_object("textbuffer1")
			sfile = self.file.get_text()
			cmd = re.escape(execdir) + '/programs/strings ' + re.escape(sfile)
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()))
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showerr()

	def carveit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.buffer1 = self.builder.get_object("textbuffer3")
		sfile = self.file.get_text()
		if sfile != '':
			head, tail = os.path.split(sfile)
			outdir = home + tail + '/foremost'
			if os.path.isdir(outdir):
				cmd = 'rm -rf ' + outdir
				proc = Popen(cmd, shell = True)
				time.sleep(3)
			os.mkdir(outdir)
			cmd = re.escape(execdir) + '/programs/foremost -c ' + re.escape(execdir) + '/programs/foremost.conf -o ' + re.escape(outdir) + ' -i ' + re.escape(sfile)
			proc = Popen(cmd, shell = True)
			self.buffer1.set_text("Output files in " + outdir + "!")	
			self.showerr()
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showerr()

