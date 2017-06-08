### CODE ===================================================

container().saveOnlyCode() # buttons are dynamically created, so the widgets shall not be saved. Only the code, which creates them shall be saved

index = 0
for widget_type in ("Message","Label","Button","Checkbutton","Radiobutton","Entry","Text","Spinbox","Scale","Listbox","Scrollbar","Frame","LabelFrame","PanedWindow","Canvas","Menu","Menubutton","Toplevel","LinkButton","LinkLabel","Paint Canvas"):

    row,column = divmod(index,3) # position in 3 columns
    width = 0 if column == 1 else 10
    if widget_type == 'Paunt Canvas':
        width = 0
    Button(widget_type,text=widget_type,padx=1,width=width) # Button with name and text of widget class

    rcgrid(row,column,sticky='ew') # grid layout row,column

    do_command(lambda msg = (decapitalize(widget_type),widget_type): send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name
    index += 1 # increase index

widget("Paint Canvas").config(fg='blue',font="TkDefaultFont 9 bold",activeforeground="blue",command="")
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

