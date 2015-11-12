config(**{'title': 'link - Config Option', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(9, 10, 0, 0)'})

Button('close',**{'text': 'Close'}).grid(**{'column': '1', 'sticky': 'ew', 'pady': '4', 'row': '7'})
Message('example',**{'text': 'The link option of LinkLabel and Linkbutton is different. It will be executed, when this label or button is pressed and this link option will be saved ever.\n\nFor better understanding, we should do an example for link, save and load', 'width': '500', 'bd': '2', 'bg': '#ffffe0', 'relief': 'solid', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'pady': '5', 'row': '6'})
LinkLabel('link_save_load',**{'text': 'link, save and load', 'font': 'TkFixedFont 12 bold underline', 'link': 'guidesigner/Help/LinkSaveLoad.py', 'fg': 'blue'}).grid(**{'column': '4', 'sticky': 'nes', 'columnspan': '3', 'row': '7'})
Message('save_types',**{'text': "Menu item File -> Save saves whole the GUI. And instead of the link entries it saves the contents of the container widgets.\n\nMenu item File -> Split & Join -> Save (part) saves only from the selected part on and doesn't save the contents of container widgets, which have set the link option. It saves the link option instead.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Message('text_link',**{'text': "The link option is very useful for splitting a large GUI application into smaller parts and join them to one application.\n\nIt's not simply an entry. It works immediately like the entry 'photoimage'. What the entry does is comparable with the GuiDesigner menu item File -> Split & Join -> Load & Run (part).\n\nOr it does, what the function 'load_script' does, when the parameter for the parent is set:", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('title_link',**{'text': 'link - Config Option', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w', 'justify': 'left'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})
Message('what_it_does',**{'text': "The entry 'link' immediately executes the linked gui script, but the gui from this script will be loaded into the container widget, which has set this link option.\n\nAnd this link can be saved, if you use for saving: File -> Split & Join -> Save (part)", 'font': 'TkDefaultFont 9 bold', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '4'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================
