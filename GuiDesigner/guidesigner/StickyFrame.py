config(**{'grid_cols': '(5, 40, 0, 1)', 'grid_multi_rows': '[5, (0, 0, 0, 0), (2, 0, 0, 0), (4, 0, 0, 0)]', 'grid_rows': '(5, 40, 0, 1)', 'grid_multi_cols': '[5, (0, 0, 0, 0), (2, 0, 0, 0), (4, 0, 0, 0)]'})

Frame('frame0',**{'grid_cols': '(1, 40, 0, 0)', 'padx': '3', 'grid_rows': '(1, 40, 0, 0)', 'pady': '3', 'bd': 2})
goIn()

Frame('nw',**{'bg': 'blue'}).place(relwidth='0.25', relheight='0.25', y='0', x='0')
Frame('ne',**{'bg': 'blue'}).place(relx='1', relwidth='0.25', anchor='ne', relheight='0.25', y='0', x='0')
Frame('w',**{'bg': 'blue'}).place(rely='0.5', relwidth='0.25', anchor='w', relheight='0.25', y='0', x='0')
Frame('e',**{'bg': 'blue'}).place(relx='1', rely='0.5', relwidth='0.25', anchor='e', relheight='0.25', y='0', x='0')
Frame('n',**{'bg': 'blue'}).place(relx='0.5', relwidth='0.25', anchor='n', relheight='0.25', y='0', x='0')
Frame('sw',**{'bg': 'blue'}).place(rely='1', relwidth='0.25', anchor='sw', relheight='0.25', y='0', x='0')
Frame('s',**{'bg': 'blue'}).place(relx='0.5', rely='1', relwidth='0.25', anchor='s', relheight='0.25', y='0', x='0')
Frame('se',**{'bg': 'blue'}).place(relx='1', rely='1', relwidth='0.25', anchor='se', relheight='0.25', y='0', x='0')
Frame('center',**{'relief': 'solid', 'bg': 'blue'}).place(relx='0.5', rely='0.5', relwidth='0.25', anchor='center', relheight='0.25', y='0', x='0')

goOut()
grid(column=1, sticky='nesw', row=1)
Frame('frame1',**{'grid_cols': '(1, 40, 0, 0)', 'padx': '3', 'grid_rows': '(1, 40, 0, 0)', 'pady': '3', 'bd': 2})
goIn()

Frame('nwe',**{'bg': 'blue'}).place(relwidth='1', relheight='0.25', y='0', x='0')
Frame('we',**{'bg': 'blue'}).place(rely='0.5', relwidth='1', anchor='w', relheight='0.25', y='0', x='0')
Frame('swe',**{'bg': 'blue'}).place(rely='1', relwidth='1', anchor='sw', relheight='0.25', y='0', x='0')

goOut()
grid(column=3, sticky='nesw', row=1)
Frame('frame2',**{'grid_cols': '(1, 40, 0, 0)', 'padx': '3', 'grid_rows': '(1, 40, 0, 0)', 'pady': '3', 'bd': 2})
goIn()

Frame('wns',**{'bg': 'blue'}).place(relwidth='0.25', relheight='1', y='0', x='0')
Frame('ens',**{'bg': 'blue'}).place(relx='1', relwidth='0.25', anchor='ne', relheight='1', y='0', x='0')
Frame('ns',**{'bg': 'blue'}).place(relx='0.5', relwidth='0.25', anchor='n', relheight='1', y='0', x='0')

goOut()
grid(column=1, sticky='nesw', row=3)
Frame('frame3',**{'grid_cols': '(1, 40, 0, 0)', 'padx': '3', 'grid_rows': '(1, 40, 0, 0)', 'pady': '3', 'bd': 2})
goIn()

Frame('news',**{'bg': 'blue'}).place(relwidth='1', relheight='1', y='0', x='0')

goOut()
grid(column=3, sticky='nesw', row=3)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(rowspan=5, sticky='ns', row=0)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(column=2, rowspan=5, sticky='ns', row=0)
ttk.Separator('separator',**{'orient': 'vertical'}).grid(column=4, rowspan=5, sticky='ns', row=0)
ttk.Separator('separator').grid(column=1, columnspan=5, sticky='ew', row=0)
ttk.Separator('separator').grid(column=1, columnspan=5, sticky='ew', row=2)
ttk.Separator('separator').grid(column=1, columnspan=5, sticky='ew', row=4)

### CODE ===================================================

