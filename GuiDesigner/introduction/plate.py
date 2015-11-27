canvas=container()

coords = (14.0,13.0,242.0,131.0)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'#ffffdc','width':'6.0','outlinestipple':'gray75','tags':'plate','outline':'#7e030c'})

coords = (166.0,72.0)
item = canvas.create_bitmap(*coords)
canvas.itemconfig(item,**{'tags':'plate','foreground':'#7e030c','bitmap':'@guidesigner/images/woman'})

coords = (78.0,71.0)
item = canvas.create_text(*coords)
canvas.itemconfig(item,**{'tags':'plate','text':'Woman','font':'TkDefaultFont 18 bold','fill':'#7e030c'})
