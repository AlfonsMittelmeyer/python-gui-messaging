Toplevel('HelpSaveAccess',**{'title': 'Save Access', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(13, 10, 0, 0)'})

Message('access_widgets',**{'text': 'mylabel_hello = access.mylabel_hello\nmybutton_ok = access.mybutton_ok', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('after_access_widgets',**{'text': 'If your GUI is more complex and you use different names for container widgets, but not for all widgets like labels or buttons in the container widgets, then you may use Save Access -> Container Depth. For container widgets you get the access in the same way as before and the widgets you access by the normal interface function widget(parent,name_in_gui):', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Message('after_load',**{'text': 'Then you may access your widgets simply by:', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Button('close',**{'text': 'Close'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '11'})
Message('lead_text',**{'text': "There may be different opinions, whether this functionality is very useful or not. It may give you a quick start. But it's not really recommended to use it for complex applications.\n\nIf all of your widgets have different names, you may use Save Access -> Widget Depth for accessing your widgets. After you have saved your GUI, maybe as 'mygui.py' you save the access, maybe as 'mygui.acc'\n\nIn your programm you load the gui and the access:", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Message('load_gui_access',**{'text': "tk.load_script('mygui.py')\naccess = tk.DynAccess('mygui.acc')", 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '4'})
Message('not_needed',**{'text': "Because the normal interface function widget(name_in_gui) - sufficient for widgets in the Application window - or widget(parent,name_in_gui) let you access first a widget, and afterwards its children, the Save Access functionality isn't really needed. So you may also access the GUI without Save Access.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '9'})
Label('title',**{'text': 'Save Access', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})
Message('widget_interface',**{'text': "myframe_customer = access.myframe_customer\ncustomer_name = widget(myframe_customer,'name')", 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '8'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================

