### CODE ===================================================

def show_save_dialog(msg,root = widget('/')):

    file_opt = options = {}
    options['defaultextension'] = '.py'
    options['filetypes'] = [('python files', '.py'),('all files', '.*')]
    options['initialfile'] = 'guiexportnames.py'
    options['parent'] = root
    options['title'] = 'Export Tk with names: ' + msg

    name = tkFileDialog.asksaveasfilename(**file_opt)
    if name:
        
        import os
        if os.path.exists(name):

            head,tail = os.path.split(name)
            readfile = os.path.join(head,"~"+tail)
            if os.path.exists(readfile):
                os.remove(readfile)
            os.rename(name,readfile)
            readhandle = open(readfile,'r')

        else: readhandle = None

        fh = open(name,'w')
        currentSelection = Selection()
        gotoRoot()
        _Selection._container = _TopLevelRoot._container
        result = saveExport(readhandle,fh,True)
        setSelection(currentSelection)
        fh.close()
        if readhandle != None: readhandle.close()
        if result !='OK':
            messagebox.showerror("Export failed",result,parent=root)

do_receive('EXPORT_ALL_NAMES',show_save_dialog,wishMessage=True)



### ========================================================
