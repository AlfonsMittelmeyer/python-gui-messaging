Entry('EntryRows',**{'width': '6'}).grid(**{'column': '1', 'row': '1'})
Entry('EntryCols',**{'width': '6'}).grid(**{'column': '2', 'row': '1'})
Spinbox('EntryRowHeight',**{'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '1', 'row': '2'})
Spinbox('EntryColWidth',**{'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '2', 'row': '2'})
Spinbox('EntryRowPad',**{'from': '0.0', 'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '1', 'row': '3'})
Spinbox('EntryColPad',**{'from': '0.0', 'width': '4', 'to': '1000.0', 'cursor': ''}).grid(**{'column': '2', 'row': '3'})
Spinbox('EntryRowWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '1', 'row': '4'})
Spinbox('EntryColWeight',**{'width': '4', 'to': '1000.0'}).grid(**{'column': '2', 'row': '4'})
Button('ButtonShow',**{'text': 'Show', 'bd': '3', 'bg': 'green'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '5'})

Button('ButtonHide',**{'text': 'Hide', 'bd': '3', 'bg': 'green'}).grid(**{'column': '3', 'sticky': 'nesw', 'row': '4'})
Button('Grid()',**{'text': 'Grid()', 'bd': '3', 'bg': 'green'}).grid(**{'row': '5'})
Label('lwidth',**{'text': 'Min Width'}).grid(**{'column': '3', 'sticky': 'w', 'row': '2'})
Label('lweight',**{'text': 'weight'}).grid(**{'sticky': 'e', 'row': '4'})
Label('lrows',**{'text': 'Rows', 'font': 'TkDefaultFont 9 bold'}).grid(**{'column': '1', 'sticky': 'nesw', 'row': '0'})
Button('ButtonGrid',**{'text': 'GRID', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'bg': 'green'}).grid(**{'column': '3', 'sticky': 'nesw', 'row': '5'})
Label('lcols',**{'text': 'Columns', 'font': 'TkDefaultFont 9 bold'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '0'})
Label('lpad',**{'text': 'pad'}).grid(**{'sticky': 'e', 'row': '3'})
Label('lheight',**{'text': 'Min Height'}).grid(**{'sticky': 'e', 'row': '2'})
Button('ButtonShow',**{'text': 'Show', 'bd': '3', 'bg': 'green'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '5'})
Label('LableTitle',**{'text': 'grid', 'font': 'TkDefaultFont 9 bold', 'bd': '3','fg': 'blue', 'relief': 'ridge'}).grid(**{'sticky': 'nesw', 'row': '0'})

### CODE ===================================================

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
        send("BASE_LAYOUT_REFRESH",this())

    widget('ButtonHide').do_command(hide_grid)

    def do_grid_forget():
        layout_before = this().Layout
        this().grid_forget()
        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

    #widget('ButtonForget').do_command(do_grid_forget)

    def set_row_height(rows_widget=widget('EntryRows'),height_widget=widget('EntryRowHeight'),pad_widget = widget('EntryRowPad'),weight_widget=widget('EntryRowWeight')):

        try:
            rows = int(rows_widget.get())
        except ValueError: 
            rows_widget.delete(0,'end')
            rows_widget.insert(0,10)
            rows = 10

        row_height = height_widget.get()
        padvalue = pad_widget.get()
        weightvalue = weight_widget.get()

        container().grid_conf_rows = (rows,row_height,padvalue,weightvalue)

        for row in range(rows):
            container().grid_rowconfigure(row,minsize =row_height,pad=padvalue,weight=weightvalue)

    widget('EntryRowHeight').do_command(set_row_height)
    widget('EntryRowHeight').do_event('<Return>',set_row_height)
    widget('EntryRowWeight').do_command(set_row_height)
    widget('EntryRowWeight').do_event('<Return>',set_row_height)
    widget('EntryRowPad').do_command(set_row_height)
    widget('EntryRowPad').do_event('<Return>',set_row_height)

    def set_col_width(cols_widget=widget('EntryCols'),width_widget=widget('EntryColWidth'),pad_widget = widget('EntryColPad'),weight_widget=widget('EntryColWeight')):

        try:
            cols = int(cols_widget.get())
        except ValueError: 
            cols_widget.delete(0,'end')
            cols_widget.insert(0,10)
            cols = 6

        col_width = width_widget.get()
        padvalue = pad_widget.get()
        weightvalue = weight_widget.get()
        
        container().grid_conf_cols = (cols,col_width,padvalue,weightvalue)
        
        for col in range(cols):
            container().grid_columnconfigure(col,minsize = col_width,pad=padvalue,weight=weightvalue)


    widget('EntryColWidth').do_command(set_col_width)
    widget('EntryColWidth').do_event('<Return>',set_col_width)
    widget('EntryColPad').do_command(set_col_width)
    widget('EntryColPad').do_event('<Return>',set_col_width)
    widget('EntryColWeight').do_command(set_col_width)
    widget('EntryColWeight').do_event('<Return>',set_col_width)

    def show_grid(rows_widget=widget('EntryRows'),cols_widget=widget('EntryCols'),set_col_width=set_col_width,set_row_height=set_row_height):

        try:
            cols = int(cols_widget.get())
            rows = int(rows_widget.get())
        except ValueError: return

        deleteWidgetsForName(container(),NONAME)

        row_conf = container().grid_conf_rows
        col_conf = container().grid_conf_cols
        
        for i in range(row_conf[0]):
            container().grid_rowconfigure(i,minsize = 0,pad=0,weight=0)

        for i in range(col_conf[0]):
            container().grid_columnconfigure(i,minsize = 0,pad=0,weight=0)

        selection_before = Selection()
        for row in range(rows):
            fill_cell = {'height': '0', 'width': '0', 'relief': 'solid','bg':'#b3d9d9','padx':0,'pady':0}
            for col in range(cols):
                Label(NONAME,**fill_cell).rcgrid(row,col,sticky='news')
                this().lower()
        setSelection(selection_before)

        set_col_width()
        set_row_height()

        send("BASE_LAYOUT_REFRESH",this())
        
    widget('ButtonShow').do_command(show_grid)
    widget('EntryRows').do_event('<Return>',show_grid)
    widget('EntryCols').do_event('<Return>',show_grid)



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


    def on_mouse_up(me,event):
        me.mydata[6] = False # stop timer
        (col,row) = me.container().grid_location(me.winfo_rootx()-me.container().winfo_rootx(),me.winfo_rooty()-me.container().winfo_rooty())
        if col < 0: col = 0
        if row < 0: row = 0
        me.rcgrid(row,col)
        send('BASE_LAYOUT_CHANGED',PLACELAYOUT) # depending on the layout change we need less or more actions
        send('POSITION_CHANGED',me)
        send('LAYOUT_VALUES_REFRESH',me)

    def on_mouse_down(me,event,me_root=container().myRoot()):

        #me_root.iconify()
        xpos = me.winfo_rootx()-me.container().winfo_rootx()
        ypos = me.winfo_rooty()-me.container().winfo_rooty()
        me.mydata = [event.x,event.y,'mouse',xpos,ypos,0,True]
        me.yxplace(ypos,xpos)
        mouse_move(me)

        if this() != me:
            setWidgetSelection(me)
            send('SELECTION_CHANGED')

    def do_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        me.mydata=(None,None,'mouse')
        me.do_event('<Button-1>',mouse_down,wishWidget=True,wishEvent=True)
        me.do_event('<ButtonRelease-1>',mouse_up,wishWidget=True,wishEvent=True)

    do_receive('GRID_MOUSE_ON',do_mouse_on,wishMessage=True)

    def do_grid(do_mouse_on=do_mouse_on):

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
    set_row_height=set_row_height
    ,set_col_width=set_col_width):


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

        set_row_height()
        set_col_width()

    do_receive("SELECTION_CHANGED",update_grid_table_on_enter)


main()


### ========================================================
