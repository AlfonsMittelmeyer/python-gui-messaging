config(**{'grid_rows': '(1, 0, 0, 0)', 'grid_cols': '(2, 75, 0, 0)'})

Label('ItemTitle',**{'font': 'TkDefaultFont 9 bold', 'text': 'pane', 'relief': 'ridge', 'bd': '3', 'bg': 'yellow', 'anchor': 'n', 'fg': 'blue'}).grid(row=0, sticky='ew')
Spinbox('pane',**{'width': 4, 'to': 100.0}).grid(row=0, sticky='nesw', column=1, padx=10)

### CODE ===================================================

widget('pane').delete(0,END)
widget('pane').insert(0,0)


def change_index(entry=widget('pane')):

    this().layout(pane=entry.get())
    entry.delete(0,END)
    entry.insert(0,this().getlayout('pane'))
    send('LAYOUT_VALUES_REFRESH',this())

widget('pane').do_event("<Return>",change_index)
widget('pane').do_command(change_index)

def refresh_index(entry=widget('pane')):
    if this().Layout in (PANELAYOUT,TTKPANELAYOUT):
        entry.delete(0,END)
        entry.insert(0,this().getlayout('pane'))
        entry['to'] = len(this().master.panes())-1

do_receive('BASE_LAYOUT_VALUE_REFRESH',refresh_index)

### ========================================================
