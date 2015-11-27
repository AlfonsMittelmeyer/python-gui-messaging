Canvas('canvas',**{'height': '500', 'width': '700', 'cursor': 'crosshair'})
goIn()


canvas=container()

coords = (97.0,133.0)
item = canvas.create_image(*coords)
canvas.itemconfig(item,**{'photoimage':'guidesigner/images/butterfly.gif'})

coords = (129.0,44.0,359.0,154.12711864406776)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'#ffffe1','width':'7.0','outlinestipple':'gray75','tags':'schild','outline':'#7c0909'})

coords = (276.16101694915255,98.57627118644064)
item = canvas.create_bitmap(*coords)
canvas.itemconfig(item,**{'tags':'schild','foreground':'#7c0909','bitmap':'@guidesigner/images/woman'})

coords = (189.42372881355936,96.62711864406776)
item = canvas.create_text(*coords)
canvas.itemconfig(item,**{'tags':'schild','text':'Woman','font':'TkDefaultFont 16 bold','fill':'#7c0909'})

coords = (386.5,43.0,406.5,55.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,63.0,406.5,75.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,83.0,406.5,95.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,103.0,406.5,115.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,123.0,406.5,135.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,143.0,406.5,155.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,163.0,406.5,175.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (386.5,183.0,406.5,195.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,43.0,526.5,55.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,63.0,526.5,75.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,83.0,526.5,95.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,103.0,526.5,115.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,123.0,526.5,135.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,143.0,526.5,155.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,163.0,526.5,175.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (506.5,183.0,526.5,195.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'gray','tags':'pin'})

coords = (406.5,23.0,506.5,214.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'fill':'#494444','tags':'pin'})

coords = (454.5,78.0)
item = canvas.create_text(*coords)
canvas.itemconfig(item,**{'tags':'pin','text':'SN XXX','font':'TkDefaultFont 20 bold','fill':'white'})


goOut()
grid(**{'row': '0'})
