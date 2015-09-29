Button('command',text="""command""",width='9').grid(row='0')
Button('cascade',text="""cascade""",width='9').grid(row='1')
Button('separator',text="""separator""",width='9').grid(row='2')
Button('checkbutton',text="""checkbutton""",width='11').grid(column='1',row='0')
Button('radiobutton',text="""radiobutton""",width='11').grid(column='1',row='1')
Button('delimiter',text="""delimiter""",width='11').grid(column='1',row='2')

### CODE ===================================================

for widget_type in ('cascade','radiobutton','command','separator','checkbutton','delimiter'):
    widget(widget_type).do_command(lambda msg = widget_type: send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

### ========================================================
