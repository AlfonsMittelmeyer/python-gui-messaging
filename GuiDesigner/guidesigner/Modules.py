Frame('GuiFrame',**{'link': 'guidesigner/GuiFrame.py'})
Frame('Toolbar',**{'link': 'guidesigner/Toolbar.py'})
LabelFrame('WidgetPath',**{'text': ' Path: ','labelanchor' : 'w','bd' : 0})
goIn()

Frame('Frame')
Message('message_path',**{'bg': '#ffffa0','anchor': 'nw'})

widget('message_path').pack(anchor='w', fill='x', expand=1)
widget('Frame').pack(anchor='nw')

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

    if isinstance(container(),_CreateTopLevelRoot):
        if this() != container():
            name_index = getNameAndIndex()
            if name_index[0] != NONAME:
                if name_index[1] == -1: name = name_index[0]
                else: name = name_index[0]+','+str(name_index[1])
                path_name = '/' + name + path_name
            

    while not isinstance(container(),_CreateTopLevelRoot):

        if this().isMainWindow: _Selection._container = _TopLevelRoot._container

        name_index = getNameAndIndex()
        if name_index[0] != NONAME:
            if name_index[1] == -1: name = name_index[0]
            else: name = name_index[0]+','+str(name_index[1])
            path_name = '/' + name + path_name
        goOut()
    
    path_widget.text('/'+path_name)

    setSelection(selection_before)
    
do_receive('SELECTION_CHANGED',show_path)

### ========================================================

goOut()


widget('Toolbar').pack(fill='x')
widget('WidgetPath').pack(anchor='w', fill='x')
widget('GuiFrame').pack(anchor='nw')
