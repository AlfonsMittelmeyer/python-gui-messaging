def main(parent):

	### NAME CreateFrame	
	CreateFrame = Frame(parent)
	load_Script(CreateFrame,"guidesigner/CreateFrame.py")
	CreateFrame.grid(sticky='n',row='0')

	### NAME CreateAndLayout
	CreateAndLayout = Frame(parent)
	load_Script(CreateAndLayout,"guidesigner/CreateAndLayout.py",)
	CreateAndLayout.grid(column='1',sticky='n',row='0')
	
	### NAME ConfigOptions
	ConfigOptions = LabelFrame(parent)
	load_Script(ConfigOptions,"guidesigner/ConfigOptions.py")
	ConfigOptions.grid(row='0', column='2',sticky='n')

	### NAME DetailedLayout
	DetailedLayout = Frame(parent)
	gui.load_Script(DetailedLayout,"guidesigner/DetailedLayout.py")
	DetailedLayout.grid(row='0',column='3',sticky='n')

	### NAME Selection
	Selection = LabelFrame(parent)
	gui.load_Script(Selection,"guidesigner/Selection.py")
	Selection.grid(row = '0',column = '4', sticky='n')

	### CODE ===================================================

	ConfigOptions.grid_remove()
	DetailedLayout.grid_remove()

	### ========================================================

