config(**{'grid_multi_cols': '[5, (4, 0, 0, 1)]', 'grid_rows': '(1, 30, 2, 0)', 'grid_cols': '(5, 0, 1, 0)'})

Button('lift',**{'pady': '2', 'bg': 'lightgreen', 'text': 'lift', 'padx': '1m', 'bd': '3', 'width': 5}).grid(column=2, row=0, padx=1)
Button('lower',**{'pady': '2', 'bg': 'lightgreen', 'text': 'lower', 'padx': '1m', 'bd': '3', 'width': 5}).grid(column=3, row=0)
Spinbox('spinbox',**{'from_': -100.0, 'width': 4, 'insertwidth': 3}).grid(sticky='ns', column=1, row=0, pady=4, padx=3)
Label('title',**{'fg': 'blue', 'bg': 'yellow', 'padx': '2', 'text': 'z-order', 'bd': '3', 'font': 'TkDefaultFont 9 bold', 'relief': 'ridge'}).grid(sticky='w', row=0)

### CODE ===================================================


def basement(event = None,spinbox = widget('spinbox')):
    value = spinbox.get()
    try:
        value = int(value)
        this().dyntk_basement(value)
    except: ValueError

    send('BASEMENTLEVEL_CHANGED')

widget('spinbox').do_command(basement)
widget('spinbox').bind('<Return>',basement)

def do_lift():
    if not isinstance(this(),Canvas):
        this().lift()
        send('BASEMENTLEVEL_CHANGED')

widget('lift').do_command(do_lift)


def do_lower():
    if not isinstance(this(),Canvas):
        this().lower()
        send('BASEMENTLEVEL_CHANGED')

widget('lower').do_command(do_lower)

def level_changed(spinbox = widget('spinbox')):
    if this() !=container()\
    and isinstance(container(),(Tk,Toplevel,Frame,LabelFrame,ttk.Frame,ttk.LabelFrame))\
    and not isinstance(this(),StatTkInter.Menu):
        children = container().winfo_children()
        children_copy = list(children)
        for child in children_copy:
            if isinstance(child,(StatTkInter.Menu,StatTkInter.Toplevel)):
                children.pop(children.index(child))
        count = len(children)
        spinbox.delete(0,END)
        spinbox.insert(0,children.index(this())-count+1)

do_receive('BASEMENTLEVEL_CHANGED',level_changed)
do_receive("SELECTION_CHANGED",level_changed)
### ========================================================
