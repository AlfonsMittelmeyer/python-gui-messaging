Label(text="Save:").rcgrid(0,0,sticky=E)
Label("Name",text="element",bg="yellow").rcgrid(0,1,sticky=W)
Label(text ="File:"),rcgrid(2,0,sticky=E)
Entry("FileName").rcgrid(2,1,columnspan=3)
Button("Cancel",text="Quit").rcgrid(3,2,sticky=E)
Button("OK",text="OK").rcgrid(3,3,sticky=E)
Label("IOError",text="Couldn't open file",fg="red").rcgrid(4,0,columnspan=4)

### CODE ===================================================

def save_module(ioerror = widget("IOError"), fname = widget("FileName"), cont = container()):
    ioerror.unlayout()
    try:
        fh = open(fname.get(),'w')

        currentSelection = Selection()
        saveWidgets(fh,True)
        setSelection(currentSelection)
        fh.close()
        cont.unlayout()
    except IOError: ioerror.grid()

widget("OK").do_command(save_module)
widget("FileName").do_event('<Return>',save_module)

widget("Cancel").do_command(lambda cont = container(): cont.unlayout())

do_receive('SELECTION_CHANGED',lambda cont = container(): cont.unlayout())

def show_frame(msg,wname = widget("Name"), fname = widget("FileName"), cont = container(), ioerror = widget("IOError")):

    wname['text'] = msg;
    fname.delete(0,END) # prepare an empty Entry for the user input
    ioerror.unlayout() # IOError
    cont.pack() # show the LoadFrame
    fname.focus_set() # and focus the entry

do_receive('SAVE_WIDGET_PART',show_frame,wishMessage=True)
### ========================================================

