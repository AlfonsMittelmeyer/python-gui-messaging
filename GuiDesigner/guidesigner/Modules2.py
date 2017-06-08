config(**{'grid_cols': '(5, 75, 0, 0)', 'grid_rows': '(1, 25, 0, 0)'})

Frame('ClassAndBaseLayout',**{'height': 100, 'bd': 2, 'width': 300})
goIn()

LabelFrame('baselayout',**{'link': 'guidesigner/BaseLayout.py'})
LabelFrame('widgetclass',**{'text': 'Widget Class'})
goIn()

Label('class_label',**{'pady': '2', 'relief': 'sunken', 'font': 'TkDefaultFont 9 bold', 'padx': '6', 'text': 'class_label', 'bg': 'yellow', 'fg': 'blue'})
Label('text',**{'padx': '4', 'text': 'Class'})

widget('text').pack(side='left')
widget('class_label').pack(padx=4, side='left', pady=6, fill='x')

goOut()
grid(sticky='ew', row=0)

goOut()
grid(column=1, sticky='new', row=0)
LabelFrame('ConfigOptions',**{'link': 'guidesigner/ConfigOptions.py'}).grid(column=2, sticky='nw', row=0)
Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(sticky='nw', row=0)
LabelFrame('DetailedLayout',**{'link': 'guidesigner/DetailedLayout.py'}).grid(column=3, sticky='nw', row=0)
LabelFrame('Selection',**{'link': 'guidesigner/Selection.py'}).grid(column=4, sticky='nw', row=0)

### CODE ===================================================

def hide_gui(message,cont = container()):
    if message: cont.unlayout()
    else: cont.pack(anchor='nw') # GuiFrame

do_receive('HIDE_GUI',hide_gui,wishMessage=True)

widget("ConfigOptions").unlayout()
widget("DetailedLayout").unlayout()

### ========================================================
