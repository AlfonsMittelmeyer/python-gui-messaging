LabelFrame('GridLayout',link="guidesigner/GridLayout.py")
grid(sticky='ew',row='0')


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
        if layout_before == NOLAYOUT: send('SELECTION_LAYOUT_CHANGED')

do_receive('BASE_LAYOUT_CHANGED',function,wishMessage=True)


# A routine for the pack and he grid layout: pack and grid must not occur in the same parent. ------------------------------------
# This would cause a system hang up of TkInter. If the parent (container) contains already the other layout (pack or grid),
# the pack or grid portion will be hidden (unlayout)

def hide_pack_or_grid(gridly=widget('GridLayout')):

    if this().Layout != LAYOUTNEVER:

        if this().tkClass == StatTkInter.Menu:
            gridly.unlayout()

        elif container() != this() and container().tkClass in (StatTkInter.PanedWindow,tkinter.tk.PanedWindow):
            gridly.unlayout()

        elif container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT:
            gridly.unlayout()

        else:
            gridly.grid()
            cont = container()
            if container() == this() and container().master != None:
                cont = container().master
            cont_layouts = getContLayouts(cont)
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
    
def mouse_select_on(select_on,select_hili_on = select_hili_on,hili_off=hili_off):
    widget_list = getAllWidgetsWithoutNoname(container())
    if not select_on:
        for wi in widget_list:
            if wi.Layout in (PACKLAYOUT,PANELAYOUT,GRIDLAYOUT,PLACELAYOUT):
                wi.unbind('<Button-1>')
                wi.unbind('<ButtonRelease-1>')
                wi.mydata = [0,0,0,0,0,0,False,False]
    else:
        for wi in widget_list:
            if wi.Layout in (PACKLAYOUT,PANELAYOUT):
                wi.do_event('<Button-1>',select_hili_on,wi)
                wi.do_event('<ButtonRelease-1>',hili_off,wi)
            elif wi.Layout == PLACELAYOUT:
                send('PLACE_MOUSE_ON',wi)
            elif wi.Layout == GRIDLAYOUT:
                send('GRID_MOUSE_ON',wi)

do_receive("MOUSE_SELECT_ON",mouse_select_on,wishMessage = True)

### ========================================================
