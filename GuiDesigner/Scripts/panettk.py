ttk.PanedWindow('panedWindow',width=400, orient='horizontal', height=200)
goIn()

ttk.LabelFrame('labelFrame',text='labelFrame1')
ttk.LabelFrame('labelFrame2',text='labelFrame2')
ttk.LabelFrame('labelFrame3',text='labelFrame3')

widget('labelFrame').pane()
widget('labelFrame2').pane()
widget('labelFrame3').pane()
container().sashpos(0,137)
container().sashpos(1,265)
# === may be neccessary: depends on your system ===============================
container().after(100,lambda funct=container().sashpos: funct(0,137))
container().after(100,lambda funct=container().sashpos: funct(1,265))

goOut()


widget('panedWindow').pack()
