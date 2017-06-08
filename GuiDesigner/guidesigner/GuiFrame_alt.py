Frame('ClassAndBaseLayout',**{'bd': 2, 'height': 100, 'width': 300})
goIn()

LabelFrame('baselayout',**{'link': 'guidesigner/BaseLayout.py'}).grid(pady=7, row=1)
LabelFrame('widgetclass',**{'text': 'Widget Class'})
goIn()

Label('class_label',**{'fg': 'blue', 'pady': '2', 'text': 'class_label', 'bg': 'yellow', 'relief': 'sunken', 'font': 'TkDefaultFont 9 bold', 'padx': '6'})
Label('text',**{'text': 'Class', 'padx': '4'})

widget('text').pack(side='left')
widget('class_label').pack(fill='x', pady=6, padx=4, side='left')

### CODE ===================================================


# Widget Class
### ========================================================

goOut()
grid(row=0, sticky='ew')

goOut()
grid(row=0, column=1, sticky='new')
LabelFrame('ConfigOptions',**{'link': 'guidesigner/ConfigOptions.py'}).grid(row=0, column=2, sticky='nw')
Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(row=0, sticky='nw')
LabelFrame('DetailedLayout',**{'link': 'guidesigner/DetailedLayout.py'}).grid(row=0, column=3, sticky='nw')
LabelFrame('Selection',**{'link': 'guidesigner/Selection.py'}).grid(row=0, column=4, sticky='nw')

### CODE ===================================================

def hide_gui(message,cont = container()):
    if message: cont.unlayout()
    else: cont.pack(anchor='nw') # GuiFrame

do_receive('HIDE_GUI',hide_gui,wishMessage=True)

widget("ConfigOptions").unlayout()
widget("DetailedLayout").unlayout()

### ========================================================
