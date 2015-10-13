Toplevel("DynTkInterGuiDesigner",title="DynTkInter GuiDesigner",geometry='+0+0',link="guidesigner/Modules.py")

Menu("TopMenu",activebackground='#ececac',link="guidesigner/TopMenu.py").select_menu()

### CODE ===================================================

def top_level_closed(msg):
    if not widget_exists(msg._widget): send('SELECTION_CHANGED')
    else: setSelection(msg)

do_receive('TOPLEVEL_CLOSED',top_level_closed,wishMessage=True)

cdApp()
send("SELECTION_CHANGED")

### ========================================================
