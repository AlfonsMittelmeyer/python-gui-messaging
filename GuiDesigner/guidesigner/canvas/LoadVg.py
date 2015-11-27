Toplevel('toplevel',**{'title': 'Load vector graphic', 'grid_cols': '(4, 10, 0, 0)', 'grid_rows': '(13, 10, 0, 0)'})
goIn()

Label('IoError',**{'text': "Couldn't open file", 'font': 'TkDefaultFont 9 bold', 'fg': 'red'}).grid(**{'column': '1', 'columnspan': '3', 'row': '11'})
Button('OK',**{'text': 'OK', 'width': 5}).grid(**{'column': '2', 'sticky': 'e', 'row': '9'})
Entry('file').grid(**{'column': '2', 'sticky': 'w', 'row': '7'})
Spinbox('height',**{'increment': 10.0, 'from': 10.0, 'width': 6, 'to': 10000.0}).grid(**{'column': '2', 'sticky': 'w', 'row': '5'})
Label('lfile',**{'text': 'file'}).grid(**{'column': '1', 'row': '7'})
Label('lheight',**{'text': 'height'}).grid(**{'column': '1', 'row': '5'})
Label('ltag',**{'text': 'tag'}).grid(**{'column': '1', 'row': '3'})
Entry('tag',**{'width': 10}).grid(**{'column': '2', 'sticky': 'w', 'row': '3'})
Label('title',**{'text': 'Load Vector Graphic', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '2', 'row': '1'})

### CODE ===================================================


class Access:
    
    def __init__(self,canvas_paint):
        
        self.canvas_paint = canvas_paint
        self.tag = widget('tag')
        self.filename = widget('file')
        self.height = widget('height')
        self.io_error = widget('IoError')
        self.io_error.unlayout()
        
        self.tag.delete(0,END)
        self.filename.delete(0,END)
        self.height.delete(0,END)

        self.tag.delete(0,END)
        self.height.insert(0,str(canvas_paint.pytkvg_height))
        self.filename.insert(0,canvas_paint.pytkvg_file)
        self.root = widget('/')
        canvas_paint.pytkvg_tag = ''


        self.ok = widget('OK')
        

        def isPosIntOkay(keyval,value,reason):
            if reason == 'focusout':
                try:
                    check = int(value)
                    return check >=1
                except ValueError:
                    return False

            elif reason == 'key':
                return keyval.isdigit()
            return True


        def _invalid_entry(widgetName,reason):
            if reason == 'focusout':
                widget = self.root.nametowidget(widgetName)
                widget.focus_set()
                widget.bell()


        self.height['vcmd'] = (self.height.register(isPosIntOkay),'%S','%P','%V')
        self.height['validate'] = 'all'
        self.height['invcmd'] = (self.height.register(_invalid_entry),'%W','%V')


        def check_file(filename):
            try:
                fh = open(filename,'r')
                fh.close()
                return True
            except: return False
        
        def do_ok():
            
            self.io_error.unlayout()
            height_ok = False

            try:
                height = int(self.height.get())
                if height > 0: height_ok = True
            except ValueError: pass
            
            if not height_ok:
                self.height.focus_set()
                self.height.bell()
                return
                
            
            filename = self.filename.get()
            if not check_file(filename):
                self.io_error.grid()
                return
            
            self.canvas_paint.pytkvg_tag = self.tag.get()
            self.canvas_paint.pytkvg_height = int(self.height.get())
            self.canvas_paint.pytkvg_file = filename
            self.root.destroy()
            
        self.ok.do_command(do_ok)
        self.filename.do_event('<Return>',do_ok)

### ========================================================

goOut()

