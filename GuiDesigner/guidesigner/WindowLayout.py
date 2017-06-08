config(**{'grid_cols': '(2, 75, 0, 0)', 'grid_rows': '(1, 25, 0, 0)'})

Button('Select',**{'text': 'Create', 'pady': '2', 'padx': '1', 'bd': '3', 'bg': 'lightgreen', 'anchor': 'nw'}).grid(**{'column': '1', 'row': '0', 'sticky': 'nsw',})
Label('Title',**{'text': 'window', 'font': 'TkDefaultFont 9 bold', 'bd': '3', 'fg': 'blue', 'relief': 'ridge', 'anchor': 'n'}).grid(**{'sticky': 'ew', 'row': '0'})

### CODE ===================================================

def select_window():
    layout_before = this().Layout
    if layout_before != WINDOWLAYOUT:
        this().unlayout()
        this().Layout = WINDOWLAYOUT
        item = container().create_window(0,0,anchor='nw',window = this())
        this().window_item = item
        CanvasItem(container(),item)
    else:
        item_list = container().find_all()
        item = -1
        for item_id in item_list:
            if container().type(item_id) == 'window':
                if str(container().itemcget(item_id,'window')) == str(this()):
                    item = item_id
                    break
        if item != -1:
            CanvasItem(container(),item,False)
        
    send('SELECTION_CHANGED')
       
    #this().select_menu()
    send("BASE_LAYOUT_CHANGED",layout_before) # and message to others

widget('Select').do_command(select_window)


def titlecolor_and_enable(title = widget("Title"),bg = widget("Title")["bg"],select = widget('Select')): 

    if this().Layout == WINDOWLAYOUT:
        title['bg'] = 'yellow'	
        select['text'] = 'Select'
    else:
        title['bg'] = bg
        select['text'] = 'Create'

do_receive('BASE_LAYOUT_REFRESH',titlecolor_and_enable)


### ========================================================
