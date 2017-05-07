
### CODE ===================================================
this().withdraw()

Toplevel("Introduction",title="DynTkInter GuiDesigner Introduction")

Menu("MouseMenu",activebackground='#ececac',link="introduction/mousemenu.py")

def top_level_closed(msg=None):
    cdApp()
    this().destroy()

proxy.do_receive(None,'TOPLEVEL_CLOSED',top_level_closed)

def activate_mousemenu(menu=widget("MouseMenu")):
    menu.select_menu()

do_receive('ACTIVATE_MOUSEMENU',activate_mousemenu)

Frame('Inside',link="introduction/img.py").grid(row=0,column=0)

cdApp()
this().config(title = 'Application Window')

### ========================================================

