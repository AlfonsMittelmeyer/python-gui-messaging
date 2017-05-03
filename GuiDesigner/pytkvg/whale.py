def Access(canvas,smooth=1):

    class Curve(object):
        def __init__(self, x,y, precision=30):
            self.coordinates = [x,y]
            self.precision = precision
     
        def __iter__(self):
            return iter(self.coordinates)
     
        def line_to(*args):
            x0 = self.coordinates[-2]
            y0 = self.coordinates[-1]
            self.coordinates.extend((x0,y0))
            
            for index in range(0,len(args),2):
                self.coordinates.append(args[index])
                self.coordinates.append(args[index+1])
                self.coordinates.append(args[index])
                self.coordinates.append(args[index+1])

        def becier(self, *coords):
            coords = iter(coords)
            px0, py0 = self.coordinates[-2:]
            for px1, py1, px2, py2, px3, py3 in zip(*[coords]*6):
                # B(t) = (1-t)^3 * P0  + 3t * (1-t)^2 * P1 + 3 t^2 * (1-t) * P2 + t^3 * P3
                for T in range(1,self.precision-1):
                    t = T/self.precision
                    Bx = (1-t)*(1-t)*(1-t)*px0 + 3*t*(1-t)*(1-t)*px1+3*t*t*(1-t)*px2+t*t*t*px3
                    By = (1-t)*(1-t)*(1-t)*py0 + 3*t*(1-t)*(1-t)*py1+3*t*t*(1-t)*py2+t*t*t*py3
                    self.coordinates.extend((Bx, By))
                px0, py0 = px3, py3
                self.coordinates.extend((px0,py0))

    splinesteps = 12

    c = Curve(6993,5862)
    c.becier(4946,5697,4904,8018,3685,8018,2639,8018,2755,6895,2810,6574,2931,6565,3092,6521,3290,6397,3819,6065,3498,5420,3498,5420,3488,5646,3188,5666,3188,5666,2628,5693,2564,6131,2546,6365,2472,6191,2296,5873,2004,5900,1609,5936,1691,6093,1268,5875,1268,5875,1202,6505,1857,6665,2027,6707,2162,6705,2266,6683,2227,10048,5458,10817,7447,9970,9739,8994,9039,6026,6993,5862)
    canvas.create_polygon(*c,tags="new_tag", fill='#64c3a3',smooth=smooth,splinesteps=splinesteps)

    c = Curve(6969,4281)
    c.becier(7050,3944,6639,1184,8227,1598,9030,1807,8820,3057,8000,3086,7230,3112,7168,3950,7046,4274,7046,4274,7030,4327,7000,4324,7000,4324,6960,4321,6969,4281)
    canvas.create_polygon(*c,tags="new_tag", fill='#64c3a3',smooth=smooth,splinesteps=splinesteps)
    
    c = Curve(6910,7636)
    c.becier(7003,7765,7143,7800,7223,7714,7302,7629,7290,7455,7197,7327,7104,7198,6964,7163,6885,7249,6806,7334,6817,7508,6910,7636)
    canvas.create_polygon(*c,tags="new_tag", fill='#085877',smooth=smooth,splinesteps=splinesteps)

    c = Curve(8373,9170)
    c.becier(8373,9170,7274,9561,6985,8468,6985,8468,6965,8432,6991,8413,7023,8389,7071,8417,7071,8417,7324,9482,8348,9080,8348,9080,8348,9080,8397,9091,8405,9110,8413,9129,8404,9166,8373,9170)
    canvas.create_polygon(*c,tags="new_tag", fill='#085877',smooth=smooth,splinesteps=splinesteps)

    c = Curve(7032,5479)
    c.becier(7097,5345,7551,4413,8384,4628,10223,5103,9898,2685,8448,3059,7312,3351,6970,5400,6942,5584,6942,5584,6939,5609,6949,5614,6988,5635,7032,5479,7032,5479)
    canvas.create_polygon(*c,tags="new_tag", fill='#085877',smooth=smooth,splinesteps=splinesteps)

    c = Curve(6892,5586)
    c.becier(6892,5586,7148,44,4249,1229,4249,1229,2910,1850,3749,3232,4078,3774,4834,3773,5395,3673,5395,3673,5875,3568,6197,3953,6520,4338,6763,5492,6807,5578,6856,5674,6892,5586,6892,5586)
    canvas.create_polygon(*c,tags="new_tag", fill='#085877',smooth=smooth,splinesteps=splinesteps)
    
    return 'whale'

def main():

    import tkinter as tk
    root = tk.Tk()
    canvas = tk.Canvas(root,width=600,height=400)
    canvas.pack()
    Access(canvas)
    scale = 0.04
    canvas.scale('new_tag',0,0,scale,scale)
    canvas.move('new_tag',0,-30)
    root.mainloop()
 
if __name__ == '__main__':
    main()
