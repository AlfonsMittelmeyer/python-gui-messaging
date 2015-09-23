def main(parent):

	Button("gotoRoot",text="\\\\")	
	pack(side=LEFT)

	Button("gotoTopLevel",text="\\\\\\\\")	
	pack(side=LEFT)

	Button("refresh",text="refresh")	
	pack(side=LEFT)

	Button("unlayout",text="unlayout")
	pack(side=LEFT,anchor=W)

	Button("rename",text="rename")
	pack(side=LEFT,anchor=W)

	Button("destroy",text="destroy")
	pack(side=LEFT,anchor=W)

### CODE ===================================================

	def do_goRoot():
		gotoRoot()
		send('SELECTION_CHANGED',this())

	widget("gotoRoot").do_command(do_goRoot)


	def go_TopRoot():
		gotoTop()
		send('SELECTION_CHANGED',this())

	widget("gotoTopLevel").do_command(go_TopRoot)

	widget("refresh").do_command(lambda: send('SELECTION_CHANGED',this()))

	def do_unlayout():
		if this().Layout & 7:
			unlayout()
			send('BASE_LAYOUT_WIDGET_CHANGED',this())
			send("SELECTION_LAYOUT_CHANGED")

	widget("unlayout").do_command(do_unlayout)

	def do_rename(cont = container()):
		if _Selection._widget == _Selection._container: messagebox.showinfo('rename container "."',"""
Please rename containers from outside!
Select: '<='""",parent=cont)
		else: send("RENAME_WIDGET",getNameAndIndex())

	widget("rename").do_command(do_rename)

	def do_destroy(cont = container()):
		if _Selection._widget == _Selection._container:
			push("destroy container content")
			if messagebox.askyesno("destroy container content","destroy container content\nReally?",parent=cont):
				container().destroyActions()
				container().destroyContent()
				send('SHOW_SELECTION')
		else:
			name_ind = getNameAndIndex()
			if name_ind[1] == -1: text = 'destroy '+"'"+name_ind[0]+"'"
			else: text = 'destroy '+"'"+name_ind[0] + ' [' + str(name_ind[1])+']'+"'"
			if messagebox.askyesno(text,text+'\nReally?',parent=cont):
				destroyElement(name_ind[0],name_ind[1])
				cdDir()
				send("SELECTION_CHANGED",this())

	widget("destroy").do_command(do_destroy)

### ========================================================

