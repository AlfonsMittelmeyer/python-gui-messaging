### CODE ===================================================

def show_save_dialog(msg,root = widget('/')):
    file_opt = options = {}
    options['defaultextension'] = '.py'
    options['filetypes'] = [('python files', '.py'),('all files', '.*')]
    options['initialfile'] = 'accesscontainers.py'
    options['parent'] = root
    options['title'] = 'Save Access Containers: ' + msg

    name = tkFileDialog.asksaveasfilename(**file_opt)
    if name:
        fh = open(name,'w',encoding="utf-8")
        currentSelection = Selection()
        gotoRoot()
        _Selection._container = _TopLevelRoot._container
        saveAccess(fh)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_ACCESS_CONTAINERS_ALL',show_save_dialog,wishMessage=True)

### ========================================================

