config(**{'text': 'Create Widget', 'grid_cols': '(4, 43, 0, 0)', 'grid_multi_cols': '[4, (1, 64, 0, 0), (2, 3, 0, 0), (3, 26, 0, 0)]', 'grid_rows': '(2, 25, 0, 0)'})

Button('Create',**{'text': 'Create', 'pady': '1', 'padx': '1', 'bd': '3', 'bg': 'green'}).grid(**{'column': '3', 'sticky': 'nes', 'row': '0'})
Label('Label',**{'text': 'Class'}).grid(**{'row': '0'})
Label('Label',**{'text': 'Name'}).grid(**{'row': '1'})
Entry('Name').grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '3', 'row': '1'})
Label('Type',**{'text': 'Button', 'font': 'TkDefaultFont 9 bold', 'bg': 'yellow', 'fg': 'blue', 'relief': 'ridge'}).grid(**{'column': '1', 'sticky': 'ew', 'row': '0'})

### CODE ===================================================

# the class name is stored in mydata of widget('Name')
callback = lambda wname = widget("Name"): send('CREATE_WIDGET_REQUEST',(wname.mydata,wname.get()))

widget("Create").do_command(callback)
widget("Name").do_event("<Return>",callback)

# ---- Receiver for message 'CREATE_CLASS_SELECTED': changes the text of Label 'Type' to the Class name and stores the Class name in mydata of Entry 'Name'

def function(msg,wname,wtype):
    wname.mydata = msg
    wname.delete(0,END)
    wname.insert(0,decapitalize(msg))
    #wname.insert(0,msg)
    wtype['text'] = msg
    wname.focus_set()

do_receive('CREATE_CLASS_SELECTED',function,(widget('Name'),widget('Type')),wishMessage=True)

# ---- Initialization with Class 'Button' ---------------------------

send('CREATE_CLASS_SELECTED','Button')

### ========================================================
