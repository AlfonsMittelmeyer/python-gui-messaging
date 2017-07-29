config(**{'grid_cols': '(2, 75, 0, 0)','grid_rows': '(1, 25, 0, 0)'})

Label('ItemTitle',**{'text': 'page', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'bg': 'yellow', 'fg': 'blue', 'relief': 'ridge', 'anchor': 'n'}).grid(**{'sticky': 'ew', 'row': '0'})
Spinbox('page',**{'from': '0.0', 'width': '4', 'to': '100.0'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '0'})

### CODE ===================================================

widget('page').delete(0,END)
widget('page').insert(0,1)


def change_page(entry=widget('page')):

    this().layout(page=entry.get())
    entry.delete(0,END)
    entry.insert(0,this().getlayout('page'))
    send('LAYOUT_VALUES_REFRESH',this())
    send('REFRESH_INDEX_ORDER')

widget('page').do_event("<Return>",change_page)
widget('page').do_command(change_page)

def refresh_page(entry=widget('page')):
    if this().Layout == PAGELAYOUT:
        entry.delete(0,END)
        entry.insert(0,this().getlayout('page'))
        parent = this().master
        entry['to'] = parent.index('end') -1
        parent.select(parent.index(this()))
      
do_receive('BASE_LAYOUT_VALUE_REFRESH',refresh_page)

### ========================================================
