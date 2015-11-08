config(**{'title': 'Link. Save and Load', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(32, 10, 0, 0)'})

Message('after_code_line',**{'text': "Only the link to the content of the menu was saved, but not, what's inside.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '15'})
Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '30'})
Label('code_line',**{'text': "Menu('menu',**{'link': 'guidesigner/TopMenu.py'}).select_menu()", 'padx': '6', 'font': 'TkFixedFont 9 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '14'})
Label('compare',**{'text': "Let's compare the saved files", 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '12'})
Label('compare_load',**{'text': "Let's compare 'Load & Edit' and 'Load & Run'", 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '17'})
Message('compare_text',**{'text': "File menu1.py contains the complete GUI of the menu, but only the GUI and no source code. The link wasn't saved.\n\nFile menu_part.py contains only one line of code:", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '13'})
Label('experiment',**{'text': 'One experiment more', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '20'})
Message('experiment_text',**{'text': "Load the file menu_part.py via 'Load & Edit' and save it via File->Save as menu2.py. What do you think, would happen? Please look into the saved File.\n\nThe menu was saved completely inclusive all its source code. Did you think this?", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '21'})
Label('explenation',**{'text': 'Explenation', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '23'})
Message('explenation_text',**{'text': "The first time we loaded the menu content just by setting the link option. This is a DynTkInter container widget option, which simply executes this script. But now we had loaded the script via 'Load & Edit' of the GuiDesigner. And the GuiDesigner loads scripts inclusive source code sections. So also additional source code was saved.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '24'})
Label('howto_split',**{'text': 'How to split GUIs', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '26'})
LinkLabel('howto_split_link',**{'text': 'how_to_split', 'font': 'TkFixedFont 12 bold underline', 'bg': 'white', 'link': 'guidesigner/HowToSplit.py', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '3', 'sticky': 'nesw', 'columnspan': '4', 'row': '28'})
Message('howto_split_text',**{'text': 'File menu2.py delivered us a joined GUI. Now we can discuss how to', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '27'})
Message('howto_split_text2',**{'text': 'split a joined GUI:', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '2', 'row': '28'})
Message('lead_text',**{'text': 'In your application you create a menu und set the layout (Select).\nThen in Config you enter as link: guidesigner/TopMenu.py\n\nThe GuiDesigner menu appears in your application and it works.', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '4'})
Label('link_label',**{'text': "Let's begin with the link", 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('link_save',**{'text': "Let's save by using File -> Save", 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('link_save_text',**{'text': 'Save the GUI in a file menu1.py', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Message('load_text',**{'text': "When you load File menu1.py thenn there is no difference, whether you load it via 'Load & Edit' or 'Load & Run', because it's only the GUI and no additional code.\n\nBut when you load File menu_part.py, then there is a difference. When you load iit by 'Load & Run', then it works.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '18'})
Label('save_part',**{'text': "Let's save by using File -> Split & Join -> Save (part)", 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '9'})
Message('save_part_text',**{'text': "If you use Save (part), you first have to select, which part you like to save. By pressing button '/' in module 'Selection' select the root.\n\nThen save the GUI in a file menu_part.py", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '10'})
Label('title',**{'text': 'Link, Save and Load (example)', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================
