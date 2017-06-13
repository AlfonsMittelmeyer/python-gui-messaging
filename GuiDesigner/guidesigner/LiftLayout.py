config(**{'grid_rows': '(1, 0, 0, 1)', 'grid_cols': '(2, 0, 0, 1)'})

Button('button',**{'pady': '2', 'text': 'ADD', 'bd': '4', 'fg': 'black', 'bg': 'lightgreen'}).grid(column=1, row=0, sticky='e', padx=3)
Label('title',**{'relief': 'ridge', 'pady': '2', 'text': 'lift & lower', 'bd': '3', 'width': 10, 'padx': '7', 'fg': 'blue', 'bg': 'yellow', 'font': 'TkDefaultFont 9 bold'}).grid(row=0, sticky='w')

### CODE ===================================================

def refresh_layout(add = widget('button')):

    if this().Layout == NOLAYOUT:
        add.grid()
    elif this().Layout == LIFTLAYOUT:
        add.unlayout()

do_receive('BASE_LAYOUT_REFRESH',refresh_layout)

### ========================================================
