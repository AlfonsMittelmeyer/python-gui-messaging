goIn()

MenuItem('Special','cascade',**{'label': 'Special', 'activebackground': ''})
goIn()

Menu('Menu',**{'activebackground':'#7bfeff','relief':'solid','bg':'white'})
goIn()

MenuItem('Toproot','command',**{'label': 'Toproot'})
MenuItem('Refresh','command',**{'label': 'Refresh'})
#MenuItem('Code','command',**{'label': 'Code'})

widget('Toproot').layout(index=1)
widget('Refresh').layout(index=2)
#widget('Code').layout(index=3)

### CODE ===================================================

#goto('code')
#DynLoad('guidesigner/Button_code.py')

def go_TopRoot():
    gotoTop()
    send('SELECTION_CHANGED',this())

widget('Toproot').do_command(go_TopRoot)
widget("Refresh").do_command(lambda: send('SELECTION_CHANGED',this()))

### ========================================================

goOut()
select_menu()

goOut()

MenuItem('File','cascade',**{'label': 'File'})
goIn()

Menu('Menu',**{'activebackground': '#7bfeff','relief':'solid','bg':'white'})
goIn()

MenuItem('Load & Edit','command',**{'label': 'Load & Edit'})
MenuItem('Load & Run','command',**{'label': 'Load & Run'})
MenuItem('Save','command',**{'label': 'Save'})

widget('Save').layout(index=1)
widget('Load & Run').layout(index=2)
widget('Load & Edit').layout(index=3)


### CODE ===================================================

def do_save():
    if this() == container(): send("SAVE_WIDGET",None)
    else: send("SAVE_WIDGET",getNameAndIndex())

widget("Save").do_command(do_save)


def do_load():
    selection = Selection()
    goOut()
    if this() == container():
        if this() == _AppRoot._widget:
            send('LOAD_WIDGET','Application Window')
        else: send('LOAD_WIDGET','Toplevel Window')
    else: send('LOAD_WIDGET',"Container: " + getNameAndIndex()[0])
    setSelection(selection)

widget('Load & Run').do_command(do_load)

def do_loadedit():
    selection = Selection()
    goOut()
    if this() == container():
        if this() == _AppRoot._widget:
            send('LOAD_EDIT','Application Window')
        else: send('LOAD_EDIT','Toplevel Window')
    else: send('LOAD_EDIT',"Container: " + getNameAndIndex()[0])
    setSelection(selection)

widget('Load & Edit').do_command(do_loadedit)


### ========================================================

goOut()
select_menu()

goOut()

widget('File').layout(index=1)
widget('Special').layout(index=2)

def enable_file(wi=widget('File')):
    wi.config(state = 'disabled' if isinstance(container(),_CreateTopLevelRoot) else 'normal')

do_receive("SELECTION_CHANGED",enable_file)


goOut()

