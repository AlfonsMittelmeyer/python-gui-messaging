config(**{'grid_cols': '(5, 75, 0, 0)', 'grid_rows': '(1, 25, 0, 0)'})

Frame('ClassAndBaseLayout',**{'height': 100, 'bd': 2, 'width': 300})
goIn()

LabelFrame('baselayout',**{'text': 'Layout'})
goIn()

LabelFrame('GridLayout',**{'link': 'guidesigner/GridLayout.py'}).grid(row=2, sticky='ew')
LabelFrame('ItemLayout',**{'link': 'guidesigner/MenuItemLayout.py'}).grid(row=5, sticky='ew')
LabelFrame('MenuLayout',**{'link': 'guidesigner/MenuLayout.py'}).grid(row=6, sticky='ew')
LabelFrame('PackLayout',**{'link': 'guidesigner/PackLayout.py'}).grid(row=1, sticky='ew')
LabelFrame('PageLayout',**{'link': 'guidesigner/PageLayout.py'}).grid(row=7, sticky='ew')
LabelFrame('PaneLayout',**{'link': 'guidesigner/PaneLayout.py'}).grid(row=4, sticky='ew')
LabelFrame('PlaceLayout',**{'link': 'guidesigner/PlaceLayout.py'}).grid(row=3, sticky='ew')
LabelFrame('WindowLayout',**{'link': 'guidesigner/WindowLayout.py'}).grid(row=0, sticky='ew')

### CODE ===================================================

# full action for new or changed widgets
# for LAYOUTNEVER the LabelFrame LayoutShortShowHide has to be hidden and otherwise shown
# sends a BASE_LAYOUT_REFRESH to inside for the pack, grid and place portions
# sends a SHOW_LAYOUT for the layout details options
# sends a SHOW_SELECTION for showing, which widget is selected 

def base_layout_widget_changed(base_layout = container()):
    if this().Layout == LAYOUTNEVER: base_layout.unlayout()
    elif base_layout.Layout == NOLAYOUT: base_layout.grid()
    send("BASE_LAYOUT_REFRESH",this())
    send("SHOW_LAYOUT",this())

do_receive('BASE_LAYOUT_WIDGET_CHANGED',base_layout_widget_changed)

# ----- message receivers for messages from outside --------------------------------------

# full actions for a new created widget or a selection of another widget

def function():
    send('BASE_LAYOUT_WIDGET_CHANGED',this())
    send('BASE_LAYOUT_VALUE_REFRESH')

do_receive('SELECTION_CHANGED',function)

# for same widget, but changed values a base layout refresh - handled by pack, grid or place portions - is sufficient
do_receive('LAYOUT_OPTIONS_CHANGED',lambda: send('BASE_LAYOUT_VALUE_REFRESH'))

# ----- message receiver for messages from inside to outside --------------------------------------

# if the layout type wasn't changed, a value change in the layout options is sufficient: message  LAYOUT_VALUES_REFRESH
# if the widget didn't have a layout before, full actions have to be done, including a selection show, because
# the selection show also contains, whether the widget has a layout or not
# if the layout changed, the selection need not be shown new, only an internal refresh and a new show layout options have to be done

def function(layout_before):
    if layout_before == this().Layout: send('LAYOUT_VALUES_REFRESH',this())
    else:
        send("BASE_LAYOUT_REFRESH",this())
        send("SHOW_LAYOUT",this())
        if layout_before == NOLAYOUT:
            send('SELECTION_LAYOUT_CHANGED')

do_receive('BASE_LAYOUT_CHANGED',function,wishMessage=True)


# A routine for the pack and he grid layout: pack and grid must not occur in the same parent. ------------------------------------
# This would cause a system hang up of TkInter. If the parent (container) contains already the other layout (pack or grid),
# the pack or grid portion will be hidden (unlayout)

def hide_pack_or_grid(
    packly=widget('PackLayout'),
    gridly=widget('GridLayout'),
    placely=widget('PlaceLayout'),
    panely=widget('PaneLayout'),
    itemly=widget('ItemLayout'),
    menuly=widget('MenuLayout'),
    windowly=widget('WindowLayout'),
    pagely=widget('PageLayout')
    ):

    if this().Layout != LAYOUTNEVER:

        if this().tkClass == StatTkInter.Menu:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            panely.unlayout()
            pagely.unlayout()
            windowly.unlayout()
            menuly.grid()
            send("ENABLE_SASH_LIST",False)

        elif container() != this() and container().tkClass is StatTtk.Notebook:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            menuly.unlayout()
            windowly.unlayout()
            panely.unlayout()
            pagely.grid()
            send("ENABLE_SASH_LIST",False)

        elif container() != this() and container().tkClass in (StatTkInter.PanedWindow,StatTtk.PanedWindow):
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            menuly.unlayout()
            windowly.unlayout()
            pagely.unlayout()
            panely.grid()
            send("ENABLE_SASH_LIST",True)

        elif container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            panely.unlayout()
            menuly.unlayout()
            windowly.unlayout()
            pagely.unlayout()
            itemly.grid()
            send("ENABLE_SASH_LIST",False)
        elif this().Layout == WINDOWLAYOUT:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            panely.unlayout()
            menuly.unlayout()
            pagely.unlayout()
            itemly.unlayout()
            windowly.grid()
            send("ENABLE_SASH_LIST",False)
        else:
            if isinstance(container(),Canvas) and this() != container():
                windowly.grid()
            else:
                windowly.unlayout()

            placely.grid()
            packly.grid()
            gridly.grid()
            panely.unlayout()
            pagely.unlayout()
            menuly.unlayout()
            itemly.unlayout()
            send("ENABLE_SASH_LIST",False)

            cont = container()
            if container() == this() and container().master != None:
                cont = container().master
            cont_layouts = getContLayouts(cont)
            if cont_layouts & GRIDLAYOUT:
                if packly.Layout != NOLAYOUT: packly.unlayout()
            elif packly.Layout == NOLAYOUT: packly.grid()
            if cont_layouts & PACKLAYOUT:
                if gridly.Layout != NOLAYOUT: gridly.unlayout()
            elif gridly.Layout == NOLAYOUT: gridly.grid()

