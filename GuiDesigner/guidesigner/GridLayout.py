config(**{'grid_cols': '(4, 50, 0, 0)', 'grid_rows': '(6, 20, 0, 0)'})

Entry('EntryRows',**{'width': '6'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '1'})
Entry('EntryCols',**{'width': '6'}).grid(**{'column': '2', 'sticky': 'ns', 'row': '1'})
Checkbutton('Individual',**{'highlightthickness': '0', 'text': 'Indi-\nvidual', 'highlightbackground': '#ff8000'}).grid(**{'rowspan': '2', 'column': '3', 'sticky': 'esw', 'row': '3'})
Button('ButtonShow',**{'text': 'Show', 'bd': '3', 'bg': 'green'}).grid(**{'column': '3', 'sticky': 'nesw', 'row': '5'})
Spinbox('EntryRowHeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '2'})
Spinbox('EntryColWidth',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '2', 'sticky': 'ns', 'row': '2'})
Spinbox('EntryRowPad',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '3'})
Spinbox('EntryColPad',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '2', 'sticky': 'ns', 'row': '3'})
Spinbox('EntryRowWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '4'})
Spinbox('EntryColWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '2', 'sticky': 'ns', 'row': '4'})
Button('ButtonGrid',**{'text': 'GRID', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'bg': 'green'}).grid(**{'sticky': 'nesw', 'row': '5'})
Button('ButtonHide',**{'text': 'Hide', 'padx': '1m', 'bd': '3', 'bg': 'green'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '5'})
Button('Grid()',**{'text': 'Grid()', 'padx': '1m', 'bd': '3', 'bg': 'green'}).grid(**{'column': '1', 'sticky': 'nesw', 'row': '5'})
Label('LableTitle',**{'text': 'grid', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'fg': 'blue', 'relief': 'ridge'}).grid(**{'sticky': 'nesw', 'row': '0'})
Label('lcols',**{'text': 'Columns', 'font': 'TkDefaultFont 9 bold'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '0'})
Label('lheight',**{'text': 'Min Height'}).grid(**{'sticky': 'e', 'row': '2'})
Label('lpad',**{'text': 'pad'}).grid(**{'sticky': 'e', 'row': '3'})
Label('lrows',**{'text': 'Rows', 'font': 'TkDefaultFont 9 bold'}).grid(**{'column': '1', 'sticky': 'nesw', 'row': '0'})
Label('lweight',**{'text': 'weight'}).grid(**{'sticky': 'e', 'row': '4'})
Label('lwidth',**{'text': 'Min Width'}).grid(**{'column': '3', 'sticky': 'w', 'row': '2'})

### CODE ===================================================

var = IntVar()
widget('Individual').config(variable = var, onvalue = 1, offvalue = 0)
widget('Individual').mydata=var

# -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------

# Order of Entries for Tab

#Entry('EntryRows',**{'width': '6'}).grid(**{'column': '1', 'row': '1'})
#Entry('EntryCols',**{'width': '6'}).grid(**{'column': '2', 'row': '1'})
#Spinbox('EntryRowHeight',**{'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '1', 'row': '2'})
#Spinbox('EntryColWidth',**{'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '2', 'row': '2'})
#Spinbox('EntryRowPad',**{'from': '0.0', 'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '1', 'row': '3'})
#Spinbox('EntryColPad',**{'from': '0.0', 'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '2', 'row': '3'})
#Spinbox('EntryRowWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'row': '4'})
#Spinbox('EntryColWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '2', 'row': '4'})
#Button('ButtonShow',**{'text': 'Show', 'bd': '3', 'bg': 'green'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '5'})


def main():

    #Button('ButtonForget',**{'text': 'Forget'}).grid(**{'column': '1', 'sticky': 'nesw', 'row': '5'})

    # -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------

    # set the bg color of the GridTitle label to yellow, if the current widget has a GRIDLAYOUT, otherwise to original color

    def do_bg_title(title = widget('LableTitle'),titlebg = widget('LableTitle')["bg"]):
        if this().Layout == GRIDLAYOUT: title['bg'] = "yellow"
        else: title['bg'] = titlebg

    do_receive('BASE_LAYOUT_REFRESH',do_bg_title)


    def hide_grid():
        deleteWidgetsForName(container(),NONAME)
        if container().grid_conf_individual_done:
            cols = container().grid_conf_cols[0]
            rows = container().grid_conf_rows[0]
            container().grid_columnconfigure(cols,minsize = 0,pad=0,weight=0)
            container().grid_rowconfigure(rows,minsize = 0,pad=0,weight=0)
            container().grid_conf_individual_done = False
        
        send("BASE_LAYOUT_REFRESH",this())

    widget('ButtonHide').do_command(hide_grid)

    def do_grid_forget():
        layout_before = this().Layout
        this().grid_forget()
        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

    #widget('ButtonForget').do_command(do_grid_forget)

    def update_rows(rows_widget=widget('EntryRows'),height_widget=widget('EntryRowHeight'),pad_widget = widget('EntryRowPad'),weight_widget=widget('EntryRowWeight')):

        try:
            rows = int(rows_widget.get())
        except ValueError: 
            rows_widget.delete(0,'end')
            rows_widget.insert(0,10)
            rows = 10

        row_height = int(height_widget.get())
        padvalue = int(pad_widget.get())
        weightvalue = int(weight_widget.get())

        container().grid_conf_rows = (rows,row_height,padvalue,weightvalue)


    def set_row_height():

        rows = container().grid_conf_rows[0]
        to_insert =  {'minsize':container().grid_conf_rows[1],'pad':container().grid_conf_rows[2],'weight':container().grid_conf_rows[3]}
        
        for row in range(rows):
            if container().grid_multi_conf_rows[row][0] == False: container().grid_multi_conf_rows[row][1] = dict(to_insert)
 
        for row in range(rows):
            container().grid_rowconfigure(row,**(container().grid_multi_conf_rows[row][1]))

    def update_row_values():
        update_rows()
        set_row_height()

    widget('EntryRowHeight').do_command(update_row_values)
    widget('EntryRowHeight').do_event('<Return>',update_row_values)
    widget('EntryRowWeight').do_command(update_row_values)
    widget('EntryRowWeight').do_event('<Return>',update_row_values)
    widget('EntryRowPad').do_command(update_row_values)
    widget('EntryRowPad').do_event('<Return>',update_row_values)

    def update_indiv_wish(wi = widget('Individual')):
        container().grid_conf_individual_wish = wi.mydata.get() == 1

    widget('Individual').do_command(update_indiv_wish)


    def update_cols(cols_widget=widget('EntryCols'),width_widget=widget('EntryColWidth'),pad_widget = widget('EntryColPad'),weight_widget=widget('EntryColWeight')):
        try:
            cols = int(cols_widget.get())
        except ValueError: 
            cols_widget.delete(0,'end')
            cols_widget.insert(0,10)
            cols = 6

        col_width = int(width_widget.get())
        padvalue = int(pad_widget.get())
        weightvalue = int(weight_widget.get())
        
        container().grid_conf_cols = (cols,col_width,padvalue,weightvalue)
       

    def set_col_width():

        cols = container().grid_conf_cols[0]
        to_insert =  {'minsize':container().grid_conf_cols[1],'pad':container().grid_conf_cols[2],'weight':container().grid_conf_cols[3]}
        
        for col in range(cols):
            if container().grid_multi_conf_cols[col][0] == False: container().grid_multi_conf_cols[col][1] = dict(to_insert)
 
        for col in range(cols):
            container().grid_columnconfigure(col,**(container().grid_multi_conf_cols[col][1]))

    def update_col_values():
        update_cols()
        set_col_width()


    widget('EntryColWidth').do_command(update_col_values)
    widget('EntryColWidth').do_event('<Return>',update_col_values)
    widget('EntryColPad').do_command(update_col_values)
    widget('EntryColPad').do_event('<Return>',update_col_values)
    widget('EntryColWeight').do_command(update_col_values)
    widget('EntryColWeight').do_event('<Return>',update_col_values)


    def shop_grid_top(x,y,indivmark,bg,index,grid_conf,update_function,item_text):

        selection_before = Selection()
        
        setWidgetSelection(indivmark) # the Frame should be the tkinter parent of the Toplevel Window
        goIn()

        Toplevel('GridTop',title='',geometry='+'+str(x)+'+'+str(y))

        Label('showRowCol',**{'text': str(index),'bg':'white','relief':'solid','width':4}).grid(**{'column': '1', 'row': '0','pady':5,'ipadx':5})
        Spinbox('EntrySize',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'row': '1','sticky':'ns'})
        this().delete(0,'end')
        this().insert(0,grid_conf['minsize'])
        Spinbox('EntryPad',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'row': '2','sticky':'ns'})
        this().delete(0,'end')
        this().insert(0,grid_conf['pad'])
        Spinbox('EntryWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'row': '3','sticky':'ns'})
        this().delete(0,'end')
        this().insert(0,grid_conf['weight'])
        Button('OK',**{'text':'OK'}).grid(**{'column': '1','row': '4'})
        do_command(lambda func=container().destroy: func())
        
        Label('lRowCol',**{'text': item_text}).grid(**{'sticky': 'e', 'row': '0'})
        Label('lpad',**{'text': 'pad'}).grid(**{'sticky': 'e', 'row': '2'})
        Label('lsize',**{'text': 'size'}).grid(**{'sticky': 'e', 'row': '1'})
        Label('lweight',**{'text': 'weight'}).grid(**{'sticky': 'e', 'row': '3'})

        top_window=container()

        def update_values(mark=indivmark,function=update_function,row_or_column=index,esize = widget('EntrySize'),epad = widget('EntryPad'), eweight = widget('EntryWeight')):
            function(mark,row_or_column,{'minsize':int(esize.get()),'pad':int(epad.get()),'weight':int(eweight.get())},bg)

        def update_size(message,mark=indivmark,wi_size=widget('EntrySize')):
            if message[1] == mark:
                wi_size.delete(0,'end')
                wi_size.insert(0,message[0])

        do_receive('UPDATE_INDIVIDUAL_GRID',update_size,wishMessage=True)
        do_receive('DESTROY_INDIVIDUAL_GRID_TOPLEVEL',lambda funct = top_window.destroy: funct())

        widget('EntrySize').do_command(update_values)
        widget('EntrySize').do_event('<Return>',update_values)
        widget('EntryPad').do_command(update_values)
        widget('EntryPad').do_event('<Return>',update_values)
        widget('EntryWeight').do_command(update_values)
        widget('EntryWeight').do_event('<Return>',update_values)
        
        top_window.transient(indivmark.myRoot())
        widget('EntrySize').focus_set()
        setSelection(selection_before)
        return top_window

    def update_individual(cont,wi=widget('Individual')):
        hilimark = 2 if cont.grid_conf_individual_has else 0
        wi['highlightthickness'] = hilimark
 
    def update_individual_mark(cont):

        mark = False

        grid_cols=cont.grid_multi_conf_cols
        for entry in grid_cols:
            if entry[0]:
                mark=True
                break

        grid_rows=cont.grid_multi_conf_rows
        for entry in grid_rows:
            if entry[0]:
                mark=True
                break
                
        cont.grid_conf_individual_has = mark
        update_individual(cont)
        

    def update_col(me,column,grid_conf,bg):
        cont = me.master
        cont.grid_multi_conf_cols[column][1] = grid_conf
        cont.grid_columnconfigure(column,**grid_conf)
        if grid_conf['minsize'] == cont.grid_conf_cols[1] and grid_conf['pad'] == cont.grid_conf_cols[2] and grid_conf['weight'] == cont.grid_conf_cols[3]:
            me['bg'] = bg
            cont.grid_multi_conf_cols[column][0] = False
        else:
            me['bg'] = 'orange'
            cont.grid_multi_conf_cols[column][0] = True
        update_individual_mark(cont)

    def update_row(me,row,grid_conf,bg):
        cont = me.master
        cont.grid_multi_conf_rows[row][1] = grid_conf
        cont.grid_rowconfigure(row,**grid_conf)
        if grid_conf['minsize'] == cont.grid_conf_rows[1] and grid_conf['pad'] == cont.grid_conf_rows[2] and grid_conf['weight'] == cont.grid_conf_rows[3]:
            me['bg'] = bg
            cont.grid_multi_conf_rows[row][0] = False
        else:
            me['bg'] = 'orange'
            cont.grid_multi_conf_rows[row][0] = True
        update_individual_mark(cont)

    def mouse_wheel_row(me,event,row,bg):
        grid_conf=me.master.grid_multi_conf_rows[row][1]
        if event.num == 5 or event.delta == -120:
            grid_conf['minsize'] -= 1
        if event.num == 4 or event.delta == 120:
            grid_conf['minsize'] += 1
        update_row(me,row,grid_conf,bg)
        send('UPDATE_INDIVIDUAL_GRID',(grid_conf['minsize'],me))

    def mouse_wheel_col(me,event,column,bg):
        grid_conf=me.master.grid_multi_conf_cols[column][1]
        if event.num == 5 or event.delta == -120:
            grid_conf['minsize'] -= 1
        if event.num == 4 or event.delta == 120:
            grid_conf['minsize'] += 1
        update_col(me,column,grid_conf,bg)
        send('UPDATE_INDIVIDUAL_GRID',(grid_conf['minsize'],me))

    def button3_event_col(me,column,bg,function=update_col,grid_top=shop_grid_top):
        xpos = me.winfo_rootx()
        ypos = me.winfo_rooty() - 130
        grid_conf=me.master.grid_multi_conf_cols[column][1]
        grid_top(xpos,ypos,me,bg,column,grid_conf,function,'Column')
        #me.myRoot().wait_window(grid_top(xpos,ypos,me,bg,column,grid_conf,function))
 
    def button3_event_row(me,row,bg,function=update_row,grid_top=shop_grid_top):
        xpos = me.winfo_rootx() - 100
        ypos = me.winfo_rooty()
        grid_conf=me.master.grid_multi_conf_rows[row][1]
        grid_top(xpos,ypos,me,bg,row,grid_conf,function,'Row')

    def button1_grid_help(me):
        messagebox.showinfo("Individual Grid","By MouseWheel you change the 'size'.\nBy Button-3 (right mouse button) you may also change 'pad' and 'weight'.",parent=me.myRoot())

    def show_grid(event=None,rows_widget=widget('EntryRows'),cols_widget=widget('EntryCols'),individual=widget('Individual'),set_col_width=set_col_width,set_row_height=set_row_height):

        try:
            cols = int(cols_widget.get())
            rows = int(rows_widget.get())
        except ValueError: return

        # delete old configuration ================

        deleteWidgetsForName(container(),NONAME)

        row_conf = container().grid_conf_rows
        col_conf = container().grid_conf_cols
        
        old_rows = row_conf[0]
        old_cols = col_conf[0]
            
        unconf_rows = old_rows
        unconf_cols = old_cols
        
        if container().grid_conf_individual_done:
            unconf_rows += 1
            unconf_cols += 1
        
        for i in range(unconf_rows):
            container().grid_rowconfigure(i,minsize = 0,pad=0,weight=0)

        for i in range(unconf_cols):
            container().grid_columnconfigure(i,minsize = 0,pad=0,weight=0)

        # decide about new configuration ================

        update_cols()
        update_rows()

        if cols <= old_cols:
            container().grid_multi_conf_cols = container().grid_multi_conf_cols[:cols]
        else:
            for i in range(cols-old_cols): container().grid_multi_conf_cols.append([False,None])
 
        if rows <= old_rows:
            container().grid_multi_conf_rows = container().grid_multi_conf_rows[:rows]
        else:
            for i in range(rows-old_rows): container().grid_multi_conf_rows.append([False,None])

        # fill cells - or not ============================

        selection_before = Selection()
        fill_cell = {'height': '0', 'width': '0','relief': 'solid','bd':'1','bg':'#b3d9d9','padx':0,'pady':0}

        individ = container().grid_conf_individual_wish

        for row in range(rows):
            for col in range(cols):
                Frame(NONAME,**fill_cell).rcgrid(row,col,sticky='news')
                this().lower()

            if individ:
                Frame(NONAME,relief='raised',cursor='sizing',bd=1).rcgrid(row,cols,sticky='news')
                do_event("<MouseWheel>", mouse_wheel_row,(row,this()['bg']),True,True)
                do_event("<Button-4>", mouse_wheel_row,(row,this()['bg']),True,True)
                do_event("<Button-5>", mouse_wheel_row,(row,this()['bg']),True,True)
                do_event("<Button-3>", button3_event_row,(row,this()['bg']),True)
                do_event("<Button-1>", button1_grid_help,wishWidget=True)
                if container().grid_multi_conf_rows[row][0]:
                        this()['bg'] = 'orange'

        if individ:
            for col in range(cols):
                Frame(NONAME,relief='raised',bd=1,cursor='sizing').rcgrid(rows,col,sticky='news')
                do_event("<MouseWheel>", mouse_wheel_col,(col,this()['bg']),True,True)
                do_event("<Button-4>", mouse_wheel_col,(col,this()['bg']),True,True)
                do_event("<Button-5>", mouse_wheel_col,(col,this()['bg']),True,True)
                do_event("<Button-3>", button3_event_col,(col,this()['bg']),True)
                do_event("<Button-1>", button1_grid_help,wishWidget=True)
                if container().grid_multi_conf_cols[col][0]:
                    this()['bg'] = 'orange'

        if individ:
            container().grid_columnconfigure(cols,minsize = 15,pad=0,weight=0)
            container().grid_rowconfigure(rows,minsize = 15,pad=0,weight=0)
            container().grid_conf_individual_done = True

        setSelection(selection_before)

        set_col_width()
        set_row_height()

        send("BASE_LAYOUT_REFRESH",this())
        
    widget('ButtonShow')['command'] = show_grid
    widget('EntryRows').bind('<Return>',show_grid)
    widget('EntryCols').bind('<Return>',show_grid)



    def mouse_move(me,wi_row=widget('Row'),wi_col=widget('Col')):
        if me.mydata[6]:
            step = 10
            diffx = me.winfo_pointerx() - me.winfo_rootx()
            diffy = me.winfo_pointery() - me.winfo_rooty()
            me.mydata[3] += diffx-me.mydata[0]
            me.mydata[4] += diffy-me.mydata[1]
            me.yxplace(me.mydata[4],me.mydata[3])
            me.mydata[5] += step
            if me.mydata[5] >= 100:
                me.mydata[5] = 0
                #send('POSITION_CHANGED',me)
                #send('LAYOUT_VALUES_REFRESH',me)
            me.mydata[5] += step
            me.after(step,mouse_move,me)

    def after_mouse_up(me):
        if me.mydata[7]:
            me.mydata[7] = False
            send('SHOW_LAYOUT',(None,True))
            send('SHOW_CONFIG',(None,True))
            send('SELECTION_CHANGED')
        else:
            send('POSITION_CHANGED',me)
            send('LAYOUT_VALUES_REFRESH',me)


    def on_mouse_up(me):
        if me.mydata[6]:
            me.mydata[6] = False # stop timer
            (col,row) = me.container().grid_location(me.winfo_rootx()-me.container().winfo_rootx(),me.winfo_rooty()-me.container().winfo_rooty())
            if col < 0: col = 0
            if row < 0: row = 0
            me.rcgrid(row,col)
            me.after(50,after_mouse_up,me)

    apprelease_id_list = [None]


    def on_app_mouse_up(me,app_id=apprelease_id_list):
        _Application.unbind('<ButtonRelease-1>',app_id[0])
        if me.mydata[6]: on_mouse_up(me)

    def on_mouse_down(me,event,me_root=container().myRoot(),app_id=apprelease_id_list):

        xpos = me.winfo_rootx()-me.container().winfo_rootx()
        ypos = me.winfo_rooty()-me.container().winfo_rooty()
        me.mydata = [event.x,event.y,'mouse',xpos,ypos,0,True,False]
        me.yxplace(ypos,xpos)
        app_id[0] =_Application.bind('<ButtonRelease-1>',lambda event=event, wi = me, func=on_app_mouse_up: func(wi))
        mouse_move(me)

        if this() != me:
            setWidgetSelection(me)
            me.mydata[7] = True
            send('SHOW_LAYOUT',(None,False))
            send('SHOW_CONFIG',(None,False))
            send('SELECTION_CHANGED')

    def do_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        me.mydata=([0,0,'mouse',0,0,0,True,False])
        me.do_event('<Button-1>',mouse_down,wishWidget=True,wishEvent=True)
        me.do_event('<ButtonRelease-1>',mouse_up,me)

    def grid_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        if type(me.mydata) != list or me.mydata[2]!= 'mouse':
            me.mydata=([0,0,'mouse',0,0,0,True,False])
            me.do_event('<Button-1>',mouse_down,wishWidget=True,wishEvent=True)
            me.do_event('<ButtonRelease-1>',mouse_up,me)

    do_receive('GRID_MOUSE_ON',grid_mouse_on,wishMessage=True)

    def do_grid(do_mouse_on=do_mouse_on):

        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        layout_before = this().Layout

        if this().Layout == NOLAYOUT: rcgrid(0,0)
        elif this().Layout == PLACELAYOUT:
            
            (col,row) = container().grid_location(this().winfo_rootx()-container().winfo_rootx(),this().winfo_rooty()-container().winfo_rooty())
            if col < 0: col = 0
            if row < 0: row = 0
            rcgrid(row,col)

        if container().is_mouse_select_on: do_mouse_on(this())
        else: send("SWITCH_MOUSE_ON")

        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions


    widget('ButtonGrid').do_command(do_grid)


    def do_grid0():
        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        layout_before = this().Layout
        grid()
        if container().is_mouse_select_on: do_mouse_on(this())
        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

    widget('Grid()').do_command(do_grid0)


    def update_grid_table_on_enter(
Rows=widget('EntryRows'),
Height=widget('EntryRowHeight'),
RowPad=widget('EntryRowPad'),
RowWeight=widget('EntryRowWeight'),
Cols=widget('EntryCols'),
Width=widget('EntryColWidth'),
ColPad=widget('EntryColPad'),
ColWeight=widget('EntryColWeight'),
set_row_height=set_row_height,
set_col_width=set_col_width,
individual = widget('Individual')):


        if this().Layout != LAYOUTNEVER:
            
            if not (container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT or isinstance(this(),Menu) or isinstance(container(),PanedWindow)):

                    not_initialized = container().grid_conf_rows == None
                    if not_initialized:
                        container().grid_conf_rows = (0,25,0,0)
                        container().grid_conf_cols = (0,75,0,0)
                    
                    Rows.delete(0,'end')
                    Rows.insert(0,container().grid_conf_rows[0])
                    Height.delete(0,'end')
                    Height.insert(0,container().grid_conf_rows[1])
                    RowPad.delete(0,'end')
                    RowPad.insert(0,container().grid_conf_rows[2])
                    RowWeight.delete(0,'end')
                    RowWeight.insert(0,container().grid_conf_rows[3])

                    Cols.delete(0,'end')
                    Cols.insert(0,container().grid_conf_cols[0])
                    Width.delete(0,'end')
                    Width.insert(0,container().grid_conf_cols[1])
                    ColPad.delete(0,'end')
                    ColPad.insert(0,container().grid_conf_cols[2])
                    ColWeight.delete(0,'end')
                    ColWeight.insert(0,container().grid_conf_cols[3])
                    
                    if container().grid_conf_individual_wish: individual.select()
                    else: individual.deselect()

                    update_individual(container())

                    #set_row_height()
                    #set_col_width()

    do_receive("SELECTION_CHANGED",update_grid_table_on_enter)


main()


### ========================================================
