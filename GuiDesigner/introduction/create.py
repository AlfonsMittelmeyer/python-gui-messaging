### CODE ===================================================
this_container=container()
### ========================================================
config(**{'grid_rows': '(11, 25, 0, 0)', 'grid_cols': '(4, 300, 0, 0)', 'grid_multi_rows': '[11, (0, 11, 0, 0), (1, 24, 0, 0), (2, 13, 0, 0), (4, 11, 0, 0), (6, 31, 0, 0), (8, 10, 0, 0), (10, 8, 0, 0)]', 'grid_multi_cols': '[4, (0, 19, 0, 0), (3, 19, 0, 0)]'})

LinkButton('Back',**{'text': 'Back', 'bd': '3', 'link': 'introduction/img.py'}).grid(**{'column': 1, 'row': 9, 'sticky': 'w'})
Frame('CreateFrame')
goIn()

LabelFrame('CreateWidget',**{'text': 'Create Widget', 'grid_rows': '(2, 25, 0, 0)', 'grid_cols': '(4, 43, 0, 0)', 'grid_multi_cols': '[4, (1, 64, 0, 0), (2, 3, 0, 0), (3, 26, 0, 0)]'})
goIn()

Button('Create',**{'text': 'Create', 'padx': '1', 'bd': '3', 'pady': '1', 'bg': 'green'}).grid(**{'column': 3, 'row': 0, 'sticky': 'nes'})
Label('Label',**{'text': 'Class'}).grid(**{'row': 0})
Label('Label',**{'text': 'Name'}).grid(**{'row': 1})
Entry('Name').grid(**{'column': 1, 'row': 1, 'sticky': 'nesw', 'columnspan': 3})
Label('Type',**{'font': 'TkDefaultFont 9 bold', 'text': 'Button', 'relief': 'ridge', 'fg': 'blue', 'bg': 'yellow'}).grid(**{'column': 1, 'row': 0, 'sticky': 'ew'})

### CODE ===================================================

# the class name is stored in mydata of widget('Name')
callback = lambda wname = widget("Name"): send('CREATE_WIDGET_REQUEST',(wname.mydata,wname.get()))

widget("Create").do_command(callback)
widget("Name").do_event("<Return>",callback)

# ---- Receiver for message 'CREATE_CLASS_SELECTED': changes the text of Label 'Type' to the Class name and stores the Class name in mydata of Entry 'Name'

def function(msg,wname,wtype):
    wname.mydata = msg
    wname.delete(0,END)
    wname.insert(0,decapitalize(msg))
    #wname.insert(0,msg)
    wtype['text'] = msg
    wname.focus_set()

do_receive('CREATE_CLASS_SELECTED',function,(widget('Name'),widget('Type')),wishMessage=True)

# ---- Initialization with Class 'Button' ---------------------------

send('CREATE_CLASS_SELECTED','Button')

### ========================================================

goOut()

LabelFrame('MenuEntryTypes',**{'text': 'Select Widget Type'})
goIn()

Button('cascade',**{'text': 'cascade', 'width': 9}).grid(**{'row': 1})
Button('checkbutton',**{'text': 'checkbutton', 'width': 11}).grid(**{'column': 1, 'row': 0})
Button('command',**{'text': 'command', 'width': 9}).grid(**{'row': 0})
Button('delimiter',**{'text': 'delimiter', 'width': 11}).grid(**{'column': 1, 'row': 2})
Button('radiobutton',**{'text': 'radiobutton', 'width': 11}).grid(**{'column': 1, 'row': 1})
Button('separator',**{'text': 'separator', 'width': 9}).grid(**{'row': 2})

### CODE ===================================================

