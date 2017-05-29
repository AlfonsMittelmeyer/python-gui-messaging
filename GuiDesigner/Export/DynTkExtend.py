try:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk as ttk
except ImportError:
    import Tkinter as tk
    from Tkinter import *
    import ttk

# =========  Menu  ===================================================

class Menu(tk.Menu):

    def __init__(self,master,**kwargs):
        kwargs.pop('name',None)        
        tk.Menu.__init__(self,master,**kwargs)

    def add(self,itemtype,**kwargs):
        kwargs.pop('name',None)
        tk.Menu.add(self,itemtype,**kwargs)

    def add_command(self,**kwargs):
        self.add('command',**kwargs)

    def add_separator(self,**kwargs):
        self.add('separator',**kwargs)

    def add_checkbutton(self,**kwargs):
        self.add('checkbutton',**kwargs)

    def add_radiobutton(self,**kwargs):
        self.add('radiobutton',**kwargs)

    def add_cascade(self,**kwargs):
        self.add('cascade',**kwargs)

    def entryconfig(self,index,**kwargs):
        kwargs.pop('name',None)
        tk.Menu.entryconfig(self,index,**kwargs)

        # neccessary during menu creation at start up time
        if not index and self['tearoff']:
            self.after(1,lambda kwargs=kwargs,widget=self: tk.Menu.entryconfig(widget,0,**kwargs))
  