class Main():


    def __init__(self):
        self.me = container()
        #self.me['width'] = 166
        #self.me['height'] = 166
    
        widget('.','frame0','nw').do_event('<ButtonRelease-1>',self.set_sticky,'nw')
        widget('.','frame0','n').do_event('<ButtonRelease-1>',self.set_sticky,'n')
        widget('.','frame0','ne').do_event('<ButtonRelease-1>',self.set_sticky,'ne')

        widget('.','frame0','w').do_event('<ButtonRelease-1>',self.set_sticky,'w')
        widget('.','frame0','center').do_event('<ButtonRelease-1>',self.set_sticky,'')
        widget('.','frame0','e').do_event('<ButtonRelease-1>',self.set_sticky,'e')

        widget('.','frame0','sw').do_event('<ButtonRelease-1>',self.set_sticky,'sw')
        widget('.','frame0','s').do_event('<ButtonRelease-1>',self.set_sticky,'s')
        widget('.','frame0','se').do_event('<ButtonRelease-1>',self.set_sticky,'se')

        widget('.','frame1','nwe').do_event('<ButtonRelease-1>',self.set_sticky,'nwe')
        widget('.','frame1','we').do_event('<ButtonRelease-1>',self.set_sticky,'we')
        widget('.','frame1','swe').do_event('<ButtonRelease-1>',self.set_sticky,'swe')

        widget('.','frame2','wns').do_event('<ButtonRelease-1>',self.set_sticky,'wns')
        widget('.','frame2','ns').do_event('<ButtonRelease-1>',self.set_sticky,'ns')
        widget('.','frame2','ens').do_event('<ButtonRelease-1>',self.set_sticky,'ens')

        widget('.','frame3','news').do_event('<ButtonRelease-1>',self.set_sticky,'news')

        do_receive("SELECT_STICKY",self.select_sticky,wishMessage=True)
        do_receive('SELECTION_CHANGED',lambda me = self.me: me.unlayout())
        do_receive('BASE_LAYOUT_CHANGED',lambda me = self.me: me.unlayout())

        self.sticky_dict = {

            'nw':widget('.','frame0','nw'),
            'n':widget('.','frame0','n'),
            'ne':widget('.','frame0','ne'),
            'w':widget('.','frame0','w'),
            '':widget('.','frame0','center'),
            'e':widget('.','frame0','e'),
            'sw':widget('.','frame0','sw'),
            's':widget('.','frame0','s'),
            'es':widget('.','frame0','se'),
            'new':widget('.','frame1','nwe'),
            'ew':widget('.','frame1','we'),
            'esw':widget('.','frame1','swe'),
            'nsw':widget('.','frame2','wns'),
            'ns':widget('.','frame2','ns'),
            'nes':widget('.','frame2','ens'),
            'nesw':widget('.','frame3','news')

        }

        self.sticky_translate = {

            '' : '',
            'w' : 'w',
            'e' : 'e',
            'n' : 'n',
            's' : 's',

            'we' : 'ew',
            'wn' : 'nw',
            'ws' : 'sw',
            'ew' : 'ew',
            'en' : 'ne',
            'es' : 'es',
            'nw' : 'nw',
            'ne' : 'ne',
            'ns' : 'ns',
            'sw' : 'sw',
            'se' : 'es',
            'sn' : 'ns',

            'wen' : 'new',
            'wes' : 'esw',
            'wne' : 'new',
            'wns' : 'nsw',
            'wse' : 'esw',
            'wsn' : 'nsw',

            'ewn' : 'new',
            'ews' : 'esw',
            'enw' : 'new',
            'ens': 'nes',
            'esw' : 'esw',
            'esn' : 'nes',

            'nwe' : 'new',
            'nws' : 'nsw',
            'new' : 'new',
            'nes' : 'nes',
            'nsw' : 'nsw',
            'nse' : 'nes',

            'swe' : 'esw',
            'swn' : 'nsw',
            'sew' : 'esw',
            'sen' : 'nes',
            'snw' : 'nsw',
            'sne' : 'nes',

            'swen' : 'nesw',
            'nwes' : 'nesw',
            'swne' : 'nesw',
            'ewns' : 'nesw',
            'nwse' : 'nesw',
            'ewsn' : 'nesw',

            'sewn' : 'nesw',
            'news' : 'nesw',
            'senw' : 'nesw',
            'wens':  'nesw',
            'nesw' : 'nesw',
            'wesn' : 'nesw',

            'snwe' : 'nesw',
            'enws' : 'nesw',
            'snew' : 'nesw',
            'wnes' : 'nesw',
            'ensw' : 'nesw',
            'wnse' : 'nesw',

            'nswe' : 'nesw',
            'eswn' : 'nesw',
            'nsew' : 'nesw',
            'wsen' : 'nesw',
            'esnw' : 'nesw',
            'wsne' : 'nesw',
        }


    def set_sticky(self,value):
        if widget_exists(self.sticky_widget) and self.sticky_widget.Layout in (GRIDLAYOUT,PAGELAYOUT):
            self.sticky_widget.setlayout('sticky',value)
            if self.sticky_widget == this():
                send("LAYOUT_VALUES_REFRESH")
        self.me.unlayout()

    def select_sticky(self,msg):
        self.sticky_widget = this()
        x = msg[0]
        y = msg[1]
        option = msg[2]
        for widget in self.sticky_dict.values():
            widget.config(bg='blue',highlightthickness = 0)

        sticky=self.sticky_widget.getlayout('sticky')
        sticky = self.sticky_translate[sticky]

        frame_widget = self.sticky_dict[sticky]
        hi_thick = 4
        frame_widget.config(bg='yellow',highlightthickness = hi_thick,highlightbackground='blue')

        self.me.yxplace(y,x,width=166,height=166)

Main()

### ========================================================
