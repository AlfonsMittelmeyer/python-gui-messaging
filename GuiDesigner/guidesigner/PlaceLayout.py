Button('MouseOn',text="""ON""",state='disabled').grid(column='3',sticky='w',row='4')
Spinbox('incX',from_='1.0',width='4',to='2000.0').grid(column='3',row='0')
Spinbox('incY',increment='1.0',from_='1.0',width='4',to='2000.0').grid(column='3',row='1')
Label('PlaceTitle',text="""place""",fg='blue').grid(sticky='w',row='0')
Label('label',text="""inc x""").grid(column='4',row='0')
Label('label',text="""y""",padx='3').grid(column='1',row='1')
Label('label',text="""inc y""").grid(column='4',row='1')
Button('MouseOff',text="""OFF""",state='disabled').grid(column='4',sticky='e',row='4')
Button('Adjust',text="""adjust""",state='disabled').grid(row='1')
Button('Place',text="""place at 0,0""",bg='green').grid(column='3',sticky='ew',columnspan='2',row='3')
Spinbox('Y',increment='10.0',width='4',from_=0,to='2000.0').grid(column='2',row='1')
Spinbox('X',increment='10.0',width='4',from_=0,to='2000.0').grid(column='2',row='0')
Label('Label',text="""x""",padx='3').grid(column='1',row='0')
Label('Label',text="""mouse move &""").grid(columnspan='3',row='3')
Label('Label',text="""mouse move:""").grid(columnspan='3',row='4')

### CODE ===================================================

def main():
    # -------------- Initialize the incX and incY Spinbox contents ------------------------------

    widget('incX').delete(0,END)
    widget('incX').insert(0,"10")
    widget('incY').delete(0,END)
    widget('incY').insert(0,"10")

    # -------------- X,Y Spinbox commands and Return key events ----------------------------------


    # do the place layout and send a 'BASE_LAYOUT_CHANGED' message

    def do_place(yentry = widget("Y"), xentry = widget("X")):
        layout_before = this().Layout
        yxplace(yentry.get(),xentry.get())
        send('BASE_LAYOUT_CHANGED',layout_before)

    widget("Y").do_command(do_place)
    widget("X").do_command(do_place)
    widget("Y").do_event("<Return>",do_place)
    widget("X").do_event("<Return>",do_place)

    # -------------- incX,incY Spinbox commands and Return key events ----------------------------------

    # the X or Y increment is set to the incX or incY value

    def set_increment(me,x_or_y): x_or_y['increment'] = me.get()

    widget("incX").do_command(set_increment,widget("X"),wishWidget=True)
    widget("incX").do_event("<Return>",set_increment,widget("X"),wishWidget=True)
    widget("incY").do_command(set_increment,widget("Y"),wishWidget=True)
    widget("incY").do_event("<Return>",set_increment,widget("Y"),wishWidget=True)

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

        send("POSITION_CHANGED",this())
        send('LAYOUT_VALUES_REFRESH',this())

    widget("Adjust").do_command(do_adjust)


    # -------------- Mouse move button commands and mouse events ----------------------------------

    # on mouse button down the current y,x offset of the mouse pointer is stored in mydata
    # if the widget isn't the selected widget, then it becomes the selected widget


    def mouse_move(me):
        if me.mydata[6]:
            step = 10
            diffx = me.winfo_pointerx() - me.winfo_rootx()
            diffy = me.winfo_pointery() - me.winfo_rooty()
            me.mydata[3] += diffx-me.mydata[0]
            me.mydata[4] += diffy-me.mydata[1]
            yxplace(me.mydata[4],me.mydata[3])
            me.mydata[5] += step
            if me.mydata[5] >= 100:
                me.mydata[5] = 0
                send('POSITION_CHANGED',me)
                send('LAYOUT_VALUES_REFRESH',me)
            me.mydata[5] += step
            me.after(step,mouse_move,me)

    def on_mouse_down(me,event):
        xpos = int(me.getlayout("x"))
        ypos = int(me.getlayout("y"))
        me.mydata = [event.x,event.y,'mouse',xpos,ypos,0,True]
        mouse_move(me)

        if this() != me:
            setWidgetSelection(me)
            send('SELECTION_CHANGED')

    def on_mouse_up(me,event):
        me.mydata[6] = False # stop timer
        send('POSITION_CHANGED',me)
        send('LAYOUT_VALUES_REFRESH',me)



    def do_mouse_on(mouse_down = on_mouse_down, mouse_up = on_mouse_up):
        config(cursor="mouse")
        this().mydata=(None,None,'mouse')
        do_event('<Button-1>',mouse_down,wishWidget=True,wishEvent=True)
        do_event('<ButtonRelease-1>',mouse_up,wishWidget=True,wishEvent=True)


    # by pressing the MouseOn button, we bind the mouse down and the mouse motion event to the selected widget
    widget("MouseOn").do_command(do_mouse_on)

    def do_mouse_off():
        config(cursor="")
        this().unbind('<Button-1>')
        this().unbind('<ButtonRelease-1>')
        this().mydata=None

    # by pressing the MouseOff button, we unbind the mouse events
    widget("MouseOff").do_command(do_mouse_off)

    def do_place_at00(mouse_on = do_mouse_on):

        layout_before = this().Layout
        yxplace(0,0)
        mouse_on()

        send('POSITION_CHANGED',this()) # show this in X an Y Spinbox
        send("BASE_LAYOUT_CHANGED",layout_before) # and message to others


    widget("Place").do_command(do_place_at00)


    # used for pack and grid layout. the mouse events have to be destroyed

    def switch_off_mousemove(mouse_off = do_mouse_off):

        if type(this().mydata) is tuple or type(this().mydata) is list:
            if len(this().mydata) >= 3:
                if type(this().mydata[2]) is str:
                    if this().mydata[2] == 'mouse': mouse_off()


    do_receive('BASE_LAYOUT_PLACE_MOUSEOFF',switch_off_mousemove)


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

        MouseOn['state'] = state
        MouseOff['state'] = state
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
