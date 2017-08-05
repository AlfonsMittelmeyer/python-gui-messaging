config(**{'grid_multi_cols': '[4, (1, 64, 0, 0), (2, 3, 0, 0), (3, 26, 0, 1)]', 'grid_cols': '(4, 43, 0, 0)', 'grid_rows': '(3, 0, 0, 0)'})

Button('Create',**{'text': 'Create', 'bg': 'lightgreen', 'pady': '1', 'padx': '1', 'bd': '2'}).grid(sticky='nes', column=3, row=0)
Label('Label',**{'width': 7, 'text': 'Class'}).grid(row=0)
Label('Label',**{'width': 7, 'text': 'Name'}).grid(row=1)
Entry('Name').grid(columnspan=3, sticky='nesw', column=1, row=1)
Label('Type',**{'fg': 'blue', 'text': 'Button', 'bg': 'yellow', 'relief': 'ridge', 'font': 'TkDefaultFont 9 bold'}).grid(sticky='ew', column=1, row=0)
Frame('orient',**{'grid_cols': '(2, 0, 0, 0)', 'grid_rows': '(1, 0, 0, 0)'})
goIn()

Label('label',**{'width': 7, 'text': 'orient'}).grid(row=0)
Entry('orient',**{'width': 10}).grid(sticky='nesw', column=1, row=0)
Button('help',**{'text': '?', 'pady': '1'}).grid(column=2, row=0)
Listbox('lbox',**{'width': 10, 'fill by text': '', 'height': 2})

### CODE ===================================================

widget('lbox').fillList(("vertical","horizontal"))
widget('orient').mydata = 'orient'

container().unlayout()


container().master.parameters = {'orient' : 'vertical'}
parameters = container().master.parameters

def setconfig(key,value,parameters=parameters):

    if key == 'orient':
        if value not in ('vertical','VERTICAL','horizontal','HORIZONTAL'):
            value = 'vertical'

    if key in parameters:
        parameters[key] = value

def do_color_action(me,msg,parameters=parameters):
    me['bg'] = 'white'
    if msg:
        me.delete(0,END)
        me.insert(0,get_entry_as_string(parameters[me.mydata]))

def entry_event(me,parameters=parameters,setconfig=setconfig):
    setconfig(me.mydata,me.get())
    me['bg']='gray'
    informLater(300,me,'color',True)


def do_lbox_click(event,lbox,entry,isMouse,setconfig=setconfig):
    if isMouse: text = lbox.get(lbox.nearest(event.y))
    else: text = lbox.get(ACTIVE)
    if text!='<=':
        setconfig(entry.mydata,text)
        entry.delete(0,END)
        entry.insert(0,text)
    lbox.unbind("<Return>")
    lbox.unbind("<Button-1>")
    lbox.unlayout()

def listbox_helpbutton(lbox,entry,lbox_click = do_lbox_click):
    lbox.select_clear(0,END) # clear a former listbox selection 
    try:
        lbox_index = lbox.getStringIndex(getconfig(entry.mydata)) # get the listbox index for the layout option
    except ValueError:
        lbox_index =0
    lbox.select_set(lbox_index) # preselect the current layout option in the listbox
    lbox.activate(lbox_index) # and set the selection cursor to it
    lbox.rcgrid(0,3) # show the listbox
    lbox.focus_set() # and focus it
    lbox.do_event("<Return>",lbox_click,(lbox,entry,False),wishEvent=True)  # bind Return key to the listbox
    lbox.do_event("<Button-1>",lbox_click,(lbox,entry,True),wishEvent=True)  # bind mouse click to the listbox

def listbox_selection(entry,listbox,helpbutton = listbox_helpbutton):
    Button(text="?").rcgrid(0,2) # create a help button for showing the listbox
    do_command(helpbutton,(listbox,entry))

widget('orient').mydata = 'orient'
widget('help').do_command(listbox_helpbutton,(widget('lbox'),widget('orient')))
widget('orient').do_action('color',do_color_action,wishWidget=True,wishMessage=True)
widget('orient').do_event("<Return>",entry_event,None,True)

def enable_orient(switch,container=container(),parameters = parameters,entry=widget('orient')):
    if switch:
        parameters.clear()
        parameters['orient'] = 'vertical'
        container.grid()
        entry.delete(0,END)
        entry.insert(0,'vertical')
    else:
        container.unlayout()
        
do_receive('ENABLE_ORIENT',enable_orient,wishMessage=True)    

### ========================================================

goOut()
grid(columnspan=5, sticky='nesw', row=2)

### CODE ===================================================


# the class name is stored in mydata of widget('Name')
def callback(wname = widget("Name"),parameters = container().parameters):
    send('CREATE_WIDGET_REQUEST',(wname.mydata,wname.get(),parameters))

widget("Create").do_command(callback)
widget("Name").do_event("<Return>",callback)

# ---- Receiver for message 'CREATE_CLASS_SELECTED': changes the text of Label 'Type' to the Class name and stores the Class name in mydata of Entry 'Name'

def function(msg,wname=widget('Name'),wtype=widget('Type'),dictionary=container().parameters):
    dictionary.clear()
    if msg[1] == 'ttk.PanedWindow':
        send('ENABLE_ORIENT',True)
    else:
        send('ENABLE_ORIENT',False)

    wname.mydata = msg[1]
    wname.delete(0,END)
    wname.insert(0,msg[0])
    wtype['text'] = msg[1]
    wname.focus_set()

do_receive('CREATE_CLASS_SELECTED',function,wishMessage=True)

# ---- Initialization with Class 'Button' ---------------------------

send('CREATE_CLASS_SELECTED',('button','Button'))

### ========================================================
