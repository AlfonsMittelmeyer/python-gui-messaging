config(geometry='316x171+792+63')

LabelFrame('labelFrame',text='Some Frame Somewhere in the GUI')
goIn()

Button('toggle',text='Toggle Satus', pady='3m', bd='3')

widget('toggle').pack(pady=20)

goOut()

Label('toggle_status',text='toggle_status', bg='white', pady='7')

widget('toggle_status').pack(fill='x', pady=2)
widget('labelFrame').pack()
