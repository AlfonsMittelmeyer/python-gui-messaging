LabelFrame('CreateWidget',text="""Create Widget""",link="guidesigner/CreateWidget.py")
pack(ipady='4',anchor='n',fill='x')

LabelFrame('SelectType',text="""Select Widget Type""",link="guidesigner/SelectType.py")
pack()

LabelFrame('MenuEntryTypes',text="""Select Widget Type""",link="guidesigner/Menubuttons.py")

LabelFrame('Menus',text="""Select Widget Type""",link="guidesigner/CascadeMenus.py")

### CODE ===================================================

container().mydata = False

def show_create(msg,cont=container()):

    if not isinstance(container(),_CreateTopLevelRoot):
        if msg: cont.grid()
        else: cont.unlayout()

    if msg: cont.mydata = True
    else: cont.mydata = False


do_receive("SHOW_CREATE",show_create,wishMessage=True)

def switch_buttons(buttons=widget('SelectType'),menubuttons=widget('MenuEntryTypes'),menus=widget('Menus')):

    if isinstance(container(),Menu):
        buttons.unlayout()
        menus.unlayout()
        menubuttons.pack()
    elif isinstance(container(),MenuItem) or isinstance(container(),Menubutton):
        buttons.unlayout()
        menubuttons.unlayout()
        menus.pack()
    else:
        menubuttons.unlayout()
        menus.unlayout()
        buttons.pack()

do_receive('SELECTION_CHANGED',switch_buttons)

def enable_container(cont=container()):
    if cont.mydata:
        if not isinstance(container(),_CreateTopLevelRoot): cont.grid()
        else: cont.unlayout()

do_receive("SELECTION_CHANGED",enable_container)


### ========================================================
