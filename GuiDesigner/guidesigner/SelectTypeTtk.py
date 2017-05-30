config(relief='groove', bd=2)

Button('button',text='Button', width=10).grid(row=0, column=1)
Button('checkbutton',text='Checkbutton', width=10).grid(row=0, column=2)
Button('combobox',text='Combobox', width=10).grid(row=4)
Button('entry',text='Entry', width=10).grid(row=1, column=1)
Button('frame',text='Frame', width=10).grid(row=2, column=1)
Button('label',text='Label', width=10).grid(row=0)
Button('labelframe',text='LabelFrame', width=10).grid(row=2, column=2)
Button('menubutton',text='Menubutton').grid(row=3, column=1)
Button('panedwindow',text='PanedWindow', width=10).grid(row=3)
Button('radiobutton',text='Radiobutton', width=10).grid(row=1)
Button('scale',text='Scale', width=10).grid(row=1, column=2)
Button('scrollbar',text='Scrollbar', width=10).grid(row=2)
Button('separator',text='Separator', width=10).grid(row=3, column=2)

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
    ('combobox','ttk.Combobox')
    
    ):
    widget(item[0]).do_command(lambda msg = (item[0],item[1]): send('CREATE_CLASS_SELECTED',msg)) # buttons send message with class name

### ========================================================
