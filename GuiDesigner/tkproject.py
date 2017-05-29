# -*- coding: utf-8 -*-
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from DynTkImports import *


# Application definition ============================

class BOStrab_Fahrzeugeinschraenkung(tk.Tk):

    def __init__(self,**kwargs):
        tk.Tk.__init__(self,**kwargs)
        self.myclass = 'BOStrab_Fahrzeugeinschraenkung'
        # widget definitions ===================================
        self.MainMenu = MenuGUI(self)
        self['menu'] = self.MainMenu

class MenuGUI(tk.Menu):

    def __init__(self,master,**kwargs):
        tk.Menu.__init__(self,master,**kwargs)
        self.myclass = 'MenuGUI'
        # widget definitions ===================================
        self.language_submenu = LanguageSubmenu(self,name='#0_language_submenu',tearoff=0)
        self.add_cascade(menu=self.language_submenu,label='Sprachen')
        # indexes for entryconfig later
        self.languages_index = 1

class LanguageSubmenu(tk.Menu):

    def __init__(self,master,**kwargs):
        tk.Menu.__init__(self,master,**kwargs)
        self.myclass = 'LanguageSubmenu'
        # widget definitions ===================================
        self.add_command(label='deutsch')
        # indexes for entryconfig later
        self.deutsch_index = 0
    # this was GuiDefinition by GuiDesigner Export (tkinter names)

        self.container = self # for compatibility with the following code

    # after GUI definition: the Code ===========================
    # this code may also be inserted in GuiDesigner Scripts
    
        self.create_menu()

    def create_menu(self):    

        # for calling more times, delete the menu, which existed before,
        # except the first command

        # for marking the end
        self.container.add_checkbutton()

        # now we delete the menu entries after deutsch
        after_deutsch = self.deutsch_index + 1
        while True:
            itemtype = self.container.type(after_deutsch)
            self.container.delete(after_deutsch)
            if itemtype == 'checkbutton':
                break
 
        # now we make a dynamic creation
        # first we get the style of the first command
        # this style should also be used for the other commands

        command_config = get_entryconfig(self.container,self.deutsch_index)
        
        # we dont't use some now not defined languagefile[i]
        # we can think later of this

        # now we create dynamic commands

        languages = ('deutsch','english','russisch','polnisch','italienisch',None,'spanisch','französisch',None,'dänisch')

        for language in languages:

            if not language:
                self.container.add_separator()
                continue
                
            command_config['label'] = language
            command_config['command'] = partial(self.do_action,language)
            self.container.add_command(**command_config)
                 
    def do_action(self,language):
        publish("SELECT_LANGUAGE",language)
            


BOStrab_Fahrzeugeinschraenkung().mainloop()
