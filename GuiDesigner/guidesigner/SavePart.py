
### CODE ===================================================
import os

def show_save_dialog(msg,root = widget('/'),os=os):
    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'guipart.py',
        'parent' : root,
        'title' : 'Save (part): ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Scripts') }

    fh = tkFileDialog.asksaveasfile(mode='w', **file_opt)
    if fh != None:
        currentSelection = Selection()
        saveWidgets(fh,True)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_WIDGET_PART',show_save_dialog,wishMessage=True)
### ========================================================

