ttk.Notebook('notebook',**{'width': 400, 'height': 300})
goIn()

LabelFrame('labelFrame1',**{'text': 'labelFrame1'})
LabelFrame('labelFrame2',**{'text': 'labelFrame2'})
LabelFrame('labelFrame3',**{'text': 'labelFrame3'})

widget('labelFrame1').page(photoimage='Images/butterfly.gif', text='Eingabe', compound='right')
widget('labelFrame2').page(text='Ausgabe')
widget('labelFrame3').page()

goOut()


widget('notebook').pack()
