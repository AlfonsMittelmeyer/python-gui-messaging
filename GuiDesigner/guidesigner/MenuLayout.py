config(**{'grid_cols': '(2, 75, 0, 0)', 'grid_rows': '(1, 25, 0, 0)'})

Button('Select',**{'text': 'Select', 'pady': '2', 'padx': '1', 'bd': '3', 'bg': 'green', 'anchor': 'n'}).grid(**{'column': '1', 'row': '0'})
Label('Title',**{'text': 'menu', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'fg': 'blue', 'relief': 'ridge', 'anchor': 'n'}).grid(**{'sticky': 'ew', 'row': '0'})

### CODE ===================================================

def activate_menu():
    layout_before = this().Layout
    this().select_menu()
    send("BASE_LAYOUT_CHANGED",layout_before) # and message to others

widget('Select').do_command(activate_menu)

def do_bg_title(title = widget("Title"),titlebg=widget("Title")["bg"]):
    if this().Layout == MENULAYOUT: title['bg'] ="yellow"
    else: title['bg'] =titlebg

do_receive('BASE_LAYOUT_REFRESH',do_bg_title)
### ========================================================
