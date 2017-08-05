config(**{'grid_cols': '(2, 40, 0, 0)', 'grid_rows': '(2, 0, 0, 0)'})

Button('button_ttk',**{'pady': '2', 'text': 'ttk', 'padx': '1', 'width': 11}).grid(row=0, pady=2, column=1)
Label('label_selected',**{'text': 'tkinter', 'padx': '0', 'bg': 'yellow', 'pady': '2', 'width': 9}).grid(row=0, padx=10)
Button('loadstyles',**{'pady': '2', 'text': 'load styles', 'padx': '1', 'width': 11}).grid(row=1, pady=2, column=1)
Label('styles',**{'text': 'styles.py', 'bg': 'gray97', 'pady': '2', 'width': 9}).grid(row=1, padx=10)

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
        exec(compile(open(filename, "r",encoding="utf-8").read(), filename, 'exec'))
        style['fg'] = 'blue'
    except (FileNotFoundError,SyntaxError) as e:
        traceback.print_exc()
                

    setSelection(selection)


widget('loadstyles')['command'] = load_styles

### ========================================================
