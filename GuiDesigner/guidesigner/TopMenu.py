MenuItem('Config','command',**{'label': 'Config ON', 'background': 'green'})
MenuItem('Create','command',**{'label': 'Create ON', 'columnbreak': '1', 'background': 'green'})
MenuItem('File','cascade',**{'label': 'File'})
goIn()

Menu('Menu',**{'bg': 'white', 'relief': 'solid', 'activebackground': '#7bfeff'})
goIn()

MenuItem('Access','cascade',**{'label': 'Save Access'})
goIn()

Menu('Menu',**{'bg': 'white', 'relief': 'solid', 'activebackground': '#7bfeff'})
goIn()

MenuItem('Container','command',**{'label': 'Container Depth'})
MenuItem('Widget','command',**{'label': 'Widget Depth'})

widget('Widget').layout(index=1)
widget('Container').layout(index=2)

### CODE ===================================================

def get_root_name_2():
    selection_before = Selection()
    gotoRoot()
    _Selection._container = _TopLevelRoot._container
    name = '//'+getNameAndIndex()[0]+'/'
    setSelection(selection_before)
    return name

widget('Widget').do_command(lambda name=get_root_name_2: send("SAVE_ACCESS_WIDGETS_ALL",name()))
widget('Container').do_command(lambda name=get_root_name_2: send("SAVE_ACCESS_CONTAINERS_ALL",name()))

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('Export','cascade',**{'label': 'Export (tk)'})
goIn()

Menu('Menu',**{'bg': 'white', 'relief': 'solid', 'activebackground': '#7bfeff'})
goIn()

MenuItem('Help','command',**{'label': 'Help'})
MenuItem('With Names','command',**{'label': 'With Names'})
MenuItem('Without Names','command',**{'label': 'Without Names'})
MenuItem('separator','separator')

widget('Help').layout(index=1)
widget('separator').layout(index=2)
widget('With Names').layout(index=3)
widget('Without Names').layout(index=4)

### CODE ===================================================

def get_root_name_3():
    selection_before = Selection()
    gotoRoot()
    _Selection._container = _TopLevelRoot._container
    name = '//'+getNameAndIndex()[0]+'/'
    setSelection(selection_before)
    return name

widget("With Names").do_command(lambda name=get_root_name_3: send('EXPORT_ALL_NAMES',name()))
widget("Without Names").do_command(lambda name=get_root_name_3: send('EXPORT_ALL_TK',name()))

def export_help(menu=widget('Help')):
    messagebox.showinfo("Export as tk or extended tk","If you export 'With Names' you may edit the GUI using the exported File. If you export 'Without Names', the exported File is nearly full tkinter compatible.",parent=menu.myRoot())

widget("Help").do_command(export_help)

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('Load & Edit','command',**{'label': 'Load & Edit'})
MenuItem('Load & Run','command',**{'label': 'Load & Run'})
MenuItem('Save','command',**{'label': 'Save'})
MenuItem('Split & Join','cascade',**{'label': 'Split & Join'})
goIn()

Menu('Menu',**{'bg': 'white', 'relief': 'solid', 'activebackground': '#7bfeff'})
goIn()

MenuItem('Help','command',**{'label': 'Help'})
MenuItem('Load & Edit','command',**{'label': 'Load & Edit (part)'})
MenuItem('Load & Run','command',**{'label': 'Load & Run (part)'})
MenuItem('Save','command',**{'label': 'Save  (part)'})
MenuItem('separator','separator')

widget('Help').layout(index=1)
widget('separator').layout(index=2)
widget('Save').layout(index=3)
widget('Load & Edit').layout(index=4)
widget('Load & Run').layout(index=5)

### CODE ===================================================

def help_options_part(menu=widget('Help')):

    messagebox.showinfo("Save and Load parts","Very useful expert Options!\n\nBut before you use these options, you should save your work. Sorry, that I didn't document these options yet. The Save option shouldn't be a problem. But the Load options could crash!",parent=menu.myRoot())
    
