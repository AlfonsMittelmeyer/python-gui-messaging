config(**{'grid_cols': '(5, 42, 0, 0)', 'grid_rows': '(2, 5, 0, 0)', 'grid_multi_rows': '[2, (1, 0, 0, 0)]'})

Button('BOTTOM',**{'padx': '1', 'bd': '3', 'bg': 'lightgreen', 'text': 'BOTTOM', 'pady': '1'}).grid(row=0, sticky='nesw', column=2)
Button('LEFT',**{'padx': '1', 'bd': '4', 'bg': 'lightgreen', 'text': 'LEFT', 'pady': '1'}).grid(row=0, sticky='nesw', column=3)
Label('PackTitle',**{'font': 'TkDefaultFont 9 bold', 'padx': '1m', 'bd': '3', 'relief': 'ridge', 'fg': 'blue', 'text': 'pack'}).grid(row=0, sticky='nesw')
Button('RIGHT',**{'padx': '1', 'bd': '3', 'bg': 'lightgreen', 'text': 'RIGHT', 'pady': '1'}).grid(row=0, sticky='nesw', column=4)
Button('TOP',**{'padx': '1m', 'bd': '3', 'bg': 'lightgreen', 'text': 'TOP', 'pady': '1'}).grid(row=0, sticky='nesw', column=1)
Spinbox('spinbox',**{'width': 0, 'to': 1000.0}).grid(row=1, columnspan=2, sticky='nesw', ipady=2, column=3)
Label('l_index',**{'font': 'TkDefaultFont 8 bold', 'bd': '2', 'bg': '#fff0b6', 'relief': 'sunken', 'fg': 'blue', 'text': 'pack index'}).grid(row=1, ipadx=2, columnspan=2, padx=2, sticky='nesw', column=1)

### CODE ===================================================

def main():
    # the buttons do a pack with parameter side = top, left, bottom or right
    # and send a 'BASE_LAYOUT_CHANGED', which contains the current packed widget reference and the layout before

    button_top = widget("TOP")
    button_left = widget("LEFT")
    button_right = widget("RIGHT")
    button_bottom = widget("BOTTOM")

    buttons = { 'left' : button_left,
                'right':button_right,
                'top': button_top,
                'bottom' : button_bottom
                }

    def raise_buttons():
        for button in buttons.values():
            button['relief'] = 'raised'

    def do_pack(packside):
        layout_before = this().Layout
        pack(side=packside)
        value_refresh()
        send('UPDATE_MOUSE_SELECT_ON')
        send('BASE_LAYOUT_CHANGED',layout_before)
        send('BASE_LAYOUT_PACK_DONE')

    button_top.do_command(do_pack,TOP)
    button_left.do_command(do_pack,LEFT)
    button_right.do_command(do_pack,RIGHT)
    button_bottom.do_command(do_pack,BOTTOM)

    # ---- Receivers for message 'BASE_LAYOUT_REFRESH' ------------------------------------------------

    # if the current user widget has a PACKLAYOUT, the background of Label 'PackTitle' shall be shown yellow, otherwise normal

    def do_bg_title(title = widget("PackTitle"),titlebg=widget("PackTitle")["bg"],w_index=widget('spinbox'),l_index = widget('l_index')):
        if this().Layout == PACKLAYOUT:
            title['bg'] ="yellow"
            w_index.grid()
            l_index.grid()
        else:
            title['bg'] =titlebg
            w_index.unlayout()
            l_index.unlayout()
            raise_buttons()

    def change_index(entry=widget('spinbox')):

        this().pack_index(entry.get())
        refresh_index()

        send('LAYOUT_VALUES_REFRESH',this())
        send('REFRESH_INDEX_ORDER')

    widget('spinbox').do_event("<Return>",change_index)
    widget('spinbox').do_command(change_index)



    def refresh_index(entry=widget('spinbox')):
        if this().Layout == PACKLAYOUT:
            entry['to'] = len(this().master.PackList)-1
            entry.delete(0,END)
            entry.insert(0,this().pack_index())

    def value_refresh():
        refresh_index()
        raise_buttons()
        if this().Layout == PACKLAYOUT:
            info = this().pack_info()
            if info:
                buttons[info['side']]['relief'] = 'solid'
        
    do_receive('BASE_LAYOUT_REFRESH',do_bg_title)
    do_receive('BASE_LAYOUT_VALUE_REFRESH',value_refresh)

main()
### ========================================================
