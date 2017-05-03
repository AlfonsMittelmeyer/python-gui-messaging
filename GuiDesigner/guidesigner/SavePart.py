
### CODE ===================================================

def show_save_dialog(msg,root = widget('/')):
    file_opt = options = {}
    options['defaultextension'] = '.py'
    options['filetypes'] = [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')]
    options['initialfile'] = 'guipart.py'
    options['parent'] = root
    options['title'] = 'Save (part): ' + msg

    fh = tkFileDialog.asksaveasfile(mode='w', **file_opt)
    if fh != None:
        currentSelection = Selection()
        saveWidgets(fh,True)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_WIDGET_PART',show_save_dialog,wishMessage=True)
### ========================================================

