Scrollbar(orient=VERTICAL)
pack(side=RIGHT,fill=Y,expand=FALSE)

Canvas(bd=0,highlightthickness=0)
pack(fill=BOTH, expand=TRUE)

Frame().pack(side=BOTTOM,anchor=NW)

### CODE ===================================================

Lock()

def geometry_refresh(me,widget):
    mydata = widget.mydata[0]
    if mydata != None:
        geometry = getconfig("geometry")
        if geometry != widget.mydata[1]:
            widget.mydata[1] = geometry
            mydata.delete(0,END)
            mydata.insert(0,str(getconfig("geometry")))
            if widget.mydata[2] != None:
                widget.mydata[2].delete(0,END)
                widget.mydata[2].insert(0,str(getconfig("height")))
            if widget.mydata[3] != None:
                widget.mydata[3].delete(0,END)
                widget.mydata[3].insert(0,str(getconfig("width")))

    informLater(1000,me,'refresh')


this().mydata=[None,None,None,None,None]

def undo_refresh(thisframe=this()):
    if thisframe.mydata[4] != None: undo_action(thisframe.mydata[4],'refresh')
    thisframe.mydata=[None,None,None,None,None]

undo_refresh()

# -------------- make a frame with a vertical scrollbar ------------------------------------

widget("Canvas").config(yscrollcommand=widget("Scrollbar").set)
widget("Scrollbar").config(command=widget("Canvas").yview)
interior_id = widget("Canvas").create_window(0, 0, window=widget("Frame"),anchor=NW)


# -------------- <Configure> events for the scrollbar frame ------------------------------------

def canvas_configure(me,frame,int_id = interior_id):
    if me.winfo_reqwidth() != frame.winfo_width(): me.itemconfigure(int_id, width=me.winfo_width())
 
widget("Canvas").do_event("<Configure>",canvas_configure,widget("Frame"),True)

def frame_configure(me,canvas):
    canvas.config(scrollregion="0 0 %s %s" % (me.winfo_reqwidth(), me.winfo_reqheight()))
    if me.winfo_reqwidth() != canvas.winfo_width(): canvas.config(width=me.winfo_reqwidth())
    if me.winfo_reqheight() > 340: canvas.config(height=340)
    else: canvas.config(height=me.winfo_reqheight())

widget("Frame").do_event("<Configure>",frame_configure,widget("Canvas"),True)

# -------------- receivers for SELECTION_CHANGED and CREATE_WIDGET_DONE messages -----------

# in both cases an internal 'SHOW_CONFIG' message will be sent
do_receive('SELECTION_CHANGED',lambda: send("SHOW_CONFIG",this()))

# -------------- receiver for message 'SHOW_CONFIG' - help functions ------------------------------------

# for Return key or mouse klick: get active selection from the listbox, hide the listbox, set the layout and insert the text in the Entry for showing

def do_lbox_click(event,lbox,entry,isMouse):
    if isMouse: text = lbox.get(lbox.nearest(event.y))
    else: text = lbox.get(ACTIVE)
    setconfig(entry.mydata,text)
    entry.delete(0,END)
    entry.insert(0,text)
    lbox.unbind("<Return>")
    lbox.unbind("<Button-1>")
    lbox.unlayout()

def listbox_helpbutton(lbox,entry,lbox_click = do_lbox_click):
    lbox.select_clear(0,END) # clear a former listbox selection 
    lbox_index = lbox.getStringIndex(getconfig(entry.mydata)) # get the listbox index for the layout option
    lbox.select_set(lbox_index) # preselect the current layout option in the listbox
    lbox.activate(lbox_index) # and set the selection cursor to it
    lbox.rcgrid(0,3) # show the listbox
    lbox.focus_set() # and focus it
    lbox.do_event("<Return>",lbox_click,(lbox,entry,False),wishEvent=True)  # bind Return key to the listbox
    lbox.do_event("<Button-1>",lbox_click,(lbox,entry,True),wishEvent=True)  # bind mouse click to the listbox

def listbox_selection(helpbutton = listbox_helpbutton):
    Button(text="?").rcgrid(0,2) # create a help button for showing the listbox
    do_command(helpbutton,(widget("Listbox"),widget("Entry")))

def select_color(mebutton,entry):
    # call color chooser and save the result
    color = getconfig(entry.mydata)
    if color == "": color = 'white'
    choosen_color = colorchooser.askcolor(parent=mebutton,initialcolor=color,title="Choose color: "+entry.mydata)
    # if a valid color was chosen
    if choosen_color[1] != None:
        selcolor = choosen_color[1]
        mebutton['bg']=selcolor # show the help button in this color (bg)
        setconfig(entry.mydata,selcolor) # config the color
        entry.delete(0,END)	
        entry.insert(0,selcolor)

