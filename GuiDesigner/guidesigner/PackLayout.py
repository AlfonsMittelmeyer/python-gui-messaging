Button('RIGHT',text="""RIGHT""",pady='2',padx='1',bg='green')
Button('BOTTOM',text="""BOTTOM""",pady='2',padx='1',bg='green')
Button('TOP',text="""TOP""",pady='2',padx='1',bg='green')
Label('Label',width='1')
Label('PackTitle',text="""pack""",fg='blue')
Button('LEFT',text="""LEFT""",pady='2',padx='1',bg='green')

widget('PackTitle').pack(side='left')
widget('Label').pack(side='left')
widget('TOP').pack(side='left')
widget('LEFT').pack(side='left')
widget('RIGHT').pack(side='left')
widget('BOTTOM').pack(side='left')

### CODE ===================================================

# the buttons do a pack with parameter side = top, left, bottom or right
# and send a 'BASE_LAYOUT_CHANGED', which contains the current packed widget reference and the layout before

def do_pack(packside):
    send('BASE_LAYOUT_PLACE_MOUSEOFF')
    layout_before = this().Layout
    pack(side=packside)
    send('BASE_LAYOUT_CHANGED',layout_before)

widget("TOP").do_command(do_pack,TOP)
widget("LEFT").do_command(do_pack,LEFT)
widget("RIGHT").do_command(do_pack,RIGHT)
widget("BOTTOM").do_command(do_pack,BOTTOM)

# ---- Receivers for message 'BASE_LAYOUT_REFRESH' ------------------------------------------------

# if the current user widget has a PACKLAYOUT, the background of Label 'PackTitle' shall be shown yellow, otherwise normal

def do_bg_title(title = widget("PackTitle"),titlebg=widget("PackTitle")["bg"]):
    if this().Layout == PACKLAYOUT: title['bg'] ="yellow"
    else: title['bg'] =titlebg

do_receive('BASE_LAYOUT_REFRESH',do_bg_title)

### ========================================================
