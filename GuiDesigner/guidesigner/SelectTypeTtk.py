config(**{'grid_rows': '(6, 40, 0, 0)', 'bd': 2, 'relief': 'groove', 'grid_cols': '(3, 0, 0, 0)'})

Button('label',**{'pady': '1', 'padx': '1', 'compound': 'center', 'text': 'Label', 'photoimage': 'guidesigner/images/labelind.gif', 'bg': 'white'}).grid(sticky='nesw', row=0)
Button('entry',**{'pady': '1', 'padx': '1', 'compound': 'center', 'text': 'Entry', 'photoimage': 'guidesigner/images/entry.gif'}).grid(sticky='nesw', column=1, row=0)
Button('radiobutton',**{'pady': '1', 'padx': '3', 'compound': 'left', 'text': ' Radiobutton', 'photoimage': 'guidesigner/images/ttkradiobutton.gif'}).grid(sticky='nesw', column=2, row=1)
Button('button',**{'pady': '1', 'padx': '1', 'compound': 'center', 'text': 'Button', 'photoimage': 'guidesigner/images/button.gif'}).grid(sticky='nesw', row=1)
Button('checkbutton',**{'pady': '1', 'padx': '3', 'compound': 'left', 'text': ' Checkbutton', 'photoimage': 'guidesigner/images/ttkcheckbutton.gif'}).grid(sticky='nesw', column=1, row=1)
Button('frame',**{'pady': '1', 'padx': '1', 'compound': 'bottom', 'text': 'Frame', 'photoimage': 'guidesigner/images/frame.gif'}).grid(sticky='nesw', row=3)
Button('labelframe',**{'pady': '1', 'padx': '1', 'text': 'LabelFrame', 'photoimage': 'guidesigner/images/labelframe.gif'}).grid(sticky='nesw', column=1, row=3)
Button('panedwindow',**{'pady': '1', 'padx': '1', 'compound': 'bottom', 'text': 'PanedWindow', 'photoimage': 'guidesigner/images/panedwindow.gif'}).grid(sticky='nesw', column=2, row=3)
Button('scale',**{'width': 10, 'padx': '1', 'compound': 'bottom', 'text': 'Scale', 'photoimage': 'guidesigner/images/scale.gif'}).grid(sticky='nesw', row=2)
Button('scrollbar',**{'pady': '1', 'padx': '1', 'compound': 'bottom', 'text': 'Scrollbar', 'photoimage': 'guidesigner/images/ttkscrollbar.gif'}).grid(sticky='nesw', column=1, row=2)
Button('progressbar',**{'width': 10, 'pady': '1', 'padx': '1', 'compound': 'bottom', 'text': 'Progressbar', 'photoimage': 'guidesigner/images/progressbar.gif'}).grid(sticky='nesw', column=2, row=2)
Button('separator',**{'pady': '1', 'padx': '1', 'compound': 'bottom', 'text': 'Separator', 'photoimage': 'guidesigner/images/separator.gif'}).grid(sticky='nesw', column=2, row=0)
Button('menubutton',**{'pady': '1', 'padx': '1', 'compound': 'left', 'text': ' Menubutton', 'photoimage': 'guidesigner/images/menubutton.gif'}).grid(sticky='nesw', row=4)
Button('sizegrip',**{'pady': '1', 'padx': '1', 'compound': 'right', 'text': 'Sizegrip', 'photoimage': 'guidesigner/images/sizegrip.gif'}).grid(sticky='nesw', column=1, row=4)
Button('combobox',**{'padx': '1', 'text': 'Combobox', 'photoimage': 'guidesigner/images/combobox.gif'}).grid(sticky='nesw', row=5)
Button('notebook',**{'pady': '1', 'padx': '1', 'text': 'Notebook', 'photoimage': 'guidesigner/images/notebook.gif'}).grid(sticky='nesw', column=1, row=5)
Button('treeview',**{'width': 10, 'padx': '1', 'compound': 'left', 'text': ' Treeview', 'photoimage': 'guidesigner/images/Actions-view-list-tree-icon.gif'}).grid(sticky='nesw', column=2, row=4)

### CODE ===================================================

for item in (
    ('button','ttk.Button'),
    ('checkbutton','ttk.Checkbutton'),
    ('entry','ttk.Entry'),
    ('frame','ttk.Frame'),
    ('label','ttk.Label'),
    ('labelframe','ttk.LabelFrame'),
    ('menubutton','ttk.Menubutton'),
    ('panedwindow','ttk.PanedWindow'),
    ('radiobutton','ttk.Radiobutton'),
    ('scale','ttk.Scale'),
    ('scrollbar','ttk.Scrollbar'),
    ('separator','ttk.Separator'),
    ('combobox','ttk.Combobox'),
    ('notebook','ttk.Notebook'),
    ('progressbar','ttk.Progressbar'),
    ('sizegrip','ttk.Sizegrip'),
    ('treeview','ttk.Treeview'),
    ):
    widget(item[0]).do_command(lambda msg = (item[0],item[1]): send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

### ========================================================
