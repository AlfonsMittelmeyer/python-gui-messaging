Toplevel('HelpAccessWidgets.py',**{'title': 'Accessing Widgets', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(16, 10, 0, 0)'})

Button('close',**{'text': 'Close'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '14'})
Message('instead_code',**{'text': "mybutton = tk.Button(parent,**configdata)\nmybutton.grid(**layoutdata)\nmybutton['command'] = somefunction", 'font': 'TkFixedFont 9 bold', 'width': '600', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('instead_comment',**{'text': '# instead of', 'font': 'TkFixedFont 9 bold', 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Message('isnt_it',**{'text': "Easy and simple, isn't it?", 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '12'})
Message('lazy_code',**{'text': "mybutton = tk.widget(parent,'mybutton',1)\nmybutton['command'] = somefunction", 'font': 'TkFixedFont 9 bold', 'width': '600', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '10'})
Message('lazy_comment',**{'text': "# and if you were lazy and three buttons have the same name in this container widget\n# (not recommended but no problem)\n# and if it's the second one", 'font': 'TkFixedFont 9 bold', 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '9'})
Message('lead_text',**{'text': "Widgets are accessed by using the function: widget\n\nFor accessing widgets in the main script, you use this function with the parent as first parameter. The second parameter is the name string and optinally there may be a third parameter for an index, if more than one widgets have the same name.\n\nYou write your programs in the same way as before, but don't code config data and don't code the layout. Instead you simply use the name.", 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Message('simply_code',**{'text': "mybutton = tk.widget(parent,'mybutton')\nmybutton['command'] = somefunction", 'font': 'TkFixedFont 9 bold', 'width': '600', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '8'})
Message('simply_comment',**{'text': '# you simply write, when you used the GuiDesigner and loaded the script', 'font': 'TkFixedFont 9 bold', 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Label('title',**{'text': 'Accessing Widgets', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================
