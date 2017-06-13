config(**{'grid_rows': '(1, 0, 0, 1)', 'grid_cols': '(5, 0, 0, 1)'})
Frame('ClassAndBaseLayout',**{'link': 'guidesigner/ClassAndBaseLayout.py'}).grid(sticky='new', column=1, row=0)
LabelFrame('ConfigOptions',**{'link': 'guidesigner/ConfigOptions.py'}).grid(sticky='nw', column=2, row=0)
Frame('CreateFrame',**{'link': 'guidesigner/CreateFrame.py'}).grid(sticky='nw', row=0)
LabelFrame('DetailedLayout',**{'link': 'guidesigner/DetailedLayout.py'}).grid(sticky='nw', column=3, row=0)
LabelFrame('Selection',**{'link': 'guidesigner/Selection.py'}).grid(sticky='nw', column=4, row=0)

### CODE ===================================================

def hide_gui(message,cont = container()):
    if message: cont.unlayout()
    else: cont.pack(anchor='nw') # GuiFrame

do_receive('HIDE_GUI',hide_gui,wishMessage=True)

widget("ConfigOptions").unlayout()
widget("DetailedLayout").unlayout()

### ========================================================
