Canvas('canvas',**{'cursor': 'crosshair'})
goIn()


canvas=container()

coords = (228.0,68.0,338.0,108.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'#ffffde','tags':'house','outline':'gray'})

coords = (20.0,20.0,132.0,132.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'white','width':'16.0','outlinestipple':'@guidesigner/images/starMask','tags':'picture','outlineoffset':'-4,-4','outline':'#99311e'})

coords = (76.0,76.0)
item = canvas.create_bitmap(*coords)
canvas.itemconfig(item,**{'tags':'picture','foreground':'#79005c','bitmap':'@guidesigner/images/woman'})

coords = (211.0,70.0,247.0,43.0,319.0,43.0,355.0,70.0)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'fill':'#a80000','tags':'house'})

coords = (245.0,80.0,263.0,90.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'azure','width':'2.0','tags':'house','outline':'brown'})

coords = (304.0,80.0,322.0,90.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'azure','width':'2.0','tags':'house','outline':'brown'})

coords = (275.0,79.0,293.0,107.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'brown','tags':'house','outline':'brown'})

coords = (295.0,33.0,305.0,43.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'#7c0000','tags':'house','outline':'#7c0000'})


goOut()
grid(**{'row': '0'})
