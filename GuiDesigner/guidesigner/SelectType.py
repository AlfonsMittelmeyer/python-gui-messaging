config(**{'grid_cols': '(3, 0, 0, 0)', 'grid_rows': '(7, 25, 0, 0)'})

Button('Canvas',**{'padx': 1, 'pady': '1', 'photoimage': 'guidesigner/images/graphics32.gif', 'text': ' Canvas', 'compound': 'left'}).grid(sticky='nesw', row=4, column=2)
Button('Label',**{'padx': 1, 'photoimage': 'guidesigner/images/labelind.gif', 'text': 'Label', 'bg': 'white', 'compound': 'center'}).grid(sticky='nesw', row=0, column=1)
Button('Menubutton',**{'padx': 1, 'photoimage': 'guidesigner/images/menubutton.gif', 'text': ' Menubutton', 'compound': 'left'}).grid(sticky='nesw', row=5, column=1)
Button('Message',**{'padx': 1, 'photoimage': 'guidesigner/images/accessories-text-editor.gif', 'text': 'Message', 'width': 10, 'compound': 'left'}).grid(sticky='nesw', row=0)
Button('Paint Canvas',**{'padx': 1, 'font': 'TkDefaultFont 9 bold', 'photoimage': 'guidesigner/images/graphics.gif', 'activeforeground': 'blue', 'text': 'Paint Canvas', 'fg': 'blue', 'compound': 'left'}).grid(sticky='nesw', row=6, column=2)
Button('Entry',**{'padx': 1, 'pady': '1', 'photoimage': 'guidesigner/images/entry.gif', 'text': 'Entry', 'compound': 'center'}).grid(sticky='nesw', row=0, column=2)
Button('Radiobutton',**{'padx': 1, 'photoimage': 'guidesigner/images/radiobutton.gif', 'text': ' Radiobutton', 'compound': 'left'}).grid(sticky='nesw', row=1, column=2)
Button('Checkbutton',**{'padx': '3', 'pady': '1', 'photoimage': 'guidesigner/images/checkbutton.gif', 'text': ' Checkbutton', 'compound': 'left'}).grid(sticky='nesw', row=1, column=1)
Button('Button',**{'padx': 1, 'photoimage': 'guidesigner/images/button.gif', 'text': 'Button', 'compound': 'center'}).grid(sticky='nesw', row=1)
Button('Spinbox',**{'padx': 1, 'pady': '1', 'photoimage': 'guidesigner/images/spinbox.gif', 'text': 'Spinbox', 'compound': 'center'}).grid(sticky='nesw', row=2)
Button('Scale',**{'padx': 1, 'photoimage': 'guidesigner/images/scale.gif', 'text': 'Scale', 'width': 10, 'compound': 'bottom'}).grid(sticky='nesw', row=2, column=1)
Button('Scrollbar',**{'padx': 1, 'photoimage': 'guidesigner/images/scrollbar.gif', 'text': 'Scrollbar', 'compound': 'bottom'}).grid(sticky='nesw', row=2, column=2)
Button('Frame',**{'padx': 1, 'photoimage': 'guidesigner/images/frame.gif', 'text': 'Frame', 'compound': 'bottom'}).grid(sticky='nesw', row=3)
Button('LabelFrame',**{'padx': 1, 'photoimage': 'guidesigner/images/labelframe.gif', 'text': 'LabelFrame', 'width': 10}).grid(sticky='nesw', row=3, column=1)
Button('PanedWindow',**{'padx': 1, 'photoimage': 'guidesigner/images/panedwindow.gif', 'text': 'PanedWindow', 'compound': 'bottom'}).grid(sticky='nesw', row=3, column=2)
Button('Listbox',**{'padx': 1, 'photoimage': 'guidesigner/images/listbox.gif', 'text': 'Listbox', 'width': 10}).grid(sticky='ew', row=4)
Button('Toplevel',**{'padx': 1, 'photoimage': 'guidesigner/images/toplevel.gif', 'text': 'Toplevel'}).grid(sticky='ew', row=5, column=2)
Button('LinkLabel',**{'padx': 1, 'photoimage': 'guidesigner/images/go-next24.gif', 'text': ' LinkLabel', 'compound': 'left'}).grid(sticky='nesw', row=6)
Button('LinkButton',**{'padx': 1, 'photoimage': 'guidesigner/images/go-next24.gif', 'text': ' LinkButton', 'width': 10, 'compound': 'left'}).grid(sticky='nesw', row=6, column=1)
Button('Menu',**{'padx': 1, 'photoimage': 'guidesigner/images/menu.gif', 'text': ' Menu', 'compound': 'left'}).grid(sticky='nesw', row=5)
Button('Text',**{'photoimage': 'guidesigner/images/text.gif', 'text': 'Text'}).grid(sticky='nesw', row=4, column=1)

### CODE ===================================================

for widget_type in ("Message","Label","Button","Checkbutton",'Text',"Radiobutton","Entry","Spinbox","Scale","Listbox","Scrollbar","Frame","LabelFrame","PanedWindow","Canvas","Menu","Menubutton","Toplevel","LinkButton","LinkLabel","Paint Canvas"):
    widget(widget_type).do_command(lambda msg = (decapitalize(widget_type),widget_type): send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

widget("Paint Canvas").unlayout()

def open_canvas_paint():
    cont = this() if isinstance(this(),Canvas) else container()
    DynAccess('guidesigner/canvas/CanvasPaint.py',(cont,this()),_Application)

widget("Paint Canvas").do_command(open_canvas_paint)


def dont_select(paint_button = widget("Paint Canvas"),menu_button = widget('Menu')):
    if isinstance(this(),Canvas) and this().Layout != NOLAYOUT or isinstance(container(),Canvas) and container().Layout != NOLAYOUT: paint_button.grid()
    else: paint_button.unlayout()

    menu_button['state'] = 'normal' if isinstance(container(),(Tk,Toplevel)) else 'disabled'

do_receive('SELECTION_LAYOUT_CHANGED',dont_select)
do_receive('SELECTION_CHANGED',dont_select)

### ========================================================
