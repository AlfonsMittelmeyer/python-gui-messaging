def main(parent):

	Button('Layout',text="""ON""",bg='green').grid(column='3',sticky='ew',row='0')
	Button('Create',text="""ON""",bg='green').grid(column='1',sticky='ew',row='1')
	Button('Config',text="""ON""",bg='green').grid(column='1',sticky='ew',row='0')
	Label('Label',text="""Config:""",width='6').grid(row='0')
	Label('Label',text="""Layout:""").grid(column='2',row='0')
	Label('Label',text="""Create:""",width='6').grid(row='1')

### CODE ===================================================

	# The command is initialized with config options switched off (False)
	# When pressed, this switch is toggled and a message 'SHOW_CONFIG' is sent, which contains this ON/OFF value
	# Further the button text is toggled between ON and OFF and the bg color between green and orange

	widget("Config").mydata = False
	widget("Layout").mydata = False
	widget("Create").mydata = True

	def function(me):
		me.mydata = not me.mydata
		send("SHOW_CONFIG",me.mydata)
		if me.mydata: me.config(text="OFF",bg="orange")
		else: me.config(text="ON",bg="green")

	widget("Config").do_command(function,wishWidget=True)

	# This button is nearly the same, but sends a 'SHOW_LAYOUT' message

	def function(me):
		me.mydata = not me.mydata
		send("SHOW_LAYOUT",me.mydata)
		if me.mydata: me.config(text="OFF",bg="orange")
		else: me.config(text="ON",bg="green")

	widget("Layout").do_command(function,wishWidget=True)

	# This button is nearly the same, but sends a 'HIDE_CREATE' message

	def function(me):
		me.mydata = not me.mydata
		send("HIDE_CREATE",me.mydata)
		if not me.mydata: me.config(text="OFF",bg="orange")
		else: me.config(text="ON",bg="green")

	widget("Create").do_command(function,wishWidget=True)

	send("HIDE_CREATE",True)

### ========================================================
