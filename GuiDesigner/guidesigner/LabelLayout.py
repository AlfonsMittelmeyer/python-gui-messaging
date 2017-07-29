Label('label',**{'relief': 'sunken', 'pady': '2', 'font': 'TkDefaultFont 9 {bold }', 'fg': 'blue', 'text': 'labelwidget', 'padx': '5', 'bd': '2'})
rcgrid(0,0)
Button('set',**{'pady': '1', 'font': 'Courier 9 {}', 'text': 'SET', 'bg': 'lightgreen', 'padx': '5m', 'bd': '3'})
rcgrid(0,1,padx=5)

### CODE ===================================================

label_bg = widget('label')['bg']

def refresh(label = widget('label'),set_button = widget('set'),bg = label_bg):
    if isinstance(container(),(LabelFrame,ttk.LabelFrame)):
        if this().Layout == LABELLAYOUT:
            label['bg'] = 'yellow'
            set_button.unlayout()
        else:
            label['bg'] = bg
            set_button.grid()

do_receive('BASE_LAYOUT_REFRESH', refresh)


def set_label(refresh=refresh):
    layout_before = this().Layout
    labelwidget()
    send('BASE_LAYOUT_CHANGED',layout_before)

widget('set').do_command(set_label)

### ========================================================
