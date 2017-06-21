MenuItem('Config','command',**{'underline': 1, 'background': 'lightgreen', 'label': 'Config ON'})
MenuItem('Create','command',**{'underline': 0, 'background': 'lightgreen', 'label': 'Create ON'})
MenuItem('File','cascade',**{'underline': 0, 'label': 'File'})
goIn()

Menu('Menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
goIn()

MenuItem('Access','cascade',**{'label': 'Save Access'})
goIn()

Menu('Menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
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

MenuItem('Export','cascade',**{'underline': 0, 'label': 'Export tkinter'})
goIn()

Menu('Menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
goIn()

MenuItem('Help','command',**{'label': 'Help'})
MenuItem('With Names','command',**{'underline': 9, 'label': 'tkinter (names)'})
MenuItem('Without Names','command',**{'underline': 0, 'label': 'tkinter'})
MenuItem('designer','command',**{'underline': 9, 'label': 'tkinter (Designer)'})
MenuItem('separator','separator')

widget('Help').layout(index=1)
widget('separator').layout(index=2)
widget('Without Names').layout(index=3)
widget('With Names').layout(index=4)
widget('designer').layout(index=5)

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
widget("designer").do_command(lambda name=get_root_name_3: send('EXPORT_ALL_DESIGNER',name()))

def export_help(menu=widget('Help')):
    messagebox.showinfo("Export as tkinter with or without names","When you export 'tkinter (names)', the exported File contains the names of the widgets in a tkinter compatible way. The advantage is, that later you may edit the GUI with the GuiDesigner directly using the exported file.\n\nIf you don't like names in your tkinter source file, then export 'tkinter'. But then you shouldn't forget to save the GUI also via menu File->Save",parent=menu.myRoot())

widget("Help").do_command(export_help)

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('Load & Edit','command',**{'underline': 0, 'label': 'Load & Edit'})
MenuItem('Load & Run','command',**{'label': 'Load & Run'})
MenuItem('Quit','command',**{'label': 'Quit'})
MenuItem('Save','command',**{'underline': 0, 'label': 'Save'})
MenuItem('Split & Join','cascade',**{'label': 'Split & Join'})
goIn()

Menu('Menu',**{'relief': 'solid', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff'})
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

MenuItem('backup','command',**{'underline': 0, 'label': 'Backup'})
MenuItem('separator','separator')
MenuItem('separator_quit','separator')

widget('backup').layout(index=1)
widget('Save').layout(index=2)
widget('Load & Edit').layout(index=3)
widget('Load & Run').layout(index=4)
widget('Split & Join').layout(index=5)
widget('separator').layout(index=6)
widget('Export').layout(index=7)
widget('Access').layout(index=8)
widget('separator_quit').layout(index=9)
widget('Quit').layout(index=10)

### CODE ===================================================

def do_quit():
    cdApp()
    this().destroy()

widget('Quit').do_command(do_quit)

def get_root_name():
    selection_before = Selection()
    gotoRoot()
    _Selection._container = _TopLevelRoot._container
    name = '//'+getNameAndIndex()[0]+'/'
    setSelection(selection_before)
    return name

widget("backup").do_command(lambda name=get_root_name: send('SAVE_BACKUP',name()))
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

MenuItem('Hide','command',**{'underline': 0, 'label': 'Hide'})
MenuItem('Layout','command',**{'underline': 0, 'background': 'lightgreen', 'label': 'Layout ON'})
MenuItem('Mouse','command',**{'underline': 0, 'background': 'lightgreen', 'label': 'Mouse ON'})
MenuItem('Special','cascade',**{'underline': 0, 'label': 'Special'})
goIn()

Menu('Menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'disabledforeground': 'black', 'fg': 'black'})
goIn()

MenuItem('ExpertOptions','cascade',**{'label': 'Expert Options'})
goIn()

Menu('Menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
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

MenuItem('Refresh','command',**{'underline': 0, 'label': 'Refresh'})
MenuItem('Toproot','command',**{'label': 'Toproot'})
MenuItem('alphabetical','radiobutton',**{'underline': 0, 'label': 'alphabetical', 'value': 'alphabetical'})
MenuItem('order','command',**{'activebackground': 'white', 'label': 'Navigation Order', 'state': 'disabled'})
MenuItem('separator','separator')
MenuItem('separator','separator')
MenuItem('z-order','radiobutton',**{'underline': 0, 'label': 'z-order', 'value': 'basement'})

widget('Refresh').layout(index=1)
widget('Toproot').layout(index=2)
widget('separator',0).layout(index=3)
widget('order').layout(index=4)
widget('alphabetical').layout(index=5)
widget('z-order').layout(index=6)
widget('separator',1).layout(index=7)
widget('ExpertOptions').layout(index=8)

### CODE ===================================================

basement = StatTkInter.StringVar()
basement.set('alphabetical')
widget('alphabetical').mydata = basement
widget('alphabetical')['variable'] = basement
widget('z-order')['variable'] = basement


def select_alphabetical():
    send('SELECT_ALPHABETICAL')

widget('alphabetical').do_command(select_alphabetical)


def select_basement():
    send('SELECT_BASEMENT')

widget('z-order').do_command(select_basement)


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
    send('SHOW_SELECTION_UPDATE') # refresh display of the current selection
    send('SELECTION_CHANGED') # refresh display of the current selection

widget("Refresh").do_command(do_refresh)

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('help','cascade',**{'label': 'Help'})
goIn()

Menu('menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
goIn()

MenuItem('backup','command',**{'label': 'Backup'})
MenuItem('code_in_scripts','cascade',**{'label': 'Code in Scripts'})
goIn()

Menu('menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
goIn()

MenuItem('dynaccess','command',**{'label': 'DynAccess'})
MenuItem('dyntkimports','command',**{'label': 'DynTkImports'})
MenuItem('functions','command',**{'label': 'Functions'})
MenuItem('imports','command',**{'label': 'Imports'})
MenuItem('namespace','command',**{'label': 'Namespace'})
MenuItem('place_code','command',**{'label': 'Place for Code'})
MenuItem('relative_access','command',**{'label': 'Relative Access'})
MenuItem('root_access','command',**{'label': 'Root Access'})

widget('functions').layout(index=1)
widget('namespace').layout(index=2)
widget('imports').layout(index=3)
widget('dyntkimports').layout(index=4)
widget('relative_access').layout(index=5)
widget('root_access').layout(index=6)
widget('place_code').layout(index=7)
widget('dynaccess').layout(index=8)

### CODE ===================================================
def load_help(filename):
    load_script(filename,_Application)

widget('functions').do_command(load_help,'guidesigner/Help/FunctionsInScripts.py')
widget('namespace').do_command(load_help,'guidesigner/Help/NameSpace.py')
widget('imports').do_command(load_help,'guidesigner/Help/Import.py')
widget('dyntkimports').do_command(load_help,'guidesigner/Help/DynTkImports.py')
widget('relative_access').do_command(load_help,'guidesigner/Help/RelativeAccess.py')
widget('root_access').do_command(load_help,'guidesigner/Help/RootAccess.py')
widget('place_code').do_command(load_help,'guidesigner/Help/PlaceForCode.py')
widget('dynaccess').do_command(load_help,'guidesigner/Help/DynAccess.py')
### ========================================================

goOut()
select_menu()

goOut()

MenuItem('config','command',**{'label': 'Config Options'})
MenuItem('examples','command',**{'label': 'Examples'})
MenuItem('export','command',**{'label': 'Export tkinter'})
MenuItem('introduction','command',**{'label': 'Introduction'})
MenuItem('menu_entries','command',**{'label': 'Menu Entries'})
MenuItem('programming','cascade',**{'label': 'Programming'})
goIn()

Menu('menu',**{'relief': 'solid', 'activeforeground': 'black', 'bg': 'white', 'tearoff': 0, 'activebackground': '#7bfeff', 'fg': 'black'})
goIn()

MenuItem('access_toplevel','command',**{'label': 'Access Toplevel'})
MenuItem('access_widgets','command',**{'label': 'Access Widgets'})
MenuItem('load_scripts','command',**{'label': 'Load Scripts'})

widget('load_scripts').layout(index=1)
widget('access_widgets').layout(index=2)
widget('access_toplevel').layout(index=3)

### CODE ===================================================
def load_help(filename):
    load_script(filename,_Application)

widget('load_scripts').do_command(load_help,'guidesigner/Help/LoadScripts.py')
widget('access_widgets').do_command(load_help,'guidesigner/Help/AccessWidgets.py')
widget('access_toplevel').do_command(load_help,'guidesigner/Help/AccessToplevel.py')
### ========================================================

goOut()
select_menu()

goOut()

MenuItem('save_access','command',**{'label': 'Save Access'})
MenuItem('save_load','command',**{'label': 'Save & Load'})
MenuItem('separator','separator')
MenuItem('tuples','command',**{'label': 'Tuple Entries'})

widget('introduction').layout(index=1)
widget('config').layout(index=2)
widget('tuples').layout(index=3)
widget('menu_entries').layout(index=4)
widget('backup').layout(index=5)
widget('save_load').layout(index=6)
widget('export').layout(index=7)
widget('save_access').layout(index=8)
widget('separator').layout(index=9)
widget('programming').layout(index=10)
widget('code_in_scripts').layout(index=11)
widget('examples').layout(index=12)

### CODE ===================================================

def start_intro(msg):
    unregister_msgid('START_INTRO')
    DynLoad('introduction/intro.py')

proxy.do_receive(None,'START_INTRO',start_intro)
    
def see_introduction(me):
    if messagebox.askokcancel("Introduction", "The introduction explains creating widgets and about the layouts. Because two GuiDesigners shouldn't run, we close one and hide the Application window. Maybe you first should save your work via menu File->Save.\n\nOr do you like, to begin now?",parent=me.myRoot()):
        me.myRoot().destroy()
        send("START_INTRO")

widget('introduction').do_command(see_introduction,wishWidget=True)

def load_help(filename):
    load_script(filename,_Application)

widget('config').do_command(load_help,'guidesigner/Help/ConfigTop.py')
widget('save_load').do_command(load_help,'guidesigner/Help/SaveLoad.py')
widget('export').do_command(load_help,'guidesigner/Help/ExportTk.py')
widget('menu_entries').do_command(load_help,'guidesigner/Help/Menu.py')
widget('save_access').do_command(load_help,'guidesigner/Help/SaveAccess.py')
widget('backup').do_command(load_help,'guidesigner/Help/Backup.py')
widget('tuples').do_command(load_help,'guidesigner/Help/Tuples.py')

def examples_help(root=widget('/')):
    messagebox.showinfo("Examples","Examples will follow soon",parent=root)

widget("examples").do_command(examples_help)

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('space','command',**{'label': ' ', 'state': 'disabled'})
MenuItem('space','command',**{'label': ' ', 'state': 'disabled'})
MenuItem('space','command',**{'label': ' ', 'state': 'disabled'})

widget('File').layout(index=1)
widget('Special').layout(index=2)
widget('help').layout(index=3)
widget('Create').layout(index=4)
widget('space',0).layout(index=5)
widget('Config').layout(index=6)
widget('space',1).layout(index=7)
widget('Layout').layout(index=8)
widget('space',2).layout(index=9)
widget('Mouse').layout(index=10)
widget('Hide').layout(index=11)

### CODE ===================================================

widget('Hide').mydata = False

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
    else: me.config(label=thisText+" ON",background="lightgreen")

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


def hide_gui(me,buttons=((widget("Config"),"SHOW_CONFIG"),(widget("Layout"),"SHOW_LAYOUT"),(widget("Create"),"SHOW_CREATE"))):

    me.mydata = not me.mydata

    if me.mydata:
        me.config(label = 'Show',underline = 1)
    else:
        me.config(label = 'Hide',underline = 0)
        
    send("HIDE_GUI",me.mydata)
    enable_state = 'disabled' if me.mydata else 'normal'
    for entry in buttons:
        entry[0].config(state = enable_state)
        if me.mydata and entry[0].mydata: send(entry[1],False)
        elif not me.mydata and entry[0].mydata: send(entry[1],True)

widget('Hide').do_command(hide_gui,wishWidget=True)


def check_mouse_on(mouse=widget('Mouse'),func=function_callback):
    #if container().is_mouse_select_on != mouse.mydata: mouse.invoke()
    if container().is_mouse_select_on != mouse.mydata: func(mouse,"MOUSE_SELECT_ON",'Mouse')

    
do_receive('SELECTION_CHANGED',check_mouse_on)

### ========================================================
