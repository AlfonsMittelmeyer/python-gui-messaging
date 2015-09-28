LabelFrame('CreateWidget',text="""Create Widget""",link="guidesigner/CreateWidget.py")
pack(ipady='4',anchor='n',fill='x')

LabelFrame('SelectType',text="""Select Widget Type""",link="guidesigner/SelectType.py")
pack()

LabelFrame('MenuEntryTypes',text="""Select Widget Type""",link="guidesigner/Menubuttons.py")

LabelFrame('Menus',text="""Select Widget Type""",link="guidesigner/CascadeMenus.py")

### CODE ===================================================

def hide_create(msg,container):
    if msg: container.unlayout()
    else: container.grid()

do_receive("HIDE_CREATE",hide_create,container(),wishMessage=True)

def switch_buttons(buttons=widget('SelectType'),menubuttons=widget('MenuEntryTypes'),menus=widget('Menus')):
    if isinstance(container(),Menu):
        buttons.unlayout()
        menus.unlayout()
        menubuttons.pack()
    elif isinstance(container(),MenuItem):
        buttons.unlayout()
        menubuttons.unlayout()
        menus.pack()
    else:
        menubuttons.unlayout()
        menus.unlayout()
        buttons.pack()

do_receive('SELECTION_CHANGED',switch_buttons)
### ========================================================
