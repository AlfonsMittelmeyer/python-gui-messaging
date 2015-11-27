Toplevel('C-Copy',**{'title': 'Copy Item', 'grid_cols': '(4, 10, 0, 0)', 'grid_rows': '(12, 10, 0, 0)'})
goIn()

Button('Cancel',**{'text': 'Cancel', 'bd': '2'}).grid(**{'column': '1', 'sticky': 'nesw', 'pady': '2', 'padx': '2', 'row': '10'})
Button('OK',**{'text': 'OK', 'width': 6, 'bd': '2'}).grid(**{'column': '2', 'sticky': 'nesw', 'pady': '2', 'padx': '2', 'row': '10'})
Spinbox('copies',**{'from': 1.0, 'width': 5, 'to': 999.0}).grid(**{'column': '2', 'sticky': 'w', 'ipady': '2', 'padx': '2', 'row': '5'})
Spinbox('dx',**{'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'column': '2', 'sticky': 'w', 'ipady': '2', 'padx': '2', 'row': '6'})
Spinbox('dy',**{'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'column': '2', 'sticky': 'w', 'ipady': '2', 'padx': '2', 'row': '7'})
Label('lcopies',**{'text': 'copies'}).grid(**{'column': '1', 'row': '5'})
Label('ldx',**{'text': 'dx'}).grid(**{'column': '1', 'row': '6'})
Label('ldy',**{'text': 'dy'}).grid(**{'column': '1', 'row': '7'})
Label('lresize',**{'text': 'resize'}).grid(**{'column': '1', 'row': '8'})
Label('lselected',**{'text': 'id or tag', 'font': 'TkDefaultFont 9 bold', 'fg': 'blue'}).grid(**{'column': '1', 'row': '3'})
Spinbox('resize',**{'increment': 0.1, 'width': 5, 'to': 100.0}).grid(**{'column': '2', 'sticky': 'w', 'ipady': '2', 'padx': '2', 'row': '8'})
Label('selected',**{'text': '5', 'padx': '10', 'font': 'TkDefaultFont 9 bold', 'bd': '2', 'bg': 'yellow', 'fg': 'blue', 'relief': 'solid'}).grid(**{'column': '2', 'sticky': 'w', 'ipady': '2', 'padx': '2', 'row': '3'})
Label('title',**{'text': 'Copy Item', 'font': 'TkDefaultFont 11 bold', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '2', 'row': '1'})

### CODE ===================================================


class Access:
    
    def __init__(self,canvas,item):
    
        self.canvas = canvas
        self.item = item
        
        widget('selected')['text'] = str(item)
        
        self.dx = widget('dx')
        self.dy = widget('dy')
        self.resize = widget('resize')
        
        self.dx.delete(0,END)
        self.dy.delete(0,END)
        self.resize.delete(0,END)

        self.dx.insert(0,'0')
        self.dy.insert(0,'0')
        self.resize.insert(0,'1.0')

        self.root = widget('/')
        self.copies = widget('copies')


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
            

        def isIntOkay(value,reason):

            if reason == 'focusout':
                try:
                    check = int(value)
                    return True
                except ValueError:
                    return False

            elif reason == 'key':
                if value == '' or value == '-': return True
                try:
                    check = int(value)
                    return True
                except ValueError:
                    return False
            return True


        def _invalid_entry(widgetName,reason):
            if reason == 'focusout':
                widget = self.root.nametowidget(widgetName)
                 
                # clear entry
                #widget.delete(0, END)
                 
                # return focus to integer entry
                widget.focus_set()
                widget.bell()



        def isFloadGreater0(value,reason):

            if reason == 'focusout':
                try:
                    check = float(value)
                    if check > 0.00001: return True
                    else: return False
                except ValueError:
                    return False

            elif reason == 'key':
                if value == '': return True
                try:
                    check = float(value)
                    return True
                except ValueError:
                    return False
            return True



        self.copies['vcmd'] = (self.copies.register(isPosIntOkay),'%S','%P','%V')
        self.copies['validate'] = 'all'
        self.copies['invcmd'] = (self.copies.register(_invalid_entry),'%W','%V')

        self.dx['vcmd'] = (self.dx.register(isIntOkay),'%P','%V')
        self.dx['validate'] = 'all'
        self.dx['invcmd'] = (self.dx.register(_invalid_entry),'%W','%V')

        self.dy['vcmd'] = (self.dy.register(isIntOkay),'%P','%V')
        self.dy['invcmd'] = (self.dy.register(_invalid_entry),'%W','%V')
        self.dy['validate'] = 'all'

        self.resize['vcmd'] = (self.resize.register(isFloadGreater0),'%P','%V')
        self.resize['invcmd'] = (self.resize.register(_invalid_entry),'%W','%V')
        self.resize['validate'] = 'all'

        def do_cancel():
            this_widget = this()
            selection_before = Selection()
            self.root.destroy()
            if widget_exists(this_widget): setSelection(selection_before)
            
        widget('Cancel').do_command(do_cancel)
       
        def do_ok(do_cancel = do_cancel):
        
            try:
                copies = int(self.copies.get())
                dx = int(self.dx.get())
                dy = int(self.dy.get())
                resize = float(self.resize.get())
            except ValueError:
                do_cancel()
                return


            size = 1.0
            
            item_list = self.canvas.find_withtag(self.item)
            first_item = item_list[0]
            first_coords = self.canvas.coords(first_item)
            first_x = first_coords[0]
            first_y = first_coords[1]
            add_sumx = 0
            add_sumy = 0
            
            for count in range(copies):
                

                for entry in item_list:
                    coords = self.canvas.coords(entry)
                    dictionary = self.canvas.get_itemconfig(entry)
                    ConfDictionaryShort(dictionary)
                    item_type = self.canvas.type(entry)
                    item = None
                    if item_type == 'line': item = self.canvas.create_line(*coords)
                    elif item_type == 'rectangle': item = self.canvas.create_rectangle(*coords)
                    elif item_type == 'polygon': item = self.canvas.create_polygon(*coords)
                    elif item_type == 'oval': item = self.canvas.create_oval(*coords)
                    elif item_type == 'arc': item = self.canvas.create_arc(*coords)
                    elif item_type == 'text': item = self.canvas.create_text(*coords)
                    elif item_type == 'bitmap': item = self.canvas.create_bitmap(*coords)
                    elif item_type == 'image': item = self.canvas.create_image(*coords)

                    if item != None:
                        self.canvas.itemconfig(item,**dictionary)
                        self.canvas.addtag_withtag('copy',item)
               
                if resize != 1.0:
                    size *= resize

                    try:
                        self.canvas.scale('copy',first_x,first_y,size,size)
                        
                        add_sumx += dx*size
                        add_sumy += dy*size
                        self.canvas.move('copy',add_sumx,add_sumy)
                    except TclError:
                        do_cancel()
                        return
                else:
                    self.canvas.move('copy',(count+1)*dx,(count+1)*dy)
                self.canvas.dtag('copy','copy')
        
            this_widget = this()
            selection_before = Selection()
            self.root.destroy()
            if widget_exists(this_widget): setSelection(selection_before)

        widget('OK').do_command(do_ok)

### ========================================================

goOut()

