### CODE ===================================================
import os

def show_load_dialog_part2(msg,root = widget('/'),os=os):

    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'guipart.py',
        'parent' : root,
        'title' : 'Load & Run (part): ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Scripts') }
    
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

