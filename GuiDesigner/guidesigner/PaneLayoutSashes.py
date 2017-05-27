config(pady='2', padx='1', text='Sashes')


### CODE ===================================================

#widget('Sashes').mydata=[False,0,None,None]
container().mydata=[False,0,None,None]
container().panewindow = None

def function_get_sash_list(pane_win = container()):
    if pane_win.panewindow == None or not widget_exists(pane_win.panewindow):
        return None
    index = 0
    sash_list = []

    if isinstance(pane_win.panewindow,StatTtk.PanedWindow):
        if str(pane_win.panewindow['orient'])=='vertical':
            while True:
                try:
                    sash_list.append((1,pane_win.panewindow.sashpos(index)))
                    index += 1
                except: break
        else:
            while True:
                try:
                    sash_list.append((pane_win.panewindow.sashpos(index),1))
                    index += 1
                except: break

    else:
        while True:
            try:
                sash_list.append(pane_win.panewindow.sash_coord(index))
                index += 1
            except: break

    return sash_list

def change_sash_position(index,x_entry,y_entry,pane_win=container()):
    if isinstance(pane_win.panewindow,StatTtk.PanedWindow):
        if str(pane_win.panewindow['orient']) =='vertical':
            try:
                y = int(y_entry.get())
                pane_win.panewindow.sashpos(index,y)
            except ValueError:
                y = pane_win.panewindow.sashpos(index)
            pos = (1,y)
        else: 
            try:
                x = int(x_entry.get())
                pane_win.panewindow.sashpos(index,x)
            except ValueError:
                x = pane_win.panewindow.sashpos(index)
            pos = (x,1)
    else:
        pane_win.panewindow.sash_place(index, int(x_entry.get()), int(y_entry.get()))
        pos = pane_win.panewindow.sash_coord(index)
    
    if pane_win.panewindow['orient'] == 'horizontal':
        y_entry.delete(0,END)
        y_entry.insert(0,pos[1])
    else:
        x_entry.delete(0,END)
        x_entry.insert(0,pos[0])
    

def refresh_sash_list(msg,me=container(),get_sash_list = function_get_sash_list,change_pos=change_sash_position,pane_win = container()):
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
                if str(pane_win.panewindow['orient'])=='vertical':
                    a['state'] = 'disabled'
                b=Spinbox('y',increment='1.0',width='4',from_=0,to='2000.0')
                rcgrid(i+1,1)
                b.delete(0,END)
                b.insert(0,sash_list[i][1])
                if str(pane_win.panewindow['orient']) !='vertical':
                    b['state'] = 'disabled'
                xy_list.append((a,b))
                a.mydata = (i,a,b)
                a.do_command(change_pos,(i,a,b))
                b.do_command(change_pos,(i,a,b))
                a.do_event("<Return>",change_pos,(i,a,b))
                b.do_event("<Return>",change_pos,(i,a,b))
            me.mydata=xy_list
            setSelection(selection_before)

def update_sash_values(index,coordinates,sashes = container()):
    sashes.mydata[index][0].delete(0,END)
    sashes.mydata[index][0].insert(0,coordinates[0])
    sashes.mydata[index][1].delete(0,END)
    sashes.mydata[index][1].insert(0,coordinates[1])

def paned_win_event(event,sash_update=update_sash_values):
    widget = event.widget
    xpos = event.x
    ypos = event.y

    if isinstance(widget,StatTtk.PanedWindow):
        index = widget.identify(xpos, ypos)
        if isinstance(index,int):
            if str(widget['orient']) =='vertical':
                sash_update(index,(1,widget.sashpos(index)))
            else:
                sash_update(index,(widget.sashpos(index),1))
    else:
        identify_data = widget.identify(xpos, ypos)
        try:
            index = identify_data[0]
            tag = identify_data[1]
        except IndexError: return

        sash_update(index, widget.sash_coord(index))

sash_enabled = [False,]

class EnabledSash:
    def __init__(self):
        self.enabled = False
        self.b1_functionid = None

def enable_motion(enable,pane_win=container(),refresh=refresh_sash_list,paned_event=paned_win_event,enabled_sash = EnabledSash):
    if enable:
        pane_win.panewindow = container()
        refresh(None)
        enabled_sash.b1_functionid = container().bind('<B1-Motion>',paned_event)
        enabled_sash.enabled = True
    else:
        if pane_win.panewindow != None and widget_exists(pane_win.panewindow):
            if enabled_sash.enabled:
                pane_win.panewindow.unbind('<B1-Motion>',enabled_sash.b1_functionid)
        enabled_sash.enabled = False

# == take another owner because of me.destroyContent() in refresh_sash_list
proxy.do_receive(container().master,'BASE_LAYOUT_REFRESH',refresh_sash_list)
proxy.do_receive(container().master,'ENABLE_SASH_LIST',enable_motion)


### ========================================================
