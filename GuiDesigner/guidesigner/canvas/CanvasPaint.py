Toplevel('CPaint',**{'title': 'Canvas Drawing', 'grid_cols': '(3, 10, 0, 0)', 'grid_multi_rows': '[5, (1, 0, 0, 0)]', 'grid_rows': '(5, 10, 0, 0)'})
goIn()

LabelFrame('Coordinates',**{'text': 'Coordinates', 'grid_cols': '(2, 10, 0, 0)', 'grid_rows': '(3, 5, 0, 0)'})
goIn()

Frame('frame')
goIn()

Canvas('canvas',**{'height': '0', 'width': '400'})
goIn()

Frame('frame')
goIn()

### CODE ===================================================

frame = container()
canvas = frame.master

canvas.create_window(0,0,window=frame,anchor=NW) 

max_height = [0]

def frame_configure(me,canvas,max_height=max_height):
    canvas.config(scrollregion="0 0 %s %s" % (me.winfo_reqwidth(), me.winfo_reqheight()))
    if me.winfo_reqheight() > max_height[0]: canvas.config(height=me.winfo_reqheight())

frame.do_event("<Configure>",frame_configure,canvas,True)

def do_set_coordinates(me):
    if isinstance(this(),CanvasItemWidget):
        item = this().item_id
        coords = container().coords(item)
        value = int(me.get())
        coords[me.mydata] = value
        container().coords(item,*coords)
        if len(coords) < 5 or me.mydata < 2: send('UPDATE_POS_NOCOORD')

def do_update_coordinates(selected,wi_coordframe = widget('/','Coordinates'),cont=container(),do_set_coordinates = do_set_coordinates):

    if False:
    #if isinstance(selected,CanvasItemWidget):
        #wi_coordframe.unlayout()
        deleteAllWidgets(cont)
        item = selected.item_id
        canvas = selected.master
        coords = canvas.coords(item)
        selection_before = Selection()
        setSelection(Create_Selection(cont,cont))

        count = int(len(coords)/2)
        for index in range(count):

            LabelFrame(NONAME,**{'text': str(index)})
            goIn()

            Spinbox('x',**{'from': -9999.0, 'width': 5, 'to': 9999.0})
            this().mydata = index*2
            do_command(do_set_coordinates,wishWidget=True)
            do_event('<Return>',do_set_coordinates,wishWidget=True)
            Spinbox('y',**{'from': -9999.0, 'width': 5, 'to': 9999.0})
            this().mydata = index*2 + 1
            do_command(do_set_coordinates,wishWidget=True)
            do_event('<Return>',do_set_coordinates,wishWidget=True)

            widget('x').delete(0,END)
            widget('y').delete(0,END)

            x=int(coords[2*index])
            y=int(coords[2*index+1])
            
            widget('x').insert(0,str(x))
            widget('y').insert(0,str(y))

            widget('x').pack(**{'ipady': '2'})
            widget('y').pack(**{'ipady': '2'})
            
            goOut()
            pack(**{'side': 'left'})
    
        wi_coordframe.grid()
        setSelection(selection_before)
    else:
        wi_coordframe.unlayout()

#def do_update_coordinates_this(do_update_coordinates = do_update_coordinates): do_update_coordinates(this())


#do_receive('SELECTION_CHANGED',do_update_coordinates_this)
do_receive('CANVAS_COORD_UPDATE',do_update_coordinates,wishMessage=True)

# Coordinates
### ========================================================

goOut()


goOut()

Scrollbar('scrollbar',**{'orient': 'horizontal'})

widget('canvas').pack(**{'expand': '1', 'fill': 'both'})
widget('scrollbar').pack(**{'side': 'bottom', 'fill': 'x'})

### CODE ===================================================

widget("canvas").config(xscrollcommand=widget("scrollbar").set)
widget("scrollbar").config(command=widget("canvas").xview)

### ========================================================

goOut()
grid(**{'row': 0, 'sticky': 'nesw', 'rowspan': 2, 'column': 1})
Label('x',**{'text': 'x'}).grid(**{'row': 0, 'sticky': 's'})
Label('y',**{'text': 'y'}).grid(**{'row': 1, 'sticky': 'n'})

goOut()
grid(**{'row': 1, 'sticky': 'nesw', 'column': 1})
Frame('Handling',**{'height': 350, 'width': 420, 'grid_rows': '(3, 25, 0, 0)', 'grid_cols': '(3, 75, 0, 0)'})
goIn()

Frame('Changing')
goIn()

Button('copy',**{'text': 'copy', 'bd': '2'})
Button('delete',**{'text': 'delete', 'bd': '2'})
Button('lower',**{'text': 'lower', 'bd': '2'})
Button('move',**{'text': 'move', 'bd': '2'})
Button('raise',**{'text': 'raise', 'bd': '2'})
Button('select',**{'text': 'select', 'bd': '2'})

widget('select').pack(**{'fill': 'x'})
widget('copy').pack(**{'fill': 'x'})
widget('move').pack(**{'fill': 'x'})
widget('lower').pack(**{'fill': 'x'})
widget('raise').pack(**{'fill': 'x'})
widget('delete').pack(**{'fill': 'x'})

goOut()
place(**{'x': '285', 'y': '130'})
LabelFrame('Drawing',**{'padx': '15', 'pady': '12', 'text': 'Drawing'})
goIn()

Canvas('arc',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (-16.0,5.0,32.0,51.0)
item = canvas.create_arc(*coords)
canvas.itemconfig(item,**{'start':'20.0','width':'2.0','extent':'60.0'})


goOut()
grid(**{'row': 2, 'column': 1})
Canvas('bitmap',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (10.0,11.0)
item = canvas.create_bitmap(*coords)
canvas.itemconfig(item,**{'anchor':'nw','bitmap':'@guidesigner/images/starMask'})


goOut()
grid(**{'row': 3, 'column': 1})
Canvas('freehand',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (18.0,16.0,16.8,11.8,14.4,9.4,11.4,9.4,7.2,12.4,7.2,19.6,16.2,26.2,18.6,26.8)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'tags':'new','width':'2.0'})

coords = (17.4,14.8,19.2,13.0,23.4,11.2,26.4,11.2,27.0,13.0,28.2,13.6,28.2,19.0,27.0,20.8,21.0,23.2,18.0,25.6)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'tags':'new','width':'2.0'})


goOut()
grid(**{'row': 0, 'column': 2})
Canvas('freehand_polygon',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (17.0,14.0,17.4,13.8,17.4,13.0,17.0,12.8,15.8,10.6,14.8,10.2,12.4,8.2,10.6,8.2,9.8,8.4,8.4,9.6,7.0,12.2,6.4,15.0,7.2,19.8,7.8,20.4,10.0,21.2,15.8,22.8,17.6,24.8,18.4,28.0,19.6,27.0,19.6,26.6,23.2,21.4,27.2,16.6,27.8,15.0,28.0,13.6,27.8,10.2,27.0,9.4,25.6,9.0,20.2,9.0,17.8,11.6,17.2,12.8)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'fill':'red','width':'2.0','outline':'black'})


