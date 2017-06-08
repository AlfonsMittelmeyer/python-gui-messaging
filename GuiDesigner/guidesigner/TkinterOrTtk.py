config(**{'text': 'tkinter or ttk'})

Button('button_ttk',**{'padx': '1', 'width': 11, 'text': 'ttk'}).grid(column=1, row=0, pady=2)
Label('label_selected',**{'padx': '0', 'bg': 'yellow', 'width': 9, 'pady': '2', 'text': 'tkinter'}).grid(row=0, padx=10)
Button('loadstyles',**{'padx': '1', 'width': 11, 'text': 'load styles'}).grid(column=1, row=1, pady=2)
Label('styles',**{'bg': 'gray97', 'width': 9, 'pady': '2', 'text': 'styles.py'}).grid(row=1, padx=10)

### CODE ===================================================
import os
def switch_ttk(
    label = widget('label_selected'),
    button = widget('button_ttk'),
    loadstyles = widget('loadstyles'),
    styles = widget('styles')
    ):

    button.mydata = not button.mydata

    if button.mydata:
        label['text'] = 'ttk'
        button['text'] = 'tkinter'
        loadstyles.grid()
        styles.grid()
    else:
        label['text'] = 'tkinter'
        button['text'] = 'ttk'
        loadstyles.unlayout()
        styles.unlayout()

    send("SELECT_TTK",button.mydata)

widget('button_ttk')['command'] = switch_ttk
widget('button_ttk').mydata = True
switch_ttk()



def load_styles(style = widget('styles')):
    selection = Selection()

    filename = 'TtkStyles/styles.py'
    try:
        exec(compile(open(filename, "r").read(), filename, 'exec'))
        style['fg'] = 'blue'
    except (FileNotFoundError,SyntaxError) as e:
        traceback.print_exc()
                

    setSelection(selection)


widget('loadstyles')['command'] = load_styles

### ========================================================
