Button('Layout',text="""ON""",bg='green').grid(column='3',sticky='ew',row='0')
Button('Create',text="""ON""",bg='green').grid(column='1',sticky='ew',row='1')
Button('Config',text="""ON""",bg='green').grid(column='1',sticky='ew',row='0')
Label('Label',text="""Config:""",width='6').grid(row='0')
Label('Label',text="""Layout:""").grid(column='2',row='0')
Label('Label',text="""Create:""",width='6').grid(row='1')

### CODE ===================================================

# The command is initialized with config options switched off (False)
# When pressed, this switch is toggled and a message 'SHOW_CONFIG' is sent, which contains this ON/OFF value
# Further the button text is toggled between ON and OFF and the bg color between green and orange

widget("Config").mydata = False
widget("Layout").mydata = False
widget("Create").mydata = False

def function_callback(me,message_to_send):
    me.mydata = not me.mydata
    send(message_to_send,me.mydata)
    if me.mydata: me.config(text="OFF",bg="orange")
    else: me.config(text="ON",bg="green")

def call(widget_name,message_to_send,callback=function_callback):
    widget(widget_name).do_command(callback,message_to_send,True)

call("Config","SHOW_CONFIG")
call("Layout","SHOW_LAYOUT")
call("Create","SHOW_CREATE")

send("SHOW_CREATE",False)

### ========================================================
