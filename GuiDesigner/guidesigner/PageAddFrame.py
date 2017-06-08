config(grid_cols='(2, 75, 0, 0)', grid_rows='(2, 0, 0, 0)')

Button('ADD',text='ADD', anchor='n', pady='2', bd='3', padx='1m', bg='lightgreen').grid(row=0, padx=5, sticky='nesw', column=1)
Label('PageTitle',text='page', font='TkDefaultFont 9 bold', anchor='n', fg='blue', bd='3', relief='ridge', bg='yellow').grid(row=0, sticky='ew')

### CODE ===================================================


def do_add():

    page()
        
    send('UPDATE_MOUSE_SELECT_ON')
    send("BASE_LAYOUT_CHANGED",NOLAYOUT) # NOLAYOUT because always trigger a sash_list_refreh via event BASE_LAYOUT_REFRESH
    send('BASE_LAYOUT_VALUE_REFRESH')


widget("ADD").do_command(do_add)

### ========================================================
