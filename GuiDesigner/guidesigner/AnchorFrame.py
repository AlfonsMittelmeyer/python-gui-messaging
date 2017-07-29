config(**{'padx': '3', 'relief': 'solid', 'pady': '3', 'bd': 2})

Frame('nw',**{'bg': 'blue'}).place(y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('ne',**{'bg': 'blue'}).place(relx='1', anchor='ne', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('w',**{'bg': 'blue'}).place(rely='0.5', anchor='w', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('e',**{'bg': 'blue'}).place(relx='1', rely='0.5', anchor='e', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('n',**{'bg': 'blue'}).place(relx='0.5', anchor='n', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('sw',**{'bg': 'blue'}).place(rely='1', anchor='sw', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('s',**{'bg': 'blue'}).place(relx='0.5', rely='1', anchor='s', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('se',**{'bg': 'blue'}).place(relx='1', rely='1', anchor='se', y='0', relheight='0.25', x='0', relwidth='0.25')
Frame('center',**{'bg': 'blue', 'relief': 'solid'}).place(relx='0.5', rely='0.5', anchor='center', y='0', relheight='0.25', x='0', relwidth='0.25')

### CODE ===================================================

class Main():


    def __init__(self):
        self.me = container()
        self.center = widget('center')
        self.option = None
    
        widget('nw').do_event('<ButtonRelease-1>',self.set_anchor,'nw')
        widget('n').do_event('<ButtonRelease-1>',self.set_anchor,'n')
        widget('ne').do_event('<ButtonRelease-1>',self.set_anchor,'ne')

        widget('w').do_event('<ButtonRelease-1>',self.set_anchor,'w')
        widget('center').do_event('<ButtonRelease-1>',self.set_anchor,'center')
        widget('e').do_event('<ButtonRelease-1>',self.set_anchor,'e')

        widget('sw').do_event('<ButtonRelease-1>',self.set_anchor,'sw')
        widget('s').do_event('<ButtonRelease-1>',self.set_anchor,'s')
        widget('se').do_event('<ButtonRelease-1>',self.set_anchor,'se')


        do_receive("SET_ANCHOR",self.select_anchor,True,wishMessage=True)
        do_receive("SET_LABELANCHOR",self.select_anchor,False,wishMessage=True)
        do_receive('SELECTION_CHANGED',lambda me = self.me: me.place_forget())
        do_receive('BASE_LAYOUT_CHANGED',lambda me = self.me, self = self: me.place_forget() if self.option == 'layout' else '')


        self.anchor_dict = {
            'nw' : widget('nw'),
            'n' : widget('n'),
            'ne':widget('ne'),
            'w':widget('w'),
            'center':widget('center'),
            'e':widget('e'),
            'sw':widget('sw'),
            's':widget('s'),
            'se':widget('se')
        }


    def set_anchor(self,value):
        if widget_exists(self.anchor_widget):
            if self.option == 'layout':
                if self.anchor_widget.Layout == PLACELAYOUT:
                    self.anchor_widget.place(anchor = value)
                elif self.anchor_widget.Layout == PACKLAYOUT:
                    self.anchor_widget.pack(anchor = value)
            else:
                self.anchor_widget[self.option] = value
            if widget_exists(self.fill_widget):
                self.fill_widget.delete(0,'end')
                self.fill_widget.insert(0,value)
        self.me.place_forget()

    def select_anchor(self,msg,set_center):
        x = msg[0]
        y = msg[1]
        self.option=msg[2]
        self.fill_widget = msg[3]
        self.anchor_widget=this()

        for widget in self.anchor_dict.values():
            widget.config(bg='blue',highlightthickness = 0)

        if self.option == 'layout':
            frame_widget = self.anchor_dict[self.anchor_widget.getlayout("anchor")]
        else:
            frame_widget = self.anchor_dict[self.anchor_widget[self.option]]
        hi_thick = 4
        frame_widget.config(bg='yellow',highlightthickness = hi_thick,highlightbackground='blue')

        master_height = self.me.master.winfo_height()

        y += 80 # own height, because of anchor 'sw'
        if y > master_height:
            y = master_height

        # distinguish anchor and labelanchor
        if set_center:
            self.center.place(relx='0.5', rely='0.5', anchor='center', y='0', relheight='0.25', x='0', relwidth='0.25')
        else:
            self.center.place_forget()
            
        self.me.place(x=x,y=y,width=80,height=80,anchor = 'sw')
        
Main()

### ========================================================
