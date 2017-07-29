config(**{'grid_cols': '(2, 75, 0, 0)','grid_rows': '(1, 25, 0, 0)'})

Label('ItemTitle',**{'text': 'index', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'bg': 'yellow', 'fg': 'blue', 'relief': 'ridge', 'anchor': 'n'}).grid(**{'sticky': 'ew', 'row': '0'})
Spinbox('index',**{'from': '0.0', 'width': '4', 'to': '100.0'}).grid(**{'column': '1', 'sticky': 'ns', 'row': '0'})

### CODE ===================================================

widget('index').delete(0,END)
widget('index').insert(0,1)


def refresh_index(entry=widget('index')):
    if this().Layout == MENUITEMLAYOUT:
        index = int(this().getlayout('index'))

        entry['from'] = this().master['tearoff']
        entry['to'] = this().master['tearoff'] + this().master.PackListLen() -1
        entry.delete(0,END)

        if not this().master['tearoff']:
            index -= 1

        entry.insert(0,index)


def change_index(entry=widget('index'),refresh = refresh_index):
    if this().Layout == MENUITEMLAYOUT:
        try:
            index = int(entry.get())
            if not this().master['tearoff']:
                index += 1
            this().layout(index=index)
            refresh()
            send('REFRESH_INDEX_ORDER')

        except ValueError:
            refresh()

widget('index').do_event("<Return>",change_index)
widget('index').do_command(change_index)


do_receive('BASE_LAYOUT_VALUE_REFRESH',refresh_index)

### ========================================================
