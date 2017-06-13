
### CODE ===================================================

def show_save_dialog(msg,root = widget('/')):
    file_opt = options = {}
    options['defaultextension'] = '.py'
    options['filetypes'] = [('python files', '.py'),('all files', '.*')]
    options['initialfile'] = 'accesswidgets.py'
    options['parent'] = root
    options['title'] = 'Save Access Widgets: ' + msg

    name = tkFileDialog.asksaveasfilename(**file_opt)
    if name:
        fh = open(name,'w',encoding="utf-8")
        currentSelection = Selection()
        gotoRoot()
        _Selection._container = _TopLevelRoot._container
        saveAccess(fh,True)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_ACCESS_WIDGETS_ALL',show_save_dialog,wishMessage=True)


### ========================================================

