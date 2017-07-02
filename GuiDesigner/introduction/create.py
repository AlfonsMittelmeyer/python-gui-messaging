### CODE ===================================================
this_container=container()
### ========================================================
config(**{'grid_rows': '(11, 25, 0, 0)', 'grid_cols': '(4, 300, 0, 0)', 'grid_multi_rows': '[11, (0, 11, 0, 0), (1, 24, 0, 0), (2, 13, 0, 0), (4, 11, 0, 0), (6, 31, 0, 0), (8, 10, 0, 0), (10, 8, 0, 0)]', 'grid_multi_cols': '[4, (0, 19, 0, 0), (3, 19, 0, 0)]'})

Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(sticky='nw', row=0)

### ========================================================

#goOut()
grid(**{'column': 1, 'row': 3, 'columnspan': 2})
Label('Label',**{'font': 'TkDefaultFont 12 bold', 'text': 'Create Widgets', 'fg': 'blue'}).grid(**{'column': 1, 'row': 1, 'sticky': 'w', 'columnspan': 2})
Message('Message',**{'text': "The Create Widget module lets you create widgets.\n\nThe buttons in the section 'Select Widget Type' let you select the class of the tkinter widget.\n\nIn the last line there are two special widgets, which don't exist in tkinter: LinkButton and LinkLabel. You just had pressed the button 'Create ON'. This was a LinkButton, which can be used as Next or Back button. The LinkLabel is just the same, but looks different.\n\nThe entry 'Name' shows the selected class type as default for the name. You should change this name. If you like to export the designed GUI as a python tkinter file, the name should be fitting for a variable name. But if you access the GUI via interface, then there are no restrictions for the name, besides, that it has to be a string. But you only can enter a string.", 'bg': 'white', 'width': 600}).grid(**{'column': 1, 'row': 5, 'sticky': 'ew', 'columnspan': 2})
Message('Message',**{'font': 'TkDefaultFont 9 bold', 'text': 'The module above is the original GuiDesigner module, so just try it.', 'anchor': 'w', 'bg': 'white', 'width': 600}).grid(**{'column': 1, 'row': 6, 'sticky': 'nesw', 'columnspan': 2})
Message('Message',**{'text': "Do you think, it doesn't work, because it doesn't create a widget? But it works, it doesn't create a widget, but informs another module to create the widget.", 'anchor': 'w', 'bg': 'white', 'width': 600}).grid(**{'column': 1, 'row': 7, 'sticky': 'ew', 'columnspan': 2})
LinkButton('Next',**{'text': 'Next', 'bd': '3', 'link': 'introduction/navy.py'}).grid(**{'column': 2, 'row': 9, 'sticky': 'e'})
LinkButton('Back',**{'text': 'Back', 'bd': '3', 'link': 'introduction/img.py'}).grid(**{'column': 1, 'row': 9, 'sticky': 'w'})

### CODE ===================================================
this_container.grid_remove()
this_container.after(100,this_container.grid)
### ========================================================
