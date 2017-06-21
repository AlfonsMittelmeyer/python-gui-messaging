# -*- coding: utf-8 -*-
import DynTkInter as tk

try:
    from tkinter import ttk as StatTtk
    from tkinter.ttk import *
except ImportError:
    import ttk as StatTtk
    from ttk import *

class Label(tk.GuiElement,StatTtk.Label):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Label,self,myname,"label")

class Button(tk.GuiElement,StatTtk.Button):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Button,self,myname,"button")

class Checkbutton(tk.GuiElement,StatTtk.Checkbutton):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Checkbutton,self,myname,"checkbutton")

class Radiobutton(tk.GuiElement,StatTtk.Radiobutton):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Radiobutton,self,myname,"radiobutton")

class Entry(tk.GuiElement,StatTtk.Entry):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Entry,self,myname,"entry")

class Scale(tk.GuiElement,StatTtk.Scale):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Scale,self,myname,"scale")

class Scrollbar(tk.GuiElement,StatTtk.Scrollbar):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Scrollbar,self,myname,"scrollbar")

class Frame(tk.GuiContainer,StatTtk.Frame):
    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.Frame,self,myname,"frame",True)

class LabelFrame(tk.GuiContainer,StatTtk.LabelFrame):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.LabelFrame,self,myname,"labelframe",True)

class Separator(tk.GuiElement,StatTtk.Separator):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Separator,self,myname,"separator")

class Combobox(tk.GuiElement,StatTtk.Combobox):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Combobox,self,myname,"combobox")

    def fillString(self,string):
        values = [e for e in string.split("\n")]
        self['values'] = values

    def getString(self): return "\n".join(self['values'])


# =======================================================================================

    def addclearinit_addconfig(self,kwargs):
        tk.Listbox.addclearinit_addconfig(self,kwargs)

    def addinit_addconfig(self,kwargs):
        tk.Listbox.addinit_addconfig(self,kwargs)

    def executeclear_addconfig(self,kwargs):
        tk.GuiElement.executeclear_addconfig(self,kwargs)
        if 'text' in kwargs:
            self.fillString(kwargs.pop('text'))
            self.current(newindex=0) 

    def addconfig(self,kwargs):
        tk.GuiElement.addconfig(self,kwargs)
        kwargs['text'] = self.getString()
        kwargs.pop('values',None)
        

    def clear_addconfig(self,kwargs):
        tk.Listbox.clear_addconfig(self,kwargs)
        kwargs.pop('values',None)

# =======================================================================================


class LabelFrame(tk.GuiContainer,StatTtk.LabelFrame):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.LabelFrame,self,myname,"labelframe",True)

class PanedWindow(tk.GuiContainer,StatTtk.PanedWindow):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.PanedWindow,self,myname,"panedwindow")
        
        self.is_setsashes = False

    def pane(self,*args,**kwargs):
        return StatTtk.PanedWindow.pane(self,*args,**kwargs)

    def add(self,child,*args,**kwargs):
        child.Layout = tk.TTKPANELAYOUT
        self.tkClass.add(self,child,*args,**kwargs)

    def forget(self,child):
        child.Layout = tk.NOLAYOUT
        StatTtk.PanedWindow.forget(self,child)

    def insert(self,pos,child,**kwargs):
        child.Layout = tk.TTKPANELAYOUT
        StatTtk.PanedWindow.insert(self,pos,child,**kwargs)


class Menubutton(tk.GuiContainer,StatTtk.Menubutton):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.Menubutton,self,myname,"menubutton")

class Progressbar(tk.GuiElement,StatTtk.Progressbar):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Progressbar,self,myname,"progressbar")


class Sizegrip(tk.GuiElement,StatTtk.Sizegrip):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Sizegrip,self,myname,"sizegrip")


class Treeview(tk.GuiElement,StatTtk.Treeview):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Treeview,self,myname,"treeview")


class Separator(tk.GuiElement,StatTtk.Separator):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Separator,self,myname,"separator")


class Notebook(tk.GuiContainer,StatTtk.Notebook):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.Notebook,self,myname,"notebook")

    def add(self,child,**kwargs):
        child.Layout = tk.PAGELAYOUT
        StatTtk.Notebook.add(self,child,**kwargs)

    def insert(self,pos,child,**kwargs):
        child.Layout = tk.PAGELAYOUT
        StatTtk.Notebook.insert(self,pos,child,**kwargs)

    def forget(self,tab_id):
        before = self.tabs()
        StatTtk.Notebook.forget(self,tab_id)
        after = self.tabs()

        forgotten = None
        for element in before:
            if element not in after:
                forgotten = self.nametowidget(element)
                break
        if forgotten:
            forgotten.Layout = tk.NOLAYOUT
        

    #tab(tab_id, option=None, **kw)
        #Query or modify the options of the specific tab_id.
        #If kw is not given, returns a dictionary of the tab option values. If option is specified, returns the value of that option. Otherwise, sets the options to the corresponding values.


    #index(tab_id)
        #Returns the numeric index of the tab specified by tab_id, or the total number of tabs if tab_id is the string “end”.


    #select(tab_id=None)
        #Selects the specified tab_id.
        #The associated child window will be displayed, and the previously-selected window (if different) is unmapped. If tab_id is omitted, returns the widget name of the currently selected pane.




    #tabs()
        #Returns a list of windows managed by the notebook.

    #enable_traversal()
        #Enable keyboard traversal for a toplevel window containing this notebook.

        #This will extend the bindings for the toplevel window containing the notebook as follows:

            #Control-Tab: selects the tab following the currently selected one.
            #Shift-Control-Tab: selects the tab preceding the currently selected one.
            #Alt-K: where K is the mnemonic (underlined) character of any tab, will select that tab.

        #Multiple notebooks in a single toplevel may be enabled for traversal, including nested notebooks. However, notebook traversal only works properly if all panes have the notebook they are in as master.



