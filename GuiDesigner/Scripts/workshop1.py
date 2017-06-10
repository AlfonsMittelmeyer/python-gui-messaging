config(**{'minsize': '500 400'})

Frame('frame_guinotes',**{'highlightthickness': 7, 'highlightbackground': '#a90000', 'highlightcolor': '#a90000'})
goIn()

Text('notes_gui',**{'pady': 8, 'font': 'TkFixedFont 12 bold', 'width': 1, 'height': 1, 'padx': 8})
this().delete(1.0, END)
this().insert(END,'Und da kommt die eigentlich GUI Anwendung')

widget('notes_gui').pack(expand=1, fill='both')

goOut()

Frame('frame_menunotes',**{'highlightthickness': 7, 'highlightbackground': 'blue', 'highlightcolor': 'blue'})
goIn()

Text('notes_menu',**{'pady': 8, 'font': 'TkFixedFont 12 bold', 'height': 1, 'padx': 8, 'fg': 'blue'})
this().delete(1.0, END)
this().insert(END,'Oben soll ein Menü sein')

widget('notes_menu').pack(expand=1, fill='both')

goOut()

Frame('frame_toolbarnotes',**{'highlightthickness': 7, 'highlightbackground': '#008900', 'relief': 'sunken', 'highlightcolor': '#008900'})
goIn()

Text('notes_toolbar',**{'pady': 8, 'font': 'TkFixedFont 12 bold', 'height': 1, 'padx': 8, 'fg': '#008900'})
this().delete(1.0, END)
this().insert(END,'Darunter kommt eine Toolbar mit Photoimages')

widget('notes_toolbar').pack(expand=1, fill='both')

goOut()

Label('label_PS',**{'anchor': 'w', 'pady': '4', 'font': 'TkFixedFont 10 bold', 'relief': 'solid', 'bd': '4', 'justify': 'left', 'text': 'Welches Layout soll man nehmen?\nUnd soll man einen GuiBuilder nehmen?\nWenn ja, welchen?', 'padx': '4', 'fg': '#a90000'})

widget('frame_menunotes').pack(fill='x')
widget('frame_toolbarnotes').pack(fill='x')
widget('frame_guinotes').pack(expand=1, fill='both')
widget('label_PS').pack(pady=3, fill='x')
