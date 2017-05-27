config(text='tkinter or ttk', grid_rows='(1, 0, 0, 0)', grid_cols='(4, 0, 0, 1)')

Button('button_ttk',text='ttk', width=8).grid(row=0, column=1)
Label('label_selected',pady='2', text='tkinter', relief='sunken', padx='0', bg='yellow', width=8).grid(row=0)
Button('loadstyles',text='load styles').grid(row=0, column=2)
Label('styles',pady='2', text='styles.py', relief='sunken', padx='12', bg='gray97').grid(row=0, column=3)

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



def load_styles():
    selection = Selection()

    filename = 'TtkStyles/styles.py'
    try:
        exec(compile(open(filename, "r").read(), filename, 'exec'))
    except (FileNotFoundError,SyntaxError) as e:
        traceback.print_exc()

    setSelection(selection)


widget('loadstyles')['command'] = load_styles

### ========================================================
