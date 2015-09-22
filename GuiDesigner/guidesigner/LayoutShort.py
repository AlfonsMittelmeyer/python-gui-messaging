def main(parent):

	LabelFrame('LayoutShortShowHide',text="""Layout""",link="guidesigner/LayoutShortShowHide.py")
	grid(sticky='new',row='0')

### CODE ===================================================

	# ----- message receivers for messages from outside --------------------------------------

	# full actions for a new created widget or a selection of another widget

	def function():
		send('BASE_LAYOUT_WIDGET_CHANGED',this())
		send('BASE_LAYOUT_VALUE_REFRESH')

	do_receive('SELECTION_CHANGED',function)

	# for same widget, but changed values a base layout refresh - handled by pack, grid or place portions - is sufficient
	do_receive('LAYOUT_OPTIONS_CHANGED',lambda: send('BASE_LAYOUT_VALUE_REFRESH'))

	# ----- message receiver for messages from inside to outside --------------------------------------

	# if the layout type wasn't changed, a value change in the layout options is sufficient: message  LAYOUT_VALUES_REFRESH
	# if the widget didn't have a layout before, full actions have to be done, including a selection show, because
	# the selection show also contains, whether the widget has a layout or not
	# if the layout changed, the selection need not be shown new, only an internal refresh and a new show layout options have to be done

	def function(layout_before):
		if layout_before == this().Layout: send('LAYOUT_VALUES_REFRESH',this())
		else:
			send("BASE_LAYOUT_REFRESH",this())
			send("SHOW_LAYOUT",this())
			if layout_before == NOLAYOUT: send('SELECTION_LAYOUT_CHANGED')

	do_receive('BASE_LAYOUT_CHANGED',function,wishMessage=True)

### ========================================================

