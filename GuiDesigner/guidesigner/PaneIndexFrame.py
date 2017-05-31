config(grid_cols='(2, 75, 0, 0)', grid_rows='(1, 0, 0, 0)')

Label('ItemTitle',relief='ridge', font='TkDefaultFont 9 bold', anchor='n', fg='blue', bd='3', bg='yellow', text='index').grid(sticky='ew', row=0)
Spinbox('index',from_=0, to=100.0, width=4).grid(sticky='nesw', column=1, padx=10, row=0)

### CODE ===================================================

widget('index').delete(0,END)
widget('index').insert(0,0)


def change_index(entry=widget('index')):

    this().layout(index=entry.get())
    entry.delete(0,END)
    entry.insert(0,this().getlayout('index'))
    send('LAYOUT_VALUES_REFRESH',this())

widget('index').do_event("<Return>",change_index)
widget('index').do_command(change_index)

def refresh_index(entry=widget('index')):
    if this().Layout in (PANELAYOUT,TTKPANELAYOUT):
        entry.delete(0,END)
        entry.insert(0,this().getlayout('index'))
        entry['to'] = this().master.PackListLen()-1

do_receive('BASE_LAYOUT_VALUE_REFRESH',refresh_index)

### ========================================================
