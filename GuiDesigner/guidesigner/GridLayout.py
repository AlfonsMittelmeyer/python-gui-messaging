config(**{'grid_rows': '(9, 20, 0, 0)', 'grid_multi_cols': '[7, (2, 0, 0, 0), (6, 0, 0, 1)]', 'grid_cols': '(7, 0, 0, 0)', 'grid_multi_rows': '[9, (0, 31, 2, 0), (5, 0, 0, 0), (6, 0, 0, 0), (8, 4, 0, 0)]'})

Button('ButtonGrid',**{'text': 'GRID', 'bd': '3', 'font': 'TkDefaultFont 9 bold', 'pady': '1', 'padx': '1', 'bg': 'lightgreen'}).grid(column=1, row=0, columnspan=2, sticky='nesw')
Button('Grid()',**{'text': 'Grid()', 'bd': '3', 'pady': '1', 'padx': '1', 'bg': 'lightgreen'}).grid(column=3, row=0, sticky='nesw')
ttk.Separator('separator').grid(row=5, columnspan=5, sticky='ew')
Entry('uniform_row',**{'width': 0}).grid(row=7, columnspan=2, sticky='nesw')
Entry('uniform_col',**{'width': 0}).grid(column=3, row=7, columnspan=2, sticky='nesw')
ttk.Label('luniformrow',**{'text': 'uniform (row)'}).grid(row=6, columnspan=2, sticky='w')
Label('luniformcol',**{'text': 'uniform (column)'}).grid(column=3, row=6, columnspan=2, sticky='w')
ttk.Separator('separator',**{'orient': 'vertical'}).grid(rowspan=8, column=2, row=1, sticky='ns')
Label('lpad',**{'text': 'pad'}).grid(row=2, sticky='e')
Label('lweight',**{'text': 'weight'}).grid(row=3, sticky='e')
Label('lheight',**{'text': 'minsize'}).grid(row=1, sticky='e')
Label('lrows',**{'text': 'Rows', 'font': 'TkDefaultFont 9 bold'}).grid(row=4, sticky='nesw')
Entry('EntryRows',**{'width': 6, 'bg': '#ffffd4'}).grid(column=1, row=4, sticky='nesw')
Entry('EntryCols',**{'width': 5, 'bg': '#ffffd4'}).grid(column=3, row=4, sticky='nesw')
Label('lcols',**{'text': 'Columns', 'font': 'TkDefaultFont 9 bold'}).grid(column=4, row=4, sticky='nesw')
Button('special',**{'text': 'special', 'bd': 2, 'photoimage': 'guidesigner/images/insert_table_row.gif'}).grid(rowspan=2, column=4, row=2)
Label('LableTitle',**{'text': 'grid', 'bd': '3', 'font': 'TkDefaultFont 9 bold', 'relief': 'ridge', 'fg': 'blue'}).grid(row=0, sticky='nesw')
Spinbox('EntryRowHeight',**{'width': 4, 'to': 1000.0}).grid(column=1, row=1, sticky='nesw')
Spinbox('EntryColWidth',**{'width': 4, 'to': 1000.0}).grid(column=3, row=1, sticky='nesw')
Spinbox('EntryRowPad',**{'width': 4, 'to': 1000.0}).grid(column=1, row=2, sticky='nesw')
Spinbox('EntryColPad',**{'width': 4, 'to': 1000.0}).grid(column=3, row=2, sticky='nesw')
Spinbox('EntryRowWeight',**{'width': 4, 'to': 1000.0}).grid(column=1, row=3, sticky='nesw')
Spinbox('EntryColWeight',**{'width': 4, 'to': 1000.0}).grid(column=3, row=3, sticky='nesw')
Checkbutton('Individual',**{'highlightthickness': '2', 'text': 'indiv.'}).grid(column=4, row=1, sticky='ew')
Label('ButtonShow',**{'text': 'Show', 'bd': '3', 'relief': 'raised', 'bg': 'lightgreen'}).grid(column=4, row=0, sticky='nesw')
ttk.Separator('separator',**{'orient': 'vertical'}).grid(rowspan=9, column=5, row=0, sticky='nsw')
#Button('help_button',**{'text': 'help_button', 'bd': '2', 'pady': '0', 'photoimage': 'guidesigner/images/help32.gif', 'padx': '0','highlightthickness' : 0}).grid(rowspan=4, padx=6, column=5, row=0, sticky='n')

### CODE ===================================================
IndividualVar =  IntVar()
widget('Individual').config(variable = IndividualVar, onvalue = 1, offvalue = 0)
widget('Individual').mydata=IndividualVar

# -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------


