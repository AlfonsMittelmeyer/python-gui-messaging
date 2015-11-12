### CODE ===================================================

container().saveOnlyCode() # buttons are dynamically created, so the widgets shall not be saved. Only the code, which creates them shall be saved

index = 0
for widget_type in ("Message","Label","Button","Checkbutton","Radiobutton","Entry","Text","Spinbox","Scale","Listbox","Scrollbar","Frame","LabelFrame","PanedWindow","Canvas","Menu","Menubutton","Toplevel","LinkButton","LinkLabel","Paint Canvas"):

    Button(widget_type,text=widget_type,width=10) # Button with name and text of widget class

    row,column = divmod(index,3) # position in 3 columns
    rcgrid(row,column) # grid layout row,column

    do_command(lambda msg = widget_type: send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name
    index += 1 # increase index

widget("Paint Canvas").config(fg='blue',font="TkDefaultFont 9 bold",activeforeground="blue",command="")
widget("Paint Canvas").unlayout()

def do_canvas_selected(paint_button = widget("Paint Canvas")):
    if isinstance(this(),Canvas): paint_button.grid()
    else: paint_button.unlayout()

#do_receive("SELECTION_CHANGED",do_canvas_selected)
### ========================================================

