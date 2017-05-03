Canvas('canvas',**{'cursor': 'crosshair'})
goIn()


canvas=container()

coords = (129.0,76.0,206.0,181.0)
item = canvas.create_oval(*coords)
coords = (279.0,64.0)
item = canvas.create_image(*coords)
canvas.itemconfig(item,**{'photoimage':'guidesigner/images/butterfly.gif'})


goOut()


widget('canvas').pack()
