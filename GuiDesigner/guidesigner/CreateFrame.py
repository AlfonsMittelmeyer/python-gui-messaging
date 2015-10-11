LabelFrame('CreateWidget',text="""Create Widget""",link="guidesigner/CreateWidget.py")
pack(ipady='4',anchor='n',fill='x')

LabelFrame('SelectType',text="""Select Widget Type""",link="guidesigner/SelectType.py")
pack()

LabelFrame('MenuEntryTypes',text="""Select Widget Type""",link="guidesigner/Menubuttons.py")

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

    elif isinstance(container(),MenuItem) or isinstance(container(),Menubutton):
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
