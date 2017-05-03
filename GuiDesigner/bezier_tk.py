Canvas('canvas',**{'height': '400', 'width': '500', 'cursor': 'crosshair'})
goIn()


canvas=container()

coords = (24.0,286.0,84.0,174.0,346.0,136.0,388.0,26.0)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'fill':'yellow','width':'7.0','smooth':'true'})

coords = (24.0,286.0,84.0,174.0,346.0,136.0,388.0,26.0)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'width':'2.0'})

coords = (20.0,288.0,31.239925925925945,269.6362962962963,42.93274074074074,253.25037037037043,55.03800000000001,238.70000000000002,67.51525925925927,225.84296296296299,80.32407407407409,214.53703703703707,93.42400000000004,204.64000000000007,106.77459259259257,196.0096296296296,120.33540740740742,188.50370370370376,134.06599999999997,181.97999999999996,147.92592592592595,176.29629629629633,161.8747407407407,171.31037037037035,175.87200000000004,166.88000000000002,189.8772592592593,162.86296296296294,203.85007407407406,159.11703703703705,217.75,155.5,231.5365925925926,151.86962962962966,245.1694074074074,148.08370370370372,258.60799999999995,143.99999999999997,271.8119259259259,139.47629629629628,284.74074074074076,134.37037037037038,297.3539999999999,128.54,309.6112592592592,121.84296296296296,321.4720740740741,114.13703703703702,332.8960000000001,105.28,343.8425925925926,95.12962962962962,354.2714074074074,83.5437037037037,364.14200000000005,70.38,373.4139259259259,55.49629629629629,390.0,20.0)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'fill':'red','width':'2.0'})

coords = (20.0,288.0,130.0,94.0,314.0,218.0,390.0,20.0)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'fill':'blue','width':'2.0','smooth':'true'})

coords = (22.0,288.0,132.0,94.0,316.0,218.0,392.0,20.0)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'fill':'#005e00','width':'2.0'})


### CODE ===================================================

def main():

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

            # B(t) = (1-t)^3 * P0  + 3t * (1-t)^2 * P1 + 3 t^2 * (1-t) * P2 + t^3 * P3    t€(0,1)
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


    canvas = container()

    move_to(18.0,146)
    becier(73.0,49.0,165.0,111.0,203.0,12.0)
    #line_to(18.0,146)
    item = canvas.create_line(*coordinates[0],fill='red',width=2)
    canvas.tag_lower(item)
    
main()

### ========================================================

goOut()


widget('canvas').pack()
