import tkinter as tk



# GUI =============================================================
root = tk.Tk()

canvas = tk.Canvas(root)

coords = (295.0,197.0,335.0,237.0)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'orange','tags':'planet'})

coords = (40.0,135.0,72.0,167.0)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'orange','tags':'planet'})

coords = (152.0,211.0,177.60000000000002,236.6)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'orange','tags':'planet'})

coords = (90.60000000000002,37.39999999999999,111.08000000000001,57.88000000000001)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'orange','tags':'planet'})

coords = (304.08000000000004,60.91999999999999,320.464,77.304)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'orange','tags':'planet'})

coords = (232.46400000000003,24.535999999999973,245.57120000000003,37.64319999999998)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'orange','tags':'planet'})

'''
coords = (225.0,129.0,235.0,149.0)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'fill':'red','tags':'shuttle'})
'''

raumschiff_img = tk.PhotoImage(file="guidesigner/images/butterfly.gif")
coords = (225.0,129.0)
item = canvas.create_image(*coords)
canvas.itemconfig(item,**{'image':raumschiff_img,'tags':'shuttle','anchor':'nw'})


canvas.pack()

# CODE MOVE BY MOUSE ( Kann man rauswerfen, da es fertig ist) ========================================================

canvas_item = [None]
paint_enabled=[False]
bbox_coord = [0,0,0,0]

def get_coord():
    xw = canvas.winfo_pointerx()-canvas.winfo_rootx()
    yw = canvas.winfo_pointery()-canvas.winfo_rooty()
    return canvas.canvasx(xw), canvas.canvasy(yw)
    
def mouse_move():
    if paint_enabled[0]:
        step = 10
        xc,yc = get_coord()
        diffx = xc - bbox_coord[0]
        diffy = yc - bbox_coord[1]
        bbox_coord[0] = xc
        bbox_coord[1] = yc
        canvas.move(canvas_item[0],diffx,diffy)
        canvas.after(step,mouse_move)

def stop_move(event = None):
    paint_enabled[0] = False

def do_move(event=None):
    xc,yc = get_coord()
    bbox_coord[0] = xc
    bbox_coord[1] = yc
    canvas_item[0] = canvas.find_closest(xc,yc)
    paint_enabled[0] = True
    mouse_move()

canvas.bind('<Button-1>',do_move)
canvas.bind('<ButtonRelease-1>',stop_move)

# SHUTTLE STEUERUNG ===========================================================

move_delta = [0,0]

def move_shuttle():
    canvas.move('shuttle',*move_delta)
    coords = canvas.coords('shuttle')
    center_x = coords[0] + raumschiff_img.width()/2
    center_y = coords[1] + raumschiff_img.height()/2
    if center_x < 0: move_delta[0] *= -1
    if center_y < 0: move_delta[1] *= -1
    if center_x > int(canvas['width']): move_delta[0] *= -1
    if center_y > int(canvas['height']): move_delta[1] *= -1
    canvas.after(10,move_shuttle)

move_shuttle()

def change_shuttle_move(event):
    
    pressed = event.char
    if pressed == 'w': move_delta[1] = -3
    elif pressed == 's': move_delta[1] = 3
    elif pressed == 'a': move_delta[0] = -3
    elif pressed == 'd': move_delta[0] = 3
    
root.event_add('<<move>>','<w>','<a>','<s>','<d>')
root.bind('<<move>>',change_shuttle_move)

# Kollisionsabfrage ============================================================

def check_collision():
    coords = canvas.coords('shuttle')
    coords.extend((coords[0]+raumschiff_img.width(),coords[1]+raumschiff_img.height()))
    overlapp_list = canvas.find_overlapping(*coords)
    for item in overlapp_list:
        if 'planet' in canvas.gettags(item):
            print("Hallo Kollision!!!")
            break
    canvas.after(100,check_collision)

check_collision()

# START =================================================================================

root.mainloop()
