config(**{'grid_multi_rows': '[2, (0, 0, 0, 0), (1, 0, 0, 0)]', 'grid_multi_cols': '[2, (0, 0, 0, 0), (1, 0, 0, 0)]', 'grid_rows': '(2, 0, 0, 0)', 'grid_cols': '(2, 0, 0, 0)'})

Frame("Buttons",link="guidesigner/Buttons.py")
grid(sticky='nw', columnspan=2, row=0)
Scrollbar('Scrollbar',orient=VERTICAL)
grid(sticky='wns', column=1, row=1)
Canvas('ScrollContainer',bd=0,highlightthickness=0,width=0).grid(sticky='nw', row=1)
goIn()
Frame("SelectionShow",bg="white",link="guidesigner/SelectionShow.py")


### CODE ===================================================


# ---- Receiver for message 'CREATE_WIDGET_REQUEST' - somewhere it has to be: 
# creates the widget with Class name and widget name in the current User selection and sends the message CREATE_WIDGET_DONE which contains the current user widget selection

def main():

    class Var:
        def __init__(self):
            self.value = False


    ALPHABET = 0
    BASEMENT = 1
    INDEX = 2

    sort_order = Var()
    sort_order.value = ALPHABET


    def create_widget(msg):
        widget_type = msg[0]
        name = msg[1]
        kwargs = msg[2]

        if widget_type in ('cascade','radiobutton','command','separator','checkbutton','delimiter'):
            if isinstance(container(),Menu):
                if widget_type == 'separator':
                    eval("MenuItem('{}','{}')".format(name,widget_type))
                elif widget_type == 'delimiter':
                    eval("MenuDelimiter('{}')".format(name))
                else:
                    eval("MenuItem('{}','{}',label = '{}')".format(name,widget_type,name))
                send('SELECTION_CHANGED')
            else:
                print("Wrong handling: cannot create a menu item outside a menu")
        elif isinstance(container(),Menu):
            print("Wrong handling: cannot create a widget inside a menu")
        elif isinstance(container(),ttk.PanedWindow):
            eval("{}('{}',**{})".format(widget_type,name,kwargs))
            text(name)
            send('SELECTION_CHANGED')
            
        elif isinstance(container(),PanedWindow):
            eval("{}('{}',**{})".format(widget_type,name,kwargs))
            text(name)
            pane()
            send('UPDATE_MOUSE_SELECT_ON')
            send('SELECTION_CHANGED')
            
        elif isinstance(container(),ttk.Notebook):
            eval("{}('{}',**{})".format(widget_type,name,kwargs))
            text(name)
            page(text=name)
            send('UPDATE_MOUSE_SELECT_ON')
            send('SELECTION_CHANGED')

        else:
            if widget_type == "Toplevel": cdApp()
            eval("{}('{}',**{})".format(widget_type,name,kwargs))
            text(name)
            if widget_type == 'Menu':
                select_menu()
                goIn()
            send('SELECTION_CHANGED')

    def selection_layout_changed():
        if isinstance(container(),(Menu,PanedWindow,ttk.PanedWindow,ttk.Notebook)):
            send('REFRESH_INDEX_ORDER')
        elif sort_order.value == INDEX:
            send('REFRESH_INDEX_ORDER')
        else:
            send('SHOW_SELECTION')

    do_receive('CREATE_WIDGET_REQUEST',create_widget,wishMessage=True)
    do_receive("SELECTION_CHANGED", lambda: send('SHOW_SELECTION'))
    do_receive("SELECTION_LAYOUT_CHANGED",selection_layout_changed)


    def select_order(value):
        sort_order.value = value

    do_receive('SELECT_INDEX_ORDER',select_order,INDEX)
    do_receive('SELECT_ALPHABETICAL',select_order,ALPHABET)
    do_receive('SELECT_BASEMENT',select_order,BASEMENT)

main()

my_frame = widget("SelectionShow")
### ========================================================


goOut() # Canvas

### CODE ========================================================

# -------------- make a frame with a vertical scrollbar ------------------------------------
my_canvas = widget('ScrollContainer')

interior_id = my_canvas.create_window(0, 0, window=my_frame,anchor=NW,width=0,height=0)

class FrameEvent:

    def __init__(self,my_frame,my_canvas,scrollbar):
        self.my_frame = my_frame
        self.my_canvas = my_canvas
        self.scrollbar = scrollbar
        self.bind_configure()

    def bind_configure(self):
        self.my_frame.bind("<Configure>",self.frame_configure)

    def frame_configure(self,event):
        #self.my_frame.unbind("<Configure>")
        self.my_canvas.config(scrollregion="0 0 %s %s" % (self.my_frame.winfo_reqwidth(), self.my_frame.winfo_reqheight()))
        if self.my_frame.winfo_reqheight() > 400:
            self.scrollbar.grid()
            self.my_canvas['height'] = 400
        else:
            self.scrollbar.unlayout()
            self.my_canvas.config(height=self.my_frame.winfo_reqheight())
            
        self.my_canvas['width'] = self.my_frame.winfo_width()
        self.my_frame.after(300,self.bind_configure)


FrameEvent(my_frame,my_canvas,widget("Scrollbar"))

my_canvas.config(yscrollcommand=widget("Scrollbar").set)
widget("Scrollbar").config(command=my_canvas.yview)
widget("Scrollbar").unlayout()
### ========================================================


