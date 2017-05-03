def Access(canvas):

    coordinates = [None]
    precision = 30

    def move_to(x,y):
        coordinates[0] = [x,y,x,y]
        
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

            paired = False
            for T in range(1,precision-1):
                t = T/precision
                Bx = (1-t)*(1-t)*(1-t)*px0 + 3*t*(1-t)*(1-t)*px1+3*t*t*(1-t)*px2+t*t*t*px3
                By = (1-t)*(1-t)*(1-t)*py0 + 3*t*(1-t)*(1-t)*py1+3*t*t*(1-t)*py2+t*t*t*py3

                if paired:

                    pre_pre_Bx = coordinates[0][-4]
                    pre_pre_By = coordinates[0][-3]
                    pre_Bx = coordinates[0][-2]
                    pre_By = coordinates[0][-1]
                    coordinates[0][-2] = int(2*pre_Bx-0.5*pre_pre_Bx-0.5*Bx +0.5)
                    coordinates[0][-1] = int(2*pre_By-0.5*pre_pre_By-0.5*By +0.5)

                    coordinates[0].extend((Bx,By,Bx,By))

                else:
                    coordinates[0].extend((Bx,By))
                paired = not paired


            coordinates[0].extend((px3,py3,px3,py3))



    def line_to(*args):

        for index in range(0,len(args),2):
            coordinates[0].append(args[index])
            coordinates[0].append(args[index+1])
            coordinates[0].append(args[index])
            coordinates[0].append(args[index+1])


    smooth = 1
    splinesteps = 12

    move_to(8988,4286)
    line_to(9770,3752,8655,3425)
    becier(7723,1788,5822,2642,5186,4199,4420,6075,2224,6760,2224,6760,3787,8619,5196,8954,6136,8880,7077,8806,9615,8066,9087,4766,9059,4595,9026,4435,8988,4286)
    canvas.create_polygon(*coordinates[0],fill='#2ba9e1',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    move_to(8655,3426)
    becier(8788,3660,8901,3945,8988,4286)
    line_to(9770,3753,8655,3426)
    canvas.create_polygon(*coordinates[0],fill='#2b3277',tags='new_tag',smooth=smooth,splinesteps=splinesteps)


    move_to(7412,5497)
    becier(7412,5497,4803,4959,4503,6411,4204,7863,6613,8705,7412,5497)
    canvas.create_polygon(*coordinates[0],fill='#2b3277',tags='new_tag',smooth=smooth,splinesteps=splinesteps)


    move_to(7915,3385)
    becier(7932,3541,7852,3678,7735,3691,7618,3705,7509,3589,7491,3433,7473,3278,7554,3140,7671,3127,7788,3114,7897,3229,7915,3385)
    canvas.create_polygon(*coordinates[0],fill='#2b3277',tags='new_tag',smooth=smooth,splinesteps=splinesteps)

    return 'bird'

def main():

    import tkinter as tk
    root = tk.Tk()
    canvas = tk.Canvas(root,width=1000,height=800)
    canvas.pack()
    Access(canvas)
    scale = 0.1
    canvas.scale('new_tag',0,0,scale,scale)
    canvas.move('new_tag',-100,-100)

    root.mainloop()
 
if __name__ == '__main__':
    main()

