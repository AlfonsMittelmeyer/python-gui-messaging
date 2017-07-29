config(**{'grid_rows': '(4, 25, 0, 0)', 'grid_cols': '(6, 51, 0, 0)', 'grid_multi_cols': '[6, (1, 26, 0, 0), (4, 42, 0, 0), (5, 0, 0, 1)]', 'grid_multi_rows': '[4, (2, 6, 0, 0)]'})

Label('Label',**{'text': 'x', 'padx': '3'}).grid(column=1, row=1)
Label('PlaceTitle',**{'bd': '3', 'text': 'place', 'fg': 'blue', 'font': 'TkDefaultFont 9 bold', 'relief': 'ridge'}).grid(row=0, sticky='nesw')
Spinbox('X',**{'to': 2000.0, 'increment': 10.0, 'width': 4}).grid(column=2, row=1, sticky='ns')
Spinbox('Y',**{'to': 2000.0, 'increment': 10.0, 'width': 4}).grid(column=2, row=0, sticky='ns')
Spinbox('incX',**{'from_': 1.0, 'to': 2000.0, 'width': 4}).grid(column=3, row=1, sticky='ns')
Spinbox('incY',**{'from_': 1.0, 'to': 2000.0, 'width': 4}).grid(column=3, row=0, sticky='ns')
Label('label',**{'text': 'inc x'}).grid(column=4, row=1)
Label('label',**{'text': 'y', 'padx': '3'}).grid(column=1, row=0)
Label('label',**{'text': 'inc y'}).grid(column=4, row=0)
ttk.Separator('separator').grid(row=2, columnspan=6, sticky='ew')
Button('Place',**{'bd': '3', 'bg': 'lightgreen', 'text': 'PLACE', 'padx': '1m', 'font': 'TkDefaultFont 9 bold'}).grid(row=3, sticky='nesw')
Button('relative',**{'bd': '3', 'text': 'relative'}).grid(column=3, row=3, columnspan=2, padx=1, sticky='nsw')
Button('Adjust',**{'bd': '3', 'text': 'adjust', 'state': 'disabled', 'padx': '1m'}).grid(column=1, row=3, columnspan=2, padx=1, sticky='nesw')

### CODE ===================================================

