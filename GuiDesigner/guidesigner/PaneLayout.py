config(**{'grid_cols': '(2, 75, 0, 0)','grid_rows': '(1, 25, 0, 0)'})

Button('ADD',**{'text': 'ADD', 'pady': '2', 'padx': '1m', 'bd': '3', 'bg': 'green', 'anchor': 'n'}).grid(**{'column': '1', 'sticky': 'nesw', 'padx': '5', 'row': '0'})
Label('PaneTitle',**{'text': 'pane', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'bg': 'yellow', 'fg': 'blue', 'relief': 'ridge', 'anchor': 'n'}).grid(**{'sticky': 'ew', 'row': '0'})
LabelFrame('Sashes',**{'text': 'Sashes', 'pady': '2', 'padx': '1'}).grid(**{'columnspan': '3', 'row': '1'})

### CODE ===================================================

widget('Sashes').mydata=[False,0,None,None]

def function_get_sash_list(pane_win = container()):
    if pane_win.mydata == None:
        return None
    index = 0
    sash_list = []
    while True:
        try:
            sash_list.append(pane_win.mydata.sash_coord(index))
            index += 1
        except: break
    return sash_list

def change_sash_position(index,x_entry,y_entry,pane_win=container()):
    pane_win.mydata.sash_place(index, int(x_entry.get()), int(y_entry.get()))
    pos = pane_win.mydata.sash_coord(index)
    if pane_win.mydata['orient'] == 'horizontal':
        y_entry.delete(0,END)
        y_entry.insert(0,pos[1])
    else:
        x_entry.delete(0,END)
        x_entry.insert(0,pos[0])

def refresh_sash_list(me=widget("Sashes"),get_sash_list = function_get_sash_list,change_pos=change_sash_position):
    sash_list = get_sash_list()
    if sash_list != None:
        xy_list = []
        me.destroyActions()
        me.destroyContent()
        if len(sash_list) > 0:
            selection_before = Selection()
            setWidgetSelection(me)
            goIn()
            Label("lx",text="x").rcgrid(0,0)
            Label("ly",text="y").rcgrid(0,1)
            for i in range(len(sash_list)):
                a=Spinbox('x',increment='1.0',width='4',from_=0,to='2000.0')
                rcgrid(i+1,0)
                a.delete(0,END)
                a.insert(0,sash_list[i][0])
                b=Spinbox('y',increment='1.0',width='4',from_=0,to='2000.0')
                rcgrid(i+1,1)
                b.delete(0,END)
                b.insert(0,sash_list[i][1])
                xy_list.append((a,b))
                a.mydata = (i,a,b)
                a.do_command(change_pos,(i,a,b))
                b.do_command(change_pos,(i,a,b))
                a.do_event("<Return>",change_pos,(i,a,b))
                b.do_event("<Return>",change_pos,(i,a,b))
            me.mydata=xy_list
            setSelection(selection_before)

def update_sash_values(index,coordinates,sashes = widget('Sashes')):
    sashes.mydata[index][0].delete(0,END)
    sashes.mydata[index][0].insert(0,coordinates[0])
    sashes.mydata[index][1].delete(0,END)
    sashes.mydata[index][1].insert(0,coordinates[1])

def paned_win_event(event,sash_update=update_sash_values):
    widget = event.widget
    xpos = event.x
    ypos = event.y

    identify_data = event.widget.identify(xpos, ypos)
    try:
        index = identify_data[0]
        tag = identify_data[1]
    except IndexError: return

    sash_update(index, widget.sash_coord(index))

def do_add():
    pane()
    send('UPDATE_MOUSE_SELECT_ON')
    send("BASE_LAYOUT_CHANGED",NOLAYOUT) # NOLAYOUT because always trigger a sash_list_refreh via event BASE_LAYOUT_REFRESH

def enable_motion(enable,panewin=container(),refresh=refresh_sash_list,paned_event=paned_win_event):
    if enable:
        panewin.mydata = container()
        refresh()
        container().bind('<B1-Motion>',paned_event)
    elif panewin.mydata != None:
        panewin.mydata.unbind('<B1-Motion>')

widget("ADD").do_command(do_add)
do_receive('BASE_LAYOUT_REFRESH',refresh_sash_list)
do_receive("ENABLE_SASH_LIST",enable_motion,wishMessage=True)

### ========================================================
