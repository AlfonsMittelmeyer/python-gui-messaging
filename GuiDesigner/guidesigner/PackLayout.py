config(**{'grid_cols': '(5, 42, 0, 0)', 'grid_multi_cols': '[5, (0, 74, 0, 0)]', 'grid_rows': '(1, 5, 0, 0)'})

Button('BOTTOM',**{'text': 'BOTTOM', 'pady': '2', 'padx': '1', 'bd': '3', 'bg': 'green'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '0'})
Button('LEFT',**{'text': 'LEFT', 'pady': '2', 'padx': '1', 'bd': '4', 'bg': 'green'}).grid(**{'column': '3', 'sticky': 'nesw', 'row': '0'})
Label('PackTitle',**{'text': 'pack', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'fg': 'blue', 'relief': 'ridge'}).grid(**{'sticky': 'ew', 'row': '0'})
Button('RIGHT',**{'text': 'RIGHT', 'pady': '2', 'padx': '1', 'bd': '3', 'bg': 'green'}).grid(**{'column': '4', 'sticky': 'nesw', 'row': '0'})
Button('TOP',**{'text': 'TOP', 'padx': '1m', 'bd': '3', 'bg': 'green'}).grid(**{'column': '1', 'sticky': 'nesw', 'row': '0'})

### CODE ===================================================

# the buttons do a pack with parameter side = top, left, bottom or right
# and send a 'BASE_LAYOUT_CHANGED', which contains the current packed widget reference and the layout before

def do_pack(packside):
    layout_before = this().Layout
    pack(side=packside)
    send('UPDATE_MOUSE_SELECT_ON')
    send('BASE_LAYOUT_CHANGED',layout_before)

widget("TOP").do_command(do_pack,TOP)
widget("LEFT").do_command(do_pack,LEFT)
widget("RIGHT").do_command(do_pack,RIGHT)
widget("BOTTOM").do_command(do_pack,BOTTOM)

# ---- Receivers for message 'BASE_LAYOUT_REFRESH' ------------------------------------------------

# if the current user widget has a PACKLAYOUT, the background of Label 'PackTitle' shall be shown yellow, otherwise normal

def do_bg_title(title = widget("PackTitle"),titlebg=widget("PackTitle")["bg"]):
    if this().Layout == PACKLAYOUT: title['bg'] ="yellow"
    else: title['bg'] =titlebg

do_receive('BASE_LAYOUT_REFRESH',do_bg_title)

### ========================================================
