### CODE ===================================================
this_container=container()
### ========================================================

config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 15, 0, 0), (1, 57, 0, 0), (3, 18, 0, 0)]', 'grid_multi_rows': '[13, (0, 14, 0, 0), (2, 13, 0, 0), (3, 26, 0, 0), (4, 11, 0, 0), (5, 22, 0, 0), (6, 10, 0, 0), (12, 9, 0, 0)]', 'grid_rows': '(13, 25, 0, 0)'})

Message('Attention',**{'text': "Please notice: this window isn't an Application window, it's only a Toplevel window. When you continue, you should find the application window, which until now was hidden.\n\nThe principle of the GuiDesigner is, that you modify live the original Application window. If you close it, also this introduction will be closed.", 'width': '400', 'bd': '2', 'bg': '#ffffd4', 'relief': 'solid'}).grid(**{'column': '2', 'sticky': 'ew', 'pady': '7', 'padx': '8', 'row': '10'})
LinkButton('Back',**{'text': 'Back', 'bd': '3', 'link': 'introduction/navy.py'}).grid(**{'column': '1', 'row': '11'})
Label('Label',**{'text': 'Layouts for Widgets', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '2', 'row': '1'})
LinkLabel('grid',**{'text': 'grid', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/grid.py', 'fg': 'blue'}).grid(**{'rowspan': '3', 'column': '1', 'sticky': 'w', 'row': '7'})
Message('grid_info',**{'text': "The widgets are positioned by using rows and columns of a table grid. Most are using this layout, if they don't have a GuiDesigner, because it's easy to do. And most of tkinter programmers would like a GuiDesigner, which supports full the grid layout.", 'width': '400', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'ew', 'row': '7'})
Message('grid_info2',**{'text': 'But there was no GuiDesigner before, which really supported grid. Now there is.', 'font': 'TkDefaultFont 9 bold', 'width': '400', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '8'})
Message('grid_info3',**{'text': 'GuiDesigners written in Java or using other GUI frameworks cannot show the real tcl/tk or tkinter grid. This GuiDesigner, written in Python with tkinter shows grid live. A this to see is a great experience.\n', 'width': '400', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '9'})
LinkLabel('pack',**{'text': 'pack', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/pack.py', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '3'})
Message('pack_info',**{'text': "A very simple layout. It's just 'top' - from top to bottom - or 'bottom' - from bottom to top - or 'left' - from left to right - or 'right' - from right to left.", 'width': '400', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'ew', 'row': '3'})
LinkLabel('place',**{'text': 'place', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/place.py', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '5'})
Message('place_info',**{'text': 'The widgets are positioned by using y and x coordinates. Easy to do with the GuiDesigner, but complicated without.', 'width': '400', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '2', 'sticky': 'ew', 'row': '5'})
LinkLabel('to_pack',**{'text': 'pack', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/pack.py', 'fg': 'blue'}).grid(**{'column': '2', 'sticky': 'e', 'row': '11'})
### CODE ===================================================
this_container.grid_remove()
this_container.after(100,this_container.grid)
### ========================================================
