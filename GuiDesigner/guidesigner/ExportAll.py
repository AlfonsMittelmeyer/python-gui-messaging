config(**{'grid_cols': '(3, 66, 0, 0)', 'grid_multi_cols': '[3, (0, 40, 0, 0), (1, 153, 0, 0), (2, 50, 0, 0)]', 'grid_rows': '(3, 25, 0, 0)'})

Button('Cancel',**{'text': 'Quit'}).grid(**{'column': '1', 'sticky': 'e', 'row': '2'})
Entry('FileName',**{'width': '28'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '3', 'row': '1'})
Label('IOError',**{'text': "Couldn't open file", 'fg': 'red'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '3', 'row': '3'})
Label('Label',**{'text': 'Save:'}).grid(**{'sticky': 'e', 'row': '0'})
Label('Label',**{'text': 'File:'}).grid(**{'sticky': 'e', 'row': '1'})
Label('Name',**{'text': 'element', 'bg': 'yellow'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '3', 'row': '0'})
Button('OK',**{'text': 'OK'}).grid(**{'column': '2', 'sticky': 'e', 'row': '2'})
Label('error_double',**{'text': 'Error:', 'fg': 'red'}).grid(**{'column': '0', 'sticky': 'w', 'columnspan': '5', 'row': '4'})

### CODE ===================================================

def save_module(ioerror = widget("IOError"), fname = widget("FileName"), cont = container(),err_double=widget('error_double')):
    ioerror.unlayout()
    err_double.unlayout()
    name = fname.get()

    import os
    if os.path.exists(name):
        head,tail = os.path.split(name)
        readfile = os.path.join(head,"~"+tail)
        if os.path.exists(readfile):
            os.remove(readfile)
        os.rename(name,readfile)
        readhandle = open(readfile,'r')

    else: readhandle = None

    try:
        fh = open(name,'w')
        currentSelection = Selection()
        gotoRoot()
        _Selection._container = _TopLevelRoot._container
        result = saveExport(readhandle,fh,True)
        setSelection(currentSelection)
        fh.close()
        if readhandle != None: readhandle.close()
        if result=='OK': cont.unlayout()
        else:
            err_double['text'] = result
            err_double.grid()
    except IOError: ioerror.grid()

widget("OK").do_command(save_module)
widget("FileName").do_event('<Return>',save_module)

widget("Cancel").do_command(lambda cont = container(): cont.unlayout())

do_receive('SELECTION_CHANGED',lambda cont = container(): cont.unlayout())

def show_frame(msg,wname = widget("Name"), fname = widget("FileName"), cont = container(), ioerror = widget("IOError"),err_double=widget('error_double')):
    wname['text'] = msg;
    fname.delete(0,END) # prepare an empty Entry for the user input
    ioerror.unlayout() # IOError
    err_double.unlayout()
    cont.pack() # show the LoadFrame
    fname.focus_set() # and focus the entry

do_receive('EXPORT_ALL_NAMES',show_frame,wishMessage=True)
### ========================================================
