import os, pwd, sys, gi, time, re, struct
from subprocess import Popen, PIPE
from gi.repository import Gtk

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

arch = str(8 * struct.calcsize("P"))

class fileops:

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
		chooser.connect("delete-event", lambda window, event: chooser.hide() or True)

	def ident(self):
		self.outfile
		cmd = 'file -b ' + re.escape(self.outfile)
		proc = Popen(cmd, shell = True,stdout=PIPE).communicate()[0]
		self.fileinfo = self.builder.get_object("entry3")
		for cake in proc.splitlines():
			print cake
			if "ASCII" in cake:
				os.rename(self.outfile,self.outfile + ".txt")
				self.outfile = self.outfile + ".txt"
			elif "PNG" in cake:
				os.rename(self.outfile,self.outfile + ".png")
				self.outfile = self.outfile + ".png"
			elif "GIF" in cake:
				os.rename(self.outfile,self.outfile + ".gif")
				self.outfile = self.outfile + ".gif"
			elif "PC bitmap" in cake:
				os.rename(self.outfile,self.outfile + ".bmp")
				self.outfile = self.outfile + ".bmp"
			elif "SVG Scalable Vector Graphics image" in cake:
				os.rename(self.outfile,self.outfile + ".svg")
				self.outfile = self.outfile + ".svg"
			elif "MP4" in cake:
				os.rename(self.outfile,self.outfile + ".mp4")
				self.outfile = self.ourfile + ".mp4"
			elif "ISO 9660" in cake:
				os.rename(self.outfile,self.outfile + ".iso")
				self.outfile = self.outfile + ".iso"
			elif "gzip" in cake:
				os.rename(self.outfile,self.outfile + ".gz")
				self.outfile = self.outfile + ".gz"
			elif "7-zip" in cake:
				os.rename(self.outfile,self.outfile + ".7z")
				self.outfile = self.outfile + ".7z"
			elif "Zip" in cake:
				os.rename(self.outfile,self.outfile + ".zip")
				self.outfile = self.outfile + ".zip"
			elif "bzip2" in cake:
				os.rename(self.outfile,self.outfile + ".bz2")
				self.outfile = self.outfile + ".bz2"
			elif "XZ compressed data" in cake:
				os.rename(self.outfile,self.outfile + ".xz")
				self.outfile = self.outfile + ".xz"
			elif "HTML" in cake:
				os.rename(self.outfile,self.outfile + ".html")
				self.outfile = self.outfile + ".html"
			elif "PDF" in cake:
				os.rename(self.outfile,self.outfile + ".PDF")
				self.outfile = self.outfile + ".pdf"
			elif "XML document text" in cake:
				os.rename(self.outfile,self.outfile + ".xml")
				self.outfile = self.outfile + ".xml"
			elif "Microsoft Word" in cake:
				os.rename(self.outfile,self.outfile + ".doc")
				self.outfile = self.outfile + ".doc"
			elif "Microsoft PowerPoint" in cake:
				os.rename(self.outfile,self.outfile + ".ppt")
				self.outfile = self.outfile + ".ppt"
			elif "OpenDocument Text" in cake:
				os.rename(self.outfile,self.outfile + ".odt")
				self.outfile = self.outfile + ".odt"
			elif "OpenDocument Presentation" in cake:
				os.rename(self.outfile,self.outfile + ".odp")
				self.outfile = self.outfile + ".odp"
			elif "PE32 executable (DLL) (GUI)" in cake:
				os.rename(self.outfile,self.outfile + ".dll")
				self.outfile = self.outfile + ".dll"
			elif "PE32 executable (GUI)" in cake:
				os.rename(self.outfile,self.outfile + ".exe")
				self.outfile = self.outfile + ".exe"
			elif "Java archive data" in cake:
				os.rename(self.outfile,self.outfile + ".jar")
				self.outfile = self.outfile + ".jar"
			elif "POSIX shell script" in cake:
				os.rename(self.outfile,self.outfile + ".sh")
				self.outfile = self.outfile + ".sh"
			elif "ELF 32-bit LSB shared object" in cake:
				os.rename(self.outfile,self.outfile + ".so")
				self.outfile = self.outfile + ".so"
			elif "Debian binary package" in cake:
				os.rename(self.outfile,self.outfile + ".deb")
				self.outfile = self.outfile + ".deb"
			elif "RPM" in cake:
				os.rename(self.outfile,self.outfile + ".rpm")
				self.outfile = self.outfile + ".rpm"
			elif "MPEG ADTS, layer III" in cake:
				os.rename(self.outfile,self.outfile + ".mp3")
				self.outfile = self.outfile + ".mp3"
			elif "Vorbis audio" in cake:
				os.rename(self.outfile,self.outfile + ".ogg")
				self.outfile = self.outfile + ".ogg"
			elif "Python script" in cake:
				os.rename(self.outfile,self.outfile + ".py")
				self.outfile = self.outfile + ".py"


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
				cmd = 'java -cp ' + re.escape(execdir) + '/programs/noarch/metadata-extractor2-2.jar:' + re.escape(execdir) + '/programs/noarch/xmpcore.jar com.drew.imaging.ImageMetadataReader ' + re.escape(sfile)			
				proc = Popen(cmd, shell = True,stdout=PIPE)
				self.textbuffer.set_text(str(proc.communicate()[0]))
			else:
				self.textbuffer.set_text("File must be jpeg/jpg!!!")	
		else:	
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()
						
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
			cmd = re.escape(execdir) + '/programs/' + arch + '/strings ' + re.escape(sfile)
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()[0]))
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()

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
			cmd = re.escape(execdir) + '/programs/' + arch + '/strings ' + re.escape(sfile)
			proc = Popen(cmd, shell = True,stdout=PIPE)
			self.textbuffer.set_text(str(proc.communicate()))
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()

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
			cmd = re.escape(execdir) + '/programs/' + arch + '/foremost -c ' + re.escape(execdir) + '/programs/noarch/foremost.conf -o ' + re.escape(outdir) + ' -i ' + re.escape(sfile)
			proc = Popen(cmd, shell = True)
			self.buffer1.set_text("Output files in " + outdir + "!")	
			self.showdiag()
		else:
			self.buffer1.set_text("Please select a file from the file menu!")	
			self.showdiag()

