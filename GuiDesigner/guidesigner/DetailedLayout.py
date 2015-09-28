LabelFrame("LayoutOptions",text="Layout Options").pack(anchor=N)

### CODE ===================================================

Lock()

# -------------- this LabelFrame contains data for a layout value refresh ---------------------

# the data reference Entries for x,y,row,column,side, and index depending an the layout type
this().mydata=[None,None,None,None,None,None]

# -------------- receiver for message 'LAYOUT_VALUES_REFRESH' ---------------------

def values_refresh(widget = widget("LayoutOptions")):
    mydata = widget.mydata
    if mydata[0] != None:
        mydata[0].delete(0,END)	
        mydata[0].insert(0,getlayout("x"))
    if mydata[1] != None:
        mydata[1].delete(0,END)	
        mydata[1].insert(0,getlayout("y"))
    if mydata[2] != None:
        mydata[2].delete(0,END)	
        mydata[2].insert(0,getlayout("row"))
    if mydata[3] != None:
        mydata[3].delete(0,END)	
        mydata[3].insert(0,getlayout("column"))
    if mydata[4] != None:
        mydata[4].delete(0,END)	
        mydata[4].insert(0,getlayout("side"))
    if mydata[5] != None:
        mydata[5].delete(0,END)	
        mydata[5].insert(0,getlayout("index"))

do_receive('LAYOUT_VALUES_REFRESH',values_refresh)

# -------------- receiver for message 'SHOW_LAYOUT' - help functions ------------------------------------

# another help function: for layout option sticky we show an info message box


# for Return key or mouse klick: get active selection from the listbox, hide the listbox, set the layout and insert the text in the Entry for showing

def do_lbox_click(event,lbox,entry,isMouse):
    if isMouse: text = lbox.get(lbox.nearest(event.y))
    else: text = lbox.get(ACTIVE)
    setlayout(entry.mydata,text)
    entry.delete(0,END)
    entry.insert(0,text)
    lbox.unbind("<Return>")
    lbox.unbind("<Button-1>")
    lbox.unlayout()

def listbox_helpbutton(lbox,entry,lbox_click = do_lbox_click):
    lbox.select_clear(0,END) # clear a former listbox selection 
    lbox_index = lbox.getStringIndex(getlayout(entry.mydata)) # get the listbox index for the layout option
    lbox.select_set(lbox_index) # preselect the current layout option in the listbox
    lbox.activate(lbox_index) # and set the selection cursor to it
    lbox.rcgrid(0,3) # show the listbox
    lbox.focus_set() # and focus it
    lbox.do_event("<Return>",lbox_click,(lbox,entry,False),wishEvent=True)  # bind Return key to the listbox
    lbox.do_event("<Button-1>",lbox_click,(lbox,entry,True),wishEvent=True)  # bind mouse click to the listbox

def listbox_selection(helpbutton = listbox_helpbutton):
    Button(text="?").rcgrid(0,2) # create a help button for showing the listbox
    do_command(helpbutton,(widget("Listbox"),widget("Entry")))

# -------------- receiver for message 'SHOW_LAYOUT' ------------------------------------


def entry_event(me):
    setlayout(me.mydata,me.get())
    me.delete(0,END)
    me.insert(0,str(getlayout(me.mydata)))
    me['bg']='gray'
    informLater(300,me,'color')
    send("LAYOUT_OPTIONS_CHANGED",this())

enable_flag = [False]

def show_layout(msg,onflag = enable_flag, cont = container(),thisframe=widget("LayoutOptions"),e_event=entry_event,lbox_select=listbox_selection):
    if isinstance(msg,bool):
        if msg:
            if not onflag[0]:
                onflag[0] = True
                send('SHOW_LAYOUT',this()) # resend message once more
        
        elif onflag[0]: #if shall switch off and SHOW_LAYOUT is on
            onflag[0]=False # switch flag to off
            cont.unlayout() # and unlayout the DetailedLayout frame
            thisframe.mydata=[None,None,None,None,None,None] # set references for value refresh  to not active
    elif onflag[0]: # a correct message arrived and show layout is on
        # reset references for value refresh  to not active
        thisframe.mydata = [None,None,None,None,None,None]
        # if the widget has a layout, then show it
        if msg.Layout & LAYOUTALL:
            current_selection = Selection() # save current selection
            cont.grid()			

            setWidgetSelection(msg) # set selection for current user widget
            maxlen = 0
            linfo = layout_info()
            for entry in linfo: maxlen = max(maxlen,len(entry))

            # make a list of tuples of the layout dictionary and sort important options at the beginning
            layoutlist = []
            for entry in (
"x",
"y",
"column",
"row",
"side",
"sticky",
"columnspan",
"rowspan",
"width",
"height",
"anchor",
"fill",
"expand",
"bordermode",
"padx",
"pady",
"ipadx",
"ipady",
"relx",
"rely",
"relwidth",
"relheight"):
                if entry in linfo: layoutlist.append((entry,linfo.pop(entry)))
            for layoutname,entry in linfo.items():layoutlist.append((layoutname,entry))
            # now delete all widgets in frame LayoutOptions and set selection to this frame
            deleteAllWidgets(thisframe) # Frame
            setWidgetSelection(thisframe,thisframe)

            for entry in layoutlist:
                # for each option, we make a frame an in this frame a label with the option name and an entry
                # for showing and changing the value
                Frame()
                goIn()
                Label(text=entry[0],width=maxlen,anchor=E).rcgrid(0,0)
                Entry("Entry")
                do_action('color',lambda me = this(): me.config(bg='white'))
                this().delete(0,END)	
                this().insert(0,entry[1])
                rcgrid(0,1,sticky=E+W)
                this().mydata=entry[0] # mydata shall also contain the option name

                do_event("<Return>",e_event,wishWidget=True) # via return key the option value can be changed

                # reference update for a value refresh without new show layout option creation
                if entry[0] == "x": thisframe.mydata[0]=this()
                elif entry[0] == "y": thisframe.mydata[1]=this()
                elif entry[0] == "row": thisframe.mydata[2]=this()
                elif entry[0] == "column": thisframe.mydata[3]=this()
                elif entry[0] == "side": thisframe.mydata[4]=this()
                elif entry[0] == "index": thisframe.mydata[5]=this()

                # listboxes and readonly state for some options
                if entry[0] =="side":
                    Listbox(width=7,height=4).fillList(("top","bottom","left","right"))
                    lbox_select()

                elif entry[0] =="anchor":
                    Listbox(width=7,height=9).fillList(("nw","n","ne","e","se","s","sw","w","center"))
                    lbox_select()

                elif entry[0] =="in": this().config(state="readonly")
                elif entry[0] =="fill":
                    Listbox(width=4,height=4).fillList(("none","x","y","both"))
                    lbox_select()

                elif entry[0] =="bordermode":
                    Listbox(width=7,height=3).fillList(("inside","outside","ignore"))
                    lbox_select()

                # help info message box for sticky option
                elif entry[0] =="sticky":
                    Button(text="?").rcgrid(0,2)
                    do_command(lambda par = this(): messagebox.showinfo("Layout option 'sticky'","The 'sticky' option may be empty or may contain one or more of these characters: 'n' 'e' 'w' 's'",parent=par))

                goOut() # leaving the frame for the option entry and pack it
                pack(fill=X)

            setSelection(current_selection)

        else:   # if the widget doesn't have a layout, then disable value refresh and hide the layout options
            cont.unlayout()
            thisframe.mydata=[None,None,None,None,None,None]


do_receive('SHOW_LAYOUT',show_layout,wishMessage = True)

### ========================================================
