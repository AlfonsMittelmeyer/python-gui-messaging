Button('Layout',text="""ON""",bg='lightgreen').grid(column='3',sticky='ew',row='0')
Button('Create',text="""ON""",bg='lightgreen').grid(column='1',sticky='ew',row='1')
Button('Config',text="""ON""",bg='lightgreen').grid(column='1',sticky='ew',row='0')
Button('Mouse',text="""ON""",bg='lightgreen').grid(column='3',sticky='ew',row='1')
Label('Label',text="""Config:""",width='6').grid(row='0')
Label('Label',text="""Layout:""").grid(column='2',row='0')
Label('Label',text="""Create:""",width='6').grid(row='1')
Label('Label',text="""Mouse:""",width='6').grid(row='1',column=2)

### CODE ===================================================

# The command is initialized with config options switched off (False)
# When pressed, this switch is toggled and a message 'SHOW_CONFIG' is sent, which contains this ON/OFF value
# Further the button text is toggled between ON and OFF and the bg color between lightgreen and orange

widget("Config").mydata = False
widget("Layout").mydata = False
widget("Create").mydata = False
widget("Mouse").mydata = False

def function_callback(me,message_to_send):
    me.mydata = not me.mydata
    if message_to_send == "MOUSE_SELECT_ON": container().is_mouse_select_on = me.mydata
    send(message_to_send,me.mydata)
    if me.mydata: me.config(text="OFF",bg="orange")
    else: me.config(text="ON",bg="lightgreen")

def call(widget_name,message_to_send,callback=function_callback):
    widget(widget_name).do_command(callback,message_to_send,True)

call("Config","SHOW_CONFIG")
call("Layout","SHOW_LAYOUT")
call("Create","SHOW_CREATE")
call("Mouse","MOUSE_SELECT_ON")

send("SHOW_CREATE",False)


def switch_mouse_on(mouse_button=widget("Mouse"),funct=function_callback):
    if not mouse_button.mydata: funct(mouse_button,"MOUSE_SELECT_ON")

do_receive("SWITCH_MOUSE_ON",switch_mouse_on)


def set_option_buttons(message,buttons=(widget("Config"),widget("Layout"),widget("Create"),widget("Mouse"))):
    for i in range(len(message)):
        if message[i] != buttons[i].mydata: buttons[i].invoke()

do_receive('SET_OPTION_BUTTONS',set_option_buttons,wishMessage=True)


def check_mouse_on(mouse=widget('Mouse')):
    if container().is_mouse_select_on != mouse.mydata: mouse.invoke()

    
do_receive('SELECTION_CHANGED',check_mouse_on)

### ========================================================
