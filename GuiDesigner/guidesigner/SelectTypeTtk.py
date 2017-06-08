config(**{'bd': 2, 'relief': 'groove', 'height': 250, 'width': 500})

Button('button',**{'text': 'Button', 'padx': '1', 'width': 10}).grid(row=0, column=1)
Button('checkbutton',**{'text': 'Checkbutton', 'padx': '1', 'width': 10}).grid(row=0, column=2)
Button('combobox',**{'text': 'Combobox', 'padx': '1'}).grid(sticky='ew', row=4)
Button('entry',**{'text': 'Entry', 'padx': '1', 'width': 10}).grid(row=1, column=1)
Button('frame',**{'text': 'Frame', 'padx': '1', 'width': 10}).grid(row=2, column=1)
Button('label',**{'text': 'Label', 'padx': '1'}).grid(sticky='ew', row=0)
Button('labelframe',**{'text': 'LabelFrame', 'padx': '1', 'width': 10}).grid(row=2, column=2)
Button('menubutton',**{'text': 'Menubutton', 'padx': '1'}).grid(sticky='ew', row=3, column=1)
Button('notebook',**{'text': 'Notebook', 'padx': '1', 'width': 10}).grid(row=4, column=1)
Button('panedwindow',**{'text': 'PanedWindow', 'padx': '1'}).grid(sticky='ew', row=3)
Button('progressbar',**{'text': 'Progressbar', 'padx': '1', 'width': 10}).grid(row=4, column=2)
Button('radiobutton',**{'text': 'Radiobutton', 'padx': '1'}).grid(sticky='ew', row=1)
Button('scale',**{'text': 'Scale', 'padx': '1', 'width': 10}).grid(row=1, column=2)
Button('scrollbar',**{'text': 'Scrollbar', 'padx': '1'}).grid(sticky='ew', row=2)
Button('separator',**{'text': 'Separator', 'padx': '1', 'width': 10}).grid(row=3, column=2)
Button('sizegrip',**{'text': 'Sizegrip', 'padx': '1'}).grid(sticky='ew', row=5)
Button('treeview',**{'text': 'Treeview', 'padx': '1', 'width': 10}).grid(row=5, column=1)

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
