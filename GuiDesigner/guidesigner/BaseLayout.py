config(text = 'Layout')
config(**{'grid_rows': '(10, 0, 0, 1)', 'grid_cols': '(1, 0, 0, 1)'})

LabelFrame('LabelLayout',link="guidesigner/LabelLayout.py")
grid(sticky='ew',row='1')

LabelFrame('WindowLayout',link="guidesigner/WindowLayout.py")
grid(sticky='ew',row='1')

LabelFrame('PackLayout',link="guidesigner/PackLayout.py")
grid(sticky='ew',row='2')

LabelFrame('GridLayout',link="guidesigner/GridLayout.py")
grid(sticky='ew',row='3')

LabelFrame('PlaceLayout',link="guidesigner/PlaceLayout.py")
grid(sticky='ew',row='4')

LabelFrame('PaneLayout',link="guidesigner/PaneLayout.py")
grid(sticky='ew',row='5')

LabelFrame('ItemLayout',link="guidesigner/MenuItemLayout.py")
grid(sticky='ew',row='6')

LabelFrame('MenuLayout',link="guidesigner/MenuLayout.py")
grid(sticky='ew',row='7')

LabelFrame('PageLayout',link="guidesigner/PageLayout.py")
grid(sticky='ew',row='8')

LabelFrame('Basement',link="guidesigner/Basement.py")
grid(sticky='ew',row='9')


### CODE ===================================================

# full action for new or changed widgets
# for LAYOUTNEVER the LabelFrame LayoutShortShowHide has to be hidden and otherwise shown
# sends a BASE_LAYOUT_REFRESH to inside for the pack, grid and place portions
# sends a SHOW_LAYOUT for the layout details options
# sends a SHOW_SELECTION for showing, which widget is selected 

