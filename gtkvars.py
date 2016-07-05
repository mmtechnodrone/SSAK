import struct
from gi.repository import Gtk, GObject

class gtkvars:
	
	def setvars(self):

		# globals
		self.window = self.builder.get_object("window1")
		self.arch = str(8 * struct.calcsize("P"))
		self.file = self.builder.get_object("entry1")
		self.fileinfo = self.builder.get_object("entry3")
		self.buffer1 = self.builder.get_object("textbuffer3")

		# menu items
		self.selectfile = self.builder.get_object("imagemenuitem1")
		self.exit = self.builder.get_object("imagemenuitem4")
		self.carveit = self.builder.get_object("imagemenuitem2")
		self.stegspy = self.builder.get_object("imagemenuitem3")
		self.diit = self.builder.get_object("imagemenuitem5")
		self.bmppacker = self.builder.get_object("imagemenuitem7")
		self.terminal = self.builder.get_object("imagemenuitem8")

		# strings
		self.readstrings1 = self.builder.get_object("button1")
		self.readstrings2 = self.builder.get_object("button3")
		self.textview = self.builder.get_object("textview1")
		self.stextbuffer = self.builder.get_object("textbuffer1")

		# exif
		self.readexif = self.builder.get_object("button2")
		self.textbuffer = self.builder.get_object("textbuffer2")
		self.textview2 = self.builder.get_object("textview2")

		# showdiag vars
		self.nofiledialog = self.builder.get_object("dialog1")
		self.nofiledialogbutton = self.builder.get_object("button5")

		# about dialog
		self.about = self.builder.get_object("imagemenuitem10")
		self.aboutwin = self.builder.get_object("window3")
		self.aboutclose = self.builder.get_object("button16")
	
		# jphide
		self.jphideit = self.builder.get_object("button6")
		self.password = self.builder.get_object("entry5")
		self.fchooser = self.builder.get_object("filechooserbutton1")
		self.checkwin = self.builder.get_object("checkbutton18")

		# jpseek
		self.jpseekit = self.builder.get_object("button9")
		self.password2 = self.builder.get_object("entry4")
		self.checkwin2 = self.builder.get_object("checkbutton19")

		#openstego
		self.pass2 = self.builder.get_object("entry7")
		self.pass4 = self.builder.get_object("entry6")

		# openstegembed
		self.ostegembed = self.builder.get_object("button8")
		self.checkbutton2 = self.builder.get_object("checkbutton2")
		self.checkbutton3 = self.builder.get_object("checkbutton3")
		self.algorithm = self.builder.get_object("comboboxtext2")
		self.fchooser2 = self.builder.get_object("filechooserbutton2")

		# openstegextract
		self.ostegextract = self.builder.get_object("button7")
		self.checkbutton4 = self.builder.get_object("checkbutton1")
		self.checkbutton4 = self.builder.get_object("checkbutton1")
		self.algorithm2 = self.builder.get_object("comboboxtext1")
		self.pass3 = self.builder.get_object("entry6")
		self.buffer2 = self.builder.get_object("textbuffer6")
		self.tw = self.builder.get_object("textview7")
		self.sw = self.builder.get_object("scrolledwindow6")
		self.passattack = self.builder.get_object("checkbutton17")
		self.passfilechoose = self.builder.get_object("filechooserbutton7")
		self.showstatus = self.builder.get_object("dialog2")
		self.statusbutton = self.builder.get_object("button12")

		# outguess embed
		self.outembed = self.builder.get_object("button17")
		self.ogpass = self.builder.get_object("entry10")
		self.extractpassbox = self.builder.get_object("checkbutton25")
		self.hidefile = self.builder.get_object("filechooserbutton8")
		self.outguessver = self.builder.get_object("checkbutton20")
		self.getformat = self.builder.get_object("comboboxtext3")
		self.getquality = self.builder.get_object("spinbutton2")

		# outguess extract
		self.outextract = self.builder.get_object("button18")
		self.ogpass2 = self.builder.get_object("entry11")
		self.extractpassbox2 = self.builder.get_object("checkbutton24")
		self.outguessver2 = self.builder.get_object("checkbutton22")

		# f5 embed
		self.f5embedf = self.builder.get_object("filechooserbutton9")
		self.f5embedit = self.builder.get_object("button19")
		self.getf5quality = self.builder.get_object("spinbutton3")
		self.gettimeout = self.builder.get_object("spinbutton4")
		self.getf5pass = self.builder.get_object("entry14")
		self.getusecomment = self.builder.get_object("checkbutton21")
		self.getcomment = self.builder.get_object("entry12")

		# f5 extract
		self.f5extractit = self.builder.get_object("button20")
		self.f5extpass = self.builder.get_object("entry13")

		# stegdetect
		self.steg = self.builder.get_object("button11")
		self.showstatus = self.builder.get_object("dialog2")
		self.statusbutton = self.builder.get_object("button12")
		self.checkbuttonjs = self.builder.get_object("checkbutton5")
		self.checkbuttonog = self.builder.get_object("checkbutton6")
		self.checkbuttonjph = self.builder.get_object("checkbutton7")
		self.checkbuttoninv = self.builder.get_object("checkbutton8")
		self.checkbuttonf5 = self.builder.get_object("checkbutton9")
		self.checkbuttonca = self.builder.get_object("checkbutton10")
		self.sensitivity = self.builder.get_object("spinbutton1")
		self.buffer = self.builder.get_object("textbuffer5")
		self.checkdir = self.builder.get_object("checkbutton4")
		self.dircheck = self.builder.get_object("filechooserbutton3")

		# stegbreak
		self.stegc = self.builder.get_object("button10")
		self.buffer3 = self.builder.get_object("textbuffer6")
		self.checkoutguess = self.builder.get_object("checkbutton11")
		self.checkjph = self.builder.get_object("checkbutton12")
		self.checkjsteg = self.builder.get_object("checkbutton13")
		self.dict = self.builder.get_object("filechooserbutton4")
		self.tw = self.builder.get_object("textview7")
		self.sw = self.builder.get_object("scrolledwindow6")

		# steghide
		self.stegh = self.builder.get_object("button13")
		self.checkcompress = self.builder.get_object("checkbutton14")
		self.checksum = self.builder.get_object("checkbutton15")
		self.checkname = self.builder.get_object("checkbutton16")
		self.enctype = self.builder.get_object("comboboxtext3")
		self.steghpass = self.builder.get_object("entry8")
		self.steghchooser = self.builder.get_object("filechooserbutton5")

		# stegextract
		self.stegx = self.builder.get_object("button14")
		self.stegradio1 = self.builder.get_object("radiobutton1")
		self.stegradio2 = self.builder.get_object("radiobutton2")
		self.stegradio3 = self.builder.get_object("radiobutton3")
		self.quitbutton = self.builder.get_object("button15")
		self.stegxpass = self.builder.get_object("entry9")
		self.stegxchooser = self.builder.get_object("filechooserbutton6")
		self.progressbar = self.builder.get_object("progressbar1")
		self.progresswindow = self.builder.get_object("window2")








