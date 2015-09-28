Button('cascade',text="""cascade""",width='9').grid(row='2')
Button('radiobutton',text="""radiobutton""",width='11').grid(column='1',row='1')
Button('command',text="""command""",width='9').grid(row='0')
Button('separator',text="""separator""",width='9').grid(row='1')
Button('checkbutton',text="""checkbutton""",width='11').grid(column='1',row='0')

### CODE ===================================================

for widget_type in ('cascade','radiobutton','command','separator','checkbutton'):
    widget(widget_type).do_command(lambda msg = widget_type: send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

### ========================================================
