### CODE ===================================================
import os

def show_save_dialog(msg,root = widget('/'),os=os):

    file_opt = {
        'defaultextension' : '.py',
        'filetypes' : [('python files', '.py'), ('gui files', '.gui'), ('all files', '*')],
        'initialfile' : 'exp.py',
        'parent' : root,
        'title' : 'Export Tk: ' + msg,
        'initialdir' : os.path.join(os.getcwd(),'Export') }

    name = tkFileDialog.asksaveasfilename(**file_opt)
    if name:
        
        import os
        # we don't like to merge now
        #if os.path.exists(name):
        if False:

            head,tail = os.path.split(name)
            readfile = os.path.join(head,"~"+tail)
            if os.path.exists(readfile):
                os.remove(readfile)
            os.rename(name,readfile)
            readhandle = open(readfile,'r',encoding="utf-8")

        else: readhandle = None

        fh = open(name,'w',encoding="utf-8")
        currentSelection = Selection()
        gotoRoot()
        _Selection._container = _TopLevelRoot._container
        result = saveExport(readhandle,fh)
        setSelection(currentSelection)
        fh.close()
        if readhandle != None: readhandle.close()
        if result !='OK':
            messagebox.showerror("Export failed",result,parent=root)

do_receive('EXPORT_ALL_TK',show_save_dialog,wishMessage=True)



### ========================================================

