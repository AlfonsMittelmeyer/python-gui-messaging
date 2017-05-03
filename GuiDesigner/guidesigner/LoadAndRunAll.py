
### CODE ===================================================

def show_load_dialog(msg,root = widget('/')):
    file_opt = options = {}
    options['defaultextension'] = '.py'
    options['filetypes'] = [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')]
    options['initialfile'] = 'Backup.py'
    options['parent'] = root
    options['title'] = 'Load & Run: ' + msg
    
    filename = tkFileDialog.askopenfilename(**file_opt)
    if filename:
        gotoRoot()
        container().destroyActions()
        container().destroyContent()
        clear_grid(container())
        setLoadWithCode(True)
        DynLoad(filename)
        setLoadWithCode(False)
        send("SELECTION_CHANGED")

do_receive('LOAD_RUN_ALL',show_load_dialog,wishMessage=True)

### ========================================================
