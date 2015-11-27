Button("gotoRoot",text="/")	
pack(side=LEFT)

Button("rename",text="rename")
pack(side=LEFT,anchor=W)

Button("unlayout",text="unlayout")
pack(side=LEFT,anchor=W)

Button("destroy",text="destroy")
pack(side=LEFT,anchor=W)

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

def enable_unlayout(button=widget("unlayout"),rename_button=widget("rename")):

    if this().Layout in (NOLAYOUT,LAYOUTNEVER,MENUITEMLAYOUT): button['state'] = 'disabled'
    else: button['state'] = 'normal'
    
    if isinstance(this(),CanvasItemWidget): rename_button['state'] = 'disabled'
    else: rename_button['state'] = 'normal'
    
do_receive('SELECTION_LAYOUT_CHANGED',enable_unlayout)
do_receive('SELECTION_CHANGED',enable_unlayout)

def do_rename(cont = container()):
    if _Selection._widget == _Selection._container: messagebox.showinfo('rename container "."',"""
Please rename containers from outside!
Select: '<='""",parent=cont)
    else: send("RENAME_WIDGET",getNameAndIndex())

widget("rename").do_command(do_rename)

'''
if this().Layout == WINDOWLAYOUT: delete_window
    this.Layout = NOLAYOUT
else: unlayout()
'''

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
            # No don't work --- we should find the referenced Object and do an unlayout --- here we only have some reference as a string
            elif isinstance(this(),CanvasItemWidget) and container().type(this().item_id) == 'window' and this().getconfig('window') != "":
                #this().getconfdict()['window'].Layout = NOLAYOUT
                ref = container().Dictionary.getEntryByStringAddress(this().getconfig('window'))
                if ref != None: ref.Layout = NOLAYOUT
            destroyElement(name_ind[0],name_ind[1])
            cdDir()
            send("SELECTION_CHANGED",this())

widget("destroy").do_command(do_destroy)

### ========================================================

