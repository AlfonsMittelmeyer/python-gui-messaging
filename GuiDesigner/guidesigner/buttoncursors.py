Toplevel('Cursors',**{'title': 'Cursors', 'grid_cols': '(9, 12, 0, 0)', 'bg': 'grey', 'grid_rows': '(25, 12, 0, 0)'})
goIn()

Button('Close',**{'text': 'Close', 'photoimage': '', 'bd': '3', 'bg': '#ffffe0'}).grid(**{'column': '7', 'sticky': 'e', 'row': '23'})
Message('Message',**{'text': 'The graphic of the cursors may vary according to your operation system. But by moving the mouse over the buttons, you can observe, how the cursors look on your system.', 'width': '600', 'bg': '#ffffe0', 'relief': 'solid'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '7', 'row': '1'})

### CODE ========================================================================

def close_cursors(cont = container()):
    selection_before = Selection()
    cont.destroy()
    if widget_exists(selection_before._widget):
        setSelection(selection_before)
    else:
        send("SELECTION_CHANGED")

widget('Close').do_command(close_cursors)


def press_button(me):
    me['relief'] = 'sunken'

def set_cursor(me):
    if this().hasConfig:
        if 'buttoncursor' in this().getconfdict():
            this()['buttoncursor'] = me['cursor']
            send('SHOW_CONFIG',this())
    me['relief'] = 'raised'
    

index = 0
for entry in (
'arrow',
'based_arrow_down',
'based_arrow_up',
'boat',
'bogosity',
'bottom_left_corner',
'bottom_right_corner',
'bottom_side',
'bottom_tee',
'box_spiral',
'center_ptr',
'circle',
'clock',
'coffee_mug',
'cross',
'crosshair',
'cross_reverse',
'diamond_cross',
'dotbox',
'dot',
'double_arrow',
'draft_large',
'draft_small',
'draped_box',
'exchange',
'fleur',
'gobbler',
'gumby',
'hand1',
'hand2',
'heart',
'icon',
'iron_cross',
'leftbutton',
'left_ptr',
'left_side',
'left_tee',
'll_angle',
'lr_angle',
'man',
'middlebutton',
'mouse',
'pencil',
'pirate',
'plus',
'question_arrow',
'rightbutton',
'right_ptr',
'right_side',
'right_tee',
'rtl_logo',
'sailboat',
'sb_down_arrow',
'sb_h_double_arrow',
'sb_left_arrow',
'sb_right_arrow',
'sb_up_arrow',
'sb_v_double_arrow',
'shuttle',
'sizing',
'spider',
'spraycan',
'star',
'target',
'tcross',
'top_left_arrow',
'top_left_corner',
'top_right_corner',
'top_side',
'top_tee',
'trek',
'ul_angle',
'umbrella',
'ur_angle',
'watch',
'X_cursor',
'xterm'):

    row,column=divmod(index,4)
    row += 3
    column = 1 + column*2

    Frame('frame',**{'bd': '2', 'relief': 'raised','cursor':entry})
    do_event('<Button-1>',press_button,wishWidget=True)
    do_event('<ButtonRelease-1>',set_cursor,wishWidget=True)
    goIn()
    Label('gif',photoimage = 'guidesigner/cursors/'+entry+'.gif').pack(side = 'left')
    do_event('<Button-1>',press_button,container())
    do_event('<ButtonRelease-1>',set_cursor,container())
    Label('text',text = entry).pack(side = 'left',expand=1)
    do_event('<Button-1>',press_button,container())
    do_event('<ButtonRelease-1>',set_cursor,container())
    goOut()
    grid(**{'column': column, 'sticky': 'nesw', 'pady': '2', 'padx': '2', 'row': row})
    index += 1

### ==========================================================

goOut()
