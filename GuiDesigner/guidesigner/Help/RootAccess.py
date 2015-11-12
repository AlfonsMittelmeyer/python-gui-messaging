Toplevel('HelpRootAccess',**{'title': 'Root Access', 'grid_cols': '(7, 75, 0, 0)', 'grid_multi_cols': '[7, (0, 10, 0, 0), (6, 10, 0, 0)]', 'grid_rows': '(17, 10, 0, 0)'})

Label('app_and_top',**{'text': 'Application and Toplevel Root', 'font': 'TkDefaultFont 11 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '9'})
Message('app_and_top_text',**{'text': "The root addressed by widget('/') doesn't neccessarily mean the Application window. If you are somewhere in the Application window, it means the Application window, but if you are somewhere in a Toplevel window, it means the Toplevel window.", 'width': '430', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '10'})
Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '5', 'sticky': 'nesw', 'row': '15'})
Message('lead_text',**{'text': "In the Main Script it shouldn't be a problem for accessing the root. Normally you should have a reference for it. When you write code in the script, there is also the Root Path Name.", 'width': '430', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '3'})
Label('root_path',**{'text': 'Root Path Name', 'font': 'TkDefaultFont 11 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '5'})
Message('root_path_text',**{'text': "The Root Path Name begins with'/'. So you access the root window:", 'width': '430', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '6'})
Message('root_window_code',**{'text': "widget('/')", 'font': 'TkFixedFont 9 bold', 'width': '430', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '7'})
Message('syntax_text',**{'text': "The syntax is the same as for the Relative Path Name and the Full Path Name. You may add further parameters for addressing widgets more inside. But don't forget, in the creation phase not all is already created, what is outside of your current position.", 'width': '430', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '13'})
Label('syntax_title',**{'text': 'Syntax', 'font': 'TkDefaultFont 11 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '12'})
Label('title',**{'text': 'Root Access', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '1'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================
