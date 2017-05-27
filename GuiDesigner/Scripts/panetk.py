PanedWindow('panedWindow',width='400', height='200')
goIn()

LabelFrame('labelFrame',text='labelFrame1')
LabelFrame('labelFrame2',text='labelFrame2')
LabelFrame('labelFrame3',text='labelFrame3')

widget('labelFrame').pane()
widget('labelFrame2').pane()
widget('labelFrame3').pane()
container().sash_place(0,103,1)
container().sash_place(1,242,1)

goOut()


widget('panedWindow').pack()

