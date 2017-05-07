### CODE ===================================================
this_container=container()
### ========================================================

config(**{'grid_cols': '(4, 75, 0, 0)', 'grid_multi_cols': '[4, (0, 11, 0, 0), (1, 67, 0, 0), (3, 10, 0, 0)]', 'grid_multi_rows': '[8, (0, 10, 0, 0), (5, 8, 0, 0), (6, 22, 0, 0), (7, 7, 0, 0)]', 'grid_rows': '(8, 25, 0, 0)'})

Frame('Frame',**{'grid_multi_rows': '[2, (0, 0, 0, 0)]', 'height': '50', 'width': '50', 'grid_cols': '(2, 75, 0, 0)', 'grid_rows': '(2, 25, 0, 0)'})
goIn()

Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(**{'sticky': 'nesw', 'row': '0'})
Frame('right_frame')
goIn()

LabelFrame('BaseLayout',**{'text': 'Layout', 'link': 'introduction/BaseLayoutMenus.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})
LabelFrame('Selection',**{'text': 'Selection', 'link': 'guidesigner/Selection.py'}).grid(**{'column': '1', 'sticky': 'nw', 'row': '1'})

goOut()
grid(**{'column': '1', 'sticky': 'nw', 'row': '0'})

goOut()
grid(**{'column': '1', 'columnspan': '2', 'pady': '9', 'row': '2'})
Label('Label',**{'text': 'Menus', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '1'})
Message('Message',**{'text': "If you also would like to make a menu for a menubutton, then you should first go back to 'layouts' and create one inclusive a layout.\n\nLet's start by creating a Menu. As a layout you only see 'Select'. This isn't really a layout. It means, that you activate the menu. You could have more than one menu and may select which of them should be active or maybe none of them in the beginning - by doing unlayout.\n\nAfter you have selected the menu, you also will not see it, because there is nothing inside yet. So let's go into the menu.\n\nInside you notice, that the widget type selection has changed. The first four ones can be used in a top menu, but separator and delimter don't make a sense there.\n\nAs a layout you see index, which is also not a real layout. By index you may change the order of the entries in the menu.\n\nVery interesting is the menu item type 'cascade'. You may go inside and create a menu once more. This is a sub menu und you may also use the 'separator'. 'delimiter' isn't really something, which you create. It's only the access to the separator at the beginning of the menu - if you would like to change the background color.", 'pady': '10', 'padx': '10', 'width': '550', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'ew', 'columnspan': '2', 'row': '3'})
LinkLabel('layouts',**{'text': 'layouts', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/layouts.py', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'row': '6'})
LinkLabel('panes',**{'text': 'PanedWindow', 'font': 'TkFixedFont 12 bold underline', 'link': 'introduction/panes.py', 'fg': 'blue'}).grid(**{'column': '2', 'sticky': 'e', 'row': '6'})

### CODE ===================================================
this_container.grid_remove()
this_container.after(100,this_container.grid)

unregister_msgid('TOPLEVEL_CLOSED')
send('ACTIVATE_MOUSEMENU')
_Application.deiconify()
send('SELECTION_CHANGED')
### ========================================================
