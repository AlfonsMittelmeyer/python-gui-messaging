### CODE ===================================================
grid_container = container()
### ========================================================

config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 11, 0, 0), (1, 67, 0, 0), (3, 10, 0, 0)]', 'grid_multi_rows': '[8, (0, 10, 0, 0), (5, 8, 0, 0), (6, 22, 0, 0), (7, 7, 0, 0)]', 'grid_rows': '(8, 25, 0, 0)'})

Frame('Frame',**{'grid_multi_rows': '[2, (0, 0, 0, 0)]', 'height': '50', 'width': '50', 'grid_cols': '(2, 75, 0, 0)', 'grid_rows': '(2, 25, 0, 0)'})
goIn()

Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(**{'sticky': 'nesw', 'row': '0'})
Frame('right_frame')
goIn()

LabelFrame('BaseLayout',**{'text': 'Layout', 'link': 'introduction/BaseLayoutGrid.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})
LabelFrame('Selection',**{'text': 'Selection', 'link': 'guidesigner/Selection.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '1'})

goOut()
grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})

goOut()
grid(**{'column': '1', 'columnspan': '2', 'pady': '9', 'row': '2'})
Label('Label',**{'text': 'Grid Layout', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '1'})
Message('Message',**{'text': "The grid layout module will only be shown, if there doesn't exist a pack layout within the same container, because grid and pack together would crash. So if you have widgets with a pack layout, then unlayout them.\n\nBefore doing a grid layout, you first should enter Rows and Columns values, for example 10 and 7.\n\nThe spinboxes below will change all cells of the table, except those columns and rows, which have an individual layout. You may set an individual layout, if you set the mark in the checkbox 'Individual' and press 'Show'.\n\nThen you will see some grey elements at the bottom and at the right side of the table. By turning the mouse wheel there, you will change the size. If you press the right mouse button, you may change also pad and weight individually.\n\nThe 'Hide' button shows the layout originally without the blue background and the lines. You position a widget without a layout or with a place layout by pressing the button 'GRID' and then you move it by mouse. If you do an unlayout, the you may position after this a widget at the same place as before, by pressing the button 'Grid()'.", 'pady': '10', 'padx': '10', 'width': '550', 'bg': 'white'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '3'})
Message('Message2',**{'text': "The grid layout is also easy and comfortable to use with this GuiDesigner and it's a great experience. Isn't it?\n", 'font': 'TkDefaultFont 9 bold', 'width': '550', 'bg': 'white'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '2', 'row': '4'})
LinkLabel('grid',**{'text': 'Menus', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/menus.py', 'fg': 'blue'}).grid(**{'column': '2', 'sticky': 'e', 'row': '6'})
LinkLabel('layouts',**{'text': 'layouts', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/layouts.py', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '6'})

### CODE ===================================================

grid_container.grid()

unregister_msgid('TOPLEVEL_CLOSED')
send('ACTIVATE_MOUSEMENU')
_Application.deiconify()
send('SELECTION_CHANGED')
### ========================================================
