config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 11, 0, 0), (1, 67, 0, 0), (3, 10, 0, 0)]', 'grid_multi_rows': '[7, (0, 10, 0, 0), (4, 8, 0, 0), (6, 8, 0, 0)]', 'grid_rows': '(7, 25, 0, 0)'})

Frame('Frame',**{'grid_multi_rows': '[2, (0, 0, 0, 0)]', 'height': '50', 'width': '50', 'grid_cols': '(2, 75, 0, 0)', 'grid_rows': '(2, 25, 0, 0)'})
goIn()

Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(**{'sticky': 'nesw', 'row': '0'})
Frame('right_frame')
goIn()

LabelFrame('BaseLayout',**{'text': 'Layout', 'link': 'introduction/BaseLayoutPack.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})
LabelFrame('Selection',**{'text': 'Selection', 'link': 'guidesigner/Selection.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '1'})

goOut()
grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})

goOut()
grid(**{'column': '1', 'columnspan': '2', 'pady': '9', 'row': '2'})
Label('Label',**{'text': 'Pack Layout', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '1'})
Message('Message',**{'text': "Maybe you don't see the pack layout module yet. If you didn't create widgets or if the application '.' is selected, then you will not see it, because the application can't be packed.\n\nSo select a widget or create one.\n\nCombining packing makes sense. So you may combine TOP and BOTTOM, or LEDT and RIGHT, if you take a strict order, e.g. first TOP, then BOTTOM.\n\nBut if you mix the order, then the result may be not, what you expect.\n\nIf you click on a button in the selection module, you will also see in the application window by highglighting, what is selected. If you switch the Mouse ON in the menu, you may select the widgets by mouse click also directly in the application window.", 'pady': '8', 'padx': '10', 'width': '550', 'bg': 'white'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '3'})
LinkLabel('layouts',**{'text': 'layouts', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/layouts.py', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '5'})
LinkLabel('place',**{'text': 'place', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/place.py', 'fg': 'blue'}).grid(**{'column': '2', 'sticky': 'e', 'row': '5'})

### CODE ===================================================
unregister_msgid('TOPLEVEL_CLOSED')
send('ACTIVATE_MOUSEMENU')
_Application.deiconify()
send('SELECTION_CHANGED')
### ========================================================