def main():

    container().help_image = StatTkInter.PhotoImage(file = 'guidesigner/images/help16.gif')

    def show_help():
        messagebox.showinfo("Move, Delete and Insert Lines and Columns","You may move the lines by mouse. After mouse button click, when the line becomes blue, you may insert and delete rows or columns by pressing the [Insert] or [Delete] key.",parent=container())
        '''
        try:
            webbrowser.open('https://github.com/AlfonsMittelmeyer/python-gui-messaging/wiki')
        except: pass
        '''

    #widget('help_button')['command'] = show_help

    MIN_HEIGHT = 40
    MIN_WIDTH = 40
    orange = '#ffe096'

    indiv_hilibg = [widget('Individual')['highlightbackground']]
    
    fill_cell = {'height': '0', 'width': '0','relief': 'solid','bd':'1','bg':'#b3d9d9','padx':0,'pady':0}
    fill_cell2 = {'height': '0', 'width': '0','relief': 'flat','bd':'0','bg':'#b3d9d9','padx':0,'pady':0}



    def update_rows_data(size,pad,weight,Width=widget('EntryRowHeight'),ColPad=widget('EntryRowPad'),ColWeight=widget('EntryRowWeight')):
        Width.delete(0,'end')
        Width.insert(0,size)
        ColPad.delete(0,'end')
        ColPad.insert(0,pad)
        ColWeight.delete(0,'end')
        ColWeight.insert(0,weight)

    def update_general_rows():
        update_rows_data(container().grid_conf_rows[1],container().grid_conf_rows[2],container().grid_conf_rows[3])

    def update_cols_data(size,pad,weight,Width=widget('EntryColWidth'),ColPad=widget('EntryColPad'),ColWeight=widget('EntryColWeight')):
        Width.delete(0,'end')
        Width.insert(0,size)
        ColPad.delete(0,'end')
        ColPad.insert(0,pad)
        ColWeight.delete(0,'end')
        ColWeight.insert(0,weight)

    def update_general_cols():
        update_cols_data(container().grid_conf_cols[1],container().grid_conf_cols[2],container().grid_conf_cols[3])

    def update_general_grid(
Rows=widget('EntryRows'),
Cols=widget('EntryCols'),
#set_row_height=set_row_height,
#set_col_width=set_col_width,
#individual = widget('Individual'),
):

        Rows.delete(0,'end')
        Rows.insert(0,container().grid_conf_rows[0])
        update_general_rows()
        
        Cols.delete(0,'end')
        Cols.insert(0,container().grid_conf_cols[0])
        update_general_cols()



    def update_uni_row(me=widget('uniform_row')):
        uniform = me.get().strip()
        if uniform:
            if container().grid_multi_conf_rows:
                for conf in container().grid_multi_conf_rows:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        update_rows_data(conf[1]['minsize'],conf[1]['pad'],conf[1]['weight'])
                        break
        else:
            if container().grid_conf_rows and container().grid_conf_rows[0]:
                update_general_rows()

        container().grid_uni_row = uniform 
        send('CANVAS_UPDATE_ROW') # update für canvasse

    def update_uni_col(me=widget('uniform_col')):
        uniform = me.get().strip()
        if uniform:
            if container().grid_multi_conf_cols:
                for conf in container().grid_multi_conf_cols:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        update_cols_data(conf[1]['minsize'],conf[1]['pad'],conf[1]['weight'])
                        break
        else:
            if container().grid_conf_cols and container().grid_conf_cols[0]:
                update_general_cols()

        container().grid_uni_col = uniform
        send('CANVAS_UPDATE_COL') # update für canvasse
        

    widget('uniform_col').do_event('<Key>',container().after,[1,update_uni_col])
    widget('uniform_row').do_event('<Key>',container().after,[1,update_uni_row])

    #Button('ButtonForget',**{'text': 'Forget'}).grid(**{'column': '1', 'sticky': 'nesw', 'row': '5'})

    # -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------

    # set the bg color of the GridTitle label to yellow, if the current widget has a GRIDLAYOUT, otherwise to original color

    def do_bg_title(title = widget('LableTitle'),titlebg = widget('LableTitle')["bg"]):
        if this().Layout == GRIDLAYOUT: title['bg'] = "yellow"
        else: title['bg'] = titlebg

    do_receive('BASE_LAYOUT_REFRESH',do_bg_title)


    def grid_cols_changed(EntryCols = widget('EntryCols')):
        EntryCols['state'] = 'normal'
        EntryCols.delete(0,'end')
        EntryCols.insert(0,str(container().grid_conf_cols[0]))
        EntryCols['state'] = 'disabled'

    do_receive('GRID_COLS_CHANGED',grid_cols_changed)


    def grid_rows_changed(EntryRows = widget('EntryRows')):
        EntryRows['state'] = 'normal'
        EntryRows.delete(0,'end')
        EntryRows.insert(0,str(container().grid_conf_rows[0]))
        EntryRows['state'] = 'disabled'

    do_receive('GRID_ROWS_CHANGED',grid_rows_changed)

    def hide_grid():
        deleteWidgetsForName(container(),NONAME)
        deleteWidgetsForName(container(),NONAMECANVAS)
        deleteWidgetsForName(container(),NONAME2)
        if container().grid_conf_individual_done:
            cols = container().grid_conf_cols[0]
            rows = container().grid_conf_rows[0]
            container().grid_columnconfigure(cols,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_columnconfigure(cols+1,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_columnconfigure(cols+2,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_rowconfigure(rows,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_rowconfigure(rows+1,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_rowconfigure(rows+2,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_conf_individual_done = False
        
        send("BASE_LAYOUT_REFRESH",this())


    def do_grid_forget():
        layout_before = this().Layout
        this().grid_forget()
        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

    #widget('ButtonForget').do_command(do_grid_forget)

    def update_rows(rows_widget=widget('EntryRows'),height_widget=widget('EntryRowHeight'),pad_widget = widget('EntryRowPad'),weight_widget=widget('EntryRowWeight'),uniform_row = widget('uniform_row')):

        is_uniform = False

        try:
            rows = int(rows_widget.get())
        except ValueError: 
            rows_widget.delete(0,'end')
            rows_widget.insert(0,10)
            rows = 10

        try:
            row_height = int(height_widget.get())
            padvalue = int(pad_widget.get())
            weightvalue = int(weight_widget.get())

            if not container().grid_conf_rows or not container().grid_conf_rows[0] or not container().grid_uni_row:
                container().grid_conf_rows = (rows,row_height,padvalue,weightvalue)
            else:
                container().grid_conf_rows = tuple([rows] + list(container().grid_conf_rows[1:]))
                is_uniform = True

            return is_uniform, row_height, padvalue, weightvalue

        except ValueError:
            return False,0,0,0


    def set_row_height():

        rows = container().grid_conf_rows[0]
        to_insert =  {'minsize':container().grid_conf_rows[1],'pad':container().grid_conf_rows[2],'weight':container().grid_conf_rows[3],'uniform' : ''}
        
        for row in range(rows):
            if container().grid_multi_conf_rows[row][0] == False: container().grid_multi_conf_rows[row][1] = dict(to_insert)
 
        for row in range(rows):
            container().grid_rowconfigure(row,**(container().grid_multi_conf_rows[row][1]))
            config = container().grid_multi_conf_rows[row][1]
            send('ROW_WEIGHT',(row,config['weight']))
            send('TOP_UPDATE_ROW',(row,config))


    def update_row_values_uniform(size,pad,weight,uniform):
        rows = container().grid_conf_rows[0]
        for row in range(rows):
            if container().grid_multi_conf_rows[row][0]:
                conf = container().grid_multi_conf_rows[row][1]
                if 'uniform' in conf and conf['uniform'] and conf['uniform'] == uniform:
                    conf.update({ 'minsize' : size, 'pad' : pad, 'weight':weight})
        set_row_height()



    def update_row_values():
        is_uniform, size, pad, weight = update_rows()
        if is_uniform:
            update_row_values_uniform(size,pad,weight,container().grid_uni_row)
       
        else:
            set_row_height()


    def update_row_values():

        is_uniform, size, pad, weight = update_rows()

        if is_uniform:
            rows = container().grid_conf_rows[0]
            for row in range(rows):
                if container().grid_multi_conf_rows[row][0]:
                    conf = container().grid_multi_conf_rows[row][1]
                    if 'uniform' in conf and conf['uniform'] and conf['uniform'] == container().grid_uni_row:
                        conf.update({ 'minsize' : size, 'pad' : pad, 'weight':weight})
        
        set_row_height()


    def check_row_values(rows_widget=widget('EntryRows')):
        try:
            rows = int(rows_widget.get())
        except ValueError: 
            rows_widget.delete(0,'end')
            rows_widget.insert(0,10)
            rows = 10

        if container().grid_conf_rows and container().grid_conf_rows[0] == rows:
            update_row_values()
        else:
            show_grid()


    widget('EntryRowHeight').do_command(check_row_values)
    widget('EntryRowHeight').do_event('<Return>',check_row_values)
    widget('EntryRowWeight').do_command(check_row_values)
    widget('EntryRowWeight').do_event('<Return>',check_row_values)
    widget('EntryRowPad').do_command(check_row_values)
    widget('EntryRowPad').do_event('<Return>',check_row_values)


    def update_cols(
        cols_widget=widget('EntryCols'),
        width_widget=widget('EntryColWidth'),
        pad_widget = widget('EntryColPad'),
        weight_widget=widget('EntryColWeight'),
        ):

        is_uniform = False
        
        try:
            cols = int(cols_widget.get())
        except ValueError: 
            cols_widget.delete(0,'end')
            cols_widget.insert(0,10)
            cols = 6

        try:
            col_width = int(width_widget.get())
            padvalue = int(pad_widget.get())
            weightvalue = int(weight_widget.get())


            if not container().grid_conf_cols or not container().grid_conf_cols[0] or not container().grid_uni_col:
                container().grid_conf_cols = (cols,col_width,padvalue,weightvalue)
            else:
                container().grid_conf_cols = tuple([cols] + list(container().grid_conf_cols[1:]))
                is_uniform = True

            return is_uniform, col_width, padvalue, weightvalue

        except ValueError:
            return False, 0,0,0


    def set_col_width():

        cols = container().grid_conf_cols[0]
        to_insert =  {'minsize':container().grid_conf_cols[1],'pad':container().grid_conf_cols[2],'weight':container().grid_conf_cols[3],'uniform' : ''}
        
        for col in range(cols):
            if container().grid_multi_conf_cols[col][0] == False: container().grid_multi_conf_cols[col][1] = dict(to_insert)
 
        for col in range(cols):
            container().grid_columnconfigure(col,**(container().grid_multi_conf_cols[col][1]))
            config = container().grid_multi_conf_cols[col][1]
            send('COL_WEIGHT',(col,config['weight']))
            send('TOP_UPDATE_COL',(col,config))



    def update_col_values_uniform(size,pad,weight,uniform):
        cols = container().grid_conf_cols[0]
        for col in range(cols):
            if container().grid_multi_conf_cols[col][0]:
                conf = container().grid_multi_conf_cols[col][1]
                if 'uniform' in conf and conf['uniform'] and conf['uniform'] == uniform:
                    conf.update({ 'minsize' : size, 'pad' : pad, 'weight':weight})
        set_col_width()

    def update_col_values():
        is_uniform, size, pad, weight = update_cols()
        if is_uniform:
            update_col_values_uniform(size,pad,weight,container().grid_uni_col)
       
        else:
            set_col_width()

    def check_col_values(cols_widget=widget('EntryCols')):
        try:
            cols = int(cols_widget.get())
        except ValueError: 
            cols_widget.delete(0,'end')
            cols_widget.insert(0,10)
            cols = 10

        if container().grid_conf_cols and container().grid_conf_cols[0] == cols:
            update_col_values()
        else:
            show_grid()

    widget('EntryColWidth').do_command(check_col_values)
    widget('EntryColWidth').do_event('<Return>',check_col_values)
    widget('EntryColPad').do_command(check_col_values)
    widget('EntryColPad').do_event('<Return>',check_col_values)
    widget('EntryColWeight').do_command(check_col_values)
    widget('EntryColWeight').do_event('<Return>',check_col_values)


    def shop_grid_top(x,y,indivmark,bg,index,grid_conf,item_text,is_row):

        selection_before = Selection()
        
        setWidgetSelection(indivmark) # the Canvas should be the tkinter parent of the Toplevel Window
        goIn()

        Toplevel('GridTop',title=' ',geometry='+'+str(x)+'+'+str(y))
        config(**{'grid_multi_rows': '[6, (5, 4, 0, 0)]', 'grid_cols': '(6, 0, 0, 0)', 'grid_rows': '(6, 0, 0, 0)', 'grid_multi_cols': '[6, (0, 4, 0, 0), (2, 4, 0, 0), (5, 4, 0, 0)]'})


        Label('lRowCol',**{'font': 'TkDefaultFont 9 bold'}).grid(column=1, sticky='e', row=0)
        Label('showRowCol',**{'font': 'TkDefaultFont 9 bold', 'relief': 'solid', 'width': 4, 'fg' : 'blue', 'bg': '#ffffd4'}).grid(pady=5, column=3, sticky='w', ipadx=5, row=0)

        Label('lsize',**{'text': 'size'}).grid(column=1, sticky='e', row=1)
        Spinbox('EntrySize',**{'to': 1000.0, 'width': 4}).grid(column=3, sticky='nsw', row=1)

        Label('lpad',**{'text': 'pad'}).grid(column=1, sticky='e', row=2)
        Spinbox('EntryPad',**{'to': 1000.0, 'width': 4}).grid(column=3, sticky='nsw', row=2)

        Label('lweight',**{'text': 'weight'}).grid(column=1, sticky='e', row=3)
        Spinbox('EntryWeight',**{'to': 1000.0, 'width': 4}).grid(column=3, sticky='nsw', row=3)

        Label('luniform',**{'text': 'uniform'}).grid(column=1, row=4)
        Entry('uniform',**{'width': 12}).grid(column=3, sticky='nesw', columnspan=2, row=4)

        Button('OK',**{'text': 'OK', 'pady': '1'}).grid(column=4, sticky='e', row=3)


        widget('lRowCol')['text'] = item_text
        widget('showRowCol')['text'] = str(index)
        widget('EntrySize').delete(0,'end')
        widget('EntrySize').insert(0,grid_conf['minsize'])
        widget('EntryPad').delete(0,'end')
        widget('EntryPad').insert(0,grid_conf['pad'])
        widget('EntryWeight').delete(0,'end')
        widget('EntryWeight').insert(0,grid_conf['weight'])
        widget('uniform').delete(0,'end')
        uniform = grid_conf['uniform']
        uniform = str(uniform) if uniform else ''
        widget('uniform').insert(0,uniform)
        
        top_window=container()

        #def container_destroyed(msg):
        #    if msg == indivmark: top_window.destroy()
            
        #do_receive('CONTAINER_DESTROYED',container_destroyed,wishMessage = True)

        def top_grid_show(msg,showRowCol = widget('showRowCol'),EntrySize = widget('EntrySize'),EntryPad=widget('EntryPad'),EntryWeight=widget('EntryWeight'),UniForm = widget('uniform')):
            if msg[0] != indivmark: return

            row_col = msg[1]
            config = msg[2]

            uniform = config['uniform']
            if not uniform:
                uniform = ''
          
            showRowCol['text'] = str(row_col)
            for entry in ((EntrySize,config['minsize']),(EntryPad,config['pad']),(EntryWeight,config['weight']),(UniForm,uniform)):
                entry[0].delete(0,'end')
                #print(entry[1])
                entry[0].insert(0,entry[1])
            
        do_receive('TOPGRIDSHOW',top_grid_show,wishMessage=True)

        def update_values(mark=indivmark,row_or_column=index,esize = widget('EntrySize'),epad = widget('EntryPad'), eweight = widget('EntryWeight'),euniform = widget('uniform')):

            try:
                minsize = int(esize.get())
            except ValueError:
                minsize = grid_conf['minsize']
                esize.delete(0,'end')
                esize.insert(0,minsize)

            try:
                pad = int(epad.get())
            except ValueError:
                pad = grid_conf['pad']
                epad.delete(0,'end')
                epad.insert(0,pad)
                
            try:
                weight = int(eweight.get())
            except ValueError:
                weight = grid_conf['weight']
                eweight.delete(0,'end')
                eweight.insert(0,weight)

            uniform = euniform.get().strip()
            send('ROW_CONFIG_CHANGED' if is_row else 'COL_CONFIG_CHANGED',(row_or_column,{'minsize': minsize,'pad':pad,'weight':weight,'uniform': uniform}))
            
        def update_and_close():
            update_values()
            top_window.destroy()
            
        widget('OK').do_command(update_and_close)


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
        widget('uniform').do_event('<Return>',update_values)
        
        top_window.transient(indivmark.myRoot())
        widget('EntrySize').focus_set()
        setSelection(selection_before)
        return top_window

    def update_individual(cont,wi=widget('Individual'),hili_bg = indiv_hilibg[0]):
        wi['highlightbackground'] = '#ff8000' if cont.grid_conf_individual_has else hili_bg
 
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

    def update_canvascolor_row(me,row,bg):
        conf =  container().grid_multi_conf_rows[row][1]
        if container().grid_uni_row:
            me['bg'] = orange if 'uniform' in conf and conf['uniform'] and conf['uniform'] == container().grid_uni_row else bg
        else:
            me['bg'] = bg  if container().grid_multi_conf_rows[row][0] else orange
        me['highlightbackground'] = 'red' if container().grid_multi_conf_rows[row][0] and 'uniform' in conf and conf['uniform'] else bg


    def update_canvascolor_col(me,col,bg):
        conf =  container().grid_multi_conf_cols[col][1]

        if container().grid_uni_col:
            me['bg'] = orange if 'uniform' in conf and conf['uniform']  and conf['uniform'] == container().grid_uni_col else bg
        else:
            me['bg'] = bg  if container().grid_multi_conf_cols[col][0] else orange
        
        me['highlightbackground'] = 'red' if container().grid_multi_conf_cols[col][0] and 'uniform' in conf and conf['uniform'] else bg


    def update_col(me,column,grid_conf,bg):
        cont = me.master
        cont.grid_multi_conf_cols[column][1] = grid_conf
        cont.grid_columnconfigure(column,**grid_conf)

        if 'uniform' not in grid_conf or not grid_conf['uniform']:
            if grid_conf['minsize'] == cont.grid_conf_cols[1] and grid_conf['pad'] == cont.grid_conf_cols[2] and grid_conf['weight'] == cont.grid_conf_cols[3]:
                cont.grid_multi_conf_cols[column][0] = False
            else:
                cont.grid_multi_conf_cols[column][0] = True
            update_canvascolor_col(me,column,bg)            
            update_individual_mark(cont)

        elif container().grid_uni_col == grid_conf['uniform']:
                cont.grid_multi_conf_cols[column][0] = True
                update_cols_data(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])
                update_col_values()

        else:
            cont.grid_multi_conf_cols[column][0] = True
            update_col_values_uniform(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'],grid_conf['uniform'])                

        update_individual_mark(cont)
        update_canvascolor_col(me,column,bg)            
        send('COL_WEIGHT',(column,grid_conf['weight']))
        send('UPDATE_INDIVIDUAL_GRID',(grid_conf['minsize'],me))

    def update_row(me,row,grid_conf,bg):
        cont = me.master
        cont.grid_multi_conf_rows[row][1] = grid_conf
        cont.grid_rowconfigure(row,**grid_conf)
        if 'uniform' not in grid_conf or not grid_conf['uniform']:
            if grid_conf['minsize'] == cont.grid_conf_rows[1] and grid_conf['pad'] == cont.grid_conf_rows[2] and grid_conf['weight'] == cont.grid_conf_rows[3]:
                cont.grid_multi_conf_rows[row][0] = False
            else:
                cont.grid_multi_conf_rows[row][0] = True

        elif container().grid_uni_row == grid_conf['uniform']:
                cont.grid_multi_conf_rows[row][0] = True
                update_rows_data(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])
                update_row_values()
        else:
            cont.grid_multi_conf_rows[row][0] = True
            update_col_values_uniform(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'],grid_conf['uniform'])                

        update_individual_mark(cont)
        update_canvascolor_row(me,row,bg)            
        send('ROW_WEIGHT',(row,grid_conf['weight']))
        send('UPDATE_INDIVIDUAL_GRID',(grid_conf['minsize'],me))

    def mouse_wheel_row(me,event,row,bg):
        grid_conf=me.master.grid_multi_conf_rows[row][1]
        if event.num == 5 or event.delta == -120:
            grid_conf['minsize'] -= 1
        if event.num == 4 or event.delta == 120:
            grid_conf['minsize'] += 1
        update_row(me,row,grid_conf,bg)

    def mouse_wheel_col(me,event,column,bg):
        grid_conf=me.master.grid_multi_conf_cols[column][1]
        if event.num == 5 or event.delta == -120:
            grid_conf['minsize'] -= 1
        if event.num == 4 or event.delta == 120:
            grid_conf['minsize'] += 1
        update_col(me,column,grid_conf,bg)

    def button3_event_col(me,column,bg,grid_top=shop_grid_top):
        xpos = me.winfo_rootx()
        ypos = me.winfo_rooty() - 130
        #grid_conf=me.master.grid_multi_conf_cols[column][1]
        grid_conf=me.master.grid_columnconfigure(column)
        grid_top(xpos,ypos,me,bg,column,grid_conf,'Column',False)
        #me.myRoot().wait_window(grid_top(xpos,ypos,me,bg,column,grid_conf,function))
 
    def button3_event_row(me,row,bg,grid_top=shop_grid_top):
        xpos = me.winfo_rootx() - 100
        ypos = me.winfo_rooty()
        #grid_conf=me.master.grid_multi_conf_rows[row][1]
        grid_conf=me.master.grid_rowconfigure(row)
        grid_top(xpos,ypos,me,bg,row,grid_conf,'Row',True)

    def button1_grid_help(me):
        messagebox.showinfo("Individual Grid","By MouseWheel you change the 'size'.\nBy Button-3 (right mouse button) you may also change 'pad' and 'weight'.",parent=me.myRoot())

    def update_canvas_col_line(me):
        coords = coords = (3,9,me.winfo_width()-3,9)
        me.coords('line',*coords)
        
    def update_canvas_row_line(me):
        coords = coords = (9,3,9,me.winfo_height()-3)
        me.coords('line',*coords)

    def update_canvas_row_line_arrow(msg,me,row):
        if msg[0] == row:
            me.itemconfig('line', arrowshape = '8 8 5' if msg[1] else '8 0 5')

    def update_canvas_col_line_arrow(msg,me,col):
        if msg[0] == col:
            me.itemconfig('line', arrowshape = '8 8 5' if msg[1] else '8 0 5')

    def top_update_col(msg,me,col):
        if msg[0] == col:
            send('TOPGRIDSHOW',(me,col,msg[1]))

    def top_update_row(msg,me,row):
        if msg[0] == row:
            send('TOPGRIDSHOW',(me,row,msg[1]))

    def col_config_changed(msg,me,col,bg):
        if msg[0] == col: update_col(me,col,msg[1],bg)

    def row_config_changed(msg,me,row,bg):
        if msg[0] == row:
            update_row(me,row,msg[1],bg)

    def create_NONAMECANVAS(rows,cols,gui_grid_container=container()):
        for row in range(rows):
            canvas_row = Canvas(NONAMECANVAS,relief='raised',width=13,height=0,cursor='sizing',highlightthickness=2,bd=1)
            canvas_row.bg = canvas_row['bg']
            canvas_row['highlightbackground'] = canvas_row.bg
            canvas_row.rcgrid(row,cols+1,sticky='ns')
            item = canvas_row.create_line(4,4,4,4)
            canvas_row.itemconfig(item,fill = 'blue',arrow = 'both',width = '3.0',tags = 'line')
            
            do_event("<MouseWheel>", mouse_wheel_row,(row,this()['bg']),True,True)
            do_event("<Button-4>", mouse_wheel_row,(row,this()['bg']),True,True)
            do_event("<Button-5>", mouse_wheel_row,(row,this()['bg']),True,True)
            do_event("<Button-3>", button3_event_row,(row,this()['bg']),True)
            do_event("<Button-1>", button1_grid_help,wishWidget=True)
            do_event('<Configure>',update_canvas_row_line,wishWidget=True)

            goIn() # the owner shall be the canvas
            do_receive('ROW_WEIGHT',update_canvas_row_line_arrow,[this(),row],wishMessage=True)
            do_receive('TOP_UPDATE_ROW',top_update_row,[this(),row],wishMessage=True)
            do_receive('ROW_CONFIG_CHANGED',row_config_changed,[this(),row,this()['bg']],wishMessage = True)
            do_receive('CANVAS_UPDATE_ROW',update_canvascolor_row,[this(),row,this()['bg']])
            goOut()
            send('ROW_WEIGHT',(row,container().grid_rowconfigure(row)['weight']))

            update_canvascolor_row(this(),row,this()['bg'])
        

        if container().grid_special:
            Button(NONAMECANVAS,padx = 0, pady = 0,image = gui_grid_container.help_image,command=show_help,cursor = 'question_arrow')
            rcgrid(rows+1,cols+1)

        for col in range(cols):
            canvas_col = Canvas(NONAMECANVAS,relief='raised',width=0,height=13,cursor='sizing',highlightthickness=2,highlightbackground=orange,bd=1)
            canvas_col.rcgrid(rows+1,col,sticky='we')
            canvas_col.bg = canvas_col['bg']
            canvas_col['highlightbackground'] = canvas_col.bg
            item = canvas_col.create_line(4,4,4,4)
            canvas_col.itemconfig(item,fill = 'blue',arrow = 'both',width = '3.0',tags = 'line')
           
            do_event("<MouseWheel>", mouse_wheel_col,(col,this()['bg']),True,True)
            do_event("<Button-4>", mouse_wheel_col,(col,this()['bg']),True,True)
            do_event("<Button-5>", mouse_wheel_col,(col,this()['bg']),True,True)
            do_event("<Button-3>", button3_event_col,(col,this()['bg']),True)
            do_event("<Button-1>", button1_grid_help,wishWidget=True)
            do_event("<Button-1>", button1_grid_help,wishWidget=True)
            do_event('<Configure>',update_canvas_col_line,wishWidget=True)
            goIn() # the owner shall be the canvas
            do_receive('COL_WEIGHT',update_canvas_col_line_arrow,[this(),col],wishMessage=True)
            do_receive('TOP_UPDATE_COL',top_update_col,[this(),col],wishMessage=True)
            do_receive('COL_CONFIG_CHANGED',col_config_changed,[this(),col,this()['bg']],wishMessage = True)
            do_receive('CANVAS_UPDATE_COL',update_canvascolor_col,[this(),col,this()['bg']])

            goOut()
            send('COL_WEIGHT',(col,container().grid_columnconfigure(col)['weight']))
           
            update_canvascolor_col(this(),col,this()['bg'])
       
        container().grid_columnconfigure(cols+1,minsize = 0,pad=0,weight=0)
        container().grid_rowconfigure(rows+1,minsize = 0,pad=0,weight=0)


    def show_grid(
        event=None,withNONAME = True,rows_widget=widget('EntryRows'),cols_widget=widget('EntryCols'),individual=widget('Individual'),set_col_width=set_col_width,set_row_height=set_row_height):

        try:
            cols = int(cols_widget.get())
            rows = int(rows_widget.get())
        except ValueError: return

        # delete old configuration ================

        deleteWidgetsForName(container(),NONAME)
        deleteWidgetsForName(container(),NONAME2)
        deleteWidgetsForName(container(),NONAMECANVAS)

        row_conf = container().grid_conf_rows
        col_conf = container().grid_conf_cols
        
        old_rows = row_conf[0]
        old_cols = col_conf[0]
            
        unconf_rows = old_rows
        unconf_cols = old_cols
        
        if container().grid_conf_individual_done:
            unconf_rows += 2
            unconf_cols += 2
        
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

        individ = container().grid_conf_individual_wish


        for row in range(rows):
            if withNONAME:
                for col in range(cols):
                    Frame(NONAME,**fill_cell).rcgrid(row,col,sticky='news')
                    this().lower()
                    do_event('<Button-1>',mouse_do_grid_NONAME,wishWidget=True)
        if individ:
            create_NONAMECANVAS(rows,cols)

            container().grid_conf_individual_done = True

        setSelection(selection_before)

        set_col_width()
        set_row_height()

        send("BASE_LAYOUT_REFRESH",this())

    def update_indiv_wish(wi = widget('Individual')):
        container().grid_conf_individual_wish = wi.mydata.get() == 1
        if container().grid_show:
            show_grid()

    widget('Individual').do_command(update_indiv_wish)

    def press_button_show(event=None,me = widget('ButtonShow')):
        if container().grid_show_enabled:
            container().grid_show = not container().grid_show
            me.is_on = container().grid_show

            if me.is_on:
                show_grid()
            else:
                hide_grid()

    def show_button_show(event=None,me = widget('ButtonShow')):
            me.is_on = container().grid_show
            me['relief'] = 'raised' if not me.is_on else 'sunken'
            me['text'] = 'Show' if not me.is_on else 'Hide'


    def animate_button_show(event=None,me = widget('ButtonShow')):
        if container().grid_show_enabled:
            me.is_on = container().grid_show
            me['relief'] = 'raised' if me.is_on else 'sunken'
            me['text'] = 'Show' if me.is_on else 'Hide'

    def entry_show_grid(event=None):
        container().grid_show = True
        show_button_show()
        show_grid()
        

    widget('ButtonShow').is_on = False
    widget('ButtonShow').bind('<Button-1>',animate_button_show)
    widget('ButtonShow').bind('<ButtonRelease-1>',press_button_show)
    widget('EntryRows').bind('<Return>',entry_show_grid)
    widget('EntryCols').bind('<Return>',entry_show_grid)



    def update_after_pack(rows_widget=widget('EntryRows'),cols_widget=widget('EntryCols'),show_grid = show_grid):
 
        if container().grid_conf_rows[0] != 0 or container().grid_conf_cols[0] != 0:
                
            rows_widget.delete(0,'end')
            rows_widget.insert(0,'0')
            cols_widget.delete(0,'end')
            cols_widget.insert(0,'0')
            show_grid()

    do_receive('BASE_LAYOUT_PACK_DONE',update_after_pack)

    def mouse_move(me,wi_row=widget('Row'),wi_col=widget('Col')):
        if me.mydata[6]:
            step = 10
            diffx = me.winfo_pointerx() - me.winfo_rootx()
            diffy = me.winfo_pointery() - me.winfo_rooty()
            me.mydata[3] += diffx-me.mydata[0]
            me.mydata[4] += diffy-me.mydata[1]
            me.place(y=me.mydata[4],x = me.mydata[3], width = me.mydata[8],height=me.mydata[9])
            
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
        me.dyntk_lift()


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
        me.myRoot().unbind('<ButtonRelease-1>',app_id[0])
        if me.mydata[6]: on_mouse_up(me)

    def on_mouse_down(me,event,app_id=apprelease_id_list):

        xpos = me.winfo_rootx()-me.container().winfo_rootx()
        ypos = me.winfo_rooty()-me.container().winfo_rooty()
        me.mydata = [event.x,event.y,'mouse',xpos,ypos,0,True,False,me.winfo_width(),me.winfo_height()]
        
        # SHOW_CONFIG geht nicht - müsste das wohl als event und nicht als message machen - also mit bind statt do_event
        #send('SHOW_LAYOUT',(None,True))
        #send('SHOW_CONFIG',(None,True))

        me.place(y=ypos,x = xpos, width = me.mydata[8],height=me.mydata[9])
        me.lift()
        app_id[0] = me.myRoot().bind('<ButtonRelease-1>',lambda event=event, wi = me, func=on_app_mouse_up: func(wi))
        mouse_move(me)

        if this() != me:
            setWidgetSelection(me)
            me.mydata[7] = True
            send('SHOW_LAYOUT',(None,False))
            send('SHOW_CONFIG',(None,False))
            send('SELECTION_CHANGED')
        else:
            if me == container():
                goOut()
                me.mydata[7] = True
                send('SHOW_LAYOUT',(None,False))
                send('SHOW_CONFIG',(None,False))
                send('SELECTION_CHANGED')
                
        send('BASEMENTLEVEL_CHANGED')

    def do_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        me.mydata=([0,0,'mouse',0,0,0,True,False])
        me.do_event('<Button-1>',mouse_down,wishWidget=True,wishEvent=True)
        me.do_event('<ButtonRelease-1>',mouse_up,me)

    def grid_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        if type(me.mydata) != list or len(me.mydata) < 3 or me.mydata[2]!= 'mouse':
            me.mydata=([0,0,'mouse',0,0,0,True,False])
            me.do_event('<Button-1>',mouse_down,wishWidget=True,wishEvent=True)
            me.do_event('<ButtonRelease-1>',mouse_up,me)

    do_receive('GRID_MOUSE_ON',grid_mouse_on,wishMessage=True)


    def do_grid_col_row(col,row,do_mouse_on=do_mouse_on):

        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        layout_before = this().Layout

        if this().Layout == NOLAYOUT:
            if isinstance(this(),GuiContainer):
                grid(row=row,column=col,sticky = 'news') # this isn't original, but makes sense

                # we don't want this for the normal grid
                if isinstance(this(),(LabelFrame,Frame,ttk.LabelFrame,ttk.Frame)) and container().grid_special:
                    this().grid_columnconfigure(0,minsize=MIN_WIDTH)
                    this().grid_rowconfigure(0,minsize=MIN_HEIGHT)
                    a = Frame((this(),NONAME))
                    a.rcgrid(0,0)
                    this().after(100,NONAME_destroy,a)
            else:
                rcgrid(row,col)
            this().dyntk_lift()
        elif this().Layout == PLACELAYOUT:
            
            (col,row) = container().grid_location(this().winfo_rootx()-container().winfo_rootx(),this().winfo_rooty()-container().winfo_rooty())
            if col < 0: col = 0
            if row < 0: row = 0
            rcgrid(row,col)
            this().dyntk_lift()
        elif this().Layout == GRIDLAYOUT:
            rcgrid(row,col)
            this().dyntk_lift()

        if container().is_mouse_select_on: do_mouse_on(this())
        else: send("SWITCH_MOUSE_ON")

        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions


    def mouse_do_grid_NONAME(me):
        if this().Layout == NOLAYOUT and not isinstance(this(),StatTkInter.Menu):
            info = me.grid_info()
            do_grid_col_row(info['column'],info['row'])
        

    def mouse_do_grid(me):
        if this().Layout == NOLAYOUT and not isinstance(this(),StatTkInter.Menu):
            x,y = me.winfo_pointerxy()
            dx = x - me.winfo_rootx()
            dy = y - me.winfo_rooty()
            col,row = me.master.grid_location(dx,dy)
            do_grid_col_row(col,row)
        

    def special_noname_frame():
        Frame(NONAME,**fill_cell2).rcgrid(0,0,sticky='news',rowspan = container().grid_conf_rows[0], columnspan = container().grid_conf_cols[0])
        this().lower()
        do_event('<Button-1>',mouse_do_grid,wishWidget = True)



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
individual = widget('Individual'),
uniform_row = widget('uniform_row'),
uniform_col = widget('uniform_col'),
):


        if not container().grid_conf_cols:
            container().grid_conf_cols,container().grid_multi_conf_cols = get_gridconfig(container().grid_cols,this().grid_cols_how_many)

        if not container().grid_conf_rows:
            container().grid_conf_rows,container().grid_multi_conf_rows = get_gridconfig(container().grid_rows,this().grid_rows_how_many)

        if this().Layout != LAYOUTNEVER:
            
            if not (container().Layout == MENULAYOUT or this().Layout == MENUITEMLAYOUT or isinstance(this(),Menu) or isinstance(container(),PanedWindow) or isinstance(container(),StatTtk.PanedWindow)):
                not_initialized = container().grid_conf_rows == None
                if not_initialized:
                    container().grid_conf_rows = (0,MIN_HEIGHT,0,0)
                    container().grid_conf_cols = (0,MIN_WIDTH,0,0)
                
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
                update_individual_mark(container())

                show_button_show()

                uniform_row.delete(0,'end')
                uniform_col.delete(0,'end')
                uniform_row.insert(0,container().grid_uni_row)
                uniform_col.insert(0,container().grid_uni_col)
                

    do_receive("SELECTION_CHANGED",update_grid_table_on_enter)


    def NONAME_destroy(a):
        selection_before = Selection()
        a.destroy()
        setSelection(selection_before)


    def do_grid():
        do_grid_col_row(0,0)
        
    widget('ButtonGrid').do_command(do_grid)


    def do_grid0():
        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        layout_before = this().Layout
        grid()
        this().dyntk_lift()
        if container().is_mouse_select_on: do_mouse_on(this())
        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

    widget('Grid()').do_command(do_grid0)


    def row_default():
        conf = container().grid_conf_rows
        uniform = container().grid_uni_row if container().grid_uni_row else ''
        return { 'minsize' : conf[1], 'pad' : conf[2], 'weight' : conf[3], 'uniform' : uniform }
       

    def col_default():
        conf = container().grid_conf_cols
        uniform = container().grid_uni_col if container().grid_uni_col else ''
        return { 'minsize' : conf[1], 'pad' : conf[2], 'weight' : conf[3], 'uniform' : uniform }

    class LineFrame(Frame):
     
        def __init__(self,master,**kwargs):
     
            self.green = '#50d090'
            self.gray = '#d9d9d9'
            self.blue = 'blue'
     
            self.is_col = kwargs.pop('is_col',None)
           
            kwargs['bg'] = self.gray
            kwargs['bd'] = 2
            kwargs['relief'] = 'raised'
            if self.is_col:
                kwargs['width'] = 6
            else:
                kwargs['height'] = 6
           
            Frame.__init__(self,(master,NONAME2),**kwargs)
            self.master = master
            self.move_started = False

        # ========================================================        
     
        def tableline_leave(self,event=None):
            self.config( cursor = '', bg = self.gray)
     
        def tableline_startmove_row(self,event = None):
            self.move_started = True
            self.button_release = self.tableline_mark_row
            self.enter = self.tableline_enter_row
            self.startmove = self.tableline_startmove_row
            self.unbind('<Enter>')
            self.unbind('<Leave>')
            self.unbind('<B1-Motion>')
            self.bind('<ButtonRelease-1>',self.move_release)
            # from gridproject
            self.mouse_startpos = self.master.winfo_pointery()
            self.row_col = int(self.grid_info()['row']) - 1
            self.line_configure = self.master.grid_rowconfigure
            self.row_col_config = self.line_configure(self.row_col)
            self.weight = int(self.row_col_config['weight'])
            self.is_endline = self.row_col + 1 == self.master.grid_conf_rows[0]
            self.measure_size = self.measure_rowheight
            self.measure_size()
            self.start_size = self.cellsize
            self.start_begin = self.begin
            self.is_moving = True
            self.startmove = self.tableline_startmove_row
            self.enter = self.tableline_enter_row
            self.pointer = self.master.winfo_pointery
            self.is_uniform = 'uniform' in self.row_col_config and self.row_col_config['uniform']
            self.uniform_count = 1
            if self.is_uniform:
                uniform = self.row_col_config['uniform']
                configs = self.master.grid_multi_conf_rows
                count = 0
                for row in range(self.row_col+1):
                    if configs[row][0] and configs[row][1]['uniform'] == uniform:
                        count += 1
                self.uniform_count = count
                
            self.move()
     
        def tableline_startmove_col(self,event = None):
            self.move_started = True
            self.button_release = self.tableline_mark_col
            self.enter = self.tableline_enter_col
            self.startmove = self.tableline_startmove_col
            self.unbind('<Enter>')
            self.unbind('<Leave>')
            self.bind('<ButtonRelease-1>',self.move_release)
            self.unbind('<B1-Motion>')
     
            # from gridproject
            self.mouse_startpos = self.master.winfo_pointerx()
            self.row_col = int(self.grid_info()['column']) -1
            self.line_configure = self.master.grid_columnconfigure
            self.row_col_config = self.line_configure(self.row_col)
            self.weight = int(self.row_col_config['weight'])
            self.is_endline = self.row_col + 1 == self.master.grid_conf_cols[0]
            self.measure_size = self.measure_colwidth
            self.measure_size()
            self.start_size = self.cellsize
            self.start_begin = self.begin
            self.is_moving = True
            self.startmove = self.tableline_startmove_col
            self.enter = self.tableline_enter_col
            self.pointer = self.master.winfo_pointerx
            self.is_uniform = 'uniform' in self.row_col_config and self.row_col_config['uniform']
            self.uniform_count = 1
            if self.is_uniform:
                uniform = self.row_col_config['uniform']
                configs = self.master.grid_multi_conf_cols
                count = 0
                for col in range(self.row_col+1):
                    if configs[col][0] and configs[col][1]['uniform'] == uniform:
                        count += 1
                self.uniform_count = count
            self.move()
     
        def measure_colwidth(self):
            self.begin,top,self.cellsize,height = self.master.grid_bbox(row = 0, column = self.row_col)
     
        def measure_rowheight(self):
            left,self.begin,width,self.cellsize = self.master.grid_bbox(row = self.row_col, column = 0)
     
        def set_size(self):
            self.row_col_config['minsize'] = self.cellsize - 2 * int(self.row_col_config['pad'])
            self.line_configure(self.row_col,**self.row_col_config)
     
        def move(self):
     
            if not self.is_moving:
                self.bind_enter()
                return
           
            pos_mouse = self.pointer()
            dpos = pos_mouse - self.mouse_startpos
            self.dpos = dpos

            
            if not self.weight:
                self.measure_size()
                self.row_col_config['minsize'] = self.cellsize
                self.line_configure(self.row_col,**self.row_col_config)

                if self.is_col:
                    send_immediate('COL_CONFIG_CHANGED',(self.row_col,self.row_col_config))
                else:
                    send_immediate('ROW_CONFIG_CHANGED',(self.row_col,self.row_col_config))
            
                    
     
            self.measure_size()
            if self.is_endline:
                self.new_cellsize = self.start_size + self.dpos
            else:
                self.new_cellsize = self.start_size + self.start_begin - self.begin + self.dpos
     
            self.new_cellsize = max(self.new_cellsize,0)
            self.increase =  (self.new_cellsize - self.cellsize)//self.uniform_count

            if self.weight:
                if self.increase < 0:
                    self.increase = min(self.increase//2,0)
               
            if self.increase > 0 and self.cellsize < self.new_cellsize or self.increase < 0 and self.cellsize > self.new_cellsize:
                minsize = self.row_col_config['minsize']
                if self.increase > 0 and minsize + self.increase <= self.new_cellsize or self.increase < 0 and minsize + self.increase >=0:
                    self.row_col_config['minsize'] = minsize + self.increase
                    self.line_configure(self.row_col,**self.row_col_config)

                    if self.is_col:
                        send_immediate('COL_CONFIG_CHANGED',(self.row_col,self.row_col_config))
                    else:
                        send_immediate('ROW_CONFIG_CHANGED',(self.row_col,self.row_col_config))
                     
            self.after(10,self.move)

        def move_release(self,event = None):
            self.is_moving = False
            self.tableline_leave()
            self.move_started = False

        def tableline_mark_end(self,event = None):
            self.tableline_leave()
            self.bind_enter()

        def tableline_mark_col(self,event = None):
            if not self.move_started:
                self.unbind('<Leave>')
                self.unbind('<Enter>')
                self.bind('<ButtonRelease-1>',self.tableline_mark_end)
                for element in self.master.dyntk_table_frames:
                    element.config( bg = self.gray)
                self.lift()
                self.config( cursor = '', bg = self.blue)
                self.focus()
                self.bind('<Insert>',self.insert)
                self.bind('<Delete>',self.delete)
                self.row_col = int(self.grid_info()['column'])
                self.grid_key = 'column'
                self.grid_configure = self.master.columnconfigure
                self.row_col_default = col_default
               
           
        def tableline_mark_row(self,event = None):
            if not self.move_started:
                self.unbind('<Leave>')
                self.unbind('<Enter>')
                self.bind('<ButtonRelease-1>',self.tableline_mark_end)
                for element in self.master.dyntk_table_frames:
                    element.config( bg = self.gray)
                self.lift()
                self.config( cursor = '', bg = self.blue)
                self.focus()
                self.bind('<Insert>',self.insert)
                self.bind('<Delete>',self.delete)
                self.row_col = int(self.grid_info()['row'])
                self.grid_key = 'row'
                self.grid_configure = self.master.rowconfigure
                self.row_col_default = row_default
           
        def bind_enter(self):
            if self.is_col:
                if int(self.grid_info()['column']):
                    self.bind('<Enter>',self.tableline_enter_col)
                    self.bind('<B1-Motion>',self.tableline_startmove_col)
                else:
                    self.bind('<Enter>',self.tableline_enter_insert_col)
                self.bind('<ButtonRelease-1>',self.tableline_mark_col)


            else:
                if int(self.grid_info()['row']):
                    self.bind('<Enter>',self.tableline_enter_row)
                    self.bind('<B1-Motion>',self.tableline_startmove_row)
                else:
                    self.bind('<Enter>',self.tableline_enter_insert_row)
                self.bind('<ButtonRelease-1>',self.tableline_mark_row)
     
        # these are double defined, but nearly identical may be we not only a single definition
        def tableline_enter_col(self,event=None):
            for element in self.master.dyntk_table_frames:
                element.config( bg = self.gray)
                element.bind_enter()
     
            self.master.focus()
            self.bind('<Leave>',self.tableline_leave)
            self.lift()
            self.config( cursor = 'sb_h_double_arrow', bg = self.green)
     
        def tableline_enter_row(self,event=None):
            for element in self.master.dyntk_table_frames:
                element.config( bg = self.gray)
                element.bind_enter()
     
            self.master.focus()
            self.bind('<Leave>',self.tableline_leave)
            self.lift()
            self.config( cursor = 'sb_v_double_arrow', bg = self.green)
     
        def tableline_enter_insert_col(self,event=None):
            for element in self.master.dyntk_table_frames:
                element.config( bg = self.gray)
                element.bind_enter()
            self.master.focus()
            self.bind('<Leave>',self.tableline_leave)
            self.lift()
            self.config( cursor = 'plus', bg = self.green)
     
        def tableline_enter_insert_row(self,event=None):
            for element in self.master.dyntk_table_frames:
                element.config( bg = self.gray)
                element.bind_enter()
            self.master.focus()
            self.bind('<Leave>',self.tableline_leave)
            self.lift()
            self.config( cursor = 'plus', bg = self.green)


        def insert(self,event = None):
            selection_before = Selection()
            deleteWidgetsForName(self.master,NONAMECANVAS)
            deleteWidgetsForName(self.master,NONAME)
            endpos = self.master.grid_conf_cols[0] if self.is_col else self.master.grid_conf_rows[0]
            # if our line is the last one, we don't insert anything

            children = self.master.grid_slaves()
            for pos in range(endpos,self.row_col-1,-1):
                for child in children:
                    if int(child.grid_info()[self.grid_key]) == pos:
                        child.grid(**{ self.grid_key : pos+1})
                self.grid_configure(pos+1,**self.grid_configure(pos))
     
            self.grid_configure(self.row_col,**self.row_col_default())
            insert_frame = self.insert_row_col(self.row_col)
     
            self['bg'] = self.gray
            self.bind_enter()
     
            if self.is_col:
     
                conf = list(self.master.grid_conf_cols)
                conf[0] += 1
                self.master.grid_conf_cols = tuple(conf)
                is_uni = True if self.master.grid_uni_col else False
                self.master.grid_multi_conf_cols.insert(self.row_col,[is_uni,self.row_col_default()])
                
                for frame in self.master.dyntk_row_frames:
                    frame.grid(column = 0, columnspan = self.master.grid_conf_cols[0])
                insert_frame.tableline_mark_col()
                send('GRID_COLS_CHANGED')
            else:
                conf = list(self.master.grid_conf_rows)
                conf[0] += 1
                self.master.grid_conf_rows = tuple(conf)

                is_uni = True if self.master.grid_uni_row else False
                self.master.grid_multi_conf_rows.insert(self.row_col,[is_uni,self.row_col_default()])

                for frame in self.master.dyntk_col_frames:
                    frame.grid(row = 0,rowspan = self.master.grid_conf_rows[0])
                insert_frame.tableline_mark_row()
                send('GRID_ROWS_CHANGED')

            create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
            special_noname_frame()            
            setSelection(selection_before)
            

        def delete(self,event = None):
            selection_before = Selection()

            endpos = self.master.grid_conf_cols[0] if self.is_col else self.master.grid_conf_rows[0]
     
            # don't delete anything, if it's the last line
            if self.row_col == endpos:
                return
     
            # check whether it's the first line or column and whether there is only one line or column
            if self.row_col == 0 and endpos == 1:
                return
     
            deleteWidgetsForName(self.master,NONAMECANVAS)
            deleteWidgetsForName(self.master,NONAME)

            # check whether the current row or column is empty

            children = self.master.grid_slaves()
            elements = [ element for element in children if int(element.grid_info()[self.grid_key]) == self.row_col and element not in self.master.dyntk_table_frames]
     
            if elements:
                create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
                special_noname_frame()
                setSelection(selection_before)
                return
     
            # ok we have an empty row or column, which isn't the first one, so we first destroy the line frame of this column or line
            if self.is_col:
                for frame in self.master.dyntk_col_frames:
                    if int(frame.grid_info()[self.grid_key]) == self.row_col + 1:
                        self.master.dyntk_col_frames.pop(self.master.dyntk_col_frames.index(frame)).destroy()
                        self.master.dyntk_table_frames.pop(self.master.dyntk_table_frames.index(frame)).destroy()
                        break

                conf = list(self.master.grid_conf_cols)
                conf[0] -= 1
                self.master.grid_conf_cols = tuple(conf)
                self.master.grid_multi_conf_cols.pop(self.row_col)

                for frame in self.master.dyntk_row_frames:
                    frame.grid(column = 0, columnspan = self.master.grid_conf_cols[0])
                self.master.grid_columnconfigure(self.master.grid_conf_cols[0]+2,minsize=0,pad=0,weight=0)
                send('GRID_COLS_CHANGED')
                

     
            else:
                for frame in self.master.dyntk_row_frames:
                    if int(frame.grid_info()[self.grid_key]) == self.row_col + 1:
                        self.master.dyntk_row_frames.pop(self.master.dyntk_row_frames.index(frame)).destroy()
                        self.master.dyntk_table_frames.pop(self.master.dyntk_table_frames.index(frame)).destroy()
                        break
     
                conf = list(self.master.grid_conf_rows)
                conf[0] -= 1
                self.master.grid_conf_rows = tuple(conf)
                self.master.grid_multi_conf_rows.pop(self.row_col)


                for frame in self.master.dyntk_col_frames:
                    frame.grid(row = 0,rowspan = self.master.grid_conf_rows[0])
                self.master.grid_rowconfigure(self.master.grid_conf_rows[0]+2,minsize=0,pad=0,weight=0)
                send('GRID_ROWS_CHANGED')
     

     
            #so we move the widgets one row or colum down

            children = self.master.winfo_children()
            child_copy = list(children)
            for child in child_copy:
                if isinstance(child,(StatTkInter.Toplevel,StatTkInter.Menu)):
                    children.pop(children.index(child))

            child_copy = list(children)
            for child in child_copy:
                if not child.grid_info():
                    children.pop(children.index(child))

            for pos in range(self.row_col,endpos):
                for child in children:
                    if int(child.grid_info()[self.grid_key]) == pos+1:
                        child.grid(**{ self.grid_key : pos })
                self.grid_configure(pos,**self.grid_configure(pos+1))
            self.grid_configure(endpos,minsize = 0, pad = 0, weight = 0)
     
            create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
            special_noname_frame()
            setSelection(selection_before)

            

    def insert_col(col):
        self = container()
        frame = LineFrame(self,is_col = True)
        frame.insert_col = insert_col
        frame.insert_row_col = insert_col
        frame.grid(column = col,row = 0, rowspan = self.grid_conf_rows[0]+1, sticky = 'nsw')
        frame.bind_enter()
        self.dyntk_table_frames.append(frame)
        self.dyntk_col_frames.append(frame)
        return frame
 
 
    def insert_row(row):
        self = container()
        frame = LineFrame(self,is_col = False)
        frame.grid(row = row, column = 0, columnspan = self.grid_conf_cols[0]+1, sticky = 'wen')
        frame.insert_row_col = insert_row
        frame.bind_enter()
        self.dyntk_table_frames.append(frame)
        self.dyntk_row_frames.append(frame)
        return frame
 
    def insert_table(self):
        for col in range(self.grid_conf_cols[0]+1):
            insert_col(col)
        for row in range(self.grid_conf_rows[0]+1):
            insert_row(row)
 

    def special_toggle(me = widget('special'),ButtonShow = widget('ButtonShow'),Individual = widget('Individual'),EntryRows = widget('EntryRows'),EntryCols = widget('EntryCols')):
        container().grid_special = not container().grid_special
        me.is_on = container().grid_special

        me['relief'] = 'sunken' if me.is_on else 'raised'
        hide_grid()

        if me.is_on:

            min_row = 0
            min_col = 0
            children = container().grid_slaves()
            for child in children:
                grid_layout = child.grid_info()
                min_row = max(min_row,int(grid_layout['row']))
                min_col = max(min_col,int(grid_layout['column']))

            grid_conf_rows_old = container().grid_conf_rows
            grid_conf_cols_old = container().grid_conf_cols

            grid_conf_rows = list(container().grid_conf_rows)
            grid_conf_cols = list(container().grid_conf_cols)

            rows = max(grid_conf_rows[0],min_row+1)
            cols = max(grid_conf_cols[0],min_col+1)

            grid_conf_rows[0] = rows
            grid_conf_cols[0] = cols

            if not children:
                grid_conf_rows[1] = max(grid_conf_rows[1],MIN_HEIGHT)
                grid_conf_cols[1] = max(grid_conf_cols[1],MIN_WIDTH)

            container().grid_conf_rows = tuple(grid_conf_rows)
            container().grid_conf_cols = tuple(grid_conf_cols)

            update_general_grid()

            container().save_grid_conf_individual_wish = container().grid_conf_individual_wish
            container().grid_conf_individual_wish = 1

            container().grid_conf_rows  = grid_conf_rows_old # show_grid corrects this, otherwise crash
            container().grid_conf_cols  = grid_conf_cols_old
            show_grid(None,False)

            selection_before = Selection()
            special_noname_frame()

            ButtonShow['state'] = 'disabled' if me.is_on else 'normal'
            container().grid_show_enabled = not me.is_on

            Individual['state'] = 'disabled' if me.is_on else 'normal'
            EntryRows['state'] = 'disabled' if me.is_on else 'normal'
            EntryCols['state'] = 'disabled' if me.is_on else 'normal'

            container().dyntk_table_frames = []
            container().dyntk_col_frames = []
            container().dyntk_row_frames = []

            insert_table(container())
            setSelection(selection_before)

        else:

            ButtonShow['state'] = 'disabled' if me.is_on else 'normal'
            container().grid_show_enabled = not me.is_on

            Individual['state'] = 'disabled' if me.is_on else 'normal'
            EntryRows['state'] = 'disabled' if me.is_on else 'normal'
            EntryCols['state'] = 'disabled' if me.is_on else 'normal'
            container().grid_conf_individual_wish = container().save_grid_conf_individual_wish

            container().dyntk_table_frames = []
            container().dyntk_col_frames = []
            container().dyntk_row_frames = []

            if container().grid_show:
                show_grid()


    def update_special_button(me = widget('special'),ButtonShow = widget('ButtonShow'),Individual = widget('Individual'),EntryRows = widget('EntryRows'),EntryCols = widget('EntryCols')):
        me.is_on = container().grid_special
        me['relief'] = 'sunken' if me.is_on else 'raised'
        ButtonShow['state'] = 'disabled' if me.is_on else 'normal'
        container().grid_show_enabled = not me.is_on

        Individual['state'] = 'disabled' if me.is_on else 'normal'
        EntryRows['state'] = 'disabled' if me.is_on else 'normal'
        EntryCols['state'] = 'disabled' if me.is_on else 'normal'

    do_receive("SELECTION_CHANGED",update_special_button)

    widget('special').is_on = False
    widget('special').do_command(special_toggle)

main()


### ========================================================
