Button('command',text='command',width='9').grid(row='0')
Button('cascade',text='cascade',width='9').grid(row='1')
Button('separator',text='separator',width='9').grid(row='2')
Button('checkbutton',text='checkbutton',width='11').grid(column='1',row='0')
Button('radiobutton',text='radiobutton',width='11').grid(column='1',row='1')
Button('tearoff',text='tearoff',width='11').grid(column='1',row='2')

### CODE ===================================================

for item in (
    ('cascade','cascade'),
    ('radiobutton','radiobutton'),
    ('command','command'),
    ('separator','separator'),
    ('checkbutton','checkbutton'),
    ('tearoff','delimiter')):
    widget(item[0]).do_command(lambda msg = (item[0],item[1]): send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

### ========================================================
