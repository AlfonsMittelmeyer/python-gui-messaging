MenuItem('Mouse','command',**{'label': 'Mouse ON', 'background': 'lightgreen'}).layout(index=1)

### CODE ===================================================

widget("Mouse").mydata = False

def function_callback(me,message_to_send,thisText=None):
    me.mydata = not me.mydata
    if message_to_send == "MOUSE_SELECT_ON": container().is_mouse_select_on = me.mydata
    send(message_to_send,me.mydata)
    if me.mydata: me.config(label=thisText+" OFF",background="orange")
    else: me.config(label=thisText+" ON",background="lightgreen")

def call(widget_name,message_to_send,callback=function_callback):
    widget(widget_name).do_command(callback,(message_to_send,widget_name),True)

call("Mouse","MOUSE_SELECT_ON")

def switch_mouse_on(mouse_button=widget("Mouse"),funct=function_callback):
    if not mouse_button.mydata: funct(mouse_button,"MOUSE_SELECT_ON",'Mouse')

do_receive("SWITCH_MOUSE_ON",switch_mouse_on)

def check_mouse_on(mouse=widget('Mouse'),func=function_callback):
    if container().is_mouse_select_on != mouse.mydata: func(mouse,"MOUSE_SELECT_ON",'Mouse')

    
do_receive('SELECTION_CHANGED',check_mouse_on)

### =========================================================
