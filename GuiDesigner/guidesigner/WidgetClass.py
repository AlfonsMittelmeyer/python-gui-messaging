config(**{'text': 'Widget Class'})

Label('class_label',**{'bg': 'yellow', 'text': 'class_label', 'padx': '6', 'pady': '2', 'fg': 'blue', 'relief': 'sunken', 'font': 'TkDefaultFont 9 bold'})
Label('text',**{'text': 'class', 'padx': '4'})

widget('text').pack(side='left')
widget('class_label').pack(pady=6, side='left', fill='x', padx=4)

### CODE ===================================================

def show_class(class_label = widget('class_label')):
    #class_label['text'] = WidgetClass(this())
    a = str(type(this()))
    b = a.split("'")
    c = b[1]
    d = c.split(".")
    e = 'ttk.'+d[1] if d[0] == 'DynTtk' else d[1]
    class_label['text'] = e

do_receive('SELECTION_CHANGED',show_class)
### ========================================================