def main():
    # -------------- Initialize the incX and incY Spinbox contents ------------------------------

    widget('incX').delete(0,END)
    widget('incX').insert(0,"10")
    widget('incY').delete(0,END)
    widget('incY').insert(0,"10")

    # -------------- incX,incY Spinbox commands and Return key events ----------------------------------

    # the X or Y increment is set to the incX or incY value

    def set_increment(me,x_or_y): x_or_y['increment'] = me.get()

    widget("incX").do_command(set_increment,widget("X"),wishWidget=True)
    widget("incX").do_event("<Return>",set_increment,widget("X"),wishWidget=True)
    widget("incY").do_command(set_increment,widget("Y"),wishWidget=True)
    widget("incY").do_event("<Return>",set_increment,widget("Y"),wishWidget=True)


    def calc_relative():

        y_diff = this().dyntk_start_frame.winfo_rooty()-container().winfo_rooty()
        selection_before = Selection()
        this().dyntk_start_frame.destroy()
        setSelection(selection_before)

        children = container().place_slaves()
        cont_width = container().winfo_width()
        cont_height = container().winfo_height()

        cont_height -= y_diff


        for child in children:
            place_info = child.place_info()
            x = int(place_info['x'])
            y = int(place_info['y'])
            relx = float(place_info['relx'])
            rely = float(place_info['rely'])
        
            width = place_info['width']
            height = place_info['height']
            relwidth = place_info['relwidth']
            relheight = place_info['relheight']

            if x:
                relx += x/cont_width
                x = 0

            if y:
                rely += y/cont_height
                y = 0

            if height:
                if relheight:
                    relheight = float(relheight)
                else:
                    relheight = 0

                relheight += int(height)/cont_height
                height = ''

            if width:
                if relwidth:
                    relwidth = float(relwidth)
                else:
                    relwidth = 0

                relwidth += int(width)/cont_width
                width = ''

            child.place(x=x,y=y,width=width,height=height,relx=relx,rely=rely,relwidth=relwidth,relheight=relheight)

        send("POSITION_CHANGED")
        send('SHOW_LAYOUT',this())

    def calc_relative_after():
        this().dyntk_start_frame = Frame((container(),NONAME_MOVE))
        this().dyntk_start_frame.yxplace(0,0)
        this().after(10,calc_relative)
        

    widget('relative').do_command(calc_relative_after)


    # -------------- Adjust button command ----------------------------------
    # round according to stepwidth inX,incY
    # do the place config
    # send a POSITION_CHANGED and LAYOUT_VALUES_REFRESH

    def do_round(value,step):
        value += step//2
        value //= step
        return value * step

    def do_adjust(incX_entry = widget("incX"),incY_entry = widget("incY"),rounding=do_round):

        xval = int(this().getlayout("x"))
        incX = int(incX_entry.get())
        xval = rounding(xval,incX)

        yval = int(this().getlayout("y"))
        incY = int(incY_entry.get())
        yval = rounding(yval,incY)

        yxplace(yval,xval)

        send("POSITION_CHANGED")
        send('LAYOUT_VALUES_REFRESH')

    widget("Adjust").do_command(do_adjust)


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
                send('POSITION_CHANGED')
                send('LAYOUT_VALUES_REFRESH')


            
    class DynTk_MouseMove:

        def __init__(self,me):
            self.me = me

            self.start_x = int(me.place_info()['x'])
            self.start_y = int(me.place_info()['y'])
            self.start_pointerx = me.winfo_pointerx()
            self.start_pointery = me.winfo_pointery()

            self.selection_changed = False
            self.step = 0
            self.is_moving=False
        
        def start_move(self,event=None):
            if not self.is_moving:
                self.me.unbind('<B1-Motion>')
                dyntk_unhighlight(self.me)
                self.me.lift()
                if this() != self.me:
                    self.selection_changed = True

                send('BASEMENTLEVEL_CHANGED')
            self.is_moving = True
            self.move()

        def stop_move(self):
            self.is_moving = False
            self.me.dyntk_lift()

        def move(self):
            if self.is_moving and widget_exists(self.me) and self.me.Layout == PLACELAYOUT:

                diff_x = self.me.winfo_pointerx() - self.start_pointerx
                diff_y = self.me.winfo_pointery() - self.start_pointery

                self.me.yxplace(self.start_y + diff_y,self.start_x + diff_x)
                if self.step >= 10:
                    self.step = 0
                    send('POSITION_CHANGED')
                    send('LAYOUT_VALUES_REFRESH')
                self.step += 1
                self.me.after(10,self.move)

    # we bind events to the widget - better not additional first, so nothing may happen with additional unexpected messages

    def place_mouse_on(me):
        me.do_event('<Button-1>',highlight_widget,wishWidget=True)

    def highlight_widget(me):
        me.dyntk_highlight = DynTk_HighLight(me)
        me.dyntk_mousemove = DynTk_MouseMove(me)
        me.do_event('<B1-Motion>',me.dyntk_mousemove.start_move)
        me.do_event('<ButtonRelease-1>',highlight_mouse_up,wishWidget=True)

    def highlight_mouse_up(me):
        if  me.dyntk_highlight:
            me.dyntk_mousemove.is_moving = False

        me.unbind('<ButtonRelease-1>')
        me.unbind('<B1-Motion>')
        me.dyntk_highlight.restore()
        me.dyntk_mousemove.stop_move()
        me.dyntk_highlight = None
        me.dyntk_mousemove = None


    do_receive('PLACE_MOUSE_ON',place_mouse_on,wishMessage=True)


    def place_after(par):
        me = par[0]
        layout_before =par[1]
        (x,y) = me.winfo_rootx()-me.dyntk_start_frame.winfo_rootx(),me.winfo_rooty()-me.dyntk_start_frame.winfo_rooty()
        yxplace(y,x,width=me.winfo_width(),height=me.winfo_height())

        selection_before = Selection()
        me.dyntk_start_frame.destroy()
        setSelection(selection_before)
        send("BASE_LAYOUT_CHANGED",layout_before) # and message to others
        send('POSITION_CHANGED') # show this in X an Y Spinbox, 'bd': '3'

    def do_place_dependent(mouse_on = place_mouse_on):

        layout_before = this().Layout

        if layout_before == NOLAYOUT:
            yxplace(0,0)
            this().dyntk_lift()
            send("BASE_LAYOUT_CHANGED",layout_before) # and message to others
            send('POSITION_CHANGED') # show this in X an Y Spinbox, 'bd': '3'

        elif layout_before != PLACELAYOUT:
            this().dyntk_start_frame = Frame((this().master,NONAME_MOVE))
            this().dyntk_start_frame.yxplace(0,0)
            this().after(10,place_after,(this(),layout_before))
        else:
            yxplace(0,0)
            send('POSITION_CHANGED') # show this in X an Y Spinbox, 'bd': '3'
        
        if container().is_mouse_select_on: mouse_on(this())
        else: send("SWITCH_MOUSE_ON")


    widget("Place").do_command(do_place_dependent)

    # -------------- X,Y Spinbox commands and Return key events ----------------------------------

    # do the place layout and send a 'BASE_LAYOUT_CHANGED' message

    def do_place(yentry = widget("Y"), xentry = widget("X")):
        layout_before = this().Layout
        yxplace(yentry.get(),xentry.get())

        if container().is_mouse_select_on: place_mouse_on(this())
        send('BASE_LAYOUT_CHANGED',layout_before)

    widget("Y").do_command(do_place)
    widget("X").do_command(do_place)
    widget("Y").do_event("<Return>",do_place)
    widget("X").do_event("<Return>",do_place)


    # -------------- Receivers for refresh ----------------------------------

    # receiver for external or internal BASE_LAYOUT_REFRESH message
    do_receive('BASE_LAYOUT_VALUE_REFRESH',lambda: send('POSITION_CHANGED'))

    # receiver for external or internal BASE_LAYOUT_REFRESH message
    # set the bg color of Label PlaceTitle to yellow, of the widget has a place layout
    # and enable or disable buttons MouseOn, MouseOff and Adjust

    def titlecolor_and_enable(title = widget("PlaceTitle"),bg = widget("PlaceTitle")["bg"],MouseOn=widget("MouseOn"),MouseOff=widget("MouseOff"),Adjust=widget("Adjust")): 

        if this().Layout == PLACELAYOUT:
            title['bg'] = 'yellow'	
            state = 'normal'
        else:
            title['bg'] = bg
            state = 'disabled'

        Adjust['state'] = state

    do_receive('BASE_LAYOUT_REFRESH',titlecolor_and_enable)

    def set_yx_entries(SpinboxX = widget("X"), SpinboxY = widget("Y")):
        if this().Layout==PLACELAYOUT:
            SpinboxX.delete(0,END)
            SpinboxX.insert(0,this().getlayout("x"))
            SpinboxY.delete(0,END)
            SpinboxY.insert(0,this().getlayout("y"))

    # set X,Y spinboxes to X,Y layout values of the widget
    do_receive('POSITION_CHANGED',set_yx_entries)

main()

### ========================================================