do_receive('BASE_LAYOUT_REFRESH', hide_pack_or_grid)


def select_hili_on(me):

    me.mydata=None
    try:
        me.mydata=[None,me["relief"],me["highlightthickness"],me["highlightbackground"]]
        me.config(relief="solid",highlightthickness=1,highlightbackground="blue")
        me.mydata[0]='hili_on'
    except TclError: pass
    if this() != me:
        setWidgetSelection(me)
        send('SELECTION_CHANGED')

def hili_off(me):
    if type(me.mydata) is list and me.mydata[0] == 'hili_on':
        me.config(relief=me.mydata[1],highlightthickness=me.mydata[2],highlightbackground=me.mydata[3])

def update_mouse_select_on(select_hili_on=select_hili_on,hili_off=hili_off):
    if container().is_mouse_select_on:
        do_event('<Button-1>',select_hili_on,this())
        do_event('<ButtonRelease-1>',hili_off,this())

do_receive('UPDATE_MOUSE_SELECT_ON',update_mouse_select_on)

def update_canvas_mouse_select_on(canvas,select_hili_on=select_hili_on,hili_off=hili_off):
    if canvas.master.is_mouse_select_on:
        canvas.mydata = [0,0,0,0,0,0,False,False]
        if canvas.Layout in (PACKLAYOUT,PANELAYOUT,WINDOWLAYOUT):
            canvas.do_event('<Button-1>',select_hili_on,this())
            canvas.do_event('<ButtonRelease-1>',hili_off,this())
        elif canvas.Layout == PLACELAYOUT:
            send('PLACE_MOUSE_ON',canvas)
        elif canvas.Layout == GRIDLAYOUT:
            send('GRID_MOUSE_ON',canvas)

do_receive("UPDATE_CANVAS_MOUSE_SELECT_ON",update_canvas_mouse_select_on,wishMessage = True)
    
def mouse_select_on(select_on,select_hili_on = select_hili_on,hili_off=hili_off):
    widget_list = getAllWidgetsWithoutNoname(container())
    if not select_on:
        for wi in widget_list:
            if wi.Layout in (PACKLAYOUT,PANELAYOUT,GRIDLAYOUT,PLACELAYOUT,WINDOWLAYOUT):
                wi.unbind('<Button-1>')
                wi.unbind('<ButtonRelease-1>')
                wi.mydata = [0,0,0,0,0,0,False,False]
    else:
        for wi in widget_list:
            if wi.Layout in (PACKLAYOUT,PANELAYOUT,WINDOWLAYOUT):
                wi.do_event('<Button-1>',select_hili_on,wi)
                wi.do_event('<ButtonRelease-1>',hili_off,wi)
            elif wi.Layout == PLACELAYOUT:
                send('PLACE_MOUSE_ON',wi)
            elif wi.Layout == GRIDLAYOUT:
                send('GRID_MOUSE_ON',wi)

do_receive("MOUSE_SELECT_ON",mouse_select_on,wishMessage = True)

### ========================================================

goOut()
grid(row=1, sticky='ew')
LabelFrame('widgetclass',**{'text': 'Widget Class'})
goIn()

Label('class_label',**{'pady': '2', 'padx': '6', 'fg': 'blue', 'text': 'class_label', 'font': 'TkDefaultFont 9 bold', 'relief': 'sunken', 'bg': 'yellow'})
Label('text',**{'padx': '4', 'text': 'Class'})

widget('text').pack(side='left')
widget('class_label').pack(pady=6, side='left', padx=4, fill='x')

goOut()
grid(row=0, sticky='ew')

goOut()
grid(row=0, column=1, sticky='new')
LabelFrame('ConfigOptions',**{'link': 'guidesigner/ConfigOptions.py'}).grid(row=0, column=2, sticky='nw')
Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(row=0, sticky='nw')
LabelFrame('DetailedLayout',**{'link': 'guidesigner/DetailedLayout.py'}).grid(row=0, column=3, sticky='nw')
LabelFrame('Selection',**{'link': 'guidesigner/Selection.py'}).grid(row=0, column=4, sticky='nw')

### CODE ===================================================

def hide_gui(message,cont = container()):
    if message: cont.unlayout()
    else: cont.pack(anchor='nw') # GuiFrame

do_receive('HIDE_GUI',hide_gui,wishMessage=True)

widget("ConfigOptions").unlayout()
widget("DetailedLayout").unlayout()

### ========================================================
