config(**{'text': 'Widget Class'})

Label('class_label',**{'bg': 'yellow', 'text': 'class_label', 'padx': '6', 'pady': '2', 'fg': 'blue', 'relief': 'sunken', 'font': 'TkDefaultFont 9 bold'})
Label('text',**{'text': 'Class', 'padx': '4'})

widget('text').pack(side='left')
widget('class_label').pack(pady=6, side='left', fill='x', padx=4)

### CODE ===================================================

def show_class(class_label = widget('class_label')):
    class_label['text'] = WidgetClass(this())

do_receive('SELECTION_CHANGED',show_class)
### ========================================================
