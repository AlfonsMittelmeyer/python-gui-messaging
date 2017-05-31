config(grid_cols='(2, 75, 0, 0)', grid_rows='(2, 0, 0, 0)')

Button('ADD',text='ADD', anchor='n', pady='2', bd='3', padx='1m', bg='green').grid(row=0, padx=5, sticky='nesw', column=1)
Label('PaneTitle',text='pane', font='TkDefaultFont 9 bold', anchor='n', fg='blue', bd='3', relief='ridge', bg='yellow').grid(row=0, sticky='ew')
Frame('weightframe',grid_cols='(2, 75, 0, 0)', grid_rows='(1, 25, 0, 0)')
goIn()

Label('label',text='weight').grid(row=0)
Spinbox('weight',width=3, to=100.0).grid(row=0, padx=10, sticky='ew', pady=6, column=1)

### CODE ===================================================

container().master.parameters = {'weight' : 1}

parameters = container().master.parameters

def setconfig(key,value,parameters=parameters):

    if key == 'weight':
        try:
            value = int(value)
        except ValueError:
            value = 1
            
    if key in parameters:
        parameters[key] = value
        

def do_color_action(me,msg,parameters=parameters):
    me['bg'] = 'white'
    if msg:
        me.delete(0,END)
        me.insert(0,get_entry_as_string(parameters[me.mydata]))

def entry_event(me,setconfig=setconfig):
    setconfig(me.mydata,me.get())
    me['bg']='gray'
    informLater(300,me,'color',True)

def return_event(me,entry_event=entry_event,parameters=parameters):
    entry_event(me)
    pane(**parameters)

    send('UPDATE_MOUSE_SELECT_ON')
    send("BASE_LAYOUT_CHANGED",NOLAYOUT) # NOLAYOUT because always trigger a sash_list_refreh via event BASE_LAYOUT_REFRESH
   

widget('weight').delete(0,'end')
widget('weight').insert(0,parameters['weight'])
widget('weight').mydata = 'weight'
widget('weight').do_action('color',do_color_action,wishWidget=True,wishMessage=True)
widget('weight').do_command(entry_event,wishWidget=True) # via up and down buttons the option value can be changed
widget('weight').do_event("<Return>",return_event,wishWidget=True)

### ========================================================

goOut()
grid(row=1, columnspan=2)

### CODE ===================================================


def show_weightframe(enable,frame = widget('weightframe')):
    if enable and isinstance(this().master,StatTtk.PanedWindow):
        frame.grid()
    else:
        frame.unlayout()

def do_add(parameters=container().parameters):

    if isinstance(container(),StatTtk.PanedWindow):
        pane(**parameters)
    else:
        pane()
        
    send('UPDATE_MOUSE_SELECT_ON')
    send("BASE_LAYOUT_CHANGED",NOLAYOUT) # NOLAYOUT because always trigger a sash_list_refreh via event BASE_LAYOUT_REFRESH
    send('BASE_LAYOUT_VALUE_REFRESH')


widget("ADD").do_command(do_add)

do_receive('ENABLE_SASH_LIST',show_weightframe,wishMessage=True)
### ========================================================
