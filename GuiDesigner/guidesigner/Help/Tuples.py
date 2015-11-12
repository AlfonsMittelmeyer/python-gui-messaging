Toplevel('HelpTuples',**{'title': 'Tuple Entries', 'grid_cols': '(7, 75, 0, 0)', 'grid_multi_cols': '[7, (0, 10, 0, 0), (6, 10, 0, 0)]', 'grid_rows': '(12, 10, 0, 0)'})
goIn()

Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '5', 'sticky': 'nesw', 'row': '10'})
Message('enter_comment',**{'text': 'just enter:', 'font': 'TkDefaultFont 9 bold', 'width': 430, 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'pady': '2', 'row': '6'})
Message('enter_entry',**{'text': '10 100', 'font': 'TkDefaultFont 9 bold', 'width': 430, 'bd': 2, 'bg': 'white', 'fg': 'blue', 'relief': 'solid', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'nesw', 'pady': '2', 'row': '6'})
Message('instead_comment',**{'text': 'instead of:', 'font': 'TkDefaultFont 9 bold', 'width': 430, 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'pady': '2', 'row': '5'})
Message('instead_entry',**{'text': '(10,100)', 'font': 'TkDefaultFont 9 bold', 'width': 430, 'bd': 2, 'bg': 'white', 'fg': 'blue', 'relief': 'solid', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'nesw', 'pady': '2', 'row': '5'})
Message('lead_text',**{'text': "Some tkinter config options or layout options have or may have a tuple as parameter. So for example padx may take a 2-tuple padx=(100, 10) for different left right padding or pady for different bottom top padding.\n\nFor a Canvas scrollregion a 4-tuple normally is expected as a tkinter parameter.\n\nYou may not enter a tuple in the GuiDesigner, because the GuiDesigner takes strings and a tuple as a text in a string would be wrong.\n\nTkinter hands over parameters to the tcl/tk interpreter. For tuple parameters tkinter converts these tuple parameters to a string. If the parameter is a string, tkinter hands over this parameter directly and doesn't complain about it.\n\nTuple parameters you have to enter in the tcl/tk style, which is understood by tcl/tk. Just enter the tuple parameters without any parentheses, just separated by one or more spaces.", 'width': 430, 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '3'})
Message('save_parameters',**{'text': "When you save your GUI and would expect it would be saved in this or this way. I can't tell, how it will be saved. The format isn't defined, it isn't consistent and varies with your tkinter version. But if tkinter wouldn't accept, what it delivers, that would be a bug. Please let me know, if there would be such bug.", 'width': 430, 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '8'})
Label('title',**{'text': 'Tuple Entries', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '5', 'row': '1'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================

goOut()