def create_color_button(entry,sel_color = select_color):
    Button(text="?").rcgrid(0,2)
    setconfig('bg',entry.get()) # the color of the button shall be the currently shown color value in the entry field
    do_command(sel_color,entry,True) # command for the button

# -------------- receiver for message 'SHOW_CONFIG'  ------------------------------------

def do_color_action(me,msg):
    me['bg'] = 'white'
    if msg:
        me.delete(0,END)
        me.insert(0,str(getconfig(me.mydata)))

def do_text_color(me):
    setconfig(me.mydata,me.get("1.0",'end-1c'))
    me['bg']='gray'
    informLater(300,me,'color',False)

def entry_event(me,button=None):
    if button != None: button.setconfig('bg',me.get())
    setconfig(me.mydata,me.get())
    if me.mydata == "geometry": this().geometry_changed = True
    if me.mydata == "title": this().title_changed = True
    me['bg']='gray'
    informLater(300,me,'color',True)

enable_flag = [False]

def show_config(msg,onflag = enable_flag, cont = container(),thisframe=widget("Frame"),color_action = do_color_action,text_color = do_text_color,color_button = create_color_button,e_event=entry_event,lbox_select=listbox_selection,wcanvas = widget('Canvas'),no_refresh=undo_refresh,geo_refresh=geometry_refresh):
    if isinstance(msg,bool):
        if msg:
            if not onflag[0]:
                onflag[0] = True
                send('SHOW_CONFIG',this()) # resend message once more
        elif onflag[0]: #if shall switch off and SHOW_LAYOUT is on
            onflag[0]=False # switch flag to off
            no_refresh()
            cont.unlayout() # and unlayout the DetailedLayout frame
    elif onflag[0]: # a correct message arrived and show layout is on
        # reset references for value refresh  to not active
        if msg.hasConfig:

            no_refresh()
            current_selection = Selection() # save current selection
            cont.grid()
            setWidgetSelection(msg) # set selection for current user widget
            maxlen = 0
            confdict = getconfdict()
            for entry in confdict: maxlen = max(maxlen,len(entry))
            # make a list of tuples of the layout dictionary and sort important options at the beginning
            conflist = []
            for entry in (
"title",
"geometry",
"from", # Spinbox (decimal default 0.0)
"to",   # Spinbox, Scale (decimal Spinbox default 0,0, Scale default 100.0)
"increment", # Spinbox, (decimal default 1.0)
"resolution", # Scale (decimal default 1.0)
"bigincrement", # Scale (decimal default 0.0)
"showvalue",
"tickinterval", # Scale (decimal default 0.0)
"digits", # Scale (Integer default 0)
"orient",
"label",
"text",
"link",
"selectmode",
"state",
"underline",
"default",
"relief",
"sliderrelief",
"overrelief",
"buttondownrelief",
"width",
"height",
"length",
"sliderlength",
"wraplength",
"padx", # often (Label: Integer default 0, Button ? default 3m)
"pady", # often (Label: Integer default 0, Button ? default 1m)
"bd",
"anchor",
"justify",
"font",
"fg",
"bg",
"background",
"troughcolor",
"selectforeground",
"selectbackground",
"insertwidth",
"insertborderwidth",
"insertontime",
"selectborderwidth",
"activeforeground",
"activebackground",
"disabledforeground",
"disabledbackground",
"highlightcolor",
"highlightbackground",
"highlightthickness",
"sashrelief",
"sashwidth",
"sashpad",
"opaqueresize",
"sashcursor",
"showhandle",
"handlesize",
"handlepad",
"takefocus",
"cursor"
):
                if entry in confdict: conflist.append((entry,confdict.pop(entry)))
            for confname,entry in confdict.items():conflist.append((confname,entry))
            # now delete all widgets in frame LayoutOptions and set selection to this frame
            deleteAllWidgets(thisframe) # Frame
            setWidgetSelection(thisframe,thisframe)

            for entry in conflist:
                # for each option, we make a frame an in this frame a label with the option name and an entry
                # for showing and changing the value
                Frame()
                goIn()
                Label(text=entry[0],width=maxlen,anchor=E).rcgrid(0,0)
                if entry[0] == "text": Text("Entry", height=3, width=20, font="TkDefaultFont").insert(END,entry[1])			
                elif entry[0] in (
"digits", # Scale (Integer default 0)
"width", # often (Integer default 0)
"height", # often (Integer default 0)
"length", # Spinbox (Integer default 100)
"sliderlength", # Spinbox (Integer default 30)
"wraplength", # often (Integer default 0)
"bd", # often (Integer default 1)
"insertwidth", # Entry (Integer default 2)
"insertborderwidth", # Entry (Integer default 0)
"selectborderwidth", # Entry (Integer default 0)
"highlightthickness",
"sashwidth", # PanedWindow (Integer default 3)
"sashpad", # PanedWindow (Integer default 0)
"opaqueresize", # PanedWindow (Integer default 1)
"handlesize", # PanedWindow (Integer default 8)
"handlepad"): # PanedWindow (Integer default 8)
                    Spinbox("Entry",from_=0,to=3000,increment=1)
                    do_command(e_event,wishWidget=True) # via return key the option value can be changed
                elif entry[0] == "insertontime":
                    Spinbox("Entry",from_=0,to=10000,increment=10)
                    do_command(e_event,wishWidget=True) # via return key the option value can be changed
                elif entry[0] == "underline":
                    Spinbox("Entry",from_=-1,to=300,increment=1)
                    do_command(e_event,wishWidget=True) # via return key the option value can be changed
                else: Entry("Entry").insert(0,entry[1])

                do_action('color',color_action,wishWidget=True,wishMessage=True)
                rcgrid(0,1,sticky=E+W)
                this().mydata=entry[0] # mydata shall also contain the option name


                if entry[0] == "text": do_event("<Return>",text_color,None,True)
                elif entry[0] in ("command","vcmd","invcmd","variable","textvariable","menu"): config(state = "readonly")
                elif (entry[0] in ["fg","bg"]) or ("foreground" in entry[0]) or ("background" in entry[0]) or ("color" in entry[0]):
                    color_button(this())
                    widget("Entry").do_event("<Return>",e_event,this(),True)
                else:
                    do_event("<Return>",e_event,None,True)


                    if entry[0] == 'geometry':
                        thisframe.mydata = [this(),None,None,None,msg]
                        msg.do_action('refresh',geo_refresh,thisframe,True)
                        inform(msg,'refresh')

                    elif entry[0] == 'height': thisframe.mydata[2] = this()
                    elif entry[0] == 'width': thisframe.mydata[3] = this()

                    elif entry[0] == "state":
                        if isinstance(msg,Spinbox) or isinstance(msg,Entry) : Listbox(width=8,height=3).fillList(("normal","disabled","readonly"))
                        elif isinstance(msg,Text) or isinstance(msg,Canvas): Listbox(width=8,height=2).fillList(("normal","disabled"))
                        else: Listbox(width=8,height=3).fillList(("normal","disabled","active"))
                        lbox_select()

                    elif entry[0] == "default":
                        Listbox(width=7,height=2).fillList(("active","disabled"))
                        lbox_select()

                    elif entry[0] in ["relief","buttonuprelief","sashrelief"]:
                        Listbox(width=7,height=6).fillList(("flat","raised","sunken","groove","ridge","solid"))
                        lbox_select()

                    elif entry[0] =="overrelief":
                        Listbox(width=7,height=7).fillList(("","flat","raised","sunken","groove","ridge","solid"))
                        lbox_select()

                    elif entry[0] =="anchor":
                        Listbox(width=7,height=9).fillList(("center","n","ne","e","se","s","sw","w","nw"))
                        lbox_select()

                    elif entry[0] =="justify":
                        Listbox(width=7,height=3).fillList(("center","left","right"))
                        lbox_select()

                    elif entry[0] =="compound":
                        Listbox(width=7,height=6).fillList(("none","center","left","right","top","bottom"))
                        lbox_select()

                    elif entry[0] =="selectmode":
                        Listbox(width=8,height=4).fillList(("browse","single","multiple","extended"))
                        lbox_select()

                    elif entry[0] =="tabstyle":
                        Listbox(width=13,height=2).fillList(("tabular","wordprocessor"))
                        lbox_select()

                    elif entry[0] =="orient":
                        Listbox(width=10,height=2).fillList(("vertical","horizontal"))
                        lbox_select()

                    elif entry[0] =="showhandle":
                        Listbox(width=4,height=2).fillList(("0","1"))
                        lbox_select()

                goOut() # leaving the frame for the option entry and pack it
                pack(fill=X)

            setSelection(current_selection)
            wcanvas.yview_moveto(0)

        else:
            cont.unlayout() # if the widget doesn't have a config, then disable value refresh and hide the layout options
            no_refresh()
    

do_receive('SHOW_CONFIG',show_config,wishMessage=True)

### ========================================================
