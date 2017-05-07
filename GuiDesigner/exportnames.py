import DynTkInter as tk
import DynTkInter as ext
#import tkinter as tk
#import DynTkExtend as ext

class Application(tk.Tk):

    def __init__(self,**kwargs):
        tk.Tk.__init__(self,**kwargs)
        self.menu = Menu(self,name = 'menu')
        self.menu.select_menu()

class Menu(ext.Menu):

    def __init__(self,master,**kwargs):
        ext.Menu.__init__(self,master,**kwargs)
        self.command = ext.MenuItem(self,'command',name = 'command',label='command')
        ext.dynTkImage(self.command,'/home/pi/GitProject/python-gui-messaging/GuiDesigner/Images/butterfly.gif')
        self.command2 = ext.MenuItem(self,'command',name = 'command2',label='command2')
        self.command.layout(index=1)
        self.command2.layout(index=2)

Application().mainloop('guidesigner/Guidesigner.py')
#Application().mainloop()
