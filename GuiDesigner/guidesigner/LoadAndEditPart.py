### CODE ===================================================
import os

def show_load_dialog_part2(msg,root = widget('/'),os=os):

    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'guipart.py',
        'parent' : root,
        'title' : 'Load & Edit (part): ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Scripts') }

    filename = tkFileDialog.askopenfilename(**file_opt)
    if filename:
        selection_before = Selection()
        setLoadForEdit(True)
        DynLoad(filename)
        setLoadForEdit(False)
        setSelection(selection_before)
        send('SELECTION_CHANGED') # for grid layout: must do an on enter
        send('SHOW_SELECTION_UPDATE')

do_receive('LOAD_EDIT_PART2',show_load_dialog_part2,wishMessage=True)

#def show_load_dialog_part1(msg,cont=container()):

    #if this() != container():
    #    goIn()
    #    send('SHOW_SELECTION')
    #send('LOAD_EDIT_PART2',msg)

do_receive('LOAD_EDIT_PART',show_load_dialog_part2,wishMessage=True)
### ========================================================

