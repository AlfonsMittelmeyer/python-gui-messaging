LabelFrame('PackLayout',link="guidesigner/PackLayout.py")
grid(sticky='ew',row='0')

LabelFrame('GridLayout',link="guidesigner/GridLayout.py")
grid(sticky='ew',row='1')

LabelFrame('PlaceLayout',link="guidesigner/PlaceLayout.py")
grid(sticky='ew',row='2')

LabelFrame('PaneLayout',link="guidesigner/PaneLayout.py")
grid(sticky='ew',row='3')

LabelFrame('ItemLayout',link="guidesigner/MenuItemLayout.py")
grid(sticky='ew',row='4')

LabelFrame('MenuLayout',link="guidesigner/MenuLayout.py")
grid(sticky='ew',row='5')


### CODE ===================================================

# A routine for the pack and he grid layout: pack and grid must not occur in the same parent. ------------------------------------
# This would cause a system hang up of TkInter. If the parent (container) contains already the other layout (pack or grid),
# the pack or grid portion will be hidden (unlayout)

def hide_pack_or_grid(packly=widget('PackLayout'),gridly=widget('GridLayout'),placely=widget('PlaceLayout'),panely=widget('PaneLayout'),itemly=widget('ItemLayout'),menuly=widget('MenuLayout')):

    if this().Layout != LAYOUTNEVER:

        if this().tkClass == StatTkInter.Menu:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            panely.unlayout()
            menuly.grid()
            send("ENABLE_SASH_LIST",False)

        elif container() != this() and container().tkClass == StatTkInter.PanedWindow:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            itemly.unlayout()
            menuly.unlayout()
            panely.grid()
            send("ENABLE_SASH_LIST",True)

        elif container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT:
            packly.unlayout()
            gridly.unlayout()
            placely.unlayout()
            panely.unlayout()
            menuly.unlayout()
            itemly.grid()
            send("ENABLE_SASH_LIST",False)
        else:
            placely.grid()
            packly.grid()
            gridly.grid()
            panely.unlayout()
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
    
def mouse_select_on(select_on,select_hili_on = select_hili_on,hili_off=hili_off):
    widget_list = getAllWidgetsWithoutNoname(container())
    if not select_on:
        for wi in widget_list:
            if wi.Layout in (PACKLAYOUT,PANELAYOUT,GRIDLAYOUT,PLACELAYOUT):
                wi.unbind('<Button-1>')
                wi.unbind('<ButtonRelease-1>')
                wi.mydata = None
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