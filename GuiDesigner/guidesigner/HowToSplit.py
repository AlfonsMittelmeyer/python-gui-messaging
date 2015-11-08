config(**{'title': 'How to split a GUI', 'grid_cols': '(9, 75, 0, 0)', 'grid_rows': '(23, 10, 0, 0)'})

Message('after_split1',**{'text': "Now let's go into the menu.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '7'})
Message('after_split2',**{'text': "This GUI part we now save via File -> Split & Join -> Save (part). Let's save it as 'split2.py'. This file contains the same as file 'guidesigner/TopMenu.py'. After we have saved this part, we press the destroy button and destroy the content of the menu. Wether we stay inside the menu or go outside doesn't make a difference now. This is the view from outside:", 'width': '580', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '11'})
Message('after_split3',**{'text': 'What we do now is: enter the link to the saved part', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '15'})
Message('after_split4',**{'text': 'Now we select the root and via File -> Split & Join -> Save (part) we save this part as split1.py', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '19'})
Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '7', 'sticky': 'esw', 'row': '21'})
Message('lead_text',**{'text': "Splitting a GUI consists of two savings and setting a link. Let's do it. Via File->Load & Edit we load menu2.py. This is whole the menu joined. The GuiDesigner shows this:", 'width': '580', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '3'})
Label('split1_gif',**{'photoimage': 'guidesigner/images/split1.gif'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '4', 'row': '5'})
Label('split2_gif',**{'photoimage': 'guidesigner/images/split2.gif'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '5', 'row': '9'})
Label('split3_gif',**{'photoimage': 'guidesigner/images/split3.gif'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '4', 'row': '13'})
Label('split4_gif',**{'photoimage': 'guidesigner/images/split4.gif'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '7', 'row': '17'})
Label('split5_gif',**{'photoimage': 'guidesigner/images/split5.gif'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '4', 'row': '21'})
Label('title',**{'text': 'How to split a GUI', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '1'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================

