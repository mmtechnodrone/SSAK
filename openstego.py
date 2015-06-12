class openstego:

	def togglepass(self, widget, data=None):
		value=''
		self.pass2 = self.builder.get_object("entry7")
		value = ("OFF", "ON")[widget.get_active()]
		print value
		if value == "OFF":
			self.pass2.set_property("editable", False)
		if value == "ON":
			self.pass2.set_property("editable", True)

	def ostegembed2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.pass2 = self.builder.get_object("entry7")
		self.algorithm = self.builder.get_object("comboboxtext2")
		self.alg = self.algorithm.get_active()
		print self.alg
