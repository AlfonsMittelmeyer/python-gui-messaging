Frame('WholeFrame')
goIn()
LabelFrame('WidgetPath',**{'text': 'Path'})
goIn()
#Label('message_path',**{'width': '70', 'anchor': 'w','bg':'#ffffa0'}).pack(**{'anchor': 'w', 'fill': 'x'})
Message('message_path',**{'width': '550', 'anchor': 'nw','bg':'#ffffa0'}).pack(**{'anchor': 'w', 'fill': 'x','expand':'1'})
Frame('Frame',**{'width': '550'}).pack(anchor = 'nw')


### CODE ===================================================



def set_wraplength(me):
    me['width'] = me.winfo_width()

widget("message_path").do_event("<Configure>",set_wraplength,wishWidget=True)


def show_path(path_widget = widget('message_path')):

    selection_before = Selection()
    path_name = ''
 
    if this() == container():
        path_name = '/'
        goOut()

    while not isinstance(container(),_CreateTopLevelRoot):

        if this().isMainWindow: _Selection._container = _TopLevelRoot._container

        name_index = getNameAndIndex()
        if name_index[1] == -1: name = name_index[0]
        else: name = name_index[0]+','+str(name_index[1])
        path_name = '/' + name + path_name

        goOut()
    
    path_widget.text('/'+path_name)
    
    setSelection(selection_before)
    
do_receive('SELECTION_CHANGED',show_path)

### ========================================================

goOut()
pack(**{'anchor': 'w', 'fill': 'x'})
Frame('GuiFrame')
goIn()

Frame('CreateFrame',link="guidesigner/CreateFrame.py")
grid(sticky='nw',row='0')

LabelFrame('BaseLayout',text="""Layout""",link="guidesigner/BaseLayout.py")
grid(column='1',sticky='nw',row='0')

LabelFrame("ConfigOptions",text="Config",link="guidesigner/ConfigOptions.py")
rcgrid(0,2,sticky='nw')

Frame("DetailedLayout",link="guidesigner/DetailedLayout.py")
rcgrid(0,3,sticky='nw')

LabelFrame("Selection",text="Selection",link="guidesigner/Selection.py")
rcgrid(0,4,sticky='nw')

### CODE ===================================================

def hide_gui(message,cont = container()):
    if message: cont.unlayout()
    else: cont.pack(anchor='nw') # GuiFrame

do_receive('HIDE_GUI',hide_gui,wishMessage=True)

widget("ConfigOptions").unlayout()
widget("DetailedLayout").unlayout()

### ========================================================

goOut()
pack(anchor='nw') # GuiFrame
goOut()
pack(anchor='nw') # WholeFrame