goOut()
grid(**{'row': 1, 'column': 2})
Canvas('image',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (4.0,4.0)
item = canvas.create_image(*coords)
canvas.itemconfig(item,**{'anchor':'nw','photoimage':'guidesigner/images/butterfly.gif'})


goOut()
grid(**{'row': 3})
Canvas('import',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (27.464,13.657999999999998,29.81,12.056000000000001,26.465,11.075,26.175958222222217,10.608611333333332,25.86902577777778,10.190850666666666,25.545692000000003,9.820526,25.207446222222224,9.496445333333334,24.85577777777778,9.217416666666669,24.492176000000008,8.982248000000002,24.118130222222216,8.789747333333333,23.735129777777782,8.63872266666667,23.344663999999995,8.527981999999998,22.948222222222224,8.456333333333335,22.54729377777777,8.422584666666664,22.143368000000002,8.425543999999999,21.737934222222222,8.464019333333333,21.332481777777776,8.536818666666665,20.9285,8.64275,20.52747822222222,8.780621333333333,20.130905777777777,8.949240666666666,19.740271999999997,9.147415999999998,19.357066222222223,9.373955333333333,18.982777777777784,9.627666666666666,18.618896,9.907357999999999,18.266910222222222,10.211837333333332,17.928309777777777,10.539912666666668,17.604584000000003,10.890392000000002,17.29722222222222,11.262083333333333,17.00771377777778,11.653794666666666,16.737548000000004,12.064334000000002,16.48821422222222,12.492509333333334,16.058,13.397,15.814302888888887,13.947946222222221,15.54442311111111,14.475409777777779,15.250778,14.979728000000003,14.93578488888889,15.461238222222224,14.601861111111115,15.920277777777779,14.251424000000004,16.357184000000004,13.886890888888889,16.77229422222222,13.510679111111115,17.165945777777782,13.125205999999997,17.538475999999996,12.73288888888889,17.890222222222224,12.336145111111108,18.221521777777774,11.937392000000003,18.532712000000004,11.539046888888887,18.824130222222223,11.143527111111108,19.096113777777777,10.753250000000001,19.348999999999997,10.370632888888888,19.583126222222223,9.99809311111111,19.798829777777776,9.638048,19.996448,9.292914888888888,20.17631822222222,8.965111111111112,20.33877777777778,8.657053999999999,20.484164,8.37116088888889,20.61281422222222,8.109849111111112,20.72506577777778,7.875536,20.821255999999998,7.67063888888889,20.901722222222226,7.497575111111111,20.96680177777778,7.3587620000000005,21.016832,7.256616888888889,21.052150222222224,7.172000000000001,21.08,7.6393249999999995,21.62258388888889,8.103359999999999,22.13543111111111,8.563895,22.619285000000005,9.02072,23.074888888888893,9.473625000000002,23.502986111111113,9.922400000000003,23.904320000000006,10.366834999999998,24.279633888888885,10.806720000000002,24.62967111111112,11.241844999999998,24.955174999999993,11.672000000000004,25.25688888888889,12.096974999999997,25.535556111111102,12.516560000000002,25.79192,12.930545000000002,26.026723888888892,13.33872,26.24071111111111,13.740875,26.434625,14.1368,26.60920888888889,14.526285,26.765206111111112,14.90912,26.90336,15.285094999999998,27.024413888888883,15.654000000000003,27.12911111111111,16.015625,27.218194999999998,16.36976,27.292408888888886,16.716195,27.35249611111112,17.054720000000003,27.399200000000004,17.385125000000002,27.433263888888888,17.7072,27.45543111111111,18.020735000000002,27.466445,18.32552,27.46704888888889,18.908,27.439999999999998,19.205751888888887,27.41092955555555,19.532335111111117,27.367276444444446,19.884641000000006,27.307778,20.25956088888889,27.231171555555562,20.65398611111111,27.13619444444445,21.064808000000006,27.021584000000008,21.488917888888885,26.886077555555552,21.923207111111118,26.728412444444444,22.364566999999997,26.547325999999998,22.809888888888892,26.341555555555562,23.256064111111108,26.10983844444444,23.699984,25.850912,24.13853988888889,25.563513555555552,24.568623111111112,25.24638044444444,24.987125000000002,24.89825,25.390936888888888,24.517859555555557,25.776950111111113,24.103946444444443,26.142055999999997,23.655247999999997,26.483145888888885,23.170501555555557,26.79711111111111,22.648444444444443,27.080843,22.087814,27.33123288888889,21.48734755555555,27.545172111111114,20.845782444444442,27.719552000000007,20.161856,27.85126388888889,19.434305555555554,27.937199111111113,18.661868444444444,27.974249000000004,17.843282000000002,27.959304888888887,16.97728355555555,27.761000000000003,15.097999999999999,27.75255,15.046809999999999,27.744,14.995840000000001,27.73535,14.945090000000002,27.72660000000001,14.894559999999998,27.717750000000002,14.844249999999999,27.70880000000001,14.794160000000002,27.699749999999995,14.744289999999996,27.690600000000003,14.694640000000007,27.681349999999995,14.645209999999995,27.672000000000004,14.596000000000004,27.66255,14.547009999999997,27.653,14.49824,27.643350000000005,14.449689999999999,27.633599999999998,14.401359999999997,27.62375,14.35325,27.613800000000005,14.30536,27.603750000000005,14.25769,27.5936,14.210239999999999,27.583349999999996,14.163009999999996,27.573000000000004,14.116,27.562549999999995,14.069209999999998,27.552,14.022640000000003,27.54135,13.976289999999999,27.530600000000007,13.930160000000004,27.519750000000002,13.884250000000002,27.508800000000004,13.838559999999998,27.497749999999996,13.793090000000001,27.4866,13.74784,27.464,13.657999999999998)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'tags':'bird','fill':'#2ba9e1'})

coords = (26.465,11.078,26.504699333333335,11.148710555555555,26.54399466666667,11.220444444444446,26.582882,11.293205000000004,26.621357333333346,11.366995555555556,26.659416666666672,11.441819444444445,26.697056000000018,11.517680000000002,26.734271333333325,11.594580555555554,26.771058666666676,11.672524444444448,26.80741399999999,11.751515,26.84333333333334,11.831555555555557,26.878812666666665,11.912649444444442,26.91384800000001,11.994800000000001,26.94843533333334,12.078010555555554,26.982570666666664,12.162284444444445,27.01625,12.247625,27.049469333333334,12.334035555555555,27.08222466666667,12.421519444444444,27.114511999999998,12.510079999999999,27.146327333333332,12.599720555555553,27.17766666666667,12.690444444444445,27.208526000000003,12.782255,27.23890133333333,12.875155555555555,27.268788666666666,12.969149444444444,27.298184,13.064240000000002,27.327083333333334,13.160430555555553,27.355482666666667,13.257724444444445,27.383378,13.356125,27.410765333333337,13.455635555555554,27.464,13.657999999999998,29.81,12.059,26.465,11.078)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'tags':'bird','fill':'#2b3277'})

coords = (22.736,17.291,22.710456444444443,17.28590088888889,22.63601155555555,17.27172711111111,22.515944000000005,17.250164,22.353532444444447,17.22289688888889,22.15205555555556,17.191611111111115,21.914792000000006,17.157992000000007,21.64502044444444,17.123724888888887,21.34601955555556,17.090495111111114,21.021067999999996,17.059987999999997,20.67344444444445,17.033888888888896,20.30642755555555,17.013883111111106,19.923296,17.001656,19.527328444444443,16.99889288888889,19.12180355555555,17.00727911111111,18.71,17.0285,18.295196444444443,17.06424088888889,17.880671555555555,17.11618711111111,17.469704,17.186023999999996,17.065572444444445,17.27543688888889,16.671555555555557,17.386111111111113,16.290932,17.519731999999998,15.926980444444442,17.677984888888886,15.582979555555557,17.862555111111114,15.262208000000001,18.075128,14.967944444444445,18.31738888888889,14.703467555555557,18.591023111111113,14.472055999999998,18.897716000000003,14.276988444444445,19.23915288888889,14.009,20.033,13.945900222222221,20.462117777777777,13.93408177777778,20.876742222222223,13.970666000000007,21.274580000000004,14.052774222222226,21.653337777777782,14.177527777777781,22.010722222222228,14.342048000000004,22.344440000000006,14.543456222222218,22.652197777777776,14.778873777777783,22.931702222222228,15.045421999999995,23.180659999999996,15.340222222222222,23.396777777777782,15.660395777777772,23.577762222222216,16.003064000000002,23.721320000000002,16.365348222222224,23.82515777777778,16.744369777777777,23.886982222222215,17.13725,23.9045,17.54111022222222,23.875417777777777,17.95307177777778,23.797442222222223,18.370256,23.668279999999996,18.789784222222224,23.48563777777778,19.208777777777776,23.247222222222227,19.624358,22.95074,20.033646222222217,22.593897777777777,20.433763777777777,22.17440222222222,20.821832000000004,21.689960000000003,21.194972222222226,21.138277777777777,21.550305777777776,20.517062222222222,21.884954000000004,19.824019999999997,22.196038222222224,19.05685777777778,22.736,17.291)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'tags':'bird','fill':'#2b3277'})

