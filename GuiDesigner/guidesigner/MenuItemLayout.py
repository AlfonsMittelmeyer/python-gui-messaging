config(**{'grid_cols': '(2, 75, 0, 0)','grid_rows': '(1, 25, 0, 0)'})

Label('ItemTitle',**{'text': 'index', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'bg': 'yellow', 'fg': 'blue', 'relief': 'ridge', 'anchor': 'n'}).grid(**{'sticky': 'ew', 'row': '0'})
Spinbox('index',**{'from': '1.0', 'width': '4', 'to': '100.0'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '0'})

### CODE ===================================================

widget('index').delete(0,END)
widget('index').insert(0,1)


def change_index(entry=widget('index')):

    this().layout(index=entry.get())
    entry.delete(0,END)
    entry.insert(0,this().getlayout('index'))
    send('LAYOUT_VALUES_REFRESH',this())

widget('index').do_event("<Return>",change_index)
widget('index').do_command(change_index)

def refresh_index(entry=widget('index')):
    if this().Layout == MENUITEMLAYOUT:
        entry.delete(0,END)
        entry.insert(0,this().getlayout('index'))
        entry['to'] = this().master.PackListLen()

do_receive('BASE_LAYOUT_VALUE_REFRESH',refresh_index)

### ========================================================
