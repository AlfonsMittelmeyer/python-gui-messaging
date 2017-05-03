def Access(canvas):

    coordinates = [None]

    def move_to(x,y):
        coordinates[0] = [x,y]
        
    def becier(*args):
        for index in range(0,len(args),6):

            px0 = coordinates[0][-2]
            py0 = coordinates[0][-1]
            px1 = args[index]
            py1 = args[index+1]
            px2 = args[index+2]
            py2 = args[index+3]
            px3 = args[index+4]
            py3 = args[index+5]

            for T in range(1,29):
                t = T/30
                Bx = (1-t)*(1-t)*(1-t)*px0 + 3*t*(1-t)*(1-t)*px1+3*t*t*(1-t)*px2+t*t*t*px3
                By = (1-t)*(1-t)*(1-t)*py0 + 3*t*(1-t)*(1-t)*py1+3*t*t*(1-t)*py2+t*t*t*py3
                coordinates[0].append(Bx)
                coordinates[0].append(By)
            coordinates[0].append(args[index+4])
            coordinates[0].append(args[index+5])


    def line_to(*args):
        for index in range(0,len(args),2):
            coordinates[0].append(args[index])
            coordinates[0].append(args[index+1])
            coordinates[0].append(args[index])
            coordinates[0].append(args[index+1])

    smooth = 1
    splinesteps = 12

    move_to(7408,4804)
    becier(6718,3138,6325,3043,6245,3043,5607,709,4471,933,4471,933,3701,956,3238,1863,2960,2981,2904,2975,2507,3005,1789,4741,1077,6460,1535,7342,1618,7479,1618,7479,1634,7509,1647,7508,1660,7507,1681,7468,1681,7468,1724,7415,2237,6768,2581,5790,2535,6610,2545,7201,2545,7202,2545,7202,2578,7587,3877,7696,3629,7850,3282,7938,3282,7938)
    line_to(3443,8231,3725,7962,3392,8315,3593,8509,3890,8143,3742,8380,4005,8486)
    becier(4154,8321,4348,7985,4456,7723,4512,7724,4569,7724,4628,7724,4759,7724,4882,7722,4997,7718,5073,7968,5194,8269,5334,8425)
    line_to(5628,8332,5569,8097,5788,8458,6067,8269,5734,7916,6016,8185,6177,7892)
    becier(6177,7892,5861,7811,5616,7670,6667,7536,6667,7196,6667,7196,6668,6740,6659,6318,6641,5926,6984,6863,7473,7479,7515,7531,7515,7531,7536,7570,7549,7571,7562,7571,7578,7542,7578,7542,7662,7405,8119,6523,7408,4804)
    canvas.create_polygon(*coordinates[0],fill='#010101',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    move_to(5039,1445)
    becier(4724,1426,4626,1703,4601,1737,4576,1770,4547,1720,4547,1720,4547,1720,4194,1319,3786,1615,3174,2060,2388,6997,3192,7300,3926,7577,4681,7535,4681,7535,6225,7535,6292,7199,6292,7199,6435,1477,5039,1445,5039,1445)
    canvas.create_polygon(*coordinates[0],fill='#ffffff',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    move_to(4872,2234)
    becier(4949,2230,5014,2319,5019,2432,5024,2544,4966,2638,4890,2642,4813,2645,4747,2556,4743,2443,4738,2331,4796,2237,4872,2234)
    canvas.create_polygon(*coordinates[0],fill='#010101',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    move_to(4071,2482)
    becier(4037,2372,4073,2263,4149,2240,4226,2217,4315,2288,4349,2399,4382,2509,4347,2618,4270,2641,4193,2664,4104,2593,4071,2482)
    canvas.create_polygon(*coordinates[0],fill='#010101',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    move_to(4965,3769)
    becier(4965,3769,4443,3563,4235,2961,4235,2961,4658,2787,5044,2921,5044,2921,5186,3294,4965,3769)
    canvas.create_polygon(*coordinates[0],fill='#010101',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    return 'pingu'
    
def main():

    import tkinter as tk
    root = tk.Tk()
    canvas = tk.Canvas(root,width=400,height=380)
    canvas.pack()
    Access(canvas)
    scale = 0.04
    canvas.scale('new_tag',0,0,scale,scale)
    root.mainloop()
 
if __name__ == '__main__':
    main()

