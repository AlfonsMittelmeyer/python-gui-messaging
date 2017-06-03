try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import appcode

class BOStrab_Fahrzeugeinschraenkung(tk.Tk):

    def __init__(self,**kwargs):
        tk.Tk.__init__(self,**kwargs)
        # widget definitions ===================================
        self.MainMenu = MenuGUI(self)
        self['menu'] = self.MainMenu
        self.plotframe = PlotFrame(self,text='Madplotlib')
        self.plotframe.pack()

class MenuGUI(tk.Menu):

    def __init__(self,master,**kwargs):
        tk.Menu.__init__(self,master,**kwargs)
        # widget definitions ===================================
        self.language_submenu = LanguageSubmenu(self,tearoff=0)
        self.add_cascade(menu=self.language_submenu,label='Sprachen')
        self.add_command(label='Test')
        # indexes for entryconfig later
        self.languages_index = 1
        self.test_index = 2
        # call Code ===================================
        appcode.MenuGUI(self)

class LanguageSubmenu(tk.Menu):

    def __init__(self,master,**kwargs):
        tk.Menu.__init__(self,master,**kwargs)
        # widget definitions ===================================
        self.add_command(label='deutsch')
        # indexes for entryconfig later
        self.deutsch_index = 0
        # call Code ===================================
        appcode.LanguageSubmenu(self)

class PlotFrame(tk.LabelFrame):

    def __init__(self,master,**kwargs):
        tk.LabelFrame.__init__(self,master,**kwargs)
        # call Code ===================================
        appcode.PlotFrame(self)

BOStrab_Fahrzeugeinschraenkung().mainloop()
