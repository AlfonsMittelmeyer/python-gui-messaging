LabelFrame('CreateWidget',link='guidesigner/CreateWidget.py').grid(row=0, sticky='ew')
LabelFrame('MenuEntryTypes',link='guidesigner/Menubuttons.py').grid(row=2, sticky='ew')
LabelFrame('SelectType',link='guidesigner/SelectType.py').grid(row=3)
LabelFrame('tkinter_or_ttk',link='guidesigner/TkinterOrTtk.py').grid(row=1, sticky='ew')
Frame('ttk_select_type',link='guidesigner/SelectTypeTtk.py').grid(row=4, sticky='nesw')

### CODE ===================================================

widget('ttk_select_type').unlayout()
widget('MenuEntryTypes').unlayout()

container().mydata = [False,GRIDLAYOUT,False]

def show_create(msg,cont=container()):

    if not isinstance(container(),_CreateTopLevelRoot):
        if msg: cont.grid()
        else: cont.unlayout()

    if msg: cont.mydata[0] = True
    else: cont.mydata[0] = False


do_receive("SHOW_CREATE",show_create,wishMessage=True)

def switch_buttons(
    buttons=widget('SelectType'),
    menubuttons=widget('MenuEntryTypes'),
    ttkbuttons=widget('ttk_select_type'),
    tk_or_ttk = widget('tkinter_or_ttk'),
    cont=container()):

    if isinstance(container(),Menu):
        if cont.mydata[1] != MENUITEMLAYOUT:
            cont.mydata[1] = MENUITEMLAYOUT
            buttons.unlayout()
            ttkbuttons.unlayout()
            tk_or_ttk.unlayout()
            menubuttons.grid()
            send('CREATE_CLASS_SELECTED',('command','command'))

    elif isinstance(container(),MenuItem) or isinstance(container(),Menubutton) or isinstance(container(),ttk.Menubutton):
        if cont.mydata[1] != MENULAYOUT:
            cont.mydata[1] = MENULAYOUT
            buttons.unlayout()
            tk_or_ttk.unlayout()
            ttkbuttons.unlayout()
            menubuttons.unlayout()
            send('CREATE_CLASS_SELECTED',('menu','Menu'))
    else:
        if cont.mydata[1] != GRIDLAYOUT:
            cont.mydata[1] = GRIDLAYOUT
            menubuttons.unlayout()
            tk_or_ttk.grid()
            send('CREATE_CLASS_SELECTED',('button','Button'))

        if cont.mydata[2]:
            if ttkbuttons.Layout == NOLAYOUT:
                ttkbuttons.grid()
                buttons.unlayout()
        else:
            if buttons.Layout == NOLAYOUT:
                buttons.grid()
                ttkbuttons.unlayout()

def switch_tk_ttk(message,cont=container(),switch_buttons = switch_buttons):
    cont.mydata[2] = message
    switch_buttons()

do_receive('SELECTION_CHANGED',switch_buttons)
do_receive("SELECT_TTK",switch_tk_ttk,wishMessage=True)

def enable_container(cont=container()):
    if cont.mydata[0]:
        if not isinstance(container(),_CreateTopLevelRoot): cont.grid()
        else: cont.unlayout()

do_receive("SELECTION_CHANGED",enable_container)


### ========================================================
