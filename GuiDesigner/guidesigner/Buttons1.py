Button('gotoRoot',text='/',padx='3m')
Button('unlayout',text='unlayout',padx='3m')
Menubutton('more',**{'highlightthickness': 1, 'relief': 'raised', 'padx': 12, 'underline': 2, 'pady': 1, 'text': 'more'})
goIn()

Menu('menu',**{'activebackground': '#7bfeff', 'bg': 'white', 'activeforeground': 'black', 'fg': 'black', 'relief': 'solid', 'tearoff': 0})
goIn()

MenuItem('copy','command',**{'underline': 0, 'photoimage': 'guidesigner/images/edit-copy.gif', 'label': 'copy', 'compound': 'left'})
MenuItem('cut','command',**{'underline': 2, 'photoimage': 'guidesigner/images/edit-cut.gif', 'label': 'cut', 'compound': 'left'})
MenuItem('destroy','command',**{'underline': 0, 'photoimage': 'guidesigner/images/edit-delete.gif', 'label': 'destroy', 'compound': 'left'})
MenuItem('paste','command',**{'underline': 0, 'photoimage': 'guidesigner/images/edit-paste.gif', 'label': 'paste', 'compound': 'left'})
MenuItem('rename','command',**{'underline': 0, 'photoimage': 'guidesigner/images/tools-check-spelling.gif', 'label': 'rename', 'compound': 'left'})

widget('paste').layout(index=1)
widget('copy').layout(index=2)
widget('cut').layout(index=3)
widget('rename').layout(index=4)
widget('destroy').layout(index=5)

### CODE ===================================================
# EDIT


widget("destroy").do_command(lambda: send('DESTROY_WIDGET'))
widget("rename").do_command(lambda: send('EDIT_RENAME_WIDGET'))


def enable_unlayout(rename=widget("rename"),copy = widget('copy'),cut=widget('cut'),paste=widget('paste')):

    is_item = isinstance(this(),CanvasItemWidget)

    rename['state'] = 'disabled' if is_item else 'normal'
    copy['state'] = 'disabled' if is_item else 'normal'
    cut['state'] = 'disabled' if is_item else 'normal'
    paste['state'] = 'disabled' if is_item else 'normal'
    
do_receive('SELECTION_LAYOUT_CHANGED',enable_unlayout)
do_receive('SELECTION_CHANGED',enable_unlayout)



def save_file():
    name = 'Testcode/clipboard.py'
    fh = open(name,'w',encoding="utf-8")
    currentSelection = Selection()
    saveWidgets(fh)
    setSelection(currentSelection)
    fh.close()

widget('copy').do_command(save_file)


def load_file():
    filename = 'Testcode/clipboard.py'
    setLoadForEdit(True)
    DynLoad(filename)
    setLoadForEdit(False)
    send('SHOW_SELECTION')
    send('SELECTION_CHANGED') # for grid layout: must do an on enter and now we change the selection to the last widget

widget('paste').do_command(load_file)


def cut(save_file = save_file):
    save_file()
    if this() == container():
        container().destroyActions()
        container().destroyContent()
        send('SHOW_SELECTION')
    else:
        name_ind = getNameAndIndex()
        if this().Layout == WINDOWLAYOUT:
            send_immediate("DELETE_WINDOW")
        destroyElement(name_ind[0],name_ind[1])
        cdDir()
        send("SELECTION_CHANGED")


widget('cut').do_command(cut)


### ========================================================

goOut()
select_menu()

goOut()


widget('gotoRoot').pack(fill='y', side='left')
widget('unlayout').pack(fill='y', side='left')
widget('more').pack(fill='y', side='left')

### CODE ===================================================

def delete_window():

    item_list = container().find_all()
    item = -1
    for item_id in item_list:
        if container().type(item_id) == 'window':
            if str(container().itemcget(item_id,'window')) == str(this()):
                item = item_id
                break
    if item != -1:
        for name,entry in dict(container().Dictionary.elements).items():
            for element in entry:
                if isinstance(element,CanvasItemWidget):
                    if item == element.item_id:
                        selection_before = Selection()
                        element.destroy()
                        setSelection(selection_before)
                        break
        container().delete(item)

do_receive("DELETE_WINDOW",delete_window)


def do_destroy(cont = container(),delete_window=delete_window):
    if _Selection._widget == _Selection._container:
        if messagebox.askyesno("destroy container content","destroy container content\nReally?",parent=cont):
            container().destroyActions()
            container().destroyContent()
            send('SHOW_SELECTION')
    else:
        name_ind = getNameAndIndex()
        if name_ind[1] == -1: text = 'destroy '+"'"+name_ind[0]+"'"
        else: text = 'destroy '+"'"+name_ind[0] + ' [' + str(name_ind[1])+']'+"'"
        if messagebox.askyesno(text,text+'\nReally?',parent=cont):
            if this().Layout == WINDOWLAYOUT: delete_window()
            elif isinstance(this(),CanvasItemWidget) and container().type(this().item_id) == 'window' and this().getconfig('window') != "":
                #this().getconfdict()['window'].Layout = NOLAYOUT
                # No don't work --- we should find the referenced Object and do an unlayout --- here we only have some reference as a string
                ref = container().Dictionary.getEntryByStringAddress(this().getconfig('window'))
                if ref != None: ref.Layout = NOLAYOUT
            destroyElement(name_ind[0],name_ind[1])
            cdDir()
            send("SELECTION_CHANGED",this())

do_receive('DESTROY_WIDGET',do_destroy)

def do_goRoot():
    gotoRoot()
    send('SELECTION_CHANGED',this())

widget("gotoRoot").do_command(do_goRoot)

def do_unlayout(delete_window=delete_window):
    if this().Layout & LAYOUTALL:
        if this().Layout == WINDOWLAYOUT:
            delete_window()
            this().Layout = NOLAYOUT
        else: unlayout()
        send('BASE_LAYOUT_WIDGET_CHANGED',this())
        send("SELECTION_LAYOUT_CHANGED")

widget("unlayout").do_command(do_unlayout)


def do_rename(cont = container()):
    if _Selection._widget == _Selection._container: messagebox.showinfo('rename container "."',"""
Please rename containers from outside!
Select: '<='""",parent=cont)
    else: send("RENAME_WIDGET",getNameAndIndex())

do_receive('EDIT_RENAME_WIDGET',do_rename)


def enable_unlayout(button=widget("unlayout")):

    if this().Layout in (NOLAYOUT,LAYOUTNEVER,MENUITEMLAYOUT): button['state'] = 'disabled'
    else: button['state'] = 'normal'
    
do_receive('SELECTION_LAYOUT_CHANGED',enable_unlayout)
do_receive('SELECTION_CHANGED',enable_unlayout)


### ========================================================
