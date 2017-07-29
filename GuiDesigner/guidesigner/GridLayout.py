config(**{'minsize': '116 1', 'maxsize': '1920 1058', 'grid_rows': '(8, 0, 0, 0)', 'grid_multi_cols': '[7, (2, 0, 0, 0), (5, 0, 0, 0), (6, 0, 0, 1)]', 'grid_cols': '(7, 45, 0, 0)'})

ttk.Separator('separator').grid(row=5, columnspan=5, sticky='ew')
Entry('uniform_row',**{'bg': '#e0ffb0', 'width': 0}).grid(row=7, columnspan=2, sticky='nesw')
Entry('uniform_col',**{'bg': '#fff0b0', 'width': 0}).grid(column=3, row=7, columnspan=2, sticky='nesw')
ttk.Label('luniformrow',**{'text': 'uniform (row)'}).grid(row=6, columnspan=2, sticky='w')
Label('luniformcol',**{'text': 'uniform (column)'}).grid(column=3, row=6, columnspan=2, sticky='w')
ttk.Separator('separator',**{'orient': 'vertical'}).grid(column=2, row=1, rowspan=7, sticky='ns')
Label('lpad',**{'text': 'pad'}).grid(row=2, sticky='e')
Label('lweight',**{'text': 'weight'}).grid(row=3, sticky='e')
Label('lheight',**{'text': 'minsize'}).grid(row=1, sticky='e')
Label('lrows',**{'font': 'TkDefaultFont 9 bold', 'text': 'Rows'}).grid(row=4, sticky='nesw')
Entry('EntryRows',**{'bg': '#ffffd4', 'width': 6}).grid(column=1, row=4, sticky='nesw')
Entry('EntryCols',**{'bg': '#ffffd4', 'width': 5}).grid(column=3, row=4, sticky='nesw')
Label('lcols',**{'font': 'TkDefaultFont 9 bold', 'text': 'Columns'}).grid(column=4, row=4, sticky='nesw')
Button('special',**{'bd': 2, 'cursor': 'star', 'text': 'special', 'photoimage': 'guidesigner/images/insert_table_row.gif'}).grid(column=4, row=2, rowspan=2)
Label('LableTitle',**{'bd': '3', 'fg': 'blue', 'font': 'TkDefaultFont 9 bold', 'relief': 'ridge', 'text': 'grid'}).grid(row=0, sticky='nesw')
Spinbox('EntryRowHeight',**{'to': 1000.0, 'width': 4}).grid(column=1, row=1, sticky='nesw')
Spinbox('EntryColWidth',**{'to': 1000.0, 'width': 4}).grid(column=3, row=1, sticky='nesw')
Spinbox('EntryRowPad',**{'to': 1000.0, 'width': 4}).grid(column=1, row=2, sticky='nesw')
Spinbox('EntryColPad',**{'to': 1000.0, 'width': 4}).grid(column=3, row=2, sticky='nesw')
Spinbox('EntryRowWeight',**{'to': 1000.0, 'width': 4}).grid(column=1, row=3, sticky='nesw')
Spinbox('EntryColWeight',**{'to': 1000.0, 'width': 4}).grid(column=3, row=3, sticky='nesw')
Checkbutton('Individual',**{'highlightthickness': '2', 'text': 'indiv.'}).grid(column=4, row=1, sticky='ew')
Label('ButtonShow',**{'bd': '3', 'bg': 'lightgreen', 'relief': 'raised', 'text': 'Show'}).grid(column=4, row=0, sticky='nesw')
Button('sticky',**{'relief': 'flat', 'text': 'sticky', 'photoimage': 'guidesigner/images/sticky.gif'}).grid(column=5, row=0, sticky='w')
ttk.Separator('separator',**{'orient': 'vertical'}).grid(column=5, row=0, rowspan=8, sticky='nsw')
Button('grid',**{'bd': '3', 'bg': 'lightgreen', 'text': 'grid'}).grid(column=1, row=0, sticky='nesw')
Button('grid0',**{'bd': '3', 'bg': 'lightgreen', 'text': 'grid 0'}).grid(column=2, row=0, columnspan=2, sticky='nesw')

### CODE ===================================================

