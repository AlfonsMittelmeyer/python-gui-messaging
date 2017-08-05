Button('Create',**{'bg': 'lightgreen', 'text': 'Create ON','pady' : 2})
Button('Config',**{'bg': 'lightgreen', 'text': 'Config ON','pady' : 2})
Button('Layout',**{'bg': 'lightgreen', 'text': 'Layout ON','pady' : 2})
Button('Mouse',**{'bg': 'lightgreen', 'text': 'Mouse ON','pady' : 2})
Button('Hide',**{'text': 'Hide','pady' : 2})

widget('Create').pack(padx=4, side='left')
widget('Config').pack(padx=4, side='left')
widget('Layout').pack(padx=4, side='left')
widget('Mouse').pack(padx=4, side='left')
widget('Hide').pack(padx=4, side='left')

### CODE ===================================================


widget('Hide').mydata = False
widget("Config").mydata = False
widget("Layout").mydata = False
widget("Create").mydata = False
widget("Mouse").mydata = False

def function_callback(me,message_to_send,thisText=None):
    me.mydata = not me.mydata
    if message_to_send == "MOUSE_SELECT_ON": container().is_mouse_select_on = me.mydata
    send(message_to_send,me.mydata)
    if me.mydata: me.config(text=thisText+" OFF",background="orange")
    else: me.config(text=thisText+" ON",background="lightgreen")

def call(widget_name,message_to_send,callback=function_callback):
    widget(widget_name).do_command(callback,(message_to_send,widget_name),True)

call("Config","SHOW_CONFIG")
call("Layout","SHOW_LAYOUT")
call("Create","SHOW_CREATE")
call("Mouse","MOUSE_SELECT_ON")

send("SHOW_CREATE",False)

def switch_Mouse(mouse_button=widget("Mouse"),funct=function_callback):
    if not mouse_button.mydata: funct(mouse_button,"MOUSE_SELECT_ON",'Mouse')

do_receive("SWITCH_MOUSE_ON",switch_Mouse)


def set_option_buttons(message,buttons=(widget("Config"),widget("Layout"),widget("Create"),widget("Mouse"))):
    for i in range(len(message)):
        if message[i] != buttons[i].mydata: buttons[i].invoke()

do_receive('SET_OPTION_BUTTONS',set_option_buttons,wishMessage=True)


def hide_gui(me,buttons=((widget("Config"),"SHOW_CONFIG"),(widget("Layout"),"SHOW_LAYOUT"),(widget("Create"),"SHOW_CREATE"))):

    me.mydata = not me.mydata

    if me.mydata:
        me.config(text = 'Show',underline = 1)
    else:
        me.config(text = 'Hide',underline = 0)
        
    send("HIDE_GUI",me.mydata)
    enable_state = 'disabled' if me.mydata else 'normal'
    for entry in buttons:
        entry[0].config(state = enable_state)
        if me.mydata and entry[0].mydata: send(entry[1],False)
        elif not me.mydata and entry[0].mydata: send(entry[1],True)

widget('Hide').do_command(hide_gui,wishWidget=True)


def check_Mouse(mouse=widget('Mouse'),func=function_callback):
    if container().is_mouse_select_on != mouse.mydata: func(mouse,"MOUSE_SELECT_ON",'Mouse')

    
do_receive('SELECTION_CHANGED',check_Mouse)

### ========================================================
