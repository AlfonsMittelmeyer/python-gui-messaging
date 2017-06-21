Button('Button',**{'text': 'Button', 'padx': 1, 'width': 10}).grid(sticky='ew', column=2, row=0)
Button('Canvas',**{'text': 'Canvas', 'padx': 1, 'width': 10}).grid(sticky='ew', column=2, row=4)
Button('Checkbutton',**{'text': 'Checkbutton', 'padx': 1, 'width': 10}).grid(sticky='ew', row=1)
Button('Entry',**{'text': 'Entry', 'padx': 1, 'width': 10}).grid(sticky='ew', column=2, row=1)
Button('Frame',**{'text': 'Frame', 'padx': 1, 'width': 10}).grid(sticky='ew', column=2, row=3)
Button('Label',**{'text': 'Label', 'padx': 1}).grid(sticky='ew', column=1, row=0)
Button('LabelFrame',**{'text': 'LabelFrame', 'padx': 1, 'width': 10}).grid(sticky='ew', row=4)
Button('LinkButton',**{'text': 'LinkButton', 'padx': 1, 'width': 10}).grid(sticky='ew', row=6)
Button('LinkLabel',**{'text': 'LinkLabel', 'padx': 1}).grid(sticky='ew', column=1, row=6)
Button('Listbox',**{'text': 'Listbox', 'padx': 1, 'width': 10}).grid(sticky='ew', row=3)
Button('Menu',**{'text': 'Menu', 'padx': 1, 'width': 10}).grid(sticky='ew', row=5)
Button('Menubutton',**{'text': 'Menubutton', 'padx': 1}).grid(sticky='ew', column=1, row=5)
Button('Message',**{'text': 'Message', 'padx': 1, 'width': 10}).grid(sticky='ew', row=0)
Button('Paint Canvas',**{'font': 'TkDefaultFont 9 bold', 'text': 'Paint Canvas', 'padx': 1, 'activeforeground': 'blue', 'fg': 'blue'}).grid(sticky='ew', column=2, row=6)
Button('PanedWindow',**{'text': 'PanedWindow', 'padx': 1}).grid(sticky='ew', column=1, row=4)
Button('Radiobutton',**{'text': 'Radiobutton', 'padx': 1}).grid(sticky='ew', column=1, row=1)
Button('Scale',**{'text': 'Scale', 'padx': 1, 'width': 10}).grid(sticky='ew', column=2, row=2)
Button('Scrollbar',**{'text': 'Scrollbar', 'padx': 1}).grid(sticky='ew', column=1, row=3)
Button('Spinbox',**{'text': 'Spinbox', 'padx': 1}).grid(sticky='ew', column=1, row=2)
Button('Text',**{'text': 'Text', 'padx': 1, 'width': 10}).grid(sticky='ew', row=2)
Button('Toplevel',**{'text': 'Toplevel', 'padx': 1, 'width': 10}).grid(sticky='ew', column=2, row=5)

### CODE ===================================================

for widget_type in ("Message","Label","Button","Checkbutton","Radiobutton","Entry","Text","Spinbox","Scale","Listbox","Scrollbar","Frame","LabelFrame","PanedWindow","Canvas","Menu","Menubutton","Toplevel","LinkButton","LinkLabel","Paint Canvas"):
    widget(widget_type).do_command(lambda msg = (decapitalize(widget_type),widget_type): send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

widget("Paint Canvas").unlayout()

def open_canvas_paint():
    cont = this() if isinstance(this(),Canvas) else container()
    DynAccess('guidesigner/canvas/CanvasPaint.py',(cont,this()),_Application)

widget("Paint Canvas").do_command(open_canvas_paint)


def do_canvas_selected(paint_button = widget("Paint Canvas")):
    if isinstance(this(),Canvas) and this().Layout != NOLAYOUT or isinstance(container(),Canvas) and container().Layout != NOLAYOUT: paint_button.grid()
    else: paint_button.unlayout()

do_receive('SELECTION_LAYOUT_CHANGED',do_canvas_selected)
do_receive('SELECTION_CHANGED',do_canvas_selected)

### ========================================================
