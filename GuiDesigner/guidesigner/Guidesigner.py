def main(parent):

	Toplevel("DynTkInterGuiDesigner",title="DynTkInter GuiDesigner",link="guidesigner/Modules.py")

### CODE ===================================================

	def top_level_closed(msg):
		if not widget_exists(msg._widget): send('SELECTION_CHANGED')
		else: setSelection(msg)

	do_receive('TOPLEVEL_CLOSED',top_level_closed,wishMessage=True)

	cdApp()
	send("SELECTION_CHANGED")

### ========================================================

