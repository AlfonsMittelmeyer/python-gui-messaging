### CODE ===================================================
import os

def show_save_dialog(msg,root = widget('/'),os=os):
    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'guiall.py',
        'parent' : root,
        'title' : 'Save (part): ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Scripts') }

    fh = tkFileDialog.asksaveasfile(mode='w', **file_opt)
    if fh != None:
        currentSelection = Selection()
        gotoRoot()
        saveWidgets(fh,True,True)
        setSelection(currentSelection)
        fh.close()

do_receive('SAVE_ALL',show_save_dialog,wishMessage=True)


def save_backup(msg,root=container().myRoot(),os=os):
    try:
        fh = open(os.path.join(os.getcwd(),'Scripts','Backup.py'),'w')

        currentSelection = Selection()
        gotoRoot()
        saveWidgets(fh,True,True)
        setSelection(currentSelection)
        fh.close()
        messagebox.showinfo("Save Backup","Backup for '"+msg+"' saved in File 'Backup.py'",parent=root)
    except IOError: messagebox.showerror("Save Backup failed","Couldn't open File 'Backup.py'",parent=root)

do_receive('SAVE_BACKUP',save_backup,wishMessage=True)

### ========================================================