def main():

    # ==================================
    # Variables:
    # ===================================

    # Widgets =======================
    
    widget_Button_Grid0 = widget('grid0')
    widget_Button_Grid = widget('grid')
    widget_Button_Show = widget('ButtonShow')
    widget_Button_Sticky = widget('sticky')
    widget_Checkbutton_Individual = widget('Individual')
    widget_Button_Special = widget('special')

    widget_Entry_Rows = widget('EntryRows')
    widget_Entry_Cols = widget('EntryCols')
    widget_Spinbox_ColWidth = widget('EntryColWidth')
    widget_Spinbox_RowHeight = widget('EntryRowHeight')
    widget_Spinbox_ColPad = widget('EntryColPad')
    widget_Spinbox_RowPad = widget('EntryRowPad')
    widget_Spinbox_RowWeight = widget('EntryRowWeight')
    widget_Spinbox_ColWeight = widget('EntryColWeight')
    widget_Entry_UniformCol = widget('uniform_col')
    widget_Entry_UniformRow = widget('uniform_row')

    # init toggle buttons
    widget_Button_Special.is_on = False
    widget_Button_Show.is_on = False

    # init checkbutton Individual =====
    IndividualVar =  IntVar()
    widget_Checkbutton_Individual.config(variable = IndividualVar, onvalue = 1, offvalue = 0)
    widget_Checkbutton_Individual.mydata=IndividualVar

    
    # images =========================
    insert_uniform_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/insert-text.gif')
    container().help_image = StatTkInter.PhotoImage(file = 'guidesigner/images/help16.gif')

    # colors =======
    orange = '#f0f080'
    color_uni_col = '#fff0b0'
    color_uni_row = '#e0ffb0'
    indiv_hilibg = widget_Checkbutton_Individual['highlightbackground']
    indiv_selcolor = widget_Checkbutton_Individual['selectcolor']

    # configuration for NONAME frames
    fill_cell = {'height': '0', 'width': '0','relief': 'solid','bd':'1','bg':'#b3d9d9','padx':0,'pady':0}
    fill_cell2 = {'height': '0', 'width': '0','relief': 'flat','bd':'0','bg':'#b3d9d9','padx':0,'pady':0}


    # Start initialisation
    MIN_HEIGHT = 40
    MIN_WIDTH = 40

    start_default_row_values = (0,MIN_HEIGHT,0,0)
    start_default_col_values = (0,MIN_WIDTH,0,0)


    # ==================================
    # Startvalues
    # ===================================

    # for each GuiElement the following initialisation is done during reset_grid
    #    self.grid_conf_rows = None
    #    self.grid_conf_cols = None
    #    self.grid_multi_conf_cols = []
    #    self.grid_multi_conf_rows = []
    #    self.grid_uni_row = ''
    #    self.grid_uni_col = ''

    # when the selection changes,update_grid_table_on_enter is called
    #    do_receive("SELECTION_CHANGED",update_grid_table_on_enter)
    #
    # update_grid_table_on_enter does the following
    #   if grid_conf_rows and/or grid_conf_cols already exists, then it's fine
    #   otherwise the function tries to get the values by definitions by tkinter application - get_gridconfig
    #   if no success, these start values are used: start_default_row_values, start_default_col_values


    # ====================================
    # changing values minsize,pad, weight
    # ====================================

    # changing may be done by the
    # - spinbox fields in the grid imput mask
    # - spinbox fields in the toplevels
    # - by mouse wheel on canvasses
    # - by moving the table lines
    # mouse wheel and table lines affect only the minsizes

    # ====================================
    # grid_uni_col and grid_uni_row
    # ====================================
    # if there exists a grid_uni_col and/or a grid_uni_row, then there has also to be updated:
    # - grid_current_uniform_col and or grid_current_uniform_row
    # if changes are made for these uniforms

    # changes by mouse wheel


    # ==================================
    # Functions:
    # ===================================


        

        # -------------------------------------------
        # Functions for highlight and mouse move
        # -------------------------------------------

        #   def mouse_move(me,wi_row=widget('Row'),wi_col=widget('Col')):

        #   def after_mouse_up(me):
        #   def on_mouse_up(me):
        #   def on_app_mouse_up(me,app_id=apprelease_id_list):
        #   def on_mouse_down(me,event,app_id=apprelease_id_list):
        #   def do_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        #   def grid_mouse_on(me,mouse_down = on_mouse_down, mouse_up = on_mouse_up):

        

        # -------------------------------------------
        # Functions which read minsize, pad, weight and set values if an exception occurs
        # -------------------------------------------
        #   def get_row_values():
        #   def get_col_values():
        #   def set_grid_conf_rows():
        #   def set_grid_conf_cols():

        # -------------------------------------------
        # Functions which set minsize, pad, weight
        # -------------------------------------------
        #   def update_rows_data(size,pad,weight):
        #   def update_cols_data(size,pad,weight):
        #   update_grid_table_on_enter(set_row_height=set_row_height,set_col_width=set_col_width)
    
        # -------------------------------------------
        # Functions which set also uniform
        # -------------------------------------------

        # -------------------------------
        #   def fill_general_multirows(cont)
        #   def configure_rows(cont)
        #   def rowupdate_canvas_top(cont)
        #   def rowconfigure_andcanvas_andtop(cont)
        #   def set_row_height()

        # -------------------------------
        #   def fill_general_multicols(cont)
        #   def configure_columns(cont)
        #   def colupdate_canvas_top(cont)
        #   def colconfigure_andcanvas_andtop(cont)
        #   def set_col_width()


    # show_help()
    # def update_rows_data(size,pad,weight):
    # def update_rows_data_uniform(uniform,config):
    # def update_cols_data_uniform(uniform,config):
    # def update_general_rows():
    # def update_cols_data(size,pad,weight):
    # def update_general_cols():
    # def update_general_grid():
    # def update_uni_row():
    # def update_uni_col():
    # def take_over_uniform_row(cont,uniform,config):
    # def take_over_uniform_col(cont,uniform,config):
    # def do_bg_title(title = widget('LableTitle'),titlebg = widget('LableTitle')["bg"]):
    # def grid_cols_changed():
    # def grid_rows_changed():
    # def hide_grid():
    # def do_grid_forget():
    # def set_grid_conf_rows():
    # def set_grid_conf_cols():
    # def update_col_values():
    # def update_row_values():
    # def check_col_values():
    # def check_row_values():
    # def update_individual(cont,hili_bg = indiv_hilibg[0]):
    # def update_individual_mark(cont):
    # def update_canvascolor_row(me,row,bg):
    # def update_canvascolor_col(me,col,bg):
    # def update_col(me,column,grid_conf,bg):
    # def take_over_uniform_row(cont,uniform,config):
    # def update_row(me,row,grid_conf,bg):
    # def mouse_wheel_row(me,event,row,bg):
    # def mouse_wheel_col(me,event,column,bg):
    # def button3_event_col(me,column):
    # def button3_event_row(me,row):
    # def button1_grid_help(me):
    # def update_canvas_col_line(me):
    # def update_canvas_row_line(me):
    # def update_canvas_row_line_arrow(msg,me,row):
    # def update_canvas_col_line_arrow(msg,me,col):
    # def top_update_col(msg,me,col):
    # def top_update_row(msg,me,row):
    # def check_update_canvascolor_col(me,col,bg):
    # def check_update_canvascolor_row(me,col,bg):
    # def create_NONAMECANVAS(rows,cols,gui_grid_container=container()):
    # def show_grid(event=None,withNONAME = True,set_col_width=set_col_width,set_row_height=set_row_height):
    # def update_indiv_wish():
    # def press_button_show(event=None):
    # def update_button_show(event=None):
    # def animate_button_show(event=None):
    # def entry_show_grid(event=None):
    # def update_after_pack(show_grid = show_grid):
    # def do_grid_col_row(col,row,do_mouse_on=do_mouse_on):
    # def mouse_do_grid_NONAME(me):
    # def mouse_do_grid(me):
    # def special_noname_frame():
    # def NONAME_destroy(a):
    # def do_grid():
    # def do_grid0():
    # def row_default(container):
    # def col_default(container):
    # def insert_col(self,col):
    # def insert_row(self,row):
    # def insert_table(self):
    # def special_toggle():
    # def update_special_button():

    # def update_grid_table_on_enter(
    #   set_row_height=set_row_height,set_col_width=set_col_width):




    # ==================================
    # Classes and methods
    # ===================================

    # class GridTop(Toplevel):
    #     def __init__(self,master,x,y,row_col,grid_configure,item_text,is_row):
    #     def update_widget_uniform(self):
    #     def take_over_uniform(self):
    #     def update_and_close(self):
    #     def update_size(self,message):
    #     def top_grid_show(self,msg,showRowCol = widget('showRowCol'),EntrySize = widget('EntrySize'),EntryPad=widget('EntryPad'),EntryWeight=widget('EntryWeight'),UniForm = widget('uniform')):
    #     def update_values(self):

    # class NonameCanvas(Canvas):
    #    def __init__(self,*args,**kwargs):
    #    def col_config_changed(self,col,config,update_col = update_col):
    #    def row_config_changed(self,row,config,update_row = update_row):

    # class LineFrame(Frame):
    #    def __init__(self,master,**kwargs):
    #    def tableline_leave(self,event=None):
    #    def tableline_startmove_col(self,event = None):
    #    def measure_colwidth(self):
    #    def measure_rowheight(self):
    #    def set_size(self):
    #    def move(self):
    #    def move_release(self,event = None):
    #    def tableline_mark_end(self,event = None):
    #    def tableline_mark_col(self,event = None):
    #    def tableline_mark_row(self,event = None):
    #    def bind_enter(self):
    #    def tableline_enter_col(self,event=None):
    #    def tableline_enter_row(self,event=None):
    #    def tableline_enter_insert_col(self,event=None):
    #    def tableline_enter_insert_row(self,event=None):
    #    def insert(self,event = None):
    #    def delete(self,event = None):

    #widget('help_button')['command'] = show_help


    # -------------------------------------------
    # Functions for highlight and mouse move
    # -------------------------------------------


    # data for mouse move are initialized also in:

    # - BaseLayout.py

    #  and in introduction:

    # - BaseLayoutGrid.py
    # - BaseLayoutPlace.py
    # - BaseLayoutPack.py
    # - BaseLayoutMenus.py


    # -------------------------------------------
    # message MOUSE_SELECT_ON
    # -------------------------------------------

    # is sent by:
    # - TopMenu.py
    # - introduction/mousemenu.py


    # is received by:
    # - BaseLayout.py

    # -------------------------------------------
    # message UPDATE_MOUSE_SELECT_ON
    # -------------------------------------------

    # is sent by:
    # - PackLayout.py
    # - PageAddFrame.py

    # is received by:
    # - BaseLayout.py

    # -------------------------------------------
    # message UPDATE_CANVAS_MOUSE_SELECT_ON
    # -------------------------------------------

    # is sent by:
    # - CanvasPaint.py
    
    # is received by:
    # - BaseLayout.py
    

    # -------------------------------------------
    # BaseLayout.py sends the following messages
    # -------------------------------------------
    # - GRID_MOUSE_ON
    # - PLACE_MOUSE_ON



    # -------------------------------------------
    # the following list is used:
    # -------------------------------------------

    # wi.mydata = [0,0,0,0,0,0,False,False] in BaseLayout.py
    # me.mydata=[0,0,'mouse',0,0,0,True,False] # PlaceLayout.py
    # me.mydata=[0,0,'mouse',0,0,0,True,False,0,0] # GridLayout.py


    # -------------------------------------------
    # these lists have to be replaced by an object of a class
    # -------------------------------------------
    # so what's the purpose?

    # in BaseLayout.py

    #   mydata[0] - 'hili_on' or None
    #   mydata[1] - backup of the relief
    #   mydata[2] - backup of the highlightthickness
    #   mydata[3] - backup of the highlightbackground


    # in PlaceLayout.py

    # mydata[0]: event.x
    # mydata[1]: event.y
    # mydata[2]: 'mouse'
    # mydata[3]: xpos - the current x position for place()
    # mydata[4]: xpos - the current y position for place()
    # mydata[5]: a counter for incrementing an after reaching the value 100 sending POSITION_CHANGED and LAYOUT_VALUES_REFRESH
    # mydata[6]: a flag for running or stopping the mouse move
    # mydata[7]: a flag that another widget was selected for sending different messages when the move ends
    
    # in GridLayout.py additionally

    # mydata[8]: width when moving via place layout
    # mydata[9]: height when moving via place layout

    # apprelease_id_list for unbinding the move from the root



    # and there is also a UPDATE_CANVAS_MOUSE_SELECT_ON




    # -------------------------------------------
    # so let's start
    # -------------------------------------------



    # -------------- Mouse move button commands and mouse events ----------------------------------


    class DynTk_HighLight:

        def __init__(self,me):
            self.me = me
            dyntk_highlight(me)

            self.selection_changed = False
            if this() != self.me:
                self.selection_changed = True
                setWidgetSelection(self.me)
                send('SHOW_LAYOUT',(None,False))
                send('SHOW_CONFIG',(None,False))
                send('SELECTION_CHANGED')

        def restore(self):
            dyntk_unhighlight(self.me)
            if self.selection_changed:
                send('SHOW_LAYOUT',(None,True))
                send('SHOW_CONFIG',(None,True))
                send('SELECTION_CHANGED')
            else:
                send('POSITION_CHANGED',self.me)
                send('LAYOUT_VALUES_REFRESH',self.me)
            
    class DynTk_MouseMove:

        def __init__(self,me):
            self.me = me
            self.diffx = self.me.winfo_pointerx() - self.me.winfo_rootx()
            self.diffy = self.me.winfo_pointery() - self.me.winfo_rooty()
            self.width = me.winfo_width()
            self.height = me.winfo_height()

            self.left = me.master.winfo_rootx()
            self.top = me.master.winfo_rooty()
            
            self.right = self.left + me.master.winfo_width() -1
            self.bottom = self.top + me.master.winfo_height() -1
            self.check_steps = 0
            self.last_x,self.last_y = me.master.winfo_pointerxy()

            self.dyntk_start_frame = Frame((self.me.master,NONAME_MOVE))
            self.dyntk_start_frame.yxplace(0,0)
                                     
            self.selection_changed = False
            self.step = 0
            self.is_moving=False
            self.started = False

        def end(self):
            selection_before = Selection()
            self.dyntk_start_frame.destroy()
            setSelection(selection_before)

        def start_move(self,event=None):
            if self.me.master.grid_conf_cols and self.me.master.grid_conf_cols[0] and self.me.master.grid_conf_rows and self.me.master.grid_conf_rows[0]:
                self.started = True
                if not self.is_moving:
                    self.me.unbind('<B1-Motion>')
                    dyntk_unhighlight(self.me)
                    for frame in self.me.master.dyntk_table_frames:
                        frame.unbind_enter()

                    self.me.lift()
                    send('BASEMENTLEVEL_CHANGED')
                    if this() != self.me:
                        self.selection_changed = True
                self.is_moving = True
                self.me.Layout = PLACELAYOUT
                self.me.after(10,self.move)

        def stop_move(self):

            if self.is_moving:
                self.is_moving = False

            (col,row) = self.me.master.grid_location(self.me.winfo_rootx()-self.me.master.winfo_rootx(),self.me.winfo_rooty()-self.me.master.winfo_rooty())
            if col < 0: col = 0
            if row < 0: row = 0
            if col >= self.me.master.grid_conf_cols[0]:
                col = self.me.master.grid_conf_cols[0] -1
            if row >= self.me.master.grid_conf_rows[0]:
                row = self.me.master.grid_conf_rows[0] -1

            self.me.rcgrid(row,col)
            self.me.dyntk_lift()
            for frame in self.me.master.dyntk_table_frames:
                frame.bind_enter()


        def move(self):
            if self.is_moving and widget_exists(self.me) and self.me.Layout == PLACELAYOUT:

                (col,row) = (self.me.master.grid_location(self.me.winfo_rootx()-self.me.master.winfo_rootx(),self.me.winfo_rooty()-self.me.master.winfo_rooty()))
                if col < 0 or row < 0:
                    highlight_mouse_up(self.me)
                    return

                # mouse outside of container doesn't react on mouse up
                if self.me.master.winfo_pointerx() >= self.me.master.winfo_rootx()+self.me.master.winfo_width() or self.me.master.winfo_pointery() >= self.me.master.winfo_rooty()+self.me.master.winfo_height():
                    highlight_mouse_up(self.me)
                    return

                xpos = self.me.winfo_pointerx() - self.dyntk_start_frame.winfo_rootx() - self.diffx
                ypos = self.me.winfo_pointery() - self.dyntk_start_frame.winfo_rooty() - self.diffy

                self.me.yxplace(ypos,xpos,width=self.width,height=self.height)
                self.me.after(10,self.move)

    # we bind events to the widget - better not additional first, so nothing may happen with additional unexpected messages

    def grid_mouse_on(me):
        me.do_event('<Button-1>',highlight_widget,wishWidget=True)

    def highlight_widget(me):
        attr = getattr(me, 'dyntk_highlight', None)
        if attr:
            me.dyntk_highlight.restore()
            
        me.dyntk_highlight = DynTk_HighLight(me)
        me.dyntk_mousemove = DynTk_MouseMove(me)
        me.do_event('<B1-Motion>',me.dyntk_mousemove.start_move)
        me.do_event('<ButtonRelease-1>',highlight_mouse_up,wishWidget=True)

    def highlight_mouse_up(me):
        if  me.dyntk_highlight:
            me.dyntk_mousemove.is_moving = False
            me.unbind('<B1-Motion>')
            me.unbind('<ButtonRelease-1>')
            if me.dyntk_mousemove.started:
                me.dyntk_mousemove.stop_move()
            me.dyntk_mousemove.end()
            me.dyntk_highlight.restore() # last, because of grid now instead of place
            me.dyntk_highlight = None
            me.dyntk_mousemove = None


    do_receive('GRID_MOUSE_ON',grid_mouse_on,wishMessage=True)

    widget_Button_Sticky.do_command(lambda me = widget_Button_Sticky, root = widget('/','GuiFrame'): send('SELECT_STICKY',(
        me.winfo_rootx() - root.winfo_rootx()+me.winfo_width(),
        me.winfo_rooty() - root.winfo_rooty(),
        this()
        )))

    def show_help():
        messagebox.showinfo("Move, Delete and Insert Lines and Columns","You may move the lines by mouse. After mouse button click, when the line becomes blue, you may insert and delete rows or columns by pressing the [Insert] or [Delete] key.",parent=container())
        '''
        try:
            webbrowser.open('https://github.com/AlfonsMittelmeyer/python-gui-messaging/wiki')
        except: pass
        '''

    def update_rows_data(size,pad,weight):
        widget_Spinbox_RowHeight.delete(0,'end')
        widget_Spinbox_RowHeight.insert(0,size)
        widget_Spinbox_RowPad.delete(0,'end')
        widget_Spinbox_RowPad.insert(0,pad)
        widget_Spinbox_RowWeight.delete(0,'end')
        widget_Spinbox_RowWeight.insert(0,weight)

    def update_rows_data_uniform(uniform,config):
        widget_Entry_UniformRow.delete(0,'end')
        widget_Entry_UniformRow.insert(0,uniform)
        update_rows_data(*config)

    def update_cols_data_uniform(uniform,config):
        widget_Entry_UniformCol.delete(0,'end')
        widget_Entry_UniformCol.insert(0,uniform)
        update_cols_data(*config)

    def update_general_rows():
        update_rows_data(container().grid_conf_rows[1],container().grid_conf_rows[2],container().grid_conf_rows[3])

    def update_cols_data(size,pad,weight):
        widget_Spinbox_ColWidth.delete(0,'end')
        widget_Spinbox_ColWidth.insert(0,size)
        widget_Spinbox_ColPad.delete(0,'end')
        widget_Spinbox_ColPad.insert(0,pad)
        widget_Spinbox_ColWeight.delete(0,'end')
        widget_Spinbox_ColWeight.insert(0,weight)

    def update_general_cols():
        update_cols_data(container().grid_conf_cols[1],container().grid_conf_cols[2],container().grid_conf_cols[3])

    def update_general_grid():

        widget_Entry_Rows.delete(0,'end')
        widget_Entry_Rows.insert(0,container().grid_conf_rows[0])
        update_general_rows()
        
        widget_Entry_Cols.delete(0,'end')
        widget_Entry_Cols.insert(0,container().grid_conf_cols[0])
        update_general_cols()


    def get_row_values():

        default = row_default(container())
        try:
            minsize = int(widget_Spinbox_RowHeight.get())
        except ValueError:
            minsize = default['minsize']

        try:
            padvalue = int(widget_Spinbox_RowPad.get())
        except ValueError:
            padvalue = default['pad']

        try:
            weightvalue = int(widget_Spinbox_RowWeight.get())
        except ValueError:
            weightvalue = default['weight']

        update_rows_data(minsize,padvalue,weightvalue)

        return minsize, padvalue, weightvalue
    


    def get_col_values():

        default = col_default(container())
        try:
            minsize = int(widget_Spinbox_ColWidth.get())
        except ValueError:
            minsize = default['minsize']

        try:
            padvalue = int(widget_Spinbox_ColPad.get())
        except ValueError:
            padvalue = default['pad']

        try:
            weightvalue = int(widget_Spinbox_ColWeight.get())
        except ValueError:
            weightvalue = default['weight']

        update_cols_data(minsize,padvalue,weightvalue)

        return minsize, padvalue, weightvalue


    # update input fields
    def update_uni_row_uniform(uniform):
        if uniform:
            found = False
            if container().grid_multi_conf_rows:
                for conf in container().grid_multi_conf_rows:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        # look for first uniform entry if it exists and update the value of the grid layout row input
                        container().grid_current_uniform_row = [conf[1]['minsize'],conf[1]['pad'],conf[1]['weight']]
                        update_rows_data(*container().grid_current_uniform_row)
                        found = True
                        break

            if not found and container().grid_multi_conf_cols:
                for conf in container().grid_multi_conf_cols:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        container().grid_current_uniform_row = [conf[1]['minsize'],conf[1]['pad'],conf[1]['weight']]
                        update_rows_data(*container().grid_current_uniform_row)
                        found is True
                        break

            if not found and container().grid_uni_col == uniform:
                container().grid_current_uniform_row = container().grid_current_uniform_col
                update_rows_data(*container().grid_current_uniform_row)
                found = True

            if not found:
                minsize,pad,weight = get_row_values()
                container().grid_current_uniform_row = [minsize,pad,weight]

        else:
            # if the uniform entry was emptied, take over general row entries
            #if container().grid_conf_rows and container().grid_conf_rows[0]:
            if container().grid_conf_rows:
                update_general_rows()




    def update_uni_col_uniform(uniform):
        if uniform:
            found = False
            if container().grid_multi_conf_cols:
                for conf in container().grid_multi_conf_cols:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        container().grid_current_uniform_col = [conf[1]['minsize'],conf[1]['pad'],conf[1]['weight']]
                        update_cols_data(*container().grid_current_uniform_col)
                        found is True
                        break
                    
            if not found and container().grid_multi_conf_rows:
                for conf in container().grid_multi_conf_rows:
                    if conf[0] and 'uniform' in conf[1] and conf[1]['uniform'] and conf[1]['uniform'] == uniform:
                        # look for first uniform entry if it exists and update the value of the grid layout column input
                        container().grid_current_uniform_col = [conf[1]['minsize'],conf[1]['pad'],conf[1]['weight']]
                        update_cols_data(*container().grid_current_uniform_col)
                        found = True
                        break

            if not found and container().grid_uni_row == uniform:
                container().grid_current_uniform_col = container().grid_current_uniform_row
                update_cols_data(*container().grid_current_uniform_col)
                found = True
                
            if not found:
                minsize,pad,weight = get_col_values()
                container().grid_current_uniform_col = [minsize,pad,weight]
        else:
            #if container().grid_conf_cols and container().grid_conf_cols[0]:
            if container().grid_conf_cols:
                update_general_cols()

    # update input fields
    def update_uni_col():
        uniform = widget_Entry_UniformCol.get().strip()
        update_uni_col_uniform(uniform)
        container().grid_uni_col = uniform
        send('CANVAS_UPDATE_ROW') # color update für canvasses for container()
        send('CANVAS_UPDATE_COL') # color update für canvasses for container()

    # update input fields
    def update_uni_row():
        uniform = widget_Entry_UniformRow.get().strip()
        update_uni_row_uniform(uniform)
        container().grid_uni_row = uniform 
        send('CANVAS_UPDATE_ROW') # update für canvasses
        send('CANVAS_UPDATE_COL') # update für canvasses

    def take_over_uniform_col(uniform):
        container().grid_uni_col = uniform
        widget_Entry_UniformCol.delete(0,'end')
        widget_Entry_UniformCol.insert(0,uniform)
        send('CANVAS_UPDATE_ROW') # color update für canvasses for container()
        send('CANVAS_UPDATE_COL') # color update für canvasses for container()


    def take_over_uniform_row(uniform):
        container().grid_uni_row = uniform
        widget_Entry_UniformRow.delete(0,'end')
        widget_Entry_UniformRow.insert(0,uniform)
        send('CANVAS_UPDATE_ROW') # color update für canvasses for container()
        send('CANVAS_UPDATE_COL') # color update für canvasses for container()
            

    widget_Entry_UniformCol.do_event('<Key>',container().after,[1,update_uni_col])
    widget_Entry_UniformRow.do_event('<Key>',container().after,[1,update_uni_row])

    # -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------

    # set the bg color of the GridTitle label to yellow, if the current widget has a GRIDLAYOUT, otherwise to original color

    def do_bg_title(title = widget('LableTitle'),titlebg = widget('LableTitle')["bg"]):
        if this().Layout == GRIDLAYOUT:
            title['bg'] = "yellow"
            if widget_exists(widget_Button_Sticky):
                widget_Button_Sticky.grid()
        else:
            title['bg'] = titlebg
            if widget_exists(widget_Button_Sticky):
                widget_Button_Sticky.grid_remove()

    do_receive('BASE_LAYOUT_REFRESH',do_bg_title)


    def grid_cols_changed():
        widget_Entry_Cols['state'] = 'normal'
        widget_Entry_Cols.delete(0,'end')
        widget_Entry_Cols.insert(0,str(container().grid_conf_cols[0]))
        widget_Entry_Cols['state'] = 'disabled'

    do_receive('GRID_COLS_CHANGED',grid_cols_changed)


    def grid_rows_changed():
        widget_Entry_Rows['state'] = 'normal'
        widget_Entry_Rows.delete(0,'end')
        widget_Entry_Rows.insert(0,str(container().grid_conf_rows[0]))
        widget_Entry_Rows['state'] = 'disabled'

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




    def set_grid_conf_rows():

        is_uniform = False

        try:
            rows = int(widget_Entry_Rows.get())
        except ValueError: 
            rows = container().grid_conf_rows[0]
            widget_Entry_Rows.delete(0,'end')
            widget_Entry_Rows.insert(0,rows)

        row_height, padvalue, weightvalue = get_row_values()


        #if not container().grid_conf_rows or not container().grid_conf_rows[0] or not container().grid_uni_row:
        if not container().grid_uni_row:
            container().grid_conf_rows = (rows,row_height,padvalue,weightvalue)
        else:
            container().grid_conf_rows = tuple([rows] + list(container().grid_conf_rows[1:]))
            is_uniform = True

        return is_uniform, row_height, padvalue, weightvalue


    def set_grid_conf_cols():

        is_uniform = False
        
        try:
            cols = int(widget_Entry_Cols.get())
        except ValueError: 
            cols = container().grid_conf_cols[0]
            widget_Entry_Cols.delete(0,'end')
            widget_Entry_Cols.insert(0,cols)

        col_width, padvalue, weightvalue = get_col_values()

        #if not container().grid_conf_cols or not container().grid_conf_cols[0] or not container().grid_uni_col:
        if not container().grid_uni_col:
            container().grid_conf_cols = (cols,col_width,padvalue,weightvalue)
        else:
            container().grid_conf_cols = tuple([cols] + list(container().grid_conf_cols[1:]))
            is_uniform = True

        return is_uniform, col_width, padvalue, weightvalue


    # ===== for new rows or columns ===========================


    # === columns ========================================
    def fill_general_multicols(cont):
        cols = cont.grid_conf_cols[0]
        to_insert =  {'minsize':cont.grid_conf_cols[1],'pad':cont.grid_conf_cols[2],'weight':cont.grid_conf_cols[3],'uniform' : ''}
        for col in range(cols):
            if cont.grid_multi_conf_cols[col][0] == False: cont.grid_multi_conf_cols[col][1] = dict(to_insert)

    def configure_columns(cont):
        cols = cont.grid_conf_cols[0]
        for col in range(cols):
            cont.grid_columnconfigure(col,**(cont.grid_multi_conf_cols[col][1]))

    def colupdate_canvas_top(cont):
        cols = cont.grid_conf_cols[0]
        for col in range(cols):
            config = cont.grid_multi_conf_cols[col][1]
            send('COL_WEIGHT',(col,config['weight'],cont))
            send('TOP_UPDATE_COL',(col,config,cont))

    def colconfigure_andcanvas_andtop(cont):
        configure_columns(cont)
        colupdate_canvas_top(cont)

    def set_col_width():
        fill_general_multicols(container())
        colconfigure_andcanvas_andtop(container())


    # === rows ========================================

    def fill_general_multirows(cont):
        rows = cont.grid_conf_rows[0]
        to_insert =  {'minsize':cont.grid_conf_rows[1],'pad':cont.grid_conf_rows[2],'weight':cont.grid_conf_rows[3],'uniform' : ''}
        for row in range(rows):
            if cont.grid_multi_conf_rows[row][0] == False: cont.grid_multi_conf_rows[row][1] = dict(to_insert)

    def configure_rows(cont):
        rows = cont.grid_conf_rows[0]
        for row in range(rows):
            cont.grid_rowconfigure(row,**(cont.grid_multi_conf_rows[row][1]))

    def rowupdate_canvas_top(cont):
        rows = cont.grid_conf_rows[0]
        for row in range(rows):
            config = cont.grid_multi_conf_rows[row][1]
            send('ROW_WEIGHT',(row,config['weight'],cont))
            send('TOP_UPDATE_ROW',(row,config,cont))

    def rowconfigure_andcanvas_andtop(cont):
        configure_rows(cont)
        rowupdate_canvas_top(cont)

    def set_row_height():
        fill_general_multirows(container())
        rowconfigure_andcanvas_andtop(container())
    # =========================================================

    def update_col_values():
        is_uniform, size, pad, weight = set_grid_conf_cols()
        if is_uniform:
            grid_conf = { 'minsize' : size, 'pad' : pad, 'weight' : weight, 'uniform' : container().grid_uni_col}
            update_all_uniforms(container(),grid_conf)
        else:
            set_col_width()

    def update_row_values():
        is_uniform, size, pad, weight = set_grid_conf_rows()
        if is_uniform:
            grid_conf = { 'minsize' : size, 'pad' : pad, 'weight' : weight, 'uniform' : container().grid_uni_row}
            update_all_uniforms(container(),grid_conf)
        else:
            set_row_height()

    def check_col_values():
        try:
            cols = int(widget_Entry_Cols.get())
        except ValueError: 
            cols = container.grid_conf_cols[0]
            widget_Entry_Cols.delete(0,'end')
            widget_Entry_Cols.insert(0,cols)

        #if container().grid_conf_cols[0] and container().grid_conf_cols[0] == cols:
        if container().grid_conf_cols[0] == cols:
            update_col_values()
        else:  # we let this, because we first have to know, what happens, when reset cols to 0
            show_grid()

    def check_row_values():
        try:
            rows = int(widget_Entry_Rows.get())
        except ValueError: 
            rows = container.grid_conf_rows[0]
            widget_Entry_Rows.delete(0,'end')
            widget_Entry_Rows.insert(0,rows)

        #if container().grid_conf_rows[0] and container().grid_conf_rows[0] == rows:
        if container().grid_conf_rows[0] == rows:
            update_row_values()
        else: # we let this, because we first have to know, what happens, when reset rows to 0
            show_grid()


    widget_Spinbox_RowHeight.do_command(check_row_values)
    widget_Spinbox_RowHeight.do_event('<Return>',check_row_values)
    widget_Spinbox_RowWeight.do_command(check_row_values)
    widget_Spinbox_RowWeight.do_event('<Return>',check_row_values)
    widget_Spinbox_RowPad.do_command(check_row_values)
    widget_Spinbox_RowPad.do_event('<Return>',check_row_values)

    widget_Spinbox_ColWidth.do_command(check_col_values)
    widget_Spinbox_ColWidth.do_event('<Return>',check_col_values)
    widget_Spinbox_ColPad.do_command(check_col_values)
    widget_Spinbox_ColPad.do_event('<Return>',check_col_values)
    widget_Spinbox_ColWeight.do_command(check_col_values)
    widget_Spinbox_ColWeight.do_event('<Return>',check_col_values)


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
            do_receive('TOP_UPDATE_UNIFORM',self.top_update_uniform,wishMessage = True)

            self.EntrySize = widget('EntrySize')
            self.EntryPad = widget('EntryPad')
            self.EntryWeight = widget('EntryWeight')
            self.EntryUniform = widget('EntryUniform')
            self.InsertUniform = widget('InsertUniform')

            setSelection(selection_before)
            self.update_widget_uniform()


        def top_update_uniform(self,msg):
            if msg[0] == self.mycanvas.master:
                config = self.grid_configure(self.row_col)
                if config['uniform'] == msg[1]:
                    for entry in ((self.EntrySize,config['minsize']),(self.EntryPad,config['pad']),(self.EntryWeight,config['weight'])):
                        entry[0].delete(0,'end')
                        entry[0].insert(0,entry[1])


        def update_widget_uniform(self):
            if self.mycanvas.master == container():
                self.InsertUniform.grid()
            else:
                self.InsertUniform.grid_remove()

        def take_over_uniform(self):
            uniform = self.EntryUniform.get().strip()
            if self.is_row:
                take_over_uniform_row(uniform)
            else:
                take_over_uniform_col(uniform)
            self.update_values()

        def update_and_close(self):
            self.update_values()
            self.destroy()

        def update_size(self,message):
            if message[1] == self.mycanvas:
                self.EntrySize.delete(0,'end')
                self.EntrySize.insert(0,message[0])

        def top_grid_show(self,msg,showRowCol = widget('showRowCol'),EntrySize = widget('EntrySize'),EntryPad=widget('EntryPad'),EntryWeight=widget('EntryWeight'),UniForm = widget('uniform')):
            if msg[0] != self.mycanvas: return

            config = msg[2]

            uniform = config['uniform']
            if not uniform:
                uniform = ''

            # showRowCol['text'] = str(row_col)  # not needed, because this will not be changed. When rows or columns are deleted or inserted the canvas and the toplevel will be destroyed
            for entry in ((self.EntrySize,config['minsize']),(self.EntryPad,config['pad']),(self.EntryWeight,config['weight']),(self.EntryUniform,uniform)):
                entry[0].delete(0,'end')
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

            return minsize,pad,weight,uniform

    def update_individual(cont,hili_bg = indiv_hilibg,selcolor=indiv_selcolor):
        widget_Checkbutton_Individual['highlightbackground'] = '#ff8000' if cont.grid_conf_individual_has else hili_bg
        widget_Checkbutton_Individual['selectcolor'] = '#ffe0a0' if cont.grid_conf_individual_has else selcolor
 
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


    def update_uniform_cols(cont,grid_conf):
        cols = cont.grid_conf_cols[0] # number of columns
        for col in range(cols):
            if cont.grid_multi_conf_cols[col][0]: # if marked as individual
                conf = container().grid_multi_conf_cols[col][1] # grid column configuration of this column
                if 'uniform' in conf and conf['uniform'] and conf['uniform'] == grid_conf['uniform']: # if it's the same uniform
                    cont.grid_multi_conf_cols[col][1] = grid_conf # update the grid column configuration
                    cont.grid_columnconfigure(col,**grid_conf) # and perform a grid_columnconfigure
                    
    def update_uniform_rows(cont,grid_conf):
        rows = cont.grid_conf_rows[0] # number of rows
        for row in range(rows):
            if cont.grid_multi_conf_rows[row][0]: # if marked as individual
                conf = container().grid_multi_conf_rows[row][1] # grid row configuration of this row
                if 'uniform' in conf and conf['uniform'] and conf['uniform'] == grid_conf['uniform']: # if it's the same uniform
                    cont.grid_multi_conf_rows[row][1] = grid_conf # update the grid row configuration
                    cont.grid_rowconfigure(row,**grid_conf) # and perform a grid_rowconfigure


    def update_all_uniforms(cont,grid_conf):
        update_uniform_rows(cont,grid_conf)
        update_uniform_cols(cont,grid_conf)

        uniform = grid_conf['uniform']
        send('CANVAS_UPDATE_UNIFORM',[cont,uniform])
        send('TOP_UPDATE_UNIFORM',[cont,uniform])
             
        if cont.grid_uni_row == uniform:
            cont.grid_current_uniform_row = (grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])
            if cont == container():
                update_rows_data(*cont.grid_current_uniform_row)
        
        if cont.grid_uni_col == uniform:
            cont.grid_current_uniform_col = (grid_conf['minsize'],grid_conf['pad'],grid_conf['weight'])
            if cont == container():
                update_cols_data(*cont.grid_current_uniform_col)


    def update_row_canvas(me,row,grid_conf,bg):
        cont = me.master # container of the canvas
        cont.grid_multi_conf_rows[row][1] = grid_conf # insert grid_conf into grid_multi_conf_rows
        cont.grid_rowconfigure(row,**grid_conf) # and do the grid_rowconfigure

        # if grid_conf contains no uniform, simply update the cont.grid_multi_conf_rows with False or True      
        if 'uniform' not in grid_conf or not grid_conf['uniform']:
            # enter True or False for general or individual grid
            if grid_conf['minsize'] == cont.grid_conf_rows[1] and grid_conf['pad'] == cont.grid_conf_rows[2] and grid_conf['weight'] == cont.grid_conf_rows[3]:
                cont.grid_multi_conf_rows[row][0] = False # general grid if identical with general grid
            else:
                cont.grid_multi_conf_rows[row][0] = True # otherwise it's an individual grid

            update_canvascolor_row(me,row,bg) # update  the color of the canvas according to the entry         
            update_canvas_row_line_arrow((row,grid_conf['weight'],cont),me,row)
            update_individual_mark(cont) # update also the highlight of widget_Checkbutton_Individual
        
        # but if it's a uniform entry then update all same uniform entries of the container
        else:
            cont.grid_multi_conf_rows[row][0] = True # uniform is an individual grid
            update_all_uniforms(cont,grid_conf)

        
    def update_col_canvas(me,col,grid_conf,bg):
        cont = me.master # container of the canvas
        cont.grid_multi_conf_cols[col][1] = grid_conf # insert grid_conf into grid_multi_conf_rows
        cont.grid_columnconfigure(col,**grid_conf) # and do the grid_rowconfigure

        # if grid_conf contains no uniform, simply update the cont.grid_multi_conf_rows with False or True      
        if 'uniform' not in grid_conf or not grid_conf['uniform']:
            # enter True or False for general or individual grid
            if grid_conf['minsize'] == cont.grid_conf_cols[1] and grid_conf['pad'] == cont.grid_conf_cols[2] and grid_conf['weight'] == cont.grid_conf_cols[3]:
                cont.grid_multi_conf_cols[col][0] = False # general grid if identical with general grid
            else:
                cont.grid_multi_conf_cols[col][0] = True # otherwise it's an individual grid

            update_canvascolor_col(me,col,bg) # update  the color of the canvas according to the entry         
            update_canvas_col_line_arrow((col,grid_conf['weight'],cont),me,col)
            update_individual_mark(cont) # update also the highlight of widget_Checkbutton_Individual
        
        # but if it's a uniform entry then update all same uniform entries of the container
        else:
            cont.grid_multi_conf_cols[col][0] = True # uniform is an individual grid
            update_all_uniforms(cont,grid_conf)



    def mouse_wheel_row(me,event,row,bg):
        grid_conf=me.master.grid_multi_conf_rows[row][1]
        if event.num == 5 or event.delta == -120:
            grid_conf['minsize'] -= 1
        if event.num == 4 or event.delta == 120:
            grid_conf['minsize'] += 1
        #update_row(me,row,grid_conf,bg)
        update_row_canvas(me,row,grid_conf,bg)

    def mouse_wheel_col(me,event,column,bg):
        grid_conf=me.master.grid_multi_conf_cols[column][1]
        if event.num == 5 or event.delta == -120:
            grid_conf['minsize'] -= 1
        if event.num == 4 or event.delta == 120:
            grid_conf['minsize'] += 1
        #update_col(me,column,grid_conf,bg)
        update_col_canvas(me,column,grid_conf,bg)
        
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
        coords = (3,9,me.winfo_width()-3,9)
        me.coords('line',*coords)
        
    def update_canvas_row_line(me):
        coords = (9,3,9,me.winfo_height()-3)
        me.coords('line',*coords)

    def update_canvas_row_line_arrow(msg,me,row):
        if me.master == msg[2] and msg[0] == row:
            me.itemconfig('line', arrowshape = '8 8 5' if msg[1] else '8 0 5')

    def update_canvas_col_line_arrow(msg,me,col):
        if me.master == msg[2] and msg[0] == col:
            me.itemconfig('line', arrowshape = '8 8 5' if msg[1] else '8 0 5')

    def top_update_col(msg,me,col):
        if me.master == msg[2] and msg[0] == col:
            send('TOPGRIDSHOW',(me,col,msg[1]))

    def top_update_row(msg,me,row):
        if me.master == msg[2] and msg[0] == row:
            send('TOPGRIDSHOW',(me,row,msg[1]))

    class NonameCanvas(Canvas):

        def __init__(self,*args,**kwargs):
            Canvas.__init__(self,*args,**kwargs)
            self.orig_bg = self['bg']

        '''
        def col_config_changed(self,col,config,update_col = update_col):
            update_col(self,col,config,self.orig_bg)

        def row_config_changed(self,row,config,update_row = update_row):
            update_row(self,row,config,self.orig_bg)
        '''


        def col_config_changed(self,col,config):
            update_col_canvas(self,col,config,self.orig_bg)

        def row_config_changed(self,row,config):
            update_row_canvas(self,row,config,self.orig_bg)


    def check_update_canvascolor_col(me,col,bg):
        if me.master == container():
            update_canvascolor_col(me,col,bg)
            
    def check_update_canvascolor_row(me,col,bg):
        if me.master == container():
            update_canvascolor_row(me,col,bg)

    def canvas_update_uniform_row(msg,me,row,bg):
        cont = me.master
        if msg[0] == cont:
            conf = cont.grid_multi_conf_rows[row][1] # grid row configuration of this row
            if 'uniform' in conf and conf['uniform'] and conf['uniform'] == msg[1]: # if it's the same uniform
                 update_canvascolor_row(me,row,bg) # update color and uniform highlight
                 update_canvas_row_line_arrow((row,conf['weight'],cont),me,row)
                    
    def canvas_update_uniform_col(msg,me,col,bg):
        cont = me.master
        if msg[0] == cont:
            conf = cont.grid_multi_conf_cols[col][1] # grid row configuration of this row
            if 'uniform' in conf and conf['uniform'] and conf['uniform'] == msg[1]: # if it's the same uniform
                 update_canvascolor_col(me,col,bg) # update color and uniform highlight
                 update_canvas_col_line_arrow((col,conf['weight'],cont),me,col)

    def create_NONAMECANVAS(rows,cols,gui_grid_container=container()):
        # not correct
        cont = container()
        for row in range(rows):
            canvas_row = NonameCanvas(NONAMECANVAS,relief='raised',width=13,height=0,cursor='sizing',highlightthickness=2,bd=1)
            canvas_row.bg = canvas_row['bg']
            canvas_row['highlightbackground'] = canvas_row.bg
            canvas_row.rcgrid(row,cols+1,sticky='ns')
            item = canvas_row.create_line(4,4,4,4)
            canvas_row.itemconfig(item,fill = 'blue',arrow = 'both',width = '3.0',tags = 'line')

            if cont.grid_special:
                for frame in cont.dyntk_row_frames:
                    if int(frame.grid_info()['row']) == row+1:
                        frame.mycanvas = canvas_row
                        break

            
            do_event("<MouseWheel>", mouse_wheel_row,(row,this()['bg']),True,True) # spin mouse wheel
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
            do_receive('CANVAS_UPDATE_UNIFORM',canvas_update_uniform_row,[this(),row,this()['bg']],wishMessage = True)
            goOut()
            send('ROW_WEIGHT',(row,cont.grid_rowconfigure(row)['weight'],cont))

            update_canvascolor_row(this(),row,this()['bg'])
        

        if cont.grid_special:
            Button(NONAMECANVAS,padx = 0, pady = 0,image = gui_grid_container.help_image,command=show_help,cursor = 'question_arrow')
            rcgrid(rows+1,cols+1)

        for col in range(cols):
            canvas_col = NonameCanvas(NONAMECANVAS,relief='raised',width=0,height=13,cursor='sizing',highlightthickness=2,highlightbackground=orange,bd=1)
            canvas_col.rcgrid(rows+1,col,sticky='we')
            canvas_col.bg = canvas_col['bg']
            canvas_col['highlightbackground'] = canvas_col.bg
            item = canvas_col.create_line(4,4,4,4)
            canvas_col.itemconfig(item,fill = 'blue',arrow = 'both',width = '3.0',tags = 'line')
           
            if cont.grid_special:
                for frame in cont.dyntk_col_frames:
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
            do_receive('CANVAS_UPDATE_UNIFORM',canvas_update_uniform_col,[this(),col,this()['bg']],wishMessage = True)

            goOut()
            send('COL_WEIGHT',(col,cont.grid_columnconfigure(col)['weight'],cont))
           
            update_canvascolor_col(this(),col,this()['bg'])
       
        cont.grid_columnconfigure(cols+1,minsize = 0,pad=0,weight=0)
        cont.grid_rowconfigure(rows+1,minsize = 0,pad=0,weight=0)


    def show_grid(event=None,withNONAME = True,set_col_width=set_col_width,set_row_height=set_row_height):


        # delete old configuration ================

        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        deleteWidgetsForName(container(),NONAME)
        deleteWidgetsForName(container(),NONAME2)
        deleteWidgetsForName(container(),NONAMECANVAS)

        # +++ hier ist ein Fehler.
        # ich hatte den content gelöscht und damit auuch
        # grid_conf_rows
        # doch es erfolgte
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

        set_grid_conf_cols()
        set_grid_conf_rows()

        cols = container().grid_conf_cols[0]
        rows = container().grid_conf_rows[0]

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


        # must be before canvases
        fill_general_multicols(container())
        fill_general_multirows(container())

        if individ and withNONAME:
            create_NONAMECANVAS(rows,cols)
            container().grid_conf_individual_done = True

        # mes be after canvases
        colconfigure_andcanvas_andtop(container())
        rowconfigure_andcanvas_andtop(container())

        setSelection(selection_before)
        # why this?
        send("BASE_LAYOUT_REFRESH",this())

    def update_indiv_wish():
        container().grid_conf_individual_wish = widget_Checkbutton_Individual.mydata.get() == 1
        if container().grid_show:
            show_grid()

    widget_Checkbutton_Individual.do_command(update_indiv_wish)

    def press_button_show(event=None):

        if container().grid_show_enabled:
            container().grid_show = not container().grid_show
            widget_Button_Show.is_on = container().grid_show

            if widget_Button_Show.is_on:
                show_grid()
            else:
                hide_grid()

    def update_button_show(event=None):
        widget_Button_Show.is_on = container().grid_show
        widget_Button_Show['relief'] = 'raised' if not widget_Button_Show.is_on else 'sunken'
        widget_Button_Show['text'] = 'Show' if not widget_Button_Show.is_on else 'Hide'
            
    def animate_button_show(event=None):
        if container().grid_show_enabled:
            widget_Button_Show.is_on = container().grid_show
            widget_Button_Show['relief'] = 'raised' if widget_Button_Show.is_on else 'sunken'
            widget_Button_Show['text'] = 'Show' if widget_Button_Show.is_on else 'Hide'

    def entry_show_grid(event=None):
        container().grid_show = True
        update_button_show()
        show_grid()
        

    widget_Button_Show.bind('<Button-1>',animate_button_show)
    widget_Button_Show.bind('<ButtonRelease-1>',press_button_show)
    widget_Entry_Rows.bind('<Return>',entry_show_grid)
    widget_Entry_Cols.bind('<Return>',entry_show_grid)



    def update_after_pack(show_grid = show_grid):
 
        if container().grid_conf_rows[0] != 0 or container().grid_conf_cols[0] != 0:
                
            widget_Entry_Rows.delete(0,'end')
            widget_Entry_Rows.insert(0,'0')
            widget_Entry_Cols.delete(0,'end')
            widget_Entry_Cols.insert(0,'0')
            show_grid()

    do_receive('BASE_LAYOUT_PACK_DONE',update_after_pack)

    def do_grid_col_row(col,row,do_mouse_on=grid_mouse_on):
        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        layout_before = this().Layout

        if isinstance(this(),GuiContainer):
            rcgrid(row,col,sticky = 'news') # this isn't original, but makes sense
        else:
            rcgrid(row,col)
        this().dyntk_lift()
        if container().is_mouse_select_on: grid_mouse_on(this())
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


    def do_grid0():
        do_grid_col_row(0,0)        
    widget_Button_Grid0.do_command(do_grid0)


    def do_grid(do_mouse_on=grid_mouse_on):
        send('DESTROY_INDIVIDUAL_GRID_TOPLEVEL')
        layout_before = this().Layout
        if layout_before == PLACELAYOUT:

            (col,row) = container().grid_location(this().winfo_rootx()-container().winfo_rootx(),this().winfo_rooty()-container().winfo_rooty())
            if col < 0: col = 0
            if row < 0: row = 0

            if isinstance(this(),GuiContainer):
                rcgrid(row,col,sticky = 'news') # this isn't original, but makes sense
            else:
                rcgrid(row,col)
        else:
            grid()
        this().dyntk_lift()
        if container().is_mouse_select_on: grid_mouse_on(this())
        send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

    widget_Button_Grid.do_command(do_grid)


    def row_default(container):
        conf = container.grid_conf_rows
        uniform = container.grid_uni_row if container.grid_uni_row else ''
        if not uniform or not getattr(container,'grid_current_uniform_row', None):
            return { 'minsize' : conf[1], 'pad' : conf[2], 'weight' : conf[3], 'uniform' : uniform }
        else: 
            conf = container.grid_current_uniform_row
            return { 'minsize' : conf[0], 'pad' : conf[1], 'weight' : conf[2], 'uniform' : uniform }
       

    def col_default(container):
        conf = container.grid_conf_cols
        uniform = container.grid_uni_col if container.grid_uni_col else ''
        if not uniform or not getattr(container,'grid_current_uniform_col', None):
            return { 'minsize' : conf[1], 'pad' : conf[2], 'weight' : conf[3], 'uniform' : uniform }
        else: 
            conf = container.grid_current_uniform_col
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
                
            #self.do_event('<B1-Motion>',self.move)
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
            #self.do_event('<B1-Motion>',self.move)
            self.move()
            
     
        def measure_colwidth(self):
            self.begin,top,self.cellsize,height = self.master.grid_bbox(row = 0, column = self.row_col)
     
        def measure_rowheight(self):
            left,self.begin,width,self.cellsize = self.master.grid_bbox(row = self.row_col, column = 0)
     
        def set_size(self):
            self.row_col_config['minsize'] = self.cellsize - 2 * int(self.row_col_config['pad'])
            self.line_configure(self.row_col,**self.row_col_config)
     
        def move(self,event=None):
     
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

        def unbind_enter(self):
            self.unbind('<Enter>')
            self.unbind('<B1-Motion>')
            self.unbind('<ButtonRelease-1>')
     
        # these are double defined, but nearly identical may be we not only a single definition
        def tableline_enter_col(self,event=None):
            for element in self.master.dyntk_table_frames:
                element.is_moving = False
                element.config( bg = self.gray)
                element.bind_enter()
     
            self.master.focus()
            self.bind('<Leave>',self.tableline_leave)
            self.lift()
            self.config( cursor = 'sb_h_double_arrow', bg = self.green)
     
        def tableline_enter_row(self,event=None):
            for element in self.master.dyntk_table_frames:
                element.is_moving = False
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
     
            self.grid_configure(self.row_col,**self.row_col_default(self.master))
            insert_frame = self.insert_row_col(self.master,self.row_col)
     
            self['bg'] = self.gray
            self.bind_enter()
     
            if self.is_col:
     
                conf = list(self.master.grid_conf_cols)
                conf[0] += 1
                self.master.grid_conf_cols = tuple(conf)
                is_uni = True if self.master.grid_uni_col else False
                self.master.grid_multi_conf_cols.insert(self.row_col,[is_uni,self.row_col_default(self.master)])
                
                for frame in self.master.dyntk_row_frames:
                    frame.grid(column = 0, columnspan = self.master.grid_conf_cols[0])
                insert_frame.tableline_mark_col()
            else:
                conf = list(self.master.grid_conf_rows)
                conf[0] += 1
                self.master.grid_conf_rows = tuple(conf)

                is_uni = True if self.master.grid_uni_row else False
                self.master.grid_multi_conf_rows.insert(self.row_col,[is_uni,self.row_col_default(self.master)])

                for frame in self.master.dyntk_col_frames:
                    frame.grid(row = 0,rowspan = self.master.grid_conf_rows[0])
                insert_frame.tableline_mark_row()

            setWidgetSelection(self)
            if self.is_col:
                configure_columns(container())
            else:
                configure_rows(container())
            create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
            special_noname_frame()            


            setSelection(selection_before)
            # this is ok, fills widget_Entry_Cols or widget_Entry_Rows, but now change, if not container()
            if self.master == container():
                send('GRID_COLS_CHANGED' if self.is_col else 'GRID_ROWS_CHANGED')


            #set_col_width()
            #set_row_height()
           

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
                setWidgetSelection(self)
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
            setWidgetSelection(self)
            if self.is_col:
                configure_columns(container())
            else:
                configure_rows(container())
            create_NONAMECANVAS(self.master.grid_conf_rows[0],self.master.grid_conf_cols[0])
            special_noname_frame()

            setSelection(selection_before)

            # this is ok, fills widget_Entry_Cols or widget_Entry_Rows, but now change, if not container()
            if self.master == container():
                send('GRID_COLS_CHANGED' if self.is_col else 'GRID_ROWS_CHANGED')
            
            #set_col_width()
            #set_row_height()

            

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
 

    def special_toggle():
        container().grid_special = not container().grid_special
        widget_Button_Special.is_on = container().grid_special

        widget_Button_Special['relief'] = 'sunken' if widget_Button_Special.is_on else 'raised'
        hide_grid()

        if widget_Button_Special.is_on:

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

            if not children:
                grid_conf_rows[1] = max(grid_conf_rows[1],MIN_HEIGHT)
                grid_conf_cols[1] = max(grid_conf_cols[1],MIN_WIDTH)

            container().grid_conf_rows = tuple(grid_conf_rows)
            container().grid_conf_cols = tuple(grid_conf_cols)

            
            # show_grid will read these values as new Rows and Columns
            widget_Entry_Cols.delete(0,'end')
            widget_Entry_Cols.insert(0,cols)

            widget_Entry_Rows.delete(0,'end')
            widget_Entry_Rows.insert(0,rows)


            # update minsize, pad, weight in the grid input mask dependent on uniform entries
            update_uni_row_uniform(container().grid_uni_row)
            update_uni_col_uniform(container().grid_uni_col)

            container().save_grid_conf_individual_wish = container().grid_conf_individual_wish
            container().grid_conf_individual_wish = 1

            show_grid(None,False)

            selection_before = Selection()
            special_noname_frame()

            widget_Button_Show['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            container().grid_show_enabled = not widget_Button_Special.is_on

            widget_Checkbutton_Individual['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            widget_Entry_Rows['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            widget_Entry_Cols['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'

            container().dyntk_table_frames = []
            container().dyntk_col_frames = []
            container().dyntk_row_frames = []

            insert_table(container())

            create_NONAMECANVAS(rows,cols)

            setSelection(selection_before)

        else:

            widget_Button_Show['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            container().grid_show_enabled = not widget_Button_Special.is_on

            widget_Checkbutton_Individual['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            widget_Entry_Rows['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            widget_Entry_Cols['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
            container().grid_conf_individual_wish = container().save_grid_conf_individual_wish

            container().dyntk_table_frames = []
            container().dyntk_col_frames = []
            container().dyntk_row_frames = []

            if container().grid_show:
                show_grid()


    def update_special_button():
        widget_Button_Special.is_on = container().grid_special
        widget_Button_Special['relief'] = 'sunken' if widget_Button_Special.is_on else 'raised'
        widget_Button_Show['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
        container().grid_show_enabled = not widget_Button_Special.is_on

        widget_Checkbutton_Individual['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
        widget_Entry_Rows['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'
        widget_Entry_Cols['state'] = 'disabled' if widget_Button_Special.is_on else 'normal'


    def update_grid_table_on_enter(set_row_height=set_row_height,set_col_width=set_col_width):

        if this().Layout != LAYOUTNEVER and not isinstance(container(),(Menu,MenuItem,PanedWindow,ttk.PanedWindow,ttk.Notebook)):

            # start values for grid_conf_cols, grid_conf_rows, grid_multi_conf_cols, grid_multi_conf_rows, if not already initialized --------------
            
            # try to get the values from definitions made by a tkinter application, otherwise take default values
            if not container().grid_conf_cols:
                container().grid_conf_cols,container().grid_multi_conf_cols = get_gridconfig(container().grid_cols,this().grid_cols_how_many)
                if not container().grid_conf_cols:
                    container().grid_conf_cols = start_default_col_values

            if not container().grid_conf_rows:
                container().grid_conf_rows,container().grid_multi_conf_rows = get_gridconfig(container().grid_rows,this().grid_rows_how_many)
                if not container().grid_conf_rows:
                    container().grid_conf_rows = start_default_row_values

            # --------------------------------------------------------------------------------------------------------------------------------------

            # update Rows and Columns
            grid_cols_changed() # update widget_Entry_Cols
            grid_rows_changed() # update widget_Entry_Rows

            # set normal states, so that we may insert values
            widget_Checkbutton_Individual['state'] = 'normal'
            widget_Entry_Rows['state'] = 'normal'
            widget_Entry_Cols['state'] = 'normal'

           
            # update check mark for widget_Checkbutton_Individual
            if container().grid_conf_individual_wish: widget_Checkbutton_Individual.select()
            else: widget_Checkbutton_Individual.deselect()

            # update highlight for widget_Checkbutton_Individual
            update_individual_mark(container())

            # update widget_Button_Show for Show or Hide
            update_button_show() 

            # update uniform entries
            widget_Entry_UniformRow.delete(0,'end')
            widget_Entry_UniformCol.delete(0,'end')
            widget_Entry_UniformRow.insert(0,container().grid_uni_row)
            widget_Entry_UniformCol.insert(0,container().grid_uni_col)

            # update minsize, pad, weight dependent on uniform entries
            update_uni_row_uniform(container().grid_uni_row)
            update_uni_col_uniform(container().grid_uni_col)

            # update widget_Button_Special and disable other buttons or entries
            update_special_button()

            # update the insert uniform buttons of Toplevels
            # +++ ATTENTION, but why?
            # should we not allow to use this functionality also, if it's not the current container?
            # or better not, could be confusing, if nothing visible happens
            send('UPDATE_INSERT_UNIFORM')

    do_receive("SELECTION_CHANGED",update_grid_table_on_enter)


    widget_Button_Special.do_command(special_toggle)

main()


### ========================================================
