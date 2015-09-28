Label('ItemTitle',text="""index""",bg='yellow',fg='blue',anchor='n').pack(side = 'left')
Spinbox('index',increment='1.0',width='4',from_=1,to='100').pack(side = 'left')

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

### CODE ===================================================
