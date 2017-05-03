config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 11, 0, 0), (1, 67, 0, 0), (3, 10, 0, 0)]', 'grid_multi_rows': '[7, (0, 10, 0, 0), (4, 8, 0, 0), (6, 8, 0, 0)]', 'grid_rows': '(7, 25, 0, 0)'})

Frame('Frame',**{'grid_multi_rows': '[2, (0, 0, 0, 0)]', 'height': '50', 'width': '50', 'grid_cols': '(2, 75, 0, 0)', 'grid_rows': '(2, 25, 0, 0)'})
goIn()

Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(**{'sticky': 'nesw', 'row': '0'})
Frame('right_frame')
goIn()

LabelFrame('BaseLayout',**{'text': 'Layout', 'link': 'introduction/BaseLayoutPlace.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})
LabelFrame('Selection',**{'text': 'Selection', 'link': 'guidesigner/Selection.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '1'})

goOut()
grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})

goOut()
grid(**{'column': '1', 'columnspan': '2', 'pady': '9', 'row': '2'})
Label('Label',**{'text': 'Place Layout', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '1'})
Message('Message',**{'text': "The place layout is easy to do. Just press the green button 'PLACE'. Then you move the widget by mouse.\n\nYou also my make tables. The button 'adjust' changes the coordinates to a multiple of inc y and inc x. For inc y a value of 15 would make sense.\n\nWhen you press the up and down buttons if the spinboxes x and y, the coordinates change by increase or decrease according to the step widths inc y or inc x.\n\nTogether with layout options like anchor='w' or 'e', tables may be done without problems.\n\nBut of course best for tables is the grid layout.", 'pady': '10', 'padx': '10', 'width': '550', 'bg': 'white'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '3'})
LinkLabel('grid',**{'text': 'grid', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/grid.py', 'fg': 'blue'}).grid(**{'column': '2', 'sticky': 'e', 'row': '5'})
LinkLabel('layouts',**{'text': 'layouts', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/layouts.py', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '5'})

### CODE ===================================================
unregister_msgid('TOPLEVEL_CLOSED')
send('ACTIVATE_MOUSEMENU')
_Application.deiconify()
send('SELECTION_CHANGED')

Geometry_Refresh(200,widget('/'))
### ========================================================