for widget_type in ('cascade','radiobutton','command','separator','checkbutton','delimiter'):
    widget(widget_type).do_command(lambda msg = widget_type: send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

### ========================================================

goOut()

LabelFrame('SelectType',**{'text': 'Select Widget Type'})
goIn()

### CODE ===================================================

container().saveOnlyCode() # buttons are dynamically created, so the widgets shall not be saved. Only the code, which creates them shall be saved

index = 0
for widget_type in ("Message","Label","Button","Checkbutton","Radiobutton","Entry","Text","Spinbox","Scale","Listbox","Scrollbar","Frame","LabelFrame","PanedWindow","Canvas","Menu","Menubutton","Toplevel","LinkButton","LinkLabel","Paint Canvas"):

    Button(widget_type,text=widget_type,width=10) # Button with name and text of widget class

    row,column = divmod(index,3) # position in 3 columns
    rcgrid(row,column) # grid layout row,column

    do_command(lambda msg = widget_type: send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name
    index += 1 # increase index

widget("Paint Canvas").config(fg='blue',font="TkDefaultFont 9 bold",activeforeground="blue",command="")
widget("Paint Canvas").unlayout()


def open_canvas_paint():
    cont = this() if isinstance(this(),Canvas) else container()
    DynAccess('guidesigner/canvas/CanvasPaint.py',(cont,this()),_Application)

widget("Paint Canvas").do_command(open_canvas_paint)


def do_canvas_selected(paint_button = widget("Paint Canvas")):
    if isinstance(this(),Canvas) and this().Layout != NOLAYOUT or isinstance(container(),Canvas) and container().Layout != NOLAYOUT: paint_button.grid()
    else: paint_button.unlayout()

do_receive('SELECTION_LAYOUT_CHANGED',do_canvas_selected)
do_receive('SELECTION_CHANGED',do_canvas_selected)

### ========================================================

goOut()


widget('CreateWidget').pack(**{'fill': 'x', 'ipady': 4, 'anchor': 'n'})
widget('SelectType').pack()

### CODE ===================================================

container().mydata = [False,GRIDLAYOUT]

def show_create(msg,cont=container()):

    if not isinstance(container(),_CreateTopLevelRoot):
        if msg: cont.grid()
        else: cont.unlayout()

    if msg: cont.mydata[0] = True
    else: cont.mydata[0] = False


do_receive("SHOW_CREATE",show_create,wishMessage=True)

def switch_buttons(buttons=widget('SelectType'),menubuttons=widget('MenuEntryTypes'),cont=container()):

    if isinstance(container(),Menu):
        if cont.mydata[1] != MENUITEMLAYOUT:
            cont.mydata[1] = MENUITEMLAYOUT
            buttons.unlayout()
            menubuttons.pack()
            send('CREATE_CLASS_SELECTED','command')

    elif isinstance(container(),MenuItem) or isinstance(container(),Menubutton) or isinstance(container(),ttk.Menubutton):
        if cont.mydata[1] != MENULAYOUT:
            cont.mydata[1] = MENULAYOUT
            buttons.unlayout()
            menubuttons.unlayout()
            send('CREATE_CLASS_SELECTED','Menu')
    else:
        if cont.mydata[1] != GRIDLAYOUT:
            cont.mydata[1] = GRIDLAYOUT
            menubuttons.unlayout()
            buttons.pack()
            send('CREATE_CLASS_SELECTED','Button')

do_receive('SELECTION_CHANGED',switch_buttons)

def enable_container(cont=container()):
    if cont.mydata[0]:
        if not isinstance(container(),_CreateTopLevelRoot): cont.grid()
        else: cont.unlayout()

do_receive("SELECTION_CHANGED",enable_container)


### ========================================================

goOut()
grid(**{'column': 1, 'row': 3, 'columnspan': 2})
Label('Label',**{'font': 'TkDefaultFont 12 bold', 'text': 'Create Widgets', 'fg': 'blue'}).grid(**{'column': 1, 'row': 1, 'sticky': 'w', 'columnspan': 2})
Message('Message',**{'text': "The Create Widget module lets you create widgets.\n\nThe buttons in the section 'Select Widget Type' let you select the class of the tkinter widget.\n\nIn the last line there are two special widgets, which don't exist in tkinter: LinkButton and LinkLabel. You just had pressed the button 'Create ON'. This was a LinkButton, which can be used as Next or Back button. The LinkLabel is just the same, but looks different.\n\nThe entry 'Name' shows the selected class type as default for the name. You should change this name. If you like to export the designed GUI as a python tkinter file, the name should be fitting for a variable name. But if you access the GUI via interface, then there are no restrictions for the name, besides, that it has to be a string. But you only can enter a string.", 'bg': 'white', 'width': 600}).grid(**{'column': 1, 'row': 5, 'sticky': 'ew', 'columnspan': 2})
Message('Message',**{'font': 'TkDefaultFont 9 bold', 'text': 'The module above is the original GuiDesigner module, so just try it.', 'anchor': 'w', 'bg': 'white', 'width': 600}).grid(**{'column': 1, 'row': 6, 'sticky': 'nesw', 'columnspan': 2})
Message('Message',**{'text': "Do you think, it doesn't work, because it doesn't create a widget? But it works, it doesn't create a widget, but informs another module to create the widget.", 'anchor': 'w', 'bg': 'white', 'width': 600}).grid(**{'column': 1, 'row': 7, 'sticky': 'ew', 'columnspan': 2})
LinkButton('Next',**{'text': 'Next', 'bd': '3', 'link': 'introduction/navy.py'}).grid(**{'column': 2, 'row': 9, 'sticky': 'e'})

### CODE ===================================================
this_container.grid_remove()
this_container.after(100,this_container.grid)
### ========================================================
