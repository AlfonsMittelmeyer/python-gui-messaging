config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 16, 0, 0), (3, 12, 0, 0)]', 'grid_multi_rows': '[10, (0, 8, 0, 0), (1, 23, 0, 0), (2, 10, 0, 0), (4, 13, 0, 0), (5, 23, 0, 0), (8, 12, 0, 0), (9, 23, 0, 0)]', 'grid_rows': '(10, 25, 0, 0)'})

LinkButton('Back',**{'text': 'Back', 'bd': '3', 'link': 'introduction/create.py'}).grid(**{'column': '1', 'sticky': 'nsw', 'row': '9'})
Frame('Frame')
goIn()

Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'})
LabelFrame('Selection',**{'text': 'Selection', 'link': 'guidesigner/Selection.py'})

widget('CreateFrame').pack(**{'side': 'left'})
widget('Selection').pack(**{'side': 'left', 'anchor': 'nw'})

goOut()
grid(**{'column': '1', 'columnspan': '2', 'row': '3'})
Label('Label',**{'text': 'Create and Navigate', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '2', 'row': '1'})
Message('Message',**{'text': "Two modules together let you create, rename and destroy widgets and let you navigate in the GUI.\n\nWhen you create a container widget like a Frame, you may go inside, if you used not the same name once more. With '/' you immediately go back to the root.\n\nWhen you select a container widget from inside - this is the '.' - and press destroy, you will destroy all widgets inside, but not the container widget itself. You may only destroy a container widget from outside.", 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '5'})
Message('Message',**{'text': 'So now and here you may create widgets.', 'font': 'TkDefaultFont 9 bold', 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '2', 'row': '6'})
Message('Message',**{'text': "Do you wonder why you don't see them? Because they don't have a layout yet. This you can see also because of the 'italic' text font.", 'width': '600', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '2', 'row': '7'})
LinkButton('Next',**{'text': 'Next', 'bd': '3', 'link': 'introduction/layouts.py'}).grid(**{'column': '2', 'sticky': 'nes', 'row': '9'})

### CODE ===================================================
send("SELECTION_CHANGED")
### ========================================================
