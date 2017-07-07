config(**{'grid_cols': '(6, 0, 0, 0)', 'grid_rows': '(8, 0, 0, 0)'})

Button('ButtonGrid',**{'bd': '3', 'bg': 'lightgreen', 'padx': '1', 'pady': '1', 'text': 'GRID', 'font': 'TkDefaultFont 9 bold'}).grid(row=0, sticky='nesw', column=1, columnspan=2)
Button('Grid()',**{'bd': '3', 'bg': 'lightgreen', 'padx': '1', 'pady': '1', 'text': 'Grid()'}).grid(row=0, sticky='nesw', column=3)
ttk.Separator('separator').grid(row=5, sticky='ew', columnspan=5)
Entry('uniform_row',**{'bg': '#e0ffb0', 'width': 0}).grid(row=7, sticky='nesw', columnspan=2)
Entry('uniform_col',**{'bg': '#fff0b0', 'width': 0}).grid(row=7, sticky='nesw', column=3, columnspan=2)
ttk.Label('luniformrow',**{'text': 'uniform (row)'}).grid(row=6, sticky='w', columnspan=2)
Label('luniformcol',**{'text': 'uniform (column)'}).grid(row=6, sticky='w', column=3, columnspan=2)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(row=1, sticky='ns', column=2, rowspan=8)
Label('lpad',**{'text': 'pad'}).grid(row=2, sticky='e')
Label('lweight',**{'text': 'weight'}).grid(row=3, sticky='e')
Label('lheight',**{'text': 'minsize'}).grid(row=1, sticky='e')
Label('lrows',**{'text': 'Rows', 'font': 'TkDefaultFont 9 bold'}).grid(row=4, sticky='nesw')
Entry('EntryRows',**{'bg': '#ffffd4', 'width': 6}).grid(row=4, sticky='nesw', column=1)
Entry('EntryCols',**{'bg': '#ffffd4', 'width': 5}).grid(row=4, sticky='nesw', column=3)
Label('lcols',**{'text': 'Columns', 'font': 'TkDefaultFont 9 bold'}).grid(row=4, sticky='nesw', column=4)
Button('special',**{'bd': 2, 'photoimage': 'guidesigner/images/insert_table_row.gif', 'cursor': 'star', 'text': 'special'}).grid(row=2, column=4, rowspan=2)
Label('LableTitle',**{'fg': 'blue', 'bd': '3', 'relief': 'ridge', 'text': 'grid', 'font': 'TkDefaultFont 9 bold'}).grid(row=0, sticky='nesw')
Spinbox('EntryRowHeight',**{'to': 1000.0, 'width': 4}).grid(row=1, sticky='nesw', column=1)
Spinbox('EntryColWidth',**{'to': 1000.0, 'width': 4}).grid(row=1, sticky='nesw', column=3)
Spinbox('EntryRowPad',**{'to': 1000.0, 'width': 4}).grid(row=2, sticky='nesw', column=1)
Spinbox('EntryColPad',**{'to': 1000.0, 'width': 4}).grid(row=2, sticky='nesw', column=3)
Spinbox('EntryRowWeight',**{'to': 1000.0, 'width': 4}).grid(row=3, sticky='nesw', column=1)
Spinbox('EntryColWeight',**{'to': 1000.0, 'width': 4}).grid(row=3, sticky='nesw', column=3)
Checkbutton('Individual',**{'highlightthickness': '2', 'text': 'indiv.'}).grid(row=1, sticky='ew', column=4)
Label('ButtonShow',**{'bd': '3', 'bg': 'lightgreen', 'relief': 'raised', 'text': 'Show'}).grid(row=0, sticky='nesw', column=4)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(row=0, sticky='nsw', column=5, rowspan=9)

### CODE ===================================================

#Entry('uniform_row',**{'bg': '#def6b4', 'width': 0}).grid(row=7, sticky='nesw', columnspan=2)
#Entry('uniform_col',**{'bg': '#fff4b1', 'width': 0}).grid(row=7, sticky='nesw', column=3, columnspan=2)



IndividualVar =  IntVar()
widget('Individual').config(variable = IndividualVar, onvalue = 1, offvalue = 0)
widget('Individual').mydata=IndividualVar

# -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------




