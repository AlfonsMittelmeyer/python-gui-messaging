Frame("Buttons",link="guidesigner/Buttons.py")
pack()

Frame("SelectionShow",bg="white",link="guidesigner/SelectionShow.py")
pack()

### CODE ===================================================

# ---- Receiver for message 'CREATE_WIDGET_REQUEST' - somewhere it has to be: 
# creates the widget with Class name and widget name in the current User selection and sends the message CREATE_WIDGET_DONE which contains the current user widget selection

def create_widget(msg):
    eval(msg[0]+"('"+msg[1]+"')")
    text(msg[1])
    send('SELECTION_CHANGED')

do_receive('CREATE_WIDGET_REQUEST',create_widget,wishMessage=True)
do_receive("SELECTION_CHANGED", lambda: send('SHOW_SELECTION'))
do_receive("SELECTION_LAYOUT_CHANGED", lambda: send('SHOW_SELECTION'))

### ========================================================
