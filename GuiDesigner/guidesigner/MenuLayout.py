Label('Title',text="""menu""",bg='yellow',fg='blue',anchor='n').pack(side = 'left')
Button('Select',text="""Select""",pady='2',padx='1',bg='green',anchor='n').pack(side = 'left')

### CODE ===================================================

def activate_menu():
    layout_before = this().Layout
    this().select_menu()
    send("BASE_LAYOUT_CHANGED",layout_before) # and message to others

widget('Select').do_command(activate_menu)

### ===================================================
