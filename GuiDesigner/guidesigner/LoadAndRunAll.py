
### CODE ===================================================
import os

def show_load_dialog(msg,root = widget('/'),os=os):
    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'Backup.py',
        'parent' : root,
        'title' : 'Load & Run: ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Scripts') }
    
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
        send("SHOW_SELECTION_UPDATE")

do_receive('LOAD_RUN_ALL',show_load_dialog,wishMessage=True)
### ========================================================