def main():

    insert_uniform_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/insert-text.gif')
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
    orange = '#f0f080'
    color_uni_col = '#fff0b0'
    color_uni_row = '#e0ffb0'

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



    # update input fields
    def update_uni_row(me=widget('uniform_row')):
        uniform = me.get().strip()
        if uniform:
            if container().grid_multi_conf_rows:
                for conf in container().grid_multi_conf_rows:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        # look for first uniform entry if it exists and update the value of the grid layout coulumn input
                        me.grid_current_uniform = (conf[1]['minsize'],conf[1]['pad'],conf[1]['weight'])
                        update_rows_data(conf[1]['minsize'],conf[1]['pad'],conf[1]['weight'])
                        break
        else:
            # if the uniform entry was emptied, take over general row entries
            if container().grid_conf_rows and container().grid_conf_rows[0]:
                update_general_rows()

        container().grid_uni_row = uniform 
        send('CANVAS_UPDATE_ROW') # update für canvasses
        send('CANVAS_UPDATE_COL') # update für canvasses


    def take_over_uniform_row(uniform,me=widget('uniform_row')):
        me.delete(0,'end')
        me.insert(0,uniform)
        update_uni_row()

    do_receive('TAKE_OVER_UNIFORM_ROW',take_over_uniform_row,wishMessage = True)


    # update input fields
    def update_uni_col(me=widget('uniform_col')):
        uniform = me.get().strip()
        if uniform:
            if container().grid_multi_conf_cols:
                for conf in container().grid_multi_conf_cols:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        me.grid_current_uniform = (conf[1]['minsize'],conf[1]['pad'],conf[1]['weight'])
                        update_cols_data(conf[1]['minsize'],conf[1]['pad'],conf[1]['weight'])
                        found is True
                        break
        else:
            if container().grid_conf_cols and container().grid_conf_cols[0]:
                update_general_cols()

        container().grid_uni_col = uniform
        send('CANVAS_UPDATE_ROW') # color update für canvasses
        send('CANVAS_UPDATE_COL') # color update für canvasses


    def take_over_uniform_col(uniform,me=widget('uniform_col')):
        me.delete(0,'end')
        me.insert(0,uniform)
        update_uni_col()

    do_receive('TAKE_OVER_UNIFORM_COL',take_over_uniform_col,wishMessage = True)


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
        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        deleteWidgetsForName(container(),NONAME)
        deleteWidgetsForName(container(),NONAMECANVAS)
        deleteWidgetsForName(container(),NONAME2)
        if container().grid_conf_individual_done:
            cols = container().grid_conf_cols[0]
            rows = container().grid_conf_rows[0]
            container().grid_columnconfigure(cols,minsize = 0,pad=0,weight=0,uniform='') # space for additional line frame
            container().grid_columnconfigure(cols+1,minsize = 0,pad=0,weight=0,uniform='') # space for canvas
            # container().grid_columnconfigure(cols+2,minsize = 0,pad=0,weight=0,uniform='') # ???

            container().grid_rowconfigure(rows,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_rowconfigure(rows+1,minsize = 0,pad=0,weight=0,uniform='')
            container().grid_rowconfigure(rows+2,minsize = 0,pad=0,weight=0,uniform='') # ???
            # container().grid_conf_individual_done = False
        
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

    def update_row_values_uniform(size,pad,weight,uniform):
        rows = container().grid_conf_rows[0]
        for row in range(rows):
            if container().grid_multi_conf_rows[row][0]:
                conf = container().grid_multi_conf_rows[row][1]
                if 'uniform' in conf and conf['uniform'] and conf['uniform'] == uniform:
                    conf.update({ 'minsize' : size, 'pad' : pad, 'weight':weight})
        set_row_height()


    def update_col_values():
        is_uniform, size, pad, weight = update_cols()
        if is_uniform:
            update_col_values_uniform(size,pad,weight,container().grid_uni_col)
            update_row_values_uniform(size,pad,weight,container().grid_uni_col)
       
        else:
            set_col_width()

    def update_row_values():
        is_uniform, size, pad, weight = update_rows()
        if is_uniform:
            update_row_values_uniform(size,pad,weight,container().grid_uni_row)
            update_col_values_uniform(size,pad,weight,container().grid_uni_row)
        else:
            set_row_height()

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

    widget('EntryColWidth').do_command(check_col_values)
    widget('EntryColWidth').do_event('<Return>',check_col_values)
    widget('EntryColPad').do_command(check_col_values)
    widget('EntryColPad').do_event('<Return>',check_col_values)
    widget('EntryColWeight').do_command(check_col_values)
    widget('EntryColWeight').do_event('<Return>',check_col_values)


    class GridTop(Toplevel):

        def __init__(self,master,x,y,row_col,grid_configure,item_text,is_row):

            self.mycanvas = master
            self.row_col = row_col
            
            self.grid_configure = grid_configure
            grid_conf = grid_configure(row_col)
            self.is_row = is_row
            
            selection_before = Selection()

            Toplevel.__init__(self,'GridTop',geometry = '+'+str(x)+'+'+str(y),**{'grid_multi_cols': "[6, (0, 4, 0, 0, 'space'), (2, 4, 0, 0, 'space'), (5, 4, 0, 0, 'space')]", 'grid_cols': '(6, 0, 0, 0)', 'grid_rows': '(6, 0, 2, 0)'})

            Label('lRowCol',**{'text': 'Column', 'font': 'TkDefaultFont 9 bold'}).grid(sticky='e', column=1, row=0)
            Label('showRowCol',**{'text': '8', 'font': 'TkDefaultFont 9 bold', 'bg': '#ffffd4', 'fg': 'blue', 'relief': 'solid', 'width': 4}).grid(ipadx=5, sticky='w', column=3, pady=5, row=0)
            Label('lsize',**{'text': 'size'}).grid(sticky='e', column=1, row=1)
            Spinbox('EntrySize',**{'to': 1000.0, 'width': 4}).grid(sticky='nsw', column=3, row=1)
            Label('lpad',**{'text': 'pad'}).grid(sticky='e', column=1, row=2)
            Spinbox('EntryPad',**{'to': 1000.0, 'width': 4}).grid(sticky='nsw', column=3, row=2)
            Label('lweight',**{'text': 'weight'}).grid(sticky='e', column=1, row=3)
            Spinbox('EntryWeight',**{'to': 1000.0, 'width': 4}).grid(sticky='nsw', column=3, row=3)
            Label('luniform',**{'text': 'uniform'}).grid(column=1, row=4)
            Entry('EntryUniform',**{'width': 12}).grid(sticky='nesw', column=3, row=4, columnspan=2)
            Button('OK',**{'pady': '1', 'text': 'OK'}).grid(sticky='e', column=3, row=5, columnspan=2)
            Button('InsertUniform',**{'pady': '0', 'padx': '0', 'highlightthickness': '0','image' : insert_uniform_gif}).grid(rowspan=2, sticky='es', column=4, row=2)

            widget('lRowCol')['text'] = item_text
            widget('showRowCol')['text'] = str(row_col)
            widget('EntrySize').delete(0,'end')
            widget('EntrySize').insert(0,grid_conf['minsize'])
            widget('EntryPad').delete(0,'end')
            widget('EntryPad').insert(0,grid_conf['pad'])
            widget('EntryWeight').delete(0,'end')
            widget('EntryWeight').insert(0,grid_conf['weight'])
            widget('EntryUniform').delete(0,'end')

            uniform = grid_conf['uniform']
            uniform = str(uniform) if uniform else ''
            widget('EntryUniform').insert(0,uniform)


            widget('EntrySize').do_command(self.update_values)
            widget('EntrySize').do_event('<Return>',self.update_values)
            widget('EntryPad').do_command(self.update_values)
            widget('EntryPad').do_event('<Return>',self.update_values)
            widget('EntryWeight').do_command(self.update_values)
            widget('EntryWeight').do_event('<Return>',self.update_values)
            widget('EntryUniform').do_event('<Return>',self.update_values)
            widget('InsertUniform').do_command(self.take_over_uniform)
            
            widget('OK').do_command(self.update_and_close)
            
            self.transient(self.mycanvas.myRoot())
            widget('EntrySize').focus_set()

            # This is OK, because the canvas reference is sent
            do_receive('UPDATE_INDIVIDUAL_GRID',self.update_size,wishMessage=True)
            do_receive('TOPGRIDSHOW',self.top_grid_show,wishMessage=True)

            # Toplevels are close, if a grid is done, this is ok, because the toplevel is disturbing
            do_receive('DESTROY_INDIVIDUAL_GRID_TOPLEVEL',self.destroy)
            do_receive('UPDATE_INSERT_UNIFORM',self.update_widget_uniform)


            self.EntrySize = widget('EntrySize')
            self.EntryPad = widget('EntryPad')
            self.EntryWeight = widget('EntryWeight')
            self.EntryUniform = widget('EntryUniform')
            self.InsertUniform = widget('InsertUniform')

            setSelection(selection_before)
            self.update_widget_uniform()

        def update_widget_uniform(self):
            if self.mycanvas.master == container():
                self.InsertUniform.grid()
            else:
                self.InsertUniform.grid_remove()

        def take_over_uniform(self):
            uniform = self.EntryUniform.get().strip()
            if self.is_row:
                send('TAKE_OVER_UNIFORM_ROW',uniform)
            else:
                send('TAKE_OVER_UNIFORM_COL',uniform)

        def update_and_close(self):
            self.update_values()
            self.destroy()

        def update_size(self,message):
            if message[1] == self.mycanvas:
                self.EntrySize.delete(0,'end')
                self.EntrySize.insert(0,message[0])

        def top_grid_show(self,msg,showRowCol = widget('showRowCol'),EntrySize = widget('EntrySize'),EntryPad=widget('EntryPad'),EntryWeight=widget('EntryWeight'),UniForm = widget('uniform')):
            if msg[0] != self.mycanvas: return

            #row_col = msg[1] # not needed, because this will not be changed. When rows or columns are deleted or inserted the canvas and the toplevel will be destroyed
            config = msg[2]

            uniform = config['uniform']
            if not uniform:
                uniform = ''
          
            # showRowCol['text'] = str(row_col)  # not needed, because this will not be changed. When rows or columns are deleted or inserted the canvas and the toplevel will be destroyed
            for entry in ((self.EntrySize,config['minsize']),(self.EntryPad,config['pad']),(self.EntryWeight,config['weight']),(self.EntryUniform,uniform)):
                entry[0].delete(0,'end')
                #print(entry[1])
                entry[0].insert(0,entry[1])

        def update_values(self):

            grid_conf = self.grid_configure(self.row_col)


            try:
                minsize = int(self.EntrySize.get())
            except ValueError:
                minsize = grid_conf['minsize']
                self.EntrySize.delete(0,'end')
                self.EntrySize.insert(0,minsize)

            try:
                pad = int(self.EntryPad.get())
            except ValueError:
                pad = grid_conf['pad']
                self.EntryPad.delete(0,'end')
                self.EntryPad.insert(0,pad)
                
            try:
                weight = int(self.EntryWeight.get())
            except ValueError:
                weight = grid_conf['weight']
                self.EntryWeight.delete(0,'end')
                self.EntryWeight.insert(0,weight)

            uniform = self.EntryUniform.get().strip()

            if self.is_row:
                self.mycanvas.row_config_changed(self.row_col,{'minsize': minsize,'pad':pad,'weight':weight,'uniform': uniform})
            else:
                self.mycanvas.col_config_changed(self.row_col,{'minsize': minsize,'pad':pad,'weight':weight,'uniform': uniform})


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
        conf =  me.master.grid_multi_conf_rows[row][1]

        if me.master.grid_uni_row:
            if 'uniform' in conf and conf['uniform'] and conf['uniform'] == me.master.grid_uni_row:
                me['bg'] = color_uni_row
            else:
                me['bg'] = color_uni_col if me.master.grid_uni_col and 'uniform' in conf and conf['uniform']  and conf['uniform'] == me.master.grid_uni_col else bg
        else:
            if me.master.grid_uni_col and 'uniform' in conf and conf['uniform']  and conf['uniform'] == me.master.grid_uni_col:
                me['bg'] = color_uni_col
            else:
                me['bg'] = bg  if me.master.grid_multi_conf_rows[row][0] else orange

        me['highlightbackground'] = 'red' if me.master.grid_multi_conf_rows[row][0] and 'uniform' in conf and conf['uniform'] else bg


    def update_canvascolor_col(me,col,bg):

        conf =  me.master.grid_multi_conf_cols[col][1]

        if me.master.grid_uni_col:
            if 'uniform' in conf and conf['uniform']  and conf['uniform'] == me.master.grid_uni_col:
                me['bg'] = color_uni_col
            else:
                me['bg'] = color_uni_row if me.master.grid_uni_row and 'uniform' in conf and conf['uniform']  and conf['uniform'] == me.master.grid_uni_row else bg
        else:
            if me.master.grid_uni_row and 'uniform' in conf and conf['uniform']  and conf['uniform'] == me.master.grid_uni_row:
                me['bg'] = color_uni_row
            else:
                me['bg'] = bg  if me.master.grid_multi_conf_cols[col][0] else orange
        
        me['highlightbackground'] = 'red' if me.master.grid_multi_conf_cols[col][0] and 'uniform' in conf and conf['uniform'] else bg


    def update_col(me,column,grid_conf,bg):
        cont = me.master
        cont.grid_multi_conf_cols[column][1] = grid_conf
        cont.grid_columnconfigure(column,**grid_conf)

        if 'uniform' not in grid_conf or not grid_conf['uniform']:
            if grid_conf['minsize'] == cont.grid_conf_cols[1] and grid_conf['pad'] == cont.grid_conf_cols[2] and grid_conf['weight'] == cont.grid_conf_cols[3]:
                cont.grid_multi_conf_cols[column][0] = False
            else:
                cont.grid_multi_conf_cols[column][0] = True

        elif container().grid_uni_col == grid_conf['uniform'] or container().grid_uni_row == grid_conf['uniform']:
                cont.grid_multi_conf_cols[column][0] = True

                if container().grid_uni_row == grid_conf['uniform']:
                    update_rows_data(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])
                if container().grid_uni_col == grid_conf['uniform']:
                    update_cols_data(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])

                update_col_values()
                update_row_values()
        else:
            cont.grid_multi_conf_cols[column][0] = True
            update_col_values_uniform(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'],grid_conf['uniform'])                
            update_row_values_uniform(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'],grid_conf['uniform'])                

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

        elif container().grid_uni_row == grid_conf['uniform'] or container().grid_uni_col == grid_conf['uniform']:
                cont.grid_multi_conf_rows[row][0] = True

                if container().grid_uni_row == grid_conf['uniform']:
                    update_rows_data(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])
                if container().grid_uni_col == grid_conf['uniform']:
                    update_cols_data(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])

                update_col_values()
                update_row_values()

        else:
            cont.grid_multi_conf_rows[row][0] = True
            update_row_values_uniform(grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'],grid_conf['uniform'])                
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

    def button3_event_col(me,column):
        xpos = me.winfo_rootx()
        ypos = me.winfo_rooty() + 20
        GridTop(me,xpos,ypos,column,me.master.grid_columnconfigure,'Column',False)

    def button3_event_row(me,row):
        xpos = me.winfo_rootx() + 20
        ypos = me.winfo_rooty() - 100
        GridTop(me,xpos,ypos,row,me.master.grid_rowconfigure,'Row',True)

    def button1_grid_help(me):
        messagebox.showinfo("Individual Grid","By MouseWheel you change the 'size'.\nBy Button-3 (right mouse button) you may also change 'pad' and 'weight'.",parent=me.myRoot())

    def update_canvas_col_line(me):
        coords = coords = (3,9,me.winfo_width()-3,9)
        me.coords('line',*coords)
        
    def update_canvas_row_line(me):
        coords = coords = (9,3,9,me.winfo_height()-3)
        me.coords('line',*coords)

    def update_canvas_row_line_arrow(msg,me,row):
        if me.master == container() and msg[0] == row:
            me.itemconfig('line', arrowshape = '8 8 5' if msg[1] else '8 0 5')

    def update_canvas_col_line_arrow(msg,me,col):
        if me.master == container() and msg[0] == col:
            me.itemconfig('line', arrowshape = '8 8 5' if msg[1] else '8 0 5')

    def top_update_col(msg,me,col):
        if me.master == container() and msg[0] == col:
            send('TOPGRIDSHOW',(me,col,msg[1]))

    def top_update_row(msg,me,row):
        if me.master == container() and msg[0] == row:
            send('TOPGRIDSHOW',(me,row,msg[1]))

    class NonameCanvas(Canvas):

        def __init__(self,*args,**kwargs):
            Canvas.__init__(self,*args,**kwargs)
            self.orig_bg = self['bg']

        def col_config_changed(self,col,config,update_col = update_col):
            update_col(self,col,config,self.orig_bg)

        def row_config_changed(self,row,config,update_row = update_row):
            update_row(self,row,config,self.orig_bg)

    def check_update_canvascolor_col(me,col,bg):
        if me.master == container():
            update_canvascolor_col(me,col,bg)
            
    def check_update_canvascolor_row(me,col,bg):
        if me.master == container():
            update_canvascolor_row(me,col,bg)





    def create_NONAMECANVAS(rows,cols,gui_grid_container=container()):
        for row in range(rows):
            canvas_row = NonameCanvas(NONAMECANVAS,relief='raised',width=13,height=0,cursor='sizing',highlightthickness=2,bd=1)
            canvas_row.bg = canvas_row['bg']
            canvas_row['highlightbackground'] = canvas_row.bg
            canvas_row.rcgrid(row,cols+1,sticky='ns')
            item = canvas_row.create_line(4,4,4,4)
            canvas_row.itemconfig(item,fill = 'blue',arrow = 'both',width = '3.0',tags = 'line')

            if container().grid_special:
                for frame in container().dyntk_row_frames:
                    if int(frame.grid_info()['row']) == row+1:
                        frame.mycanvas = canvas_row
                        break

            
            do_event("<MouseWheel>", mouse_wheel_row,(row,this()['bg']),True,True)
            do_event("<Button-4>", mouse_wheel_row,(row,this()['bg']),True,True)
            do_event("<Button-5>", mouse_wheel_row,(row,this()['bg']),True,True)
            do_event("<Button-3>", button3_event_row,row,True)
            do_event("<Button-1>", button1_grid_help,wishWidget=True)
            do_event('<Configure>',update_canvas_row_line,wishWidget=True)

            goIn() # the owner shall be the canvas
            do_receive('ROW_WEIGHT',update_canvas_row_line_arrow,[this(),row],wishMessage=True)
            do_receive('TOP_UPDATE_ROW',top_update_row,[this(),row],wishMessage=True)
            #do_receive('ROW_CONFIG_CHANGED',row_config_changed,[this(),row,this()['bg']],wishMessage = True)
            do_receive('CANVAS_UPDATE_ROW',check_update_canvascolor_row,[this(),row,this()['bg']])
            goOut()
            send('ROW_WEIGHT',(row,container().grid_rowconfigure(row)['weight']))

            update_canvascolor_row(this(),row,this()['bg'])
        

        if container().grid_special:
            Button(NONAMECANVAS,padx = 0, pady = 0,image = gui_grid_container.help_image,command=show_help,cursor = 'question_arrow')
            rcgrid(rows+1,cols+1)

        for col in range(cols):
            canvas_col = NonameCanvas(NONAMECANVAS,relief='raised',width=0,height=13,cursor='sizing',highlightthickness=2,highlightbackground=orange,bd=1)
            canvas_col.rcgrid(rows+1,col,sticky='we')
            canvas_col.bg = canvas_col['bg']
            canvas_col['highlightbackground'] = canvas_col.bg
            item = canvas_col.create_line(4,4,4,4)
            canvas_col.itemconfig(item,fill = 'blue',arrow = 'both',width = '3.0',tags = 'line')
           
            if container().grid_special:
                for frame in container().dyntk_col_frames:
                    if int(frame.grid_info()['column']) == col+1:
                        frame.mycanvas = canvas_col
                        break

            do_event("<MouseWheel>", mouse_wheel_col,(col,this()['bg']),True,True)
            do_event("<Button-4>", mouse_wheel_col,(col,this()['bg']),True,True)
            do_event("<Button-5>", mouse_wheel_col,(col,this()['bg']),True,True)
            do_event("<Button-3>", button3_event_col,col,True)
            do_event("<Button-1>", button1_grid_help,wishWidget=True)
            do_event("<Button-1>", button1_grid_help,wishWidget=True)
            do_event('<Configure>',update_canvas_col_line,wishWidget=True)
            goIn() # the owner shall be the canvas
            do_receive('COL_WEIGHT',update_canvas_col_line_arrow,[this(),col],wishMessage=True)
            do_receive('TOP_UPDATE_COL',top_update_col,[this(),col],wishMessage=True)
            #do_receive('COL_CONFIG_CHANGED',col_config_changed,[this(),col,this()['bg']],wishMessage = True)
            do_receive('CANVAS_UPDATE_COL',check_update_canvascolor_col,[this(),col,this()['bg']])

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

        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
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

        if individ and withNONAME:
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
                if isinstance(this(),(LabelFrame,Frame,ttk.LabelFrame,ttk.Frame)): # and container().grid_special:
                    this().grid_columnconfigure(0,minsize=MIN_WIDTH)
                    this().grid_rowconfigure(0,minsize=MIN_HEIGHT)
                    this().grid_conf_rows = (1,MIN_HEIGHT,0,0)
                    this().grid_conf_cols = (1,MIN_WIDTH,0,0)
                    this().grid_multi_conf_rows = [[False,None]]
                    this().grid_multi_conf_cols = [[False,None]]
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


    def row_default(me = widget('uniform_row')):
        conf = container().grid_conf_rows
        uniform = container().grid_uni_row if container().grid_uni_row else ''
        if not uniform or not getattr(me,'grid_current_uniform', None):
            return { 'minsize' : conf[1], 'pad' : conf[2], 'weight' : conf[3], 'uniform' : uniform }
        else: 
            conf = me.grid_current_uniform
            return { 'minsize' : conf[0], 'pad' : conf[1], 'weight' : conf[2], 'uniform' : uniform }
       

    def col_default(me = widget('uniform_col')):
        conf = container().grid_conf_cols
        uniform = container().grid_uni_col if container().grid_uni_col else ''
        if not uniform or not getattr(me,'grid_current_uniform', None):
            return { 'minsize' : conf[1], 'pad' : conf[2], 'weight' : conf[3], 'uniform' : uniform }
        else: 
            conf = me.grid_current_uniform
            return { 'minsize' : conf[0], 'pad' : conf[1], 'weight' : conf[2], 'uniform' : uniform }

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
                    if configs[row][0] and 'uniform' in configs[row][1] and configs[row][1]['uniform'] == uniform:
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
                    if configs[col][0] and 'uniform' in configs[col][1] and configs[col][1]['uniform'] == uniform:
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
                    self.mycanvas.col_config_changed(self.row_col,self.row_col_config)
                else:
                    self.mycanvas.row_config_changed(self.row_col,self.row_col_config)
                    
     
            self.measure_size()
            if self.is_endline:
                if self.is_uniform:
                    self.new_cellsize = self.start_size + self.dpos//self.uniform_count
                else:
                    self.new_cellsize = self.start_size + self.dpos
            else:
                self.new_cellsize = self.start_size + self.start_begin - self.begin + self.dpos
     
            self.new_cellsize = max(self.new_cellsize,0)

            if self.is_uniform and self.is_endline:
                self.increase =  self.new_cellsize - self.cellsize
            else:
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
                        self.mycanvas.col_config_changed(self.row_col,self.row_col_config)
                    else:
                        self.mycanvas.row_config_changed(self.row_col,self.row_col_config)

                     
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

            send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
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
            insert_frame = self.insert_row_col(self.master,self.row_col)
     
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
            else:
                conf = list(self.master.grid_conf_rows)
                conf[0] += 1
                self.master.grid_conf_rows = tuple(conf)

                is_uni = True if self.master.grid_uni_row else False
                self.master.grid_multi_conf_rows.insert(self.row_col,[is_uni,self.row_col_default()])

                for frame in self.master.dyntk_col_frames:
                    frame.grid(row = 0,rowspan = self.master.grid_conf_rows[0])
                insert_frame.tableline_mark_row()

            setSelection(selection_before)
            create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
            special_noname_frame()            
            setSelection(selection_before)
            send('GRID_COLS_CHANGED' if self.is_col else 'GRID_ROWS_CHANGED')
            set_col_width()
            set_row_height()

           

        def delete(self,event = None):
            selection_before = Selection()

            endpos = self.master.grid_conf_cols[0] if self.is_col else self.master.grid_conf_rows[0]
     
            # don't delete anything, if it's the last line
            if self.row_col == endpos:
                return
     
            # check whether it's the first line or column and whether there is only one line or column
            if self.row_col == 0 and endpos == 1:
                return

            send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
            deleteWidgetsForName(self.master,NONAMECANVAS)
            deleteWidgetsForName(self.master,NONAME)

            # check whether the current row or column is empty

            children = self.master.grid_slaves()
            elements = [ element for element in children if int(element.grid_info()[self.grid_key]) == self.row_col and element not in self.master.dyntk_table_frames]
     
            # if row or column isn't empty create the noname canvasses and the noname frame again and finished
            if elements:
                create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
                special_noname_frame()
                setSelection(selection_before)
                return
     
            # ok we have an empty row or column, which isn't the first one
            if self.is_col:
                # so we first destroy the line frame of this column or line
                for frame in self.master.dyntk_col_frames:
                    # if it's the line or colframe for this row or column
                    if int(frame.grid_info()[self.grid_key]) == self.row_col + 1:
                        # we pop it from dyntk_col_frames
                        self.master.dyntk_col_frames.pop(self.master.dyntk_col_frames.index(frame))
                        # we pop it also from dyntk_table_frames and destroy it
                        self.master.dyntk_table_frames.pop(self.master.dyntk_table_frames.index(frame)).destroy()
                        break

                # now we decrease the number of columns in grid_conf_cols
                conf = list(self.master.grid_conf_cols)
                conf[0] -= 1
                self.master.grid_conf_cols = tuple(conf)

                # and pop the entry from grid_multi_conf_cols
                self.master.grid_multi_conf_cols.pop(self.row_col)

                # now we decrease the columnspan for horizontal line frames
                for frame in self.master.dyntk_row_frames:
                    frame.grid(column = 0, columnspan = self.master.grid_conf_cols[0])

                # what's this ??? It was the former master.grid_conf_cols[0]+1, means the space of the canvas
                #self.master.grid_columnconfigure(self.master.grid_conf_cols[0]+2,minsize=0,pad=0,weight=0)

                # I think, it should be this, but it isn't needed, because it will be done later
                #self.master.grid_columnconfigure(self.master.grid_conf_cols[0],minsize=0,pad=0,weight=0)
                

     
            else:
                for frame in self.master.dyntk_row_frames:
                    if int(frame.grid_info()[self.grid_key]) == self.row_col + 1:
                        self.master.dyntk_row_frames.pop(self.master.dyntk_row_frames.index(frame))
                        self.master.dyntk_table_frames.pop(self.master.dyntk_table_frames.index(frame)).destroy()
                        break
     
                conf = list(self.master.grid_conf_rows)
                conf[0] -= 1
                self.master.grid_conf_rows = tuple(conf)
                self.master.grid_multi_conf_rows.pop(self.row_col)


                for frame in self.master.dyntk_col_frames:
                    frame.grid(row = 0,rowspan = self.master.grid_conf_rows[0])
                # I think, it should be this
                #self.master.grid_rowconfigure(self.master.grid_conf_rows[0],minsize=0,pad=0,weight=0)
     

     
            #so we move the widgets one row or colum down

            children = self.master.grid_slaves()
            for pos in range(self.row_col,endpos):
                for child in children:
                    if int(child.grid_info()[self.grid_key]) == pos+1:
                        child.grid(**{ self.grid_key : pos })
                self.grid_configure(pos,**self.grid_configure(pos+1))
            # endpos ist the former rows or columns, means the place of the end line

            self.grid_configure(endpos-1,minsize = 0, pad = 0, weight = 0,uniform='')
            setSelection(selection_before)
            create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
            special_noname_frame()
            setSelection(selection_before)
            send('GRID_COLS_CHANGED' if self.is_col else 'GRID_ROWS_CHANGED')
            set_col_width()
            set_row_height()

            

    def insert_col(self,col):
        frame = LineFrame(self,is_col = True)
        frame.insert_col = insert_col
        frame.insert_row_col = insert_col
        frame.grid(column = col,row = 0, rowspan = self.grid_conf_rows[0]+1, sticky = 'nsw')
        frame.bind_enter()
        self.dyntk_table_frames.append(frame)
        self.dyntk_col_frames.append(frame)
        return frame
 
 
    def insert_row(self,row):
        frame = LineFrame(self,is_col = False)
        frame.grid(row = row, column = 0, columnspan = self.grid_conf_cols[0]+1, sticky = 'wen')
        frame.insert_row_col = insert_row
        frame.bind_enter()
        self.dyntk_table_frames.append(frame)
        self.dyntk_row_frames.append(frame)
        return frame
 
    def insert_table(self):
        for col in range(self.grid_conf_cols[0]+1):
            insert_col(self,col)
        for row in range(self.grid_conf_rows[0]+1):
            insert_row(self,row)
 

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

            create_NONAMECANVAS(rows,cols)

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
                

                individual['state'] = 'normal'
                Cols['state'] = 'normal'
                Rows['state'] = 'normal'

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

                update_special_button()
                send('UPDATE_INSERT_UNIFORM')

    do_receive("SELECTION_CHANGED",update_grid_table_on_enter)


    widget('special').is_on = False
    widget('special').do_command(special_toggle)

main()


### ========================================================
