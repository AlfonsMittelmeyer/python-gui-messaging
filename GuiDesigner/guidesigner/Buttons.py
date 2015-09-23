def main(parent):

	Frame("Buttons1",link="guidesigner/Buttons1.py")
	pack()

	Frame("Buttons2",link="guidesigner/Buttons2.py")
	pack(fill=X)

	LabelFrame("LoadFrame",link="guidesigner/LoadFrame.py") # the frame with the save dialog
	LabelFrame("LoadEdit",link="guidesigner/LoadEdit.py") # the frame with the load dialog
	LabelFrame("SaveFrame",link="guidesigner/SaveFrame.py") # the frame with the save dialog
	LabelFrame("RenameFrame",link="guidesigner/RenameFrame.py") # the frame with the rename dialog
