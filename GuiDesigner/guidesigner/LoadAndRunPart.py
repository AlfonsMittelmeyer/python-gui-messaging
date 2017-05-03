### CODE ===================================================

def show_load_dialog_part2(msg,root = widget('/')):

    file_opt = options = {}
    options['defaultextension'] = '.py'
    options['filetypes'] = [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')]
    options['initialfile'] = 'Backup.py'
    options['parent'] = root
    options['title'] = 'Load & Run (part): ' + msg
    
    filename = tkFileDialog.askopenfilename(**file_opt)
    if filename:
        selection_before = Selection()
        setLoadWithCode(True)
        DynLoad(filename)
        setLoadWithCode(False)
        setSelection(selection_before)
        send('SHOW_SELECTION_UPDATE')

do_receive('LOAD_RUN_PART2',show_load_dialog_part2,wishMessage=True)

def show_load_dialog_part1(msg,cont=container()):

    if this() != container():
        goIn()
        send('SHOW_SELECTION')
    send('LOAD_RUN_PART2',msg)

do_receive('LOAD_RUN_PART',show_load_dialog_part1,wishMessage=True)
### ========================================================

