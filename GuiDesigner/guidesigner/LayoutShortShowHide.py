def main(parent):

	LabelFrame('PackLayout',link="guidesigner/PackLayout.py")
	grid(sticky='ew',row='0')

	LabelFrame('GridLayout',link="guidesigner/GridLayout.py")
	grid(sticky='ew',row='1')

	LabelFrame('PlaceLayout',link="guidesigner/PlaceLayout.py")
	grid(sticky='ew',row='2')

### CODE ===================================================

	# A routine for the pack and he grid layout: pack and grid must not occur in the same parent. ------------------------------------
	# This would cause a system hang up of TkInter. If the parent (container) contains already the other layout (pack or grid),
	# the pack or grid portion will be hidden (unlayout)

	def hide_pack_or_grid(msg):
		if getContLayouts(container()) & msg[0]:
			if msg[1].Layout != NOLAYOUT: msg[1].unlayout()
		elif msg[1].Layout == NOLAYOUT: msg[1].grid()

	do_receive('HIDELAYOUT_PackOrGrid',hide_pack_or_grid,wishMessage=True)

	# full action for new or changed widgets
	# for LAYOUTNEVER the LabelFrame LayoutShortShowHide has to be hidden and otherwise shown
	# sends a BASE_LAYOUT_REFRESH to inside for the pack, grid and place portions
	# sends a SHOW_LAYOUT for the layout details options
	# sends a SHOW_SELECTION for showing, which widget is selected 

	def base_layout_widget_changed(cont = container()):
		if this().Layout == LAYOUTNEVER: cont.unlayout()
		elif cont.Layout == NOLAYOUT: cont.grid()
		send("BASE_LAYOUT_REFRESH",this())
		send("SHOW_LAYOUT",this())

	do_receive('BASE_LAYOUT_WIDGET_CHANGED',base_layout_widget_changed)

### ========================================================
