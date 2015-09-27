### CODE ===================================================

container().saveOnlyCode() # buttons are dynamically created, so the widgets shall not be saved. Only the code, which creates them shall be saved

index = 0
for widget_type in ("Message","Label","Button","Checkbutton","Radiobutton","Entry","Text","Spinbox","Scale","Listbox","Scrollbar","Frame","LabelFrame","PanedWindow","Canvas","Menu","Menubutton","Toplevel"):

    Button(widget_type,text=widget_type,width=10) # Button with name and text of widget class

    row,column = divmod(index,2) # position in 2 columns
    rcgrid(row,column) # grid layout row,column

    do_command(lambda msg = widget_type: send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name
    index += 1 # increase index

### ========================================================

