config(**{'relief': 'groove', 'grid_rows': '(7, 40, 0, 0)', 'bd': 2, 'grid_multi_rows': '[7, (0, 0, 0, 0)]', 'grid_cols': '(3, 0, 0, 0)', 'grid_multi_cols': '[3, (0, 5, 0, 0)]'})

Label('lnone',**{'bg': 'white', 'text': 'label text', 'photoimage': 'guidesigner/images/image.gif'}).grid(row=1, sticky='nesw', column=2)
Label('lcenter',**{'bg': 'white', 'text': 'label text', 'compound': 'center', 'photoimage': 'guidesigner/images/image.gif'}).grid(row=2, sticky='nesw', column=2)
Label('lleft',**{'bg': 'white', 'text': 'label text', 'compound': 'left', 'photoimage': 'guidesigner/images/image.gif'}).grid(row=3, sticky='nesw', column=2)
Label('lright',**{'bg': 'white', 'text': 'label text', 'compound': 'right', 'photoimage': 'guidesigner/images/image.gif'}).grid(row=4, sticky='nesw', column=2)
ttk.Radiobutton('bnone',**{'value': 'none', 'text': 'none'}).grid(row=1, sticky='nesw', column=1)
ttk.Radiobutton('bcenter',**{'value': 'center', 'text': 'center'}).grid(row=2, sticky='nesw', column=1)
ttk.Radiobutton('bleft',**{'value': 'left', 'text': 'left'}).grid(row=3, sticky='nesw', column=1)
ttk.Radiobutton('bright',**{'value': 'right', 'text': 'right'}).grid(row=4, sticky='nesw', column=1)
ttk.Separator('separator').grid(row=1, sticky='esw', columnspan=4)
ttk.Separator('separator').grid(row=2, sticky='esw', columnspan=4)
ttk.Separator('separator').grid(row=3, sticky='esw', columnspan=4)
ttk.Separator('separator').grid(row=4, sticky='esw', columnspan=4)
ttk.Radiobutton('bbottom',**{'value': 'bottom', 'text': 'bottom'}).grid(row=5, sticky='nesw', column=1)
Label('lbottom',**{'bg': 'white', 'text': 'label text', 'compound': 'bottom', 'photoimage': 'guidesigner/images/image.gif'}).grid(row=5, sticky='nesw', column=2)
ttk.Radiobutton('btop',**{'value': 'top', 'text': 'top'}).grid(row=6, sticky='nesw', column=1)
Label('ltop',**{'bg': 'white', 'text': 'label text', 'compound': 'top', 'photoimage': 'guidesigner/images/image.gif'}).grid(row=6, sticky='nesw', column=2)
ttk.Separator('separator').grid(row=5, sticky='esw', columnspan=4)
### CODE ===================================================

class Main():


    def __init__(self):
        self.me = container()
        self.option = None


        self.compound_var = StringVar()
        self.height = 0
        widget('bnone').config(variable=self.compound_var,command=self.set_compound)
        widget('bleft').config(variable=self.compound_var,command=self.set_compound)
        widget('bright').config(variable=self.compound_var,command=self.set_compound)
        widget('btop').config(variable=self.compound_var,command=self.set_compound)
        widget('bbottom').config(variable=self.compound_var,command=self.set_compound)
        widget('bcenter').config(variable=self.compound_var,command=self.set_compound)

        widget('lnone').bind('<Button-1>',lambda event:self.set_compound('none'))
        widget('lleft').bind('<Button-1>',lambda event:self.set_compound('left'))
        widget('lright').bind('<Button-1>',lambda event:self.set_compound('right'))
        widget('ltop').bind('<Button-1>',lambda event:self.set_compound('top'))
        widget('lbottom').bind('<Button-1>',lambda event:self.set_compound('bottom'))
        widget('lcenter').bind('<Button-1>',lambda event:self.set_compound('center'))

        do_receive("SET_COMPOUND",self.set_compound_init,True,wishMessage=True)
        do_receive('SELECTION_CHANGED',lambda me = self.me: me.unlayout())
        do_receive('BASE_LAYOUT_CHANGED',lambda me = self.me, self = self: me.unlayout() if self.option == 'layout' else '')
        

    def set_compound(self,value=None):
        if value:
            self.compound_var.set(value)
        if widget_exists(self.compound_widget): # not neccessary because of 'SELECTION_CHANGED'
            if self.option == 'layout':
                self.compound_widget.setlayout('compound',self.compound_var.get())
            else:
                self.compound_widget['compound'] = self.compound_var.get()
            if widget_exists(self.fill_widget):
                self.fill_widget.delete(0,'end')
                self.fill_widget.insert(0,self.compound_var.get())
        self.me.unlayout()

    def set_position(self,y):
        self.get_height()
        if y + self.height > self.me.master.winfo_height():
            self.me.place(y=0,rely=1,anchor='sw')

    def get_height(self):
        self.height = self.me.winfo_height()

    def set_compound_init(self,msg,set_center):

        # x,y are absolute coordinates
        x = msg[0] # column for layout
        y = msg[1] # row for layout

        self.compound_widget = this()
        self.option=msg[2] # we know, it's 'compound', but we have to distinguish 'config' or 'layout'
        self.fill_widget = msg[3]
        if self.option == 'layout':
            self.compound_var.set(this().getlayout('compound'))
        else:
            self.compound_var.set(this()['compound'])

        self.me.lift()
        if self.option == 'layout':
            self.me.rcgrid(y,x,sticky='nw')
            if not self.height:
                self.me.after(100,self.get_height)
        else:
            if not self.height:
                self.me.place(x=x,y=y)
                self.me.after(100,self.set_position,y)
            elif y + self.height > self.me.master.winfo_height():
                self.me.place(x=x,y=0,rely=1,anchor='sw')
            else:
                self.me.place(x=x,y=y)
        
Main()

### ========================================================
