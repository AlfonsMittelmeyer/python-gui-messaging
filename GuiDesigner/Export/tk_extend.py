try:
    from tkinter import *
    import tkinter as tk_original
except ImportError:
    from Tkinter import *
    import Tkinter as tk_original


class Menu(tk_original.Menu):

    def entryconfig(self,index,**kwargs):

        if kwargs and self['tearoff'] and not index:
            self.after_idle( lambda
                             function = tk_original.Menu.entryconfig,
                             menu = self,
                             kwargs = kwargs :
                             function(menu,0,**kwargs)
                             )
        return tk_original.Menu.entryconfig(self,index,**kwargs)
                
        