widget('Help').do_command(help_options_part)


def enable_parts(menu_items=(widget('Load & Edit'),widget('Load & Run'))):

    if isinstance(container(),_CreateTopLevelRoot) or this().isLocked: state = 'disabled'
    else: state = 'normal'
    for wi in menu_items: wi.config(state = state)

do_receive("SELECTION_CHANGED",enable_parts)

def get_part_name():
    if isinstance(this(),_CreateTopLevelRoot): return None
    name = ''
    if isinstance(container(),_CreateTopLevelRoot): name = '//'+getNameAndIndex()[0]+'/'
    else:
        if this() == _Application or isinstance(this(),Toplevel):
            _Selection._container = _TopLevelRoot._container
            name = '//'+getNameAndIndex()[0]+'/'
            _Selection._container = this()
        elif this() == container():
            goOut()
            name = getNameAndIndex()[0]
            goIn()
            send('SHOW_SELECTION')
        else: name = getNameAndIndex()[0]
        return name

widget("Save").do_command(lambda name=get_part_name: send('SAVE_WIDGET_PART',name()))
widget('Load & Edit').do_command(lambda name=get_part_name: send('LOAD_EDIT_PART',name()))
widget('Load & Run').do_command(lambda name=get_part_name: send('LOAD_RUN_PART',name()))

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('separator','separator')

widget('Save').layout(index=1)
widget('Export').layout(index=2)
widget('Access').layout(index=3)
widget('Load & Edit').layout(index=4)
widget('Load & Run').layout(index=5)
widget('separator').layout(index=6)
widget('Split & Join').layout(index=7)

### CODE ===================================================

def get_root_name():
    selection_before = Selection()
    gotoRoot()
    _Selection._container = _TopLevelRoot._container
    name = '//'+getNameAndIndex()[0]+'/'
    setSelection(selection_before)
    return name

widget("Save").do_command(lambda name=get_root_name: send('SAVE_ALL',name()))
widget('Load & Run').do_command(lambda name=get_root_name: send('LOAD_RUN_ALL',name()))
widget('Load & Edit').do_command(lambda name=get_root_name: send('LOAD_EDIT_ALL',name()))

def enable_save_and_load(menu_items=(widget('Save'),widget('Load & Edit'),widget('Load & Run'))):

    state = 'disabled' if isinstance(container(),_CreateTopLevelRoot) else 'normal'
    for wi in menu_items: wi.config(state = state)

do_receive("SELECTION_CHANGED",enable_save_and_load)


### ========================================================

goOut()
select_menu()

goOut()

MenuItem('Layout','command',**{'label': 'Layout ON', 'background': 'green'})
MenuItem('Mouse','command',**{'label': 'Mouse ON', 'background': 'green'})
MenuItem('Special','cascade',**{'label': 'Special'})
goIn()

Menu('Menu',**{'bg': 'white', 'relief': 'solid', 'activebackground': '#7bfeff'})
goIn()

MenuItem('ExpertOptions','cascade',**{'label': 'Expert Options'})
goIn()

Menu('Menu',**{'bg': 'white', 'relief': 'solid', 'activebackground': '#7bfeff'})
goIn()

MenuItem('Code','command',**{'label': 'Code'})
MenuItem('Help','command',**{'label': 'Help'})
MenuItem('separator','separator')

widget('Help').layout(index=1)
widget('separator').layout(index=2)
widget('Code').layout(index=3)

### CODE ===================================================

def help_code(menu=widget('Help')):

    messagebox.showinfo("Write Code and modify Code during program is running","The option 'Code' is predistined for causing program crash. So you should save your work before experimenting with this option.\n\nBut there is no problem, if you had saved your work. Simply start anew. Choose this option again and press button 'Load'. Then look, what you typed wrong.",parent=menu.myRoot())

widget('Help').do_command(help_code)
widget("Code").do_command(lambda name=get_part_name: send('EDIT_CODE',name()))

