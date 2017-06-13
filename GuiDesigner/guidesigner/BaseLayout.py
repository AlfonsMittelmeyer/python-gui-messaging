config(text = 'Layout')
config(**{'grid_rows': '(9, 0, 0, 1)', 'grid_cols': '(1, 0, 0, 1)'})

LabelFrame('WindowLayout',link="guidesigner/WindowLayout.py")
grid(sticky='ew',row='0')

LabelFrame('PackLayout',link="guidesigner/PackLayout.py")
grid(sticky='ew',row='1')

LabelFrame('GridLayout',link="guidesigner/GridLayout.py")
grid(sticky='ew',row='2')

LabelFrame('PlaceLayout',link="guidesigner/PlaceLayout.py")
grid(sticky='ew',row='3')

LabelFrame('PaneLayout',link="guidesigner/PaneLayout.py")
grid(sticky='ew',row='4')

LabelFrame('ItemLayout',link="guidesigner/MenuItemLayout.py")
grid(sticky='ew',row='5')

LabelFrame('MenuLayout',link="guidesigner/MenuLayout.py")
grid(sticky='ew',row='6')

LabelFrame('PageLayout',link="guidesigner/PageLayout.py")
grid(sticky='ew',row='7')

LabelFrame('LiftLayout',link="guidesigner/LiftLayout.py")
grid(sticky='ew',row='8')

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
    pagely=widget('PageLayout'),
    liftly=widget('LiftLayout'),
    ):

    if this().Layout != LAYOUTNEVER:

        if this().tkClass == StatTkInter.Menu:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            liftly.unlayout()
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
            liftly.unlayout()
            windowly.unlayout()
            panely.unlayout()
            pagely.grid()
            send("ENABLE_SASH_LIST",False)

        elif container() != this() and container().tkClass in (StatTkInter.PanedWindow,StatTtk.PanedWindow):
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            liftly.unlayout()
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
            liftly.unlayout()
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
            liftly.unlayout()
            pagely.unlayout()
            itemly.unlayout()
            windowly.grid()
            send("ENABLE_SASH_LIST",False)
        elif container() != this() and isinstance(container(),LiftWindow):
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            panely.unlayout()
            menuly.unlayout()
            liftly.grid()
            pagely.unlayout()
            itemly.unlayout()
            windowly.unlayout()
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
            liftly.unlayout()
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