coords = (24.245,10.955,24.249136666666665,11.001598333333334,24.251373333333337,11.047746666666669,24.25175,11.093375000000002,24.250306666666674,11.138413333333336,24.24708333333334,11.182791666666668,24.24212000000001,11.22644,24.235456666666664,11.269288333333332,24.22713333333334,11.31126666666667,24.217189999999995,11.352304999999998,24.205666666666673,11.392333333333335,24.192603333333327,11.431281666666663,24.17804,11.469080000000002,24.162016666666666,11.505658333333333,24.144573333333334,11.540946666666667,24.12575,11.574875,24.10558666666667,11.607373333333332,24.084123333333334,11.638371666666668,24.0614,11.6678,24.037456666666667,11.695588333333333,24.012333333333334,11.721666666666668,23.986069999999998,11.745964999999998,23.958706666666668,11.768413333333331,23.930283333333332,11.788941666666668,23.900840000000002,11.807480000000002,23.870416666666667,11.823958333333334,23.839053333333336,11.838306666666668,23.806790000000003,11.850455,23.773666666666667,11.860333333333333,23.705,11.873,23.669989222222224,11.87591,23.63519377777778,11.876280000000001,23.600669000000007,11.874170000000003,23.566470222222225,11.86964,23.53265277777778,11.862750000000002,23.499272000000005,11.853560000000002,23.466383222222216,11.842129999999997,23.434041777777786,11.828520000000005,23.402302999999993,11.812789999999996,23.371222222222226,11.795000000000002,23.340854777777775,11.775209999999998,23.311256000000004,11.75348,23.282481222222227,11.729870000000002,23.25458577777778,11.70444,23.227625,11.67725,23.201654222222224,11.64836,23.17672877777778,11.617830000000001,23.152903999999996,11.585719999999998,23.130235222222222,11.55209,23.10877777777778,11.517000000000003,23.088587,11.480509999999999,23.06971822222222,11.44268,23.052226777777776,11.403570000000002,23.036168,11.36324,23.021597222222223,11.321750000000002,23.00856977777778,11.27916,22.997141,11.23553,22.98736622222222,11.190920000000002,22.973,11.099,22.968583000000002,11.052681999999999,22.966103999999998,11.006776000000002,22.965521000000003,10.961354000000002,22.96679200000001,10.916488000000001,22.969875000000002,10.872250000000003,22.974728000000006,10.828712000000003,22.981309,10.785946,22.989576000000003,10.744024000000001,22.999487,10.703017999999997,23.011000000000006,10.663000000000002,23.024072999999998,10.624041999999998,23.038664,10.586216000000002,23.054731,10.549594,23.072232,10.514247999999998,23.091125,10.48025,23.111368,10.447672,23.132919,10.416586,23.155735999999994,10.387063999999999,23.179776999999998,10.359178,23.205000000000002,10.333000000000002,23.231362999999998,10.308601999999999,23.258824,10.286055999999999,23.287341,10.265433999999999,23.316872,10.246808,23.347375,10.230250000000002,23.378808000000003,10.215832,23.411129,10.203626,23.444296,10.193703999999999,23.513,10.181000000000001,23.548010777777773,10.178370333333332,23.582806222222224,10.178242666666666,23.617331000000004,10.180559,23.65152977777778,10.185261333333333,23.685347222222223,10.192291666666668,23.718728000000006,10.201592000000002,23.751616777777773,10.21310433333333,23.783958222222225,10.226770666666669,23.815696999999993,10.242532999999998,23.84677777777778,10.260333333333335,23.877145222222214,10.280113666666663,23.906744,10.301815999999999,23.935518777777773,10.325382333333334,23.963414222222223,10.350754666666667,23.990375,10.377875,24.01634577777778,10.406685333333334,24.04127122222222,10.437127666666667,24.065095999999997,10.469143999999998,24.087764777777775,10.502676333333332,24.109222222222225,10.537666666666667,24.129412999999996,10.574056999999998,24.148281777777772,10.61178933333333,24.165773222222224,10.650805666666667,24.181832,10.691047999999999,24.196402777777777,10.732458333333332,24.209430222222224,10.774978666666666,24.220859000000004,10.818551000000001,24.23063377777778,10.863117333333332,24.245,10.955)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'tags':'bird','fill':'#2b3277'})


goOut()
grid(**{'row': 2, 'column': 2})
Canvas('line',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (7.0,28.0,27.0,8.0)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'width':'2.0'})