def enable_code(code = widget("Code")):
    if this().isContainer: code.config(state = 'normal') 
    else: code.config(state = 'disabled')

do_receive('SELECTION_CHANGED',enable_code)

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('Refresh','command',**{'label': 'Refresh'})
MenuItem('Toproot','command',**{'label': 'Toproot'})
MenuItem('separator','separator')

widget('Toproot').layout(index=1)
widget('Refresh').layout(index=2)
widget('separator').layout(index=3)
widget('ExpertOptions').layout(index=4)

### CODE ===================================================

def go_TopRoot():
    gotoTop()
    send('SELECTION_CHANGED')

widget('Toproot').do_command(go_TopRoot)

def do_refresh():
    selection_before = Selection()

    gotoTop() # go into the TopRoot
    goto('DynTkInterGuiDesigner')

    my_geo = this().geometry()
    find_plus = my_geo.find("+")
    find_minus = my_geo.find("-")
    if find_plus < 0: begin = find_minus
    elif find_minus < 0: begin = find_plus
    else: begin = min(find_plus,find_minus)
    my_geo = my_geo[begin:]
    
    this().geometry('') # refresh the geometry of the GUI Designer
    this().withdraw()
    this().geometry(my_geo)
    this().deiconify()

    setSelection(selection_before)
    send('SELECTION_CHANGED') # refresh display of the current selection

widget("Refresh").do_command(do_refresh)

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('space','command',**{'label': ''})
MenuItem('space','command',**{'label': ''})
MenuItem('space','command',**{'label': ''})

widget('File').layout(index=1)
widget('Special').layout(index=2)
widget('Create').layout(index=3)
widget('space',0).layout(index=4)
widget('Config').layout(index=5)
widget('space',1).layout(index=6)
widget('Layout').layout(index=7)
widget('space',2).layout(index=8)
widget('Mouse').layout(index=9)

### CODE ===================================================

def enable_file(wi=widget('File')):

    state = 'disabled' if isinstance(this(),_CreateTopLevelRoot) else 'normal'
    wi.config(state = state)

do_receive("SELECTION_CHANGED",enable_file)


# ----

widget("Config").mydata = False
widget("Layout").mydata = False
widget("Create").mydata = False
widget("Mouse").mydata = False

def function_callback(me,message_to_send,thisText=None):
    me.mydata = not me.mydata
    if message_to_send == "MOUSE_SELECT_ON": container().is_mouse_select_on = me.mydata
    send(message_to_send,me.mydata)
    if me.mydata: me.config(label=thisText+" OFF",background="orange")
    else: me.config(label=thisText+" ON",background="green")

def call(widget_name,message_to_send,callback=function_callback):
    widget(widget_name).do_command(callback,(message_to_send,widget_name),True)

call("Config","SHOW_CONFIG")
call("Layout","SHOW_LAYOUT")
call("Create","SHOW_CREATE")
call("Mouse","MOUSE_SELECT_ON")

send("SHOW_CREATE",False)

def switch_mouse_on(mouse_button=widget("Mouse"),funct=function_callback):
    if not mouse_button.mydata: funct(mouse_button,"MOUSE_SELECT_ON",'Mouse')

do_receive("SWITCH_MOUSE_ON",switch_mouse_on)


def set_option_buttons(message,buttons=(widget("Config"),widget("Layout"),widget("Create"),widget("Mouse"))):
    for i in range(len(message)):
        if message[i] != buttons[i].mydata: buttons[i].invoke()

do_receive('SET_OPTION_BUTTONS',set_option_buttons,wishMessage=True)


def check_mouse_on(mouse=widget('Mouse'),func=function_callback):
    #if container().is_mouse_select_on != mouse.mydata: mouse.invoke()
    if container().is_mouse_select_on != mouse.mydata: func(mouse,"MOUSE_SELECT_ON",'Mouse')

    
do_receive('SELECTION_CHANGED',check_mouse_on)


### ========================================================
