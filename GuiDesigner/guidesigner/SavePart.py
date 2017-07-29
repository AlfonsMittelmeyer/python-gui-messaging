
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

    name = tkFileDialog.asksaveasfilename(**file_opt)
    if name:
        fh = open(name,'w',encoding="utf-8")
        currentSelection = Selection()
        saveWidgets(fh)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_WIDGET_PART',show_save_dialog,wishMessage=True)



def show_save_dialog_config(msg,root = widget('/'),os=os):
    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'guipart.py',
        'parent' : root,
        'title' : 'Save (part): ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Scripts') }

    name = tkFileDialog.asksaveasfilename(**file_opt)
    if name:
        fh = open(name,'w',encoding="utf-8")
        currentSelection = Selection()
        saveWidgets(fh,True)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_WIDGET_PART_CONFIG',show_save_dialog_config,wishMessage=True)


### ========================================================

