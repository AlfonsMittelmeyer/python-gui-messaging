Label('Label',text="Load into:").grid(sticky='e',row='0')
Label('Name',bg='yellow').grid(column='1',sticky='w',row='0')
Label('Label',text="File:").grid(sticky='e',row='2')
Entry('FileName').grid(column='1',columnspan='3',row='2',sticky='we')
Button('Cancel',text="""Quit""").grid(column='2',sticky='e',row='3')
Button('OK',text="""OK""").grid(column='3',sticky='e',row='3')
Label("IOError",text="Couldn't open file",fg="red").rcgrid(4,0,columnspan=4)
Message('Message',**{'bg': '#ffffe4', 'width': '220', 'text': 'Caution:\n\nThis will delete the current content', 'relief': 'sunken'}).grid(**{'sticky': 'nesw', 'columnspan': '4', 'padx': '10', 'row': '5'})

### CODE ===================================================

def load_module(ioerror = widget("IOError"), fname = widget("FileName"), cont = container()):
    ioerror.unlayout()
    try:
        fh = open(fname.get(),'r')
        fh.close()
        cont.unlayout()
        # don't do this in the root of the GUI designer
        gotoRoot()
        container().destroyActions()
        container().destroyContent()
        setLoadForEdit(True)
        DynLoad(fname.get())
        setLoadForEdit(False)
        send("SELECTION_CHANGED")
    except IOError: ioerror.grid()

widget("OK").do_command(load_module)
widget("FileName").do_event('<Return>',load_module)
widget("Cancel").do_command(lambda cont = container(): cont.unlayout())

def show_frame(msg,wname = widget("Name"), fname = widget("FileName"), cont = container(), ioerror = widget("IOError")):
    wname['text'] = msg;
    fname.delete(0,END) # prepare an empty Entry for the user input
    ioerror.unlayout() # IOError
    cont.pack() # show the LoadFrame
    fname.focus_set() # and focus the entry

do_receive('LOAD_EDIT_ALL',show_frame,wishMessage=True)
### ========================================================