goOut()
grid(**{'row': 0})
Canvas('oval',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (5.0,7.0,30.0,27.0)
item = canvas.create_oval(*coords)
canvas.itemconfig(item,**{'width':'2.0'})


goOut()
grid(**{'row': 2})
Canvas('polygon',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (11.0,6.0,23.0,6.0,31.0,18.0,23.0,30.0,11.0,30.0,3.0,18.0)
item = canvas.create_polygon(*coords)
canvas.itemconfig(item,**{'fill':'gold','width':'2.0','outline':'blue'})


goOut()
grid(**{'row': 1, 'column': 1})
Canvas('polyline',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (19.0,81.0,19.0,81.0)
item = canvas.create_line(*coords)
coords = (34.0,38.0,34.0,38.0)
item = canvas.create_line(*coords)
coords = (5.0,24.0,11.5,9.75,15.5,24.5,21.25,11.5,24.25,20.25,29.0,16.5)
item = canvas.create_line(*coords)
canvas.itemconfig(item,**{'width':'2.0'})


goOut()
grid(**{'row': 0, 'column': 1})
Canvas('rectangle',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (4.0,5.0,29.0,30.0)
item = canvas.create_rectangle(*coords)
canvas.itemconfig(item,**{'width':'2.0'})


goOut()
grid(**{'row': 1})
Canvas('text',**{'height': '30', 'width': '30', 'relief': 'raised', 'bd': '2'})
goIn()


canvas=container()

coords = (12.0,4.0)
item = canvas.create_text(*coords)
canvas.itemconfig(item,**{'font':'TkDefaultFont 20 bold','anchor':'nw','text':'A'})


goOut()
grid(**{'row': 3, 'column': 2})

goOut()
grid(**{'row': 2, 'sticky': 'nesw', 'column': 1})
LabelFrame('Scaling',**{'grid_rows': '(6, 10, 0, 0)', 'grid_cols': '(4, 10, 0, 0)', 'text': 'Scaling'})
goIn()

Button('OK',**{'text': 'OK'}).grid(**{'row': 4, 'sticky': 'nesw', 'column': 1})
Checkbutton('both',**{'text': 'both'}).grid(**{'row': 4, 'column': 2})
Label('lscalex',**{'text': 'scale x'}).grid(**{'row': 1, 'column': 1})
Label('lscaley',**{'text': 'scale y'}).grid(**{'row': 1, 'column': 2})
Spinbox('scalex',**{'increment': 0.1, 'width': 6, 'to': 10.0}).grid(**{'row': 2, 'ipady': 3, 'column': 1})
Spinbox('scaley',**{'increment': 0.1, 'width': 6, 'to': 10.0}).grid(**{'row': 2, 'ipady': 3, 'column': 2})

goOut()
grid(**{'row': 0, 'sticky': 'nesw', 'rowspan': 2, 'column': 1})
LabelFrame('Selected',**{'height': 108, 'width': 140, 'pady': '5', 'text': 'Selected'})
goIn()

Label('id',**{'font': 'TkDefaultFont 9 bold', 'relief': 'solid', 'pady': '3', 'padx': '5', 'fg': 'blue', 'bg': 'yellow', 'bd': '2'}).grid(**{'row': 1, 'padx': 2, 'sticky': 'w', 'pady': 2, 'column': 1})
Label('lid',**{'text': 'id'}).grid(**{'row': 1})
Label('ltype',**{'text': 'type'}).grid(**{'row': 0})
Label('type',**{'font': 'TkDefaultFont 9 bold', 'relief': 'solid', 'pady': '3', 'padx': '5', 'fg': 'blue', 'bg': 'yellow', 'bd': '2'}).grid(**{'row': 0, 'padx': 2, 'sticky': 'w', 'pady': 2, 'column': 1})

goOut()
grid(**{'row': 0, 'sticky': 'nesw', 'column': 2})
LabelFrame('Settings',**{'height': 100, 'width': 100, 'text': 'Settings'})
goIn()

Checkbutton('flat_default',**{'anchor': 'w', 'text': 'flat default'})
Checkbutton('line_default',**{'anchor': 'w', 'text': 'line default'})

widget('line_default').pack(**{'fill': 'x', 'anchor': 'w', 'pady': 4})
widget('flat_default').pack(**{'fill': 'x', 'anchor': 'w', 'pady': 1})

goOut()
grid(**{'row': 0, 'sticky': 'nesw'})
LabelFrame('Tagging',**{'text': 'Tagging'})
goIn()

Button('dtag',**{'text': 'dtag', 'bd': '2'})
Button('enclosed',**{'text': 'enclosed', 'bd': '2'})
LabelFrame('find_tag',**{'text': 'select by tag'})
goIn()

Entry('entry',**{'width': 14, 'disabledforeground': 'blue'})

widget('entry').pack(**{'fill': 'both', 'pady': 1})

goOut()

Button('overlapped',**{'text': 'overlapping', 'bd': '2'})
Checkbutton('same_tag',**{'anchor': 'w', 'text': 'select tag'})
LabelFrame('set_tag',**{'text': 'add/del tag'})
goIn()

Entry('entry',**{'width': 14})

widget('entry').pack(**{'fill': 'both', 'pady': 1})

goOut()

Button('withtag',**{'text': 'withtag', 'bd': '2'})

widget('same_tag').pack(**{'fill': 'x', 'anchor': 'w', 'pady': 1})
widget('find_tag').pack(**{'pady': 3})
widget('set_tag').pack()
widget('withtag').pack(**{'fill': 'x'})
widget('overlapped').pack(**{'fill': 'x'})
widget('enclosed').pack(**{'fill': 'x'})
widget('dtag').pack(**{'fill': 'x'})

goOut()
grid(**{'row': 1, 'sticky': 'nesw', 'rowspan': 2})

goOut()
grid(**{'row': 3, 'column': 1})
LabelFrame('Position')
goIn()

LabelFrame('Move',**{'text': 'Move'})
goIn()

Button('OK',**{'text': 'OK', 'bd': '2'}).grid(**{'row': 2, 'sticky': 'nesw', 'pady': 2, 'columnspan': 2})
Spinbox('dx',**{'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'row': 0, 'sticky': 'nesw', 'pady': 2, 'column': 1})
Spinbox('dy',**{'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'row': 1, 'sticky': 'nesw', 'column': 1})
Label('ldx',**{'text': 'dx'}).grid(**{'row': 0, 'sticky': 'nesw'})
Label('ldy',**{'text': 'dy'}).grid(**{'row': 1, 'sticky': 'nesw'})

goOut()
grid(**{'row': 0, 'sticky': 'nsw', 'column': 2})
LabelFrame('Position',**{'grid_rows': '(4, 10, 0, 0)', 'grid_cols': '(6, 10, 0, 0)', 'text': 'Position'})
goIn()

Spinbox('incx1',**{'width': 4, 'to': 1000.0}).grid(**{'row': 1, 'ipady': 2, 'padx': 4, 'sticky': 'nesw', 'pady': 2, 'column': 3})
Spinbox('incy1',**{'width': 4, 'to': 1000.0}).grid(**{'row': 2, 'ipady': 2, 'padx': 4, 'sticky': 'nesw', 'pady': 2, 'column': 3})
Label('lincx1',**{'text': 'inc x0'}).grid(**{'row': 1, 'sticky': 'nesw', 'column': 4})
Label('lincy1',**{'text': 'inc y0'}).grid(**{'row': 2, 'sticky': 'nesw', 'column': 4})
Label('lx1',**{'text': 'x0'}).grid(**{'row': 1, 'sticky': 'nesw', 'column': 1})
Label('ly1',**{'text': 'y0'}).grid(**{'row': 2, 'sticky': 'nesw', 'column': 1})
Spinbox('x1',**{'increment': 10.0, 'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'row': 1, 'ipady': 2, 'padx': 4, 'sticky': 'nesw', 'pady': 2, 'column': 2})
Spinbox('y1',**{'increment': 10.0, 'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'row': 2, 'ipady': 2, 'padx': 4, 'sticky': 'nesw', 'pady': 2, 'column': 2})

goOut()
grid(**{'row': 0, 'sticky': 'nsw'})
LabelFrame('Size',**{'grid_rows': '(4, 10, 0, 0)', 'grid_cols': '(2, 10, 0, 0)', 'text': 'Size'})
goIn()

Spinbox('height',**{'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'row': 2, 'ipady': 2, 'padx': 4, 'sticky': 'nesw', 'pady': 2, 'column': 1})
Label('lheight',**{'text': 'height'}).grid(**{'row': 2, 'sticky': 'nesw'})
Label('lwidth',**{'text': 'width'}).grid(**{'row': 1, 'sticky': 'nesw'})
Spinbox('width',**{'from': -9999.0, 'width': 5, 'to': 9999.0}).grid(**{'row': 1, 'ipady': 2, 'padx': 4, 'sticky': 'nesw', 'pady': 2, 'column': 1})

goOut()
grid(**{'row': 0, 'sticky': 'nsw', 'column': 1})

goOut()
grid(**{'row': 2, 'sticky': 'nesw', 'column': 1})

### CODE ===================================================

#Button('window',**{'text': 'window', 'pady': '3', 'padx': '3', 'bd': '2', 'relief': 'raised'})
#grid(**{'column': '3', 'sticky': 'nesw', 'row': '3'})

class Access:

    def __init__(self,canvas,selected):
        
        from RDP import rdp
        
        #global _CANVAS_WIDGET
        #_CANVAS_WIDGET = None

        self.canvas = canvas

        def noop(): pass

        def check_closed(msg,cont=container(),noop=noop):
            if msg == cont.myRoot():
                if widget_exists(self.canvas):
                    '''
                    self.canvas.do_event('<Button-1>',noop)
                    self.canvas.do_event('<ButtonRelease-1>',noop)
                    self.canvas.do_event('<Button-3>',noop)
                    '''

                    self.canvas['cursor'] = ''
                    self.canvas.unbind('<Button-1>')
                    self.canvas.unbind('<ButtonRelease-1>')
                    self.canvas.unbind('<Button-3>')
                    send("UPDATE_CANVAS_MOUSE_SELECT_ON",self.canvas)

        do_receive('THIS_TOPLEVEL_CLOSED',check_closed,wishMessage = True)

        def check_container_destroyed(msg,root = widget('/')):
            if msg == canvas: root.destroy()

        do_receive("CONTAINER_DESTROYED",check_container_destroyed,wishMessage=True)

 
        self.pytkvg_file = 'pytkvg/bird.py'
        self.pytkvg_height = 50
        self.pytkvg_tag = ''

        self.selected_item = None
 
        self.canvas.do_event('<Button-1>',noop)
        self.canvas.do_event('<ButtonRelease-1>',noop)
        self.canvas.do_event('<Button-3>',noop)

        self.x1 = widget('.','Position','Position','x1')
        self.y1 = widget('.','Position','Position','y1')
        self.incx1 = widget('.','Position','Position','incx1')
        self.incy1 = widget('.','Position','Position','incy1')

        self.width = widget('.','Position','Size','width')
        self.height = widget('.','Position','Size','height')
        self.dx = widget('.','Position','Move','dx')
        self.dy = widget('.','Position','Move','dy')
        self.dxdyOK = widget('.','Position','Move','OK')
        self.position_frame = widget('.','Position','Position')
        self.size_frame = widget('.','Position','Size')
        
        self.line = widget('.','Handling','Drawing','line')
        self.polyline = widget('.','Handling','Drawing','polyline')
        self.freehand = widget('.','Handling','Drawing','freehand')

        self.rectangle = widget('.','Handling','Drawing','rectangle')
        self.polygon = widget('.','Handling','Drawing','polygon')
        self.freehand_polygon = widget('.','Handling','Drawing','freehand_polygon')

        self.oval = widget('.','Handling','Drawing','oval')
        self.arc = widget('.','Handling','Drawing','arc')
        
        self.pytkvg = widget('.','Handling','Drawing','import')
        self.image = widget('.','Handling','Drawing','image')
        self.bitmap = widget('.','Handling','Drawing','bitmap')
        self.text = widget('.','Handling','Drawing','text')
        self.window = widget('.','Handling','Drawing','window')

        self.move = widget('.','Handling','Changing','move')
        self.copy = widget('.','Handling','Changing','copy')
        self.select = widget('.','Handling','Changing','select')
        self.tag_lower = widget('.','Handling','Changing','lower')
        self.tag_raise = widget('.','Handling','Changing','raise')
        self.delete = widget('.','Handling','Changing','delete')

        self.widget_line_default = widget('.','Handling','Settings','line_default')
        self.widget_flat_default = widget('.','Handling','Settings','flat_default')

        self.same_tag = widget('.','Handling','Tagging','same_tag')
        self.find_tag = widget('.','Handling','Tagging','find_tag','entry')
        self.set_tag = widget('.','Handling','Tagging','set_tag','entry')
        
        self.scalex = widget('.','Handling','Scaling','scalex')
        self.scaley = widget('.','Handling','Scaling','scaley')
        self.scale_both = widget('.','Handling','Scaling','both')
        self.scale_OK = widget('.','Handling','Scaling','OK')
        self.selected_id = widget('.','Handling','Selected','id')
        self.selected_type = widget('.','Handling','Selected','type')

        self.withtag = widget('.','Handling','Tagging','withtag')
        self.enclosed = widget('.','Handling','Tagging','enclosed')
        self.overlapped = widget('.','Handling','Tagging','overlapped')
        self.dtag = widget('.','Handling','Tagging','dtag')

        var = IntVar()
        self.widget_line_default.mydata = var
        self.widget_line_default['variable'] = var

        var = IntVar()
        self.widget_flat_default.mydata = var
        default_bg = self.arc['bg']

        self.widget_flat_default['variable'] = var

        def do_same_tag(me): self.do_same_tag(me,default_bg)
        self.same_tag.do_command(do_same_tag,wishWidget=True)

        var = IntVar()
        var.set(1)
        self.same_tag.mydata = var
        self.same_tag['variable'] = var
        do_same_tag(self.same_tag)
        
        var = IntVar()
        self.scale_both['variable'] = var
        self.scale_both.mydata = var
        self.scale_both.select()

        var = StringVar()
        var.set('1.0')
        self.scalex.mydata = var
        self.scalex['textvariable'] = var
        self.scaley['textvariable'] = var
        
        var = StringVar()
        var.set('1.0')
        self.scaley.mydata = var
        
        self.incx1.delete(0,END)
        self.incy1.delete(0,END)
        self.incx1.insert(0,'10')
        self.incy1.insert(0,'10')
        self.dx.delete(0,END)
        self.dy.delete(0,END)
        self.dx.insert(0,'0')
        self.dy.insert(0,'0')
        
        widgets = (self.rectangle,self.oval,self.arc,self.line,self.polygon,self.polyline,self.text,self.move,self.select,self.image,self.bitmap,self.freehand,self.freehand_polygon,self.overlapped,self.enclosed,self.pytkvg)
        canvas_item = [None]
        bbox_coord = [0,0,0,0]
        self.poly_coord = []
        paint_enabled=[False]
        bbox_function = [None]
        is_arc = [False]
        self.line_default = None
        self.flat_default = None
        self.set_tag.delete(0,END)



        def do_set_tag():
            tag = self.find_tag.get()
            if tag == '': 
                tag = None
                if container() == self.canvas and isinstance(this(),CanvasItemWidget): tag = this().item_id
            else:
                tags = self.canvas.find_withtag(tag)
                if len(tags) == 0:
                    tag = None
            self.selected_item = tag
            self.update_position()

        self.find_tag.do_event('<Return>',do_set_tag)
        

        def set_increment(me,x_or_y): 
            try:
                dxy = int(me.get())
                x_or_y['increment'] = dxy
            except ValueError: pass

        self.incx1.do_command(set_increment,self.x1,wishWidget=True)
        self.incx1.do_event("<Return>",set_increment,self.x1,wishWidget=True)
        self.incy1.do_command(set_increment,self.y1,wishWidget=True)
        self.incy1.do_event("<Return>",set_increment,self.y1,wishWidget=True)
        

        def update_widgetposition(): self.update_widgetposition(this())
        do_receive('SELECTION_CHANGED',update_widgetposition)
        send('CANVAS_COORD_UPDATE',selected)
        self.update_widgetposition(selected)
        
        def update_position(): self.update_position()

        '''
        def update_position_tag(tag):
            self.selected_item = tag
            #self.update_position()

        #do_receive('CANVAS_UPDATE_POSITION',update_position_tag,wishMessage=True)
        #send('CANVAS_UPDATE_POSITION')
        '''

        def update_position_tagchanged(tag):
            if self.selected_item == tag: self.update_position()

        do_receive('CANVAS_TAGCHANGED',update_position_tagchanged,wishMessage=True)



        '''
        # think about it later, when showing coordinates
        def update_position_nocoord(): self.update_position(this(),False)
        do_receive('UPDATE_POS_NOCOORD',update_position_nocoord)
        '''

        
        def get_coord():
            xw = self.canvas.winfo_pointerx()-self.canvas.winfo_rootx()
            yw = self.canvas.winfo_pointery()-self.canvas.winfo_rooty()
            return self.canvas.canvasx(xw), self.canvas.canvasy(yw)

        def set_buttons_normal():
            for element in widgets: element.config(bg=default_bg,relief='raised')
            self.canvas.do_event('<Button-1>',noop)
            self.canvas.do_event('<ButtonRelease-1>',noop)
            self.canvas.do_event('<Button-3>',noop)

        def mouse_move():
            if paint_enabled[0]:
                step = 10
                xc,yc = get_coord()
                bbox_coord[2] = xc
                bbox_coord[3] = yc

                if is_arc[0]:

                    diffx = xc - bbox_coord[0]
                    diffy = yc - bbox_coord[1]
                    # could be dependent on angle
                    x1 = bbox_coord[0]-diffx
                    x2 = xc
                    y1 = bbox_coord[1]
                    y2 = yc+diffy

                    self.canvas.coords(canvas_item[0],*(x1,y1,x2,y2))
                else:
                    self.canvas.coords(canvas_item[0],bbox_coord[0],bbox_coord[1],xc,yc)
                self.canvas.after(step,mouse_move)


        def mouse_move_polygon():
            if paint_enabled[0]:
                step = 10
                xc,yc = get_coord()
                self.poly_coord[-2] = xc
                self.poly_coord[-1] = yc
                self.canvas.coords(canvas_item[0],*self.poly_coord)
                self.canvas.after(step,mouse_move_polygon)

        def mouse_move_freehand():
            if paint_enabled[0]:
                step = 10
                xc,yc = get_coord()
                self.poly_coord.append(xc)
                self.poly_coord.append(yc)
                self.poly_coord[-2] = xc
                self.poly_coord[-1] = yc
                self.canvas.coords(canvas_item[0],*self.poly_coord)
                self.canvas.after(step,mouse_move_freehand)

        def mouse_move_move():
            if paint_enabled[0]:
                step = 10
                xc,yc = get_coord()
                diffx = xc - bbox_coord[0]
                diffy = yc - bbox_coord[1]
                bbox_coord[0] = xc
                bbox_coord[1] = yc
                self.canvas.move(canvas_item[0],diffx,diffy)
                self.canvas.after(step,mouse_move_move)

        #def do_paint(canvas_item=canvas_item,bbox_coord=bbox_coord,paint_enabled=paint_enabled,mouse_move=mouse_move):
        def do_paint():
            xc,yc = get_coord()
            bbox_coord[2] = bbox_coord[0] = xc
            bbox_coord[3] = bbox_coord[1] = yc
            paint_enabled[0] = True
            canvas_item[0] = bbox_function[0](xc,yc,xc,yc)
            if self.line_default != None and bbox_function[0] == self.canvas.create_line: self.canvas.itemconfig(canvas_item[0],**self.line_default)
            if self.flat_default != None and bbox_function[0] in (self.canvas.create_rectangle,self.canvas.create_oval,self.canvas.create_arc): self.canvas.itemconfig(canvas_item[0],**self.flat_default)
            tag = self.set_tag.get()
            if tag != '': self.canvas.addtag_withtag(tag, canvas_item[0])
            mouse_move()


        def stop_paint():
            paint_enabled[0] = False
            if is_arc[0]:
                xc,yc = get_coord()
                diffx = xc - bbox_coord[0]
                diffy = yc - bbox_coord[1]
                # could be dependent on angle
                x1 = bbox_coord[0]-diffx
                x2 = xc
                y1 = bbox_coord[1]
                y2 = yc+diffy
                bbox_coord[0] = x1
                bbox_coord[1] = y1
                bbox_coord[2] = x2
                bbox_coord[3] = y2
            self.canvas.coords(canvas_item[0],*bbox_coord)
            CanvasItem(self.canvas,canvas_item[0])
            send('SELECTION_CHANGED')

        def stop_move():
            paint_enabled[0] = False
            update_position()

        def add_paint_polygon():
            xc,yc = get_coord()
            self.poly_coord[-2] = xc
            self.poly_coord[-1] = yc

            if bbox_function[0] == self.canvas.create_polygon and len(self.poly_coord) == 4:
                self.canvas.delete(canvas_item[0])
                canvas_item[0] = self.canvas.create_polygon(*self.poly_coord)
                if self.flat_default != None: self.canvas.itemconfig(canvas_item[0],**self.flat_default)
                tag = self.set_tag.get()
                if tag != '': self.canvas.addtag_withtag(tag, canvas_item[0])

            self.poly_coord.append(xc)
            self.poly_coord.append(yc)

        def do_paint_polygon():
            xc,yc = get_coord()
            self.poly_coord = [0,0,0,0]
            self.poly_coord[2] = self.poly_coord[0] = xc
            self.poly_coord[3] = self.poly_coord[1] = yc
            paint_enabled[0] = True
            canvas_item[0] = self.canvas.create_line(xc,yc,xc,yc)
            if self.line_default != None and bbox_function[0] == self.canvas.create_line: self.canvas.itemconfig(canvas_item[0],**self.line_default)
            tag = self.set_tag.get()
            if tag != '': self.canvas.addtag_withtag(tag, canvas_item[0])
            self.canvas.do_event('<ButtonRelease-1>',noop)
            self.canvas.do_event('<Button-1>',add_paint_polygon)
            mouse_move_polygon()


        def do_freehand():
            xc,yc = get_coord()
            self.poly_coord = [0,0,0,0]
            self.poly_coord[2] = self.poly_coord[0] = xc
            self.poly_coord[3] = self.poly_coord[1] = yc
            paint_enabled[0] = True
            canvas_item[0] = bbox_function[0](xc,yc,xc,yc)
            if self.line_default != None and bbox_function[0] == self.canvas.create_line: self.canvas.itemconfig(canvas_item[0],**self.line_default)
            if self.flat_default != None and bbox_function[0] == self.canvas.create_polygon: self.canvas.itemconfig(canvas_item[0],**self.flat_default)
            tag = self.set_tag.get()
            if tag != '': self.canvas.addtag_withtag(tag, canvas_item[0])
            mouse_move_freehand()

        def stop_freehand():
            paint_enabled[0] = False
            #canvas_item[0] = self.canvas.create_line(*self.poly_coord)
            line = []
            for i in range(0,len(self.poly_coord),2):
                line.append((self.poly_coord[i],self.poly_coord[i+1]))
            bline = rdp(line, 1.0)
            self.poly_coord=[]
            for entry in bline:
                self.poly_coord.append(entry[0])
                self.poly_coord.append(entry[1])
            self.canvas.coords(canvas_item[0],*self.poly_coord)
            CanvasItem(self.canvas,canvas_item[0])
            send('SELECTION_CHANGED')

        def stop_paint_polygon():
            paint_enabled[0] = False
            self.canvas.do_event('<Button-1>',do_paint_polygon)
            CanvasItem(self.canvas,canvas_item[0])
            send('SELECTION_CHANGED')

        def do_text():
            xc,yc = get_coord()
            item = self.canvas.create_text(xc,yc,text="Text")
            tag = self.set_tag.get()
            if tag != '': self.canvas.addtag_withtag(tag,item)
            CanvasItem(self.canvas,item)
            send('SELECTION_CHANGED')

        def do_image():
            xc,yc = get_coord()
            item = self.canvas.create_image(xc,yc)
            tag = self.set_tag.get()
            if tag != '': self.canvas.addtag_withtag(tag,item)
            CanvasItem(self.canvas,item)
            send('SELECTION_CHANGED')

        def do_pytkvg():
            xc,yc = get_coord()
            tag = DynAccess(self.pytkvg_file,self.canvas)
            if self.pytkvg_tag != '': tag = self.pytkvg_tag
            self.selected_item = tag
            x_min,y_min,x_max,y_max = self.get_area('new_tag')
            center_x = (x_min+x_max)/2
            center_y = (y_min+y_max)/2
            self.canvas.move('new_tag',xc-center_x,yc-center_y)
            vg_height = y_max-y_min
            self.canvas.scale('new_tag',xc,yc,self.pytkvg_height/vg_height,self.pytkvg_height/vg_height)
            self.canvas.addtag_withtag(tag,'new_tag')
            self.canvas.dtag('new_tag')
            self.same_tag.mydata.set(1)
            do_same_tag(self.same_tag)
            self.find_tag['state'] = 'normal'
            self.find_tag.delete(0,END)
            self.find_tag.insert(0,tag)
            self.find_tag['state'] = 'disabled'
            set_buttons_normal()
            self.move.config(bg='#80e0e0',relief='sunken')
            self.canvas['cursor'] = 'crosshair'
            self.canvas.do_event('<Button-1>',do_move)
            self.canvas.do_event('<ButtonRelease-1>',stop_move)
            self.canvas.do_event('<Button-3>',noop)
            

        def do_bitmap():
            xc,yc = get_coord()
            item = self.canvas.create_bitmap(xc,yc,bitmap="@guidesigner/images/starMask")
            tag = self.set_tag.get()
            if tag != '': self.canvas.addtag_withtag(tag,item)
            CanvasItem(self.canvas,item)
            send('SELECTION_CHANGED')


        def set_selected_item(item):
            if type(item) is tuple:
                if len(item) == 0: self.selected_item = None
                else: self.selected_item = item[0]
            else: self.selected_item = item
            

        def do_move():
            xc,yc = get_coord()
            bbox_coord[0] = xc
            bbox_coord[1] = yc
            is_same_tag = self.same_tag.mydata.get() == 1
            if is_same_tag:
                item = self.canvas.find_closest(xc,yc)
                mytags = self.canvas.gettags(item)
                self.find_tag['state'] = 'normal'
                self.find_tag.delete(0,END)
                if len(mytags) < 3:
                    tags = list(mytags)
                    if 'current' in tags:
                        index = tags.index('current')
                        tags.pop(index)
                    if len(tags) == 1:
                        item = tags[0]
                        self.find_tag.insert(0,item)
                self.find_tag['state'] = 'disabled'
            else:
                item = self.find_tag.get()
                if item == '': 
                    item = self.canvas.find_closest(xc,yc)
                    
            canvas_item[0] = item
            set_selected_item(item)
            update_position()
            paint_enabled[0] = True
            mouse_move_move()

        def do_select():
            xc,yc = get_coord()
            item = self.canvas.find_closest(xc,yc)
            if len(item) > 0:
                CanvasItem(self.canvas,item[0],False)
                is_same_tag = self.same_tag.mydata.get() == 1
                if is_same_tag:
                    mytags = self.canvas.gettags(item)
                    self.find_tag['state'] = 'normal'
                    self.find_tag.delete(0,END)
                    if len(mytags) < 3:
                        tags = list(mytags)
                        if 'current' in tags:
                            index = tags.index('current')
                            tags.pop(index)
                        if len(tags) == 1:
                            item = tags[0]
                            self.find_tag.insert(0,item)
                    self.find_tag['state'] = 'disabled'
                send('SELECTION_CHANGED')
                

        def do_button_click(me):
            set_buttons_normal()
            me.config(bg='#80e0e0',relief='sunken')
            self.canvas['cursor'] = 'crosshair'
            is_arc[0] = False
            if me == self.arc:
                is_arc[0] = True
                bbox_function[0] = self.canvas.create_arc
            elif me  == self.oval: bbox_function[0] = self.canvas.create_oval
            elif me == self.rectangle: bbox_function[0] = self.canvas.create_rectangle
            elif me == self.line: bbox_function[0] = self.canvas.create_line
     
            if me == self.polygon or me == self.polyline:
                if me == self.polygon: bbox_function[0] = self.canvas.create_polygon
                else: bbox_function[0] = self.canvas.create_line
                self.canvas.do_event('<Button-1>',do_paint_polygon)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',stop_paint_polygon)
            elif me == self.text:
                self.canvas.do_event('<Button-1>',do_text)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',noop)
            elif me == self.image:
                self.canvas.do_event('<Button-1>',do_image)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',noop)
            elif me == self.pytkvg:
                self.canvas.do_event('<Button-1>',do_pytkvg)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',noop)
                DynAccess('guidesigner/canvas/LoadVg.py',self)
            elif me == self.bitmap:
                self.canvas.do_event('<Button-1>',do_bitmap)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',noop)
            elif me  == self.move:
                self.canvas.do_event('<Button-1>',do_move)
                self.canvas.do_event('<ButtonRelease-1>',stop_move)
                self.canvas.do_event('<Button-3>',noop)
            elif me  == self.select:
                self.canvas.do_event('<Button-1>',do_select)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',noop)
            elif me  == self.freehand or me == self.freehand_polygon:
                bbox_function[0] = self.canvas.create_line if me  == self.freehand else self.canvas.create_polygon
                self.canvas.do_event('<Button-1>',do_freehand)
                self.canvas.do_event('<ButtonRelease-1>',stop_freehand)
                self.canvas.do_event('<Button-3>',noop)
            else: # bbox rectangle, line, oval, arc
                self.canvas.do_event('<Button-1>',do_paint)
                self.canvas.do_event('<ButtonRelease-1>',stop_paint)
                self.canvas.do_event('<Button-3>',noop)
            
        for element in widgets:
            element.do_event('<Button-1>',do_button_click,wishWidget = True)
            
        '''
        def create_a_window():
            if container() == self.canvas and this() != container() and not isinstance(this(),CanvasItemWidget):
                #if not isinstance(this(),CanvasItemWidget):
                this().unlayout()
                this().Layout = WINDOWLAYOUT
                set_buttons_normal()
                self.canvas.do_event('<Button-1>',noop)
                self.canvas.do_event('<ButtonRelease-1>',noop)
                self.canvas.do_event('<Button-3>',noop)
                item = self.canvas.create_window(0,0,anchor='nw',window = this())
                #ref_string = self.canvas.itemcget(item,'window')
                #print(repr(Widget.nametowidget(None,ref_string)))
                this().window_item = item
                tag = self.set_tag.get()
                if tag != '': self.canvas.addtag_withtag(tag,item)
                CanvasItem(self.canvas,item)
                send('SELECTION_CHANGED')

        self.window.do_command(create_a_window)
        '''
        

        def do_tag_lower():
            if self.selected_item == None: return
            self.canvas.tag_lower(self.selected_item)

        self.tag_lower.do_command(do_tag_lower)


        def do_tag_raise():
            if self.selected_item == None: return
            self.canvas.tag_raise(self.selected_item)

        self.tag_raise.do_command(do_tag_raise)


        def do_scale():

            if self.selected_item == None: return
            item = self.selected_item
            x,y = self.center_of_tag(item)
            try:
                factorx = float(self.scalex.get())
                factory = float(self.scaley.get())
                self.canvas.scale(item,x,y,factorx,factory)
                update_position()
            except: ValueError

        self.scale_OK.do_command(do_scale)

        def do_line_default(me):
            if me.mydata.get() == 0:
                self.line_default = None
                me.config(relief = 'raised',bg = default_bg)
            elif container() == self.canvas and isinstance(this(),CanvasItemWidget) and self.canvas.type(this().item_id) == 'line':
                me.config(relief = 'sunken',bg = '#b0ff60')
                self.line_default = getconfdict()
            else: me.deselect()

        self.widget_line_default.do_command(do_line_default,wishWidget=True)
        
        def do_flat_default(me):
            if me.mydata.get() == 0:
                self.flat_default = None
                me.config(relief = 'raised',bg = default_bg)
            elif container() == self.canvas and isinstance(this(),CanvasItemWidget):
                my_type = self.canvas.type(this().item_id)
                if my_type in ('rectangle','oval','polygon'):
                    me.config(relief = 'sunken',bg = '#b0ff60')
                    self.flat_default = getconfdict()
                else: me.deselect()
            else: me.deselect()

        self.widget_flat_default.do_command(do_flat_default,wishWidget=True)


        def do_scale_both(me):
            if me.mydata.get() == 0:
                self.scaley.mydata.set(self.scalex.mydata.get())
                self.scaley['textvariable'] = self.scaley.mydata
            else:
                self.scaley['textvariable'] = self.scalex.mydata
        
        self.scale_both.do_command(do_scale_both,wishWidget=True)


        def do_delete():

            if self.selected_item != None:
                self.canvas.delete(self.selected_item)
                self.selected_item = None
                setSelection(Create_Selection(self.canvas,self.canvas))
                send('SELECTION_CHANGED')



            '''
            tag = self.find_tag.get()
            if tag != '': 
                self.canvas.delete(tag)
                setSelection(Create_Selection(self.canvas,self.canvas))
                send('SELECTION_CHANGED')
            elif container() == self.canvas and isinstance(this(),CanvasItemWidget):
                this().destroy()
                setSelection(Create_Selection(self.canvas,self.canvas))
                send('SELECTION_CHANGED')
            '''

        self.delete.do_command(do_delete)
        
        def do_withtag():
            if self.selected_item != None:
                set_tag = self.set_tag.get()
                self.canvas.addtag_withtag(set_tag,self.selected_item)

        self.withtag.do_command(do_withtag)

        def do_dtag():
            if self.selected_item != None:
                set_tag = self.set_tag.get()
                self.canvas.dtag(self.selected_item,set_tag)

        self.dtag.do_command(do_dtag)


        def start_overlapped():
            xc,yc = get_coord()
            bbox_coord[2] = bbox_coord[0] = xc
            bbox_coord[3] = bbox_coord[1] = yc
            paint_enabled[0] = True
            bbox_function[0] = self.canvas.create_rectangle
            canvas_item[0] = bbox_function[0](xc,yc,xc,yc,width=6,outlinestipple='gray25')
            mouse_move()

        def stop_overlapped():
            paint_enabled[0] = False
            xc,yc = get_coord()
            selection_before = Selection()
            self.canvas.delete(canvas_item[0])
            setSelection(selection_before)
            self.canvas.do_event('<ButtonRelease-1>',noop)
            self.canvas.do_event('<Button-1>',noop)
            self.overlapped.config(relief = 'raised',bg = default_bg)
            set_tag = self.set_tag.get()
            self.canvas.addtag_overlapping(set_tag,bbox_coord[0],bbox_coord[1],xc,yc)
            send('SELECTION_CHANGED')

        def do_overlapped(me):
            set_buttons_normal()
            me.config(relief = 'sunken',bg = '#80e0e0')
            self.canvas.do_event('<Button-1>',start_overlapped)
            self.canvas.do_event('<ButtonRelease-1>',stop_overlapped)
            self.canvas.do_event('<Button-3>',noop)

        self.overlapped.do_command(do_overlapped,wishWidget=True)

        def stop_enclosed():
            paint_enabled[0] = False
            xc,yc = get_coord()
            selection_before = Selection()
            self.canvas.delete(canvas_item[0])
            setSelection(selection_before)
            self.canvas.do_event('<ButtonRelease-1>',noop)
            self.canvas.do_event('<Button-1>',noop)
            self.enclosed.config(relief = 'raised',bg = default_bg)
            set_tag = self.set_tag.get()
            self.canvas.addtag_enclosed(set_tag,bbox_coord[0],bbox_coord[1],xc,yc)
            send('SELECTION_CHANGED')

        def do_enclosed(me):
            set_buttons_normal()
            me.config(relief = 'sunken',bg = '#80e0e0')
            self.canvas.do_event('<Button-1>',start_overlapped)
            self.canvas.do_event('<ButtonRelease-1>',stop_enclosed)
            self.canvas.do_event('<Button-3>',noop)

        self.enclosed.do_command(do_enclosed,wishWidget=True)


        def do_setwidth():
            try:
                width = int(self.width.get())
                item = self.selected_item
                if type(item) is int and len(self.canvas.coords(item)) == 4: 
                    coords = self.canvas.coords(item)
                    coords[2] = coords[0] + width
                    self.canvas.coords(item,*coords)
                else:
                    x1,y1,x2,y2 = self.get_area(item)
                    self.canvas.scale(item,x1,y1,width/(x2-x1),width/(x2-x1))

                update_position()
                #send('CANVAS_COORD_UPDATE',this())
            except ValueError: pass

        self.width.do_command(do_setwidth)
        self.width.do_event('<Return>',do_setwidth)

        def do_setheight():
            try:
                height = int(self.height.get())
                item = self.selected_item
                if type(item) is int and len(self.canvas.coords(item)) == 4: 
                    coords = self.canvas.coords(item)
                    coords[3] = coords[1] + height
                    self.canvas.coords(item,*coords)
                else:
                    x1,y1,x2,y2 = self.get_area(item)
                    self.canvas.scale(item,x1,y1,height/(y2-y1),height/(y2-y1))

                update_position()
                #send('CANVAS_COORD_UPDATE',this())
            except ValueError: pass

        self.height.do_command(do_setheight)
        self.height.do_event('<Return>',do_setheight)


        def do_setx1():
            if self.selected_item != None:
                item = self.selected_item

                try:
                    new_x1 = int(self.x1.get())
                    
                    if type(item) is int and len(self.canvas.coords(item)) < 5: x1 = self.canvas.coords(item)[0]
                    else: x1,y1,x2,y2 = self.get_area(item)
                    self.canvas.move(item,new_x1-x1,0)
                    update_position()
                    #send('CANVAS_COORD_UPDATE',this())
                except: ValueError

        self.x1.do_command(do_setx1)
        self.x1.do_event('<Return>',do_setx1)

        def do_sety1():
            if self.selected_item != None:
                item = self.selected_item
                try:
                    new_y1 = int(self.y1.get())
                    if type(item) is int and len(self.canvas.coords(item)) < 5: y1 = self.canvas.coords(item)[1]
                    else: x1,y1,x2,y2 = self.get_area(item)
                    self.canvas.move(item,0,new_y1-y1)
                    update_position()
                    #send('CANVAS_COORD_UPDATE',this())
                except: ValueError

        self.y1.do_command(do_sety1)
        self.y1.do_event('<Return>',do_sety1)


        def do_copy():
            if self.selected_item != None: DynAccess('guidesigner/canvas/Copy.py',(self.canvas,self.selected_item))

        self.copy.do_command(do_copy)

        def do_move_dx_dy():

            if self.selected_item != None:
                try:
                    dx = int(self.dx.get())
                    dy = int(self.dy.get())
                    self.canvas.move(self.selected_item,dx,dy)
                    update_position()
                except: ValueError

        self.dx.do_event('<Return>',do_move_dx_dy)
        self.dy.do_event('<Return>',do_move_dx_dy)
        self.dxdyOK.do_command(do_move_dx_dy)


    
    # difference bbox and not bbox? There should be also a text, which kind it is
    def update_position(self):

        if self.selected_item == None:
            self.position_frame.unlayout()
            self.size_frame.unlayout()
            self.selected_type['text'] = ""
            self.selected_id['text'] = ""
            return

       
        if type(self.selected_item) is int: self.selected_type['text'] = self.canvas.type(self.selected_item)
        else: self.selected_type['text'] = 'tag'
        self.selected_id['text'] = self.selected_item
            
        if type(self.selected_item) is int and len(self.canvas.coords(self.selected_item)) == 4:
            
            coords = self.canvas.coords(self.selected_item)
            x1 = int(coords[0])
            y1 = int(coords[1])
            width = int(coords[2]) - x1
            height = int(coords[3]) - y1
            self.size_frame.grid()
        elif type(self.selected_item) is int and len(self.canvas.coords(self.selected_item)) == 2:
            self.selected_type['text'] = self.canvas.type(self.selected_item)
            coords = self.canvas.coords(self.selected_item)
            x1 = int(coords[0])
            y1 = int(coords[1])
            width = 0
            height = 0
            self.size_frame.unlayout()
        else:
            
            x1,y1,x2,y2 = self.get_area(self.selected_item)
            width = int(x2-x1)
            height = int(y2-y1)
            x1 = int(x1)
            y1 = int(y1)
            self.size_frame.grid()

        self.x1.delete(0,END)
        self.y1.delete(0,END)
        self.width.delete(0,END)
        self.height.delete(0,END)

        self.x1.insert(0,str(x1))
        self.y1.insert(0,str(y1))
        self.width.insert(0,str(width))
        self.height.insert(0,str(height))
            
        self.position_frame.grid()


    def update_widgetposition(self,selected,update_coord = True):

        if isinstance(selected,CanvasItemWidget):
            self.selected_item = selected.item_id
        else:
            self.selected_item = None
        self.update_position()
        if update_coord: send('CANVAS_COORD_UPDATE',selected)


    def do_same_tag(self,me,default_bg):
        if me.mydata.get() == 0:
            me.config(relief = 'flat',bg = default_bg)
            self.find_tag.config(state='normal')
            self.find_tag.delete(0,END)
        else:
            me.config(relief = 'sunken',bg = '#b0ff60')
            self.find_tag.delete(0,END)
            self.find_tag.config(state='disabled')


    def get_area(self,tag):
        x_min = 100000
        y_min = 100000
        x_max = -100000
        y_max = -100000
        item_list = self.canvas.find_withtag(tag)
        for item in item_list:
            coords = self.canvas.coords(item)
            for index in range(0,len(coords),2):
                if coords[index] < x_min: x_min = coords[index]
                if coords[index] > x_max: x_max = coords[index]
                if coords[index+1] < y_min: y_min = coords[index+1]
                if coords[index+1] > y_max: y_max = coords[index+1]
        return (x_min,y_min,x_max,y_max)

    def center_of_tag(self,tag):
        x0,y0,x1,y1 = self.get_area(tag)
        return ((x0+x1)/2,(y0+y1)/2)

### ========================================================

goOut()