def main():


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
            #if layout_before == NOLAYOUT:
                #send('SELECTION_LAYOUT_CHANGED')
            send('SELECTION_LAYOUT_CHANGED')

    do_receive('BASE_LAYOUT_CHANGED',function,wishMessage=True)


    # A routine for the pack and he grid layout: pack and grid must not occur in the same parent. ------------------------------------
    # This would cause a system hang up of TkInter. If the parent (container) contains already the other layout (pack or grid),
    # the pack or grid portion will be hidden (unlayout)

    def hide_pack_or_grid(
        lably = widget('LabelLayout'),
        packly=widget('PackLayout'),
        gridly=widget('GridLayout'),
        placely=widget('PlaceLayout'),
        panely=widget('PaneLayout'),
        itemly=widget('ItemLayout'),
        menuly=widget('MenuLayout'),
        windowly=widget('WindowLayout'),
        pagely=widget('PageLayout'),
        basement = widget('Basement'),
        ):

        if this().Layout != LAYOUTNEVER:

            if this().tkClass == StatTkInter.Menu:
                lably.unlayout()
                packly.unlayout()
                gridly.unlayout()
                placely.unlayout()
                itemly.unlayout()
                panely.unlayout()
                pagely.unlayout()
                windowly.unlayout()
                menuly.grid()
                basement.unlayout()

                send("ENABLE_SASH_LIST",False)

            elif container() != this() and container().tkClass is StatTtk.Notebook:
                lably.unlayout()
                packly.unlayout()
                gridly.unlayout()
                basement.unlayout()
                placely.unlayout()
                itemly.unlayout()
                menuly.unlayout()
                windowly.unlayout()
                panely.unlayout()
                pagely.grid()
                send("ENABLE_SASH_LIST",False)

            elif container() != this() and container().tkClass in (StatTkInter.PanedWindow,StatTtk.PanedWindow):
                lably.unlayout()
                packly.unlayout()
                gridly.unlayout()
                placely.unlayout()
                itemly.unlayout()
                basement.unlayout()
                menuly.unlayout()
                windowly.unlayout()
                pagely.unlayout()
                panely.grid()
                send("ENABLE_SASH_LIST",True)

            elif container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT:
                lably.unlayout()
                packly.unlayout()
                gridly.unlayout()
                basement.unlayout()
                placely.unlayout()
                panely.unlayout()
                menuly.unlayout()
                windowly.unlayout()
                pagely.unlayout()
                itemly.grid()
                send("ENABLE_SASH_LIST",False)
            elif this().Layout == WINDOWLAYOUT:
                lably.unlayout()
                packly.unlayout()
                gridly.unlayout()
                placely.unlayout()
                panely.unlayout()
                basement.unlayout()
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

                if this() !=container()\
                and isinstance(container(),(Tk,Toplevel,Frame,LabelFrame,ttk.Frame,ttk.LabelFrame))\
                and not isinstance(this(),StatTkInter.Menu):
                    basement.grid()
                else:
                    basement.unlayout()
                if isinstance(container(),(LabelFrame,ttk.LabelFrame)) and container() != this():
                    lably.grid()
                else:
                    lably.unlayout()
                    
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
                if cont_layouts & GRIDLAYOUT:# or this().grid_slaves():
                    if packly.Layout != NOLAYOUT: packly.unlayout()
                elif packly.Layout == NOLAYOUT: packly.grid()
                if cont_layouts & PACKLAYOUT:# or this().master.Layout == PACKLAYOUT:
                    if gridly.Layout != NOLAYOUT: gridly.unlayout()
                elif gridly.Layout == NOLAYOUT: gridly.grid()

    do_receive('BASE_LAYOUT_REFRESH', hide_pack_or_grid)



    class DynTk_HighLight:

        def __init__(self,me):
            self.me = me
            dyntk_highlight(me)

            if this() != me:
                setWidgetSelection(me)
                send('SELECTION_CHANGED')

        def restore(self):
            dyntk_unhighlight(self.me)
            
    def highlight_widget(me):
        me.dyntk_highlight = DynTk_HighLight(me)
        me.do_event('<ButtonRelease-1>',highlight_mouse_up,me)

    def highlight_mouse_up(me):
        me.unbind('<ButtonRelease-1>')
        me.dyntk_highlight.restore()
        me.dyntk_highlight = None



    # this is sent bei PackLayout.py and PaneLayout.py ========================
    # and should also be sent by PageLayout.py and WindowLayout

    def update_mouse_select_on():
        if container().is_mouse_select_on:
            do_event('<Button-1>',highlight_widget,this())

    do_receive('UPDATE_MOUSE_SELECT_ON',update_mouse_select_on)


    # this is sent by CanvasPaint, when canvas paint ends, the canvas shall be selectable normal again,
    # if mouse select is on
    # but it's not a special canvas treating and could be used by every widget
    def update_canvas_mouse_select_on(canvas):
        if canvas.master.is_mouse_select_on:
            if canvas.Layout in (PACKLAYOUT,WINDOWLAYOUT,PANELAYOUT,TTKPANELAYOUT,PAGELAYOUT):
                canvas.do_event('<Button-1>',highlight_widget,canvas)
            elif canvas.Layout == PLACELAYOUT:
                send('PLACE_MOUSE_ON',canvas)
            elif canvas.Layout == GRIDLAYOUT:
                send('GRID_MOUSE_ON',canvas)

    do_receive("UPDATE_CANVAS_MOUSE_SELECT_ON",update_canvas_mouse_select_on,wishMessage = True)
        

    # this is for all widgets in the container ========================
    def mouse_select_on(select_on):
        widget_list = getAllWidgetsWithoutNoname(container())
        if not select_on:
            for wi in widget_list:
                if wi.Layout in (GRIDLAYOUT,PLACELAYOUT,PACKLAYOUT,WINDOWLAYOUT,PANELAYOUT,TTKPANELAYOUT,PAGELAYOUT):
                    wi.unbind('<Button-1>')
        else:
            for wi in widget_list:
                if wi.Layout in (PACKLAYOUT,WINDOWLAYOUT,PANELAYOUT,TTKPANELAYOUT,PAGELAYOUT):
                    wi.do_event('<Button-1>',highlight_widget,wi)
                elif wi.Layout == GRIDLAYOUT:
                    send('GRID_MOUSE_ON',wi)
                elif wi.Layout == PLACELAYOUT:
                    send('PLACE_MOUSE_ON',wi)


    do_receive("MOUSE_SELECT_ON",mouse_select_on,wishMessage = True)

main()

### ========================================================
