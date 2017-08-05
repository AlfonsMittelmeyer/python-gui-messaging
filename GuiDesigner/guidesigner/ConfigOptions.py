Scrollbar('Scrollbar',orient=VERTICAL)
Canvas('Canvas',bd=0,highlightthickness=0)
goIn()
Frame('Frame')
goIn()

### CODE ===================================================

my_frame = container()
my_canvas = my_frame.master


def main():
    import os

    about_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/about.gif')
    #color_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/graphics.gif')
    edit_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/edit-select-all.gif')
    help_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/help16.gif')
    sticky_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/sticky.gif')
    labelanchor_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/labelanchor.gif')
    font_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/format-text-bold16.gif')
    justify_left_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/format-justify-left16.gif')
    justify_right_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/format-justify-right16.gif')
    justify_center_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/format-justify-center16.gif')
    insert_image_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/insert-image16.gif')
    compound_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/view-fullscreen16.gif')
    Lock()

    my_frame = container()
    my_canvas = my_frame.master
    config_frame = my_canvas.master


    class ToggleButton(Label):

        def __init__(self,name,option):
            Label.__init__(self,name,bg = '#ffa000', activebackground = 'lightgreen',width=3)
            self.option = option
            self.bind('<Button-1>',self.toggle)
            

        def show_value(self):
            if self.value:
                self['state'] = 'active'
                self['relief'] = 'sunken'
                self['text'] = '1'
            else:
                self['state'] = 'normal'
                self['relief'] = 'raised'
                self['text'] = '0'

        def set(self,value):
            if not value:
                self.value = 0
            elif isinstance(value,str):
                self.value = int(value)
                
            self.show_value()

        def toggle(self,event):
            self.value = not self.value
            this().setconfig(self.option,self.value)
            self.show_value()
            if self.option == 'tearoff':
                send('CHECK_TEAROFF')
                if not self.value:

                    selection_before = Selection()
                    children = this().Dictionary.getChildrenList()
                    for child in children:
                        if isinstance(child,MenuDelimiter):
                            child.destroy()
                    setSelection(selection_before)

                if this() == container():
                    send('REFRESH_INDEX_ORDER')

    RefDict = {}

    class RefEntry:

        def __init__(self,entry,option):
            self.option = option
            self.color_button = None

            if isinstance(entry,ToggleButton):
                self.variable = entry
            elif isinstance(entry,Text):
                self.variable = self
                self.entry = entry
            else:
                self.variable = StringVar()
                entry['textvariable'] = self.variable

        def update(self):
            value = this().getconfig(self.option)
            self.variable.set(get_entry_as_string(value))
            if self.color_button:
                self.color_button['bg'] = value if value else self.color_button_bg

        def colorbutton(self,button,bg):
            self.color_button = button
            self.color_button_bg = bg

        def set(self,value):
            self.entry.delete(1.0, END)
            self.entry.insert(END,value)
            
    def ref_entry(entry,option):
        RefDict[option] = RefEntry(entry,option)


    def set_color_button(option,button,bg):
        RefDict[option].colorbutton(button,bg)
        

    def can_update(config):
        if len(RefDict) != len(config): return False
        for entry in config:
            if entry not in RefDict: return False
        for entry in config:
            RefDict[entry].update()
        return True

    def geometry_refresh():
        if 'geometry' in RefDict:
            if this().hasConfig:
                RefDict['geometry'].update()
            my_frame.after(200,geometry_refresh)


    '''
    interior_id = my_canvas.create_window(0, 0, window=my_frame,anchor=NW)


    # -------------- <Configure> events for the scrollbar frame ------------------------------------

    def canvas_configure(me,frame,int_id = interior_id):
        if me.winfo_reqwidth() != frame.winfo_width(): me.itemconfigure(int_id, width=me.winfo_width())
     
    my_canvas.do_event("<Configure>",canvas_configure,my_frame,True)

    def frame_configure(me,canvas):
        canvas.config(scrollregion="0 0 %s %s" % (me.winfo_reqwidth(), me.winfo_reqheight()))
        if me.winfo_reqwidth() > canvas.winfo_width(): canvas.config(width=me.winfo_reqwidth())
        if me.winfo_reqheight() > 340: canvas.config(height=340)
        else: canvas.config(height=me.winfo_reqheight())

    my_frame.do_event("<Configure>",frame_configure,my_canvas,True)
    '''
    # -------------- receivers for SELECTION_CHANGED and CREATE_WIDGET_DONE messages -----------

    # in both cases an internal 'SHOW_CONFIG' message will be sent
    do_receive('SELECTION_CHANGED',lambda: send("SHOW_CONFIG",this()))

    # -------------- receiver for message 'SHOW_CONFIG' - help functions ------------------------------------

    justify_var = StringVar()


    def justify_button(entry,justify_left_gif = justify_left_gif, justify_right_gif = justify_right_gif,justify_center_gif = justify_center_gif,justify_var = justify_var):

        def set_justify():
            this()['justify'] = justify_var.get()
            entry.delete(0,'end')
            entry.insert(0,justify_var.get())
            
        Menubutton('justify',**{'font': 'TkMenuFont 10 {}', 'bg': 'white', 'text': '?'})
        goIn()

        Menu('menu',**{'activebackground': '#7bfeff', 'tearoff': 0, 'bg': 'white', 'activeforeground': 'black', 'fg': 'black', 'relief': 'solid'})
        goIn()

        MenuItem('center','radiobutton',**{'label': 'center', 'compound': 'left', 'value': 'center'})
        MenuItem('left','radiobutton',**{'label': 'left', 'compound': 'left', 'value': 'left'})
        MenuItem('right','radiobutton',**{'label': 'right', 'compound': 'left', 'value': 'right'})


        widget('left').config(image = justify_left_gif,variable = justify_var,command = set_justify)
        widget('center').config(image = justify_center_gif,variable = justify_var,command = set_justify)
        widget('right').config(image = justify_right_gif,variable = justify_var,command = set_justify)

        widget('left').layout(index=1)
        widget('center').layout(index=2)
        widget('right').layout(index=3)


        goOut()
        select_menu()

        goOut()
        this()['image'] = justify_left_gif
        

    def choose_bitmap(entry,title,root=widget('/'),os=os):

        file_opt = {
            'filetypes' : [('Graphics Interchange Format', '.gif'),('Portable Pixmap', '.ppm'),('Portable Graymap','.pgm'),('all files', '*')],
            'filetypes' : [('all files', '*')],
            'parent' : root,
            'title' : title,
            'initialdir' : os.path.join(os.getcwd(),'Bitmaps') }

        filename = tkFileDialog.askopenfilename(**file_opt)
        if filename:
            filename = os.path.relpath(filename)
            filename = filename.replace('\\','/')
            setconfig(entry.mydata,'@'+filename)
            entry.delete(0,END)	
            entry.insert(0,getconfig(entry.mydata))

    # for Return key or mouse klick: get active selection from the listbox, hide the listbox, set the layout and insert the text in the Entry for showing

    def do_lbox_click(event,lbox,entry,isMouse,choose_bitmap=choose_bitmap):
        if isMouse: text = lbox.get(lbox.nearest(event.y))
        else: text = lbox.get(ACTIVE)
        if text == '@file':
            choose_bitmap(entry,entry.mydata)
        elif text!='<=':
            setconfig(entry.mydata,text)
            entry.delete(0,END)
            entry.insert(0,text)
            if entry.mydata == 'tearoff':
                send('REFRESH_INDEX_ORDER')

        lbox.unbind("<Return>")
        lbox.unbind("<Button-1>")
        lbox.unlayout()

    def listbox_helpbutton(grid_row,lbox,entry,lbox_click = do_lbox_click):
        lbox.select_clear(0,END) # clear a former listbox selection 
        try:
            lbox_index = lbox.getStringIndex(getconfig(entry.mydata)) # get the listbox index for the layout option
        except ValueError:
            lbox_index =0
        lbox.select_set(lbox_index) # preselect the current layout option in the listbox
        lbox.activate(lbox_index) # and set the selection cursor to it
        lbox.rcgrid(grid_row,3) # show the listbox
        lbox.focus_set() # and focus it
        lbox.do_event("<Return>",lbox_click,(lbox,entry,False),wishEvent=True)  # bind Return key to the listbox
        lbox.do_event("<Button-1>",lbox_click,(lbox,entry,True),wishEvent=True)  # bind mouse click to the listbox

    def listbox_selection(grid_row,image_par=None,helpbutton = listbox_helpbutton,about_gif = about_gif):
        image = about_gif if not image_par else image_par
        if not image_par:
            Button(pady=1,padx=1,image=image,bg='blue',text="?").rcgrid(grid_row,2) # create a help button for showing the listbox
        else:
            Button(pady=1,padx=1,image=image,text="?").rcgrid(grid_row,2) # create a help button for showing the listbox
        do_command(helpbutton,(grid_row,widget("listbox"),widget("Entry")))

    def listbox_bitmap_selection(grid_row,helpbutton = listbox_helpbutton,about_gif = about_gif):
        Button(pady=1,padx=1,bitmap='@guidesigner/images/icon',text="?").rcgrid(grid_row,2) # create a help button for showing the listbox
        do_command(helpbutton,(grid_row,widget("listbox"),widget("Entry")))

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

    def create_color_button(grid_row,entry,sel_color = select_color,about_gif = about_gif):
        Button(pady=1,padx=1,image=about_gif,text="?").rcgrid(grid_row,2)
        bg = this()['bg']
        setconfig('bg',entry.get()) # the color of the button shall be the currently shown color value in the entry field
        do_command(sel_color,entry,True) # command for the button
        return bg

    # -------------- receiver for message 'SHOW_CONFIG'  ------------------------------------

    def do_color_action(me,msg):
        me['bg'] = 'white'
        if msg:
            me.delete(0,END)
            me.insert(0,get_entry_as_string(getconfig(me.mydata)))

    def do_text_color(me):
        setconfig(me.mydata,me.get("1.0",'end-1c'))
        me['bg']='gray'
        informLater(300,me,'color',False)

    def entry_event(me,button=None,bg=None,justify_var = justify_var):
        setconfig(me.mydata,me.get())

        if button != None:
            value = getconfig(me.mydata)
            if not value:
                value = bg
            button.setconfig('bg',value)
            
        if me.mydata == 'tearoff':
            send('REFRESH_INDEX_ORDER')
        elif me.mydata == 'justify':
            justify_var.set(this()['justify'])
        me['bg']='gray'
        informLater(300,me,'color',True)

    enable_flag = [False,False,False]


    def choose_image(entry,title,root=widget('/'),os=os):

        file_opt = {
            'defaultextension' : '.gif',
            'filetypes' : [('Graphics Interchange Format', '.gif'),('Portable Pixmap', '.ppm'),('Portable Graymap','.pgm'),('all files', '*')],
            'parent' : root,
            'title' : title,
            'initialdir' : os.path.join(os.getcwd(),'Images') }

        filename = tkFileDialog.askopenfilename(**file_opt)
        if filename:
            filename = os.path.relpath(filename)
            filename = filename.replace('\\','/')
            setconfig(entry.mydata,filename)
            entry.delete(0,END)	
            entry.insert(0,getconfig(entry.mydata))



    def show_config(
        msg,
        onflag = enable_flag,
        cont = config_frame,
        thisframe=my_frame,
        color_action = do_color_action,
        text_color = do_text_color,
        color_button = create_color_button,
        e_event=entry_event,
        lbox_select=listbox_selection,
        wcanvas = my_canvas,
        geo_refresh=geometry_refresh,
        choose_image=choose_image,
        about_gif = about_gif,
        edit_gif = edit_gif,
        help_gif = help_gif,
        sticky_gif = sticky_gif,
        labelanchor_gif = labelanchor_gif,
        font_gif = font_gif,
        justify_left_gif = justify_left_gif,
        justify_var = justify_var,
        justify_button = justify_button,
        insert_image_gif = insert_image_gif,
        lbox_bitmap_select = listbox_bitmap_selection,
        compound_gif = compound_gif,
        ToggleButton = ToggleButton,
        ):

        if isinstance(msg,bool):
            if msg:
                if not onflag[0]:
                    onflag[0] = True
                    send('SHOW_CONFIG',this()) # resend message once more
            elif onflag[0]: #if shall switch off and SHOW_LAYOUT is on
                onflag[0]=False # switch flag to off
                cont.unlayout() # and unlayout the DetailedLayout frame
                if 'geometry' in RefDict:
                    RefDict.clear() # should not refresh geometry

        elif type(msg) is tuple: # temporarily don't show

            if msg[1]: # set on [0], if shall show [1]
                onflag[0] = onflag[1]
                onflag[2] = False # was not set off temporarily
                selection_before = Selection()
                setWidgetSelection(my_frame)
                widget('/','GuiFrame','HideConfigOptions').lower()
                setSelection(selection_before)

            else: # set off 0, 
                if not onflag[2]: # if not set off temporarily
                    onflag[1] = onflag[0] # save on off state

                    selection_before = Selection()
                    setWidgetSelection(my_frame)
                    widget('/','GuiFrame','HideConfigOptions').lift()
                    setSelection(selection_before)

                onflag[0] = False
                onflag[2] = True # was set off temporarily

                #RefDict.clear()
                # why this? container shall be shown, but without content
                # isn't there a better way than:
                #deleteAllWidgets(thisframe) 


        elif onflag[0]: # a correct message arrived and show layout is on
            # reset references for value refresh  to not active
            if msg.hasConfig:

                current_selection = Selection() # save current selection
                selected_widget = this()
                cont.grid()
                setWidgetSelection(msg) # set selection for current user widget
                confdict = getconfdict()
                if can_update(confdict):
                    setSelection(current_selection)
                    return
                RefDict.clear()
                if 'geometry' in confdict:
                    thisframe.after(100,geometry_refresh)

                # make a list of tuples of the layout dictionary and sort important options at the beginning
                conflist = []
                for entry in (
    '@orientation',
    "orient",

    '@text, label, menu title',
    "text",
    "label",
    'menu title',
    "underline",
    "accelerator",


    '@special options',
    "fill by text",
    "title",
    "geometry",
    'minsize',
    'maxsize',
    'resizable',

    '@font, anchor, justify ...',
    "font",
    "anchor",
    "labelanchor",
    "justify",
    "aspect",
    "wraplength",

    '@images und bitmaps',
    "photoimage",
    "selectphotoimage",
    "tristatephotoimage",
    "activephotoimage",
    "disabledphotoimage",
    'bitmap',
    'activebitmap',
    'disabledbitmap',
    "compound",


    '@width, height, length, padding',
    "width",
    "height",
    "length",
    "sliderlength",
    "padx", # often (Label: Integer default 0, Button ? default 3m)
    "pady", # often (Label: Integer default 0, Button ? default 1m)
    "padding",


    '@foreground and background',
    "fg",
    "bg",
    "foreground",
    "background",
    "buttonbackground",
    "troughcolor",
    "selectcolor",
    "selectforeground",
    "selectbackground",
    "inactiveselectbackground",
    "activeforeground",
    "activebackground",
    "disabledforeground",
    "disabledbackground",
    'readonlybackground',

    '@state, border, relief',
    "state",
    "default",
    "bd",
    "borderwidth",
    "elementborderwidth",
    "selectborderwidth",
    "activeborderwidth",
    "relief",
    "activerelief",
    "overrelief",
    "buttonuprelief",
    "buttondownrelief",
    "sliderrelief",
    "offrelief",



    "@widget special",
    'show', # Listbox, Combobox
    "columns",  # Treeview
    "displaycolumns", # Treeview

    "mode", # Progressbar
    "maximum", # Progressbar

    "hidemargin",
    "columnbreak",
    "direction",
    "tearoff",
    "jump",
    "wrap",
    'setgrid',
    'autoseparators',
    "tabstyle",
    "tabs",
    "spacing1",
    "spacing2",
    "spacing3",
    "startline",
    "endline",
    'undo',
    'maxundo',



    "activestyle",
    "tags",
    "from", # Spinbox (decimal default 0.0)
    "to",   # Spinbox, Scale (decimal Spinbox default 0,0, Scale default 100.0)
    "increment", # Spinbox, (decimal default 1.0)
    "resolution", # Scale (decimal default 1.0)
    "bigincrement", # Scale (decimal default 0.0)
    "showvalue",
    "digits", # Scale (Integer default 0)


    # Checkbutton, Radiobutton, Listbox ----------
    "indicatoron", #Checkbutton
    "onvalue",
    "offvalue",
    "tristatevalue",


    # Listbox, Text 
    "format", # Spinbox
    "selectmode",
    'exportselection',
    'validate',



    # --------------



    "type",
    'style',
    'start',
    'extent',
    'arrow',
    'arrowshape',
    'capstyle',
    'joinstyle',
    'smooth',
    'splinesteps',
    "outline",
    "dash",
    "dashoffset",
    "outlinestipple",
    "outlineoffset",
    "fill",
    "stipple",
    "offset",
    "activewidth",
    "activeoutline",
    "activeoutlineoffset",
    "activedash",
    "activeoutlinestipple",
    "activefill",
    "activestipple",
    "disabledwidth",
    "disabledoutline",
    "disabledoutlineoffset",
    "disableddash",
    "disabledoutlinestipple",
    "disabledfill",
    "disabledstipple",
    "opaqueresize",
    "sashrelief",
    "sashwidth",
    "sashpad",
    "sashcursor",
    "showhandle",
    "handlesize",
    "handlepad",

    # Canvas
    'confine',
    'closeenough',
    'scrollregion',
    'xscrollincrement',
    'yscrollincrement',


    '@values, variables, commands, etc',
    "value",
    "values",
    "phase",
    "variable",
    "listvariable",
    "textvariable",
    "labelwidget",
    "menu",
    "window",
    "command",
    "vcmd",
    "invcmd",
    "xscrollcommand",
    "yscrollcommand",
    "tearoffcommand",
    "postcommand",

    '@cursor and focus',
    "blockcursor",
    'insertunfocussed',
    "insertwidth",
    'insertbackground',
    "insertborderwidth",
    "cursor",
    "buttoncursor",
    "takefocus",
    "highlightthickness",
    "highlightcolor",
    "highlightbackground",

    '@delays and intervals',
    'repeatinterval',
    'repeatdelay',
    "insertontime",
    "insertofftime",
    "tickinterval", # Scale (decimal default 0.0)




    # Export
    '@export',
    "myclass",
    "baseclass",
    "call Code(self)",
    "methods",

    # DynTkInter
    '@DynTkInter',
    "link",

    '@other',
    ):
                    if entry[0] == '@':
                        conflist.append(entry)
                    elif entry == 'wraplength':
                        if entry in confdict:
                            conflist.append((entry,confdict.pop(entry)))
                        elif isinstance(selected_widget,Message):
                            conflist.append(('width',confdict.pop('width')))
                    elif entry == 'menu title' and isinstance(selected_widget,Menu):
                        conflist.append(('title',confdict.pop('title')))
                    elif entry in confdict:
                        conflist.append((entry,confdict.pop(entry)))
                for confname,entry in confdict.items():conflist.append((confname,entry))
                # now delete all widgets in frame LayoutOptions and set selection to this frame
                deleteAllWidgets(thisframe) # Frame
                setWidgetSelection(thisframe,thisframe)

                if isinstance(selected_widget,MenuItem):
                    text = "menu item: " +  selected_widget.mytype
                elif isinstance(selected_widget,MenuDelimiter):
                    text = "menu tearoff"

                elif isinstance(selected_widget,CanvasItemWidget):
                    text = "canvas item: " + selected_widget.master.type(selected_widget.item_id)


                else:
                    a = str(type(selected_widget))
                    b = a.split("'")
                    c = b[1]
                    d = c.split(".")
                    e = 'ttk.'+d[1] if d[0] == 'DynTtk' else d[1]
                    text = 'class '+e

                grid_row = 0

                Label('Label',bg='blue',fg='yellow',font = 'TkDefaultFont 12 bold',text=text,padx=0)
                rcgrid(grid_row,0,columnspan=3,sticky='we')
                grid_row += 1
                ttk.Separator('separator')
                rcgrid(grid_row,0,columnspan=3,sticky='we')
                grid_row += 1
                for index,entry in enumerate(conflist):
                    # for each option, we make a frame an in this frame a label with the option name and an entry
                    # for showing and changing the value
                    if entry[0] == '@':
                        if index != len(conflist)-1 and conflist[index+1][0] != '@':
                            Label('Label',bg='blue',fg='white',font = 'TkDefaultFont 10 bold',text = entry[1:],padx=0)
                            rcgrid(grid_row,0,columnspan=3,sticky='we')
                            grid_row+=1
                            
                        continue

                    Label(text=entry[0]).rcgrid(grid_row,0,sticky='e')
                    
                    if entry[0] in ("text","fill by text","methods"):
                        Button(pady=1,padx=1,image=edit_gif,text="+",bg='blue').rcgrid(grid_row,2)
                        do_command(lambda entry = entry[0]: DynAccess('guidesigner/text_edit.py',(this(),entry)))
                        Text("Entry", height=3, width=20, font="TkDefaultFont")
                    elif entry[0] in (

    "startline", # Text
    "endline", # Text
    "digits", # Scale (Integer default 0)
    "width", # often (Integer default 0)
    "borderwidth", # often (Integer default 0)
    "elementborderwidth", # often (Integer default 0)
    "padding", # often (Integer default 0)
    "activewidth", # often (Integer default 0)
    "disabledwidth", # often (Integer default 0)
    "height", # often (Integer default 0)
    "length", # Spinbox (Integer default 100)
    "sliderlength", # Spinbox (Integer default 30)
    "wraplength", # often (Integer default 0)
    "bd", # often (Integer default 1)
    "padx", # often (Label: Integer default 0, Button ? default 3m)
    "pady", # often (Label: Integer default 0, Button ? default 1m)
    "insertwidth", # Entry (Integer default 2)
    "insertborderwidth", # Entry (Integer default 0)
    "activeborderwidth", # Menu
    "selectborderwidth", # Entry (Integer default 0)
    "highlightthickness",
    "sashwidth", # PanedWindow (Integer default 3)
    "sashpad", # PanedWindow (Integer default 0)
    "handlesize", # PanedWindow (Integer default 8)
    "aspect", # Message
    "handlepad",  # PanedWindow (Integer default 8)
    "maximum", # Progressbar

    ):
                        Spinbox("Entry",from_=0,to=3000,increment=1)
                        do_command(e_event,wishWidget=True) # via up and down buttons the option value can be changed
                    elif entry[0] in ("insertontime",'insertofftime'):
                        Spinbox("Entry",from_=0,to=10000,increment=10)
                        do_command(e_event,wishWidget=True) # via up and down buttons the option value can be changed
                    elif entry[0] in ("spacing1",'spacing2','spacing3'):
                        Spinbox("Entry",from_=0,to=10000,increment=1)
                        do_command(e_event,wishWidget=True) # via up and down buttons the option value can be changed
                    elif entry[0] == "underline":
                        Spinbox("Entry",from_=-1,to=300,increment=1)
                        do_command(e_event,wishWidget=True) # via up and down buttons the option value can be changed
                    elif entry[0] == "maxundo":
                        Spinbox("Entry",from_=-1,to=10000,increment=1)
                        do_command(e_event,wishWidget=True) # via up and down buttons the option value can be changed
                    elif entry[0] in ("showhandle","blockcursor","setgrid",'autoseparators','undo','exportselection','jump','tearoff',"hidemargin","columnbreak",'opaqueresize','indicatoron'):
                        ToggleButton('Entry',entry[0]).rcgrid(grid_row,1,sticky=W,padx=1)
                    elif entry[0] == 'takefocus' and 'DynTtk' not in str(type(selected_widget)):
                        ToggleButton('Entry',entry[0]).rcgrid(grid_row,1,sticky=W,padx=1)
                    else: 
                        Entry("Entry")

                    ref_entry(this(),entry[0]) 

                    if not isinstance(this(),ToggleButton):
                        do_action('color',color_action,wishWidget=True,wishMessage=True)
                        rcgrid(grid_row,1,sticky=E+W)
                        this().mydata=entry[0] # mydata shall also contain the option name


                    if entry[0] in ("text",'fill by text','methods'): do_event("<Return>",text_color,None,True)
                    elif entry[0] in ("command","vcmd","invcmd","variable","textvariable","menu","window","xscrollcommand",'yscrollcommand','labelwidget','tearoffcommand','postcommand','phase'):
                        config(state = "readonly")
                    elif (entry[0] in ["fg","bg","outline","activeoutline","disabledoutline"]) or ("foreground" in entry[0]) or ("background" in entry[0]) or ("color" in entry[0]) or ("fill" in entry[0]):
                        bg = color_button(grid_row,this())
                        set_color_button(entry[0],this(),bg)
                        widget("Entry").do_event("<Return>",e_event,(this(),bg),True)
                    elif "photoimage" in entry[0]:
                        Button(pady=1,padx=1,image=insert_image_gif,text="?").rcgrid(grid_row,2)
                        do_command(choose_image,(widget("Entry"),entry[0]))
                        #do_command(lambda par = this(): messagebox.showinfo("Photo Image","Enter the path to a PhotoImage file (gif,ppm,pgm)",parent=par))
                        widget("Entry").do_event("<Return>",e_event,None,True)

                    else:
                        do_event("<Return>",e_event,None,True)

                        # help info message box for sticky option
                        if entry[0] =="myclass":
                            Button(pady=1,padx=1,image=help_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda par = this(): messagebox.showinfo("Widget Class","If you enter a class name, this name for the class will be exported instead a generated one",parent=par))

                        elif entry[0] =="baseclass":
                            Button(pady=1,padx=1,image=help_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda par = this(): messagebox.showinfo("Base Class","If you enter a base class name, the export generates inheritance from this base class instead of a tkinter or ttk widget class",parent=par))

                        elif entry[0] =="call Code(self)":
                            Button(pady=1,padx=1,image=help_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda par = this(): messagebox.showinfo("call Function or Class","If you fill in a function or class name, the following call will be exported\n\nCode(self)\n\nSo you may generate calling code for your gui container.\n\n The Code shall be in another file, so that it will not be overwritten by export.",parent=par))

                        elif entry[0] =="link":
                            Button(pady=1,padx=1,image=help_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda: load_script('guidesigner/Help/LinkTop.py'))

                        elif entry[0] == "cursor":
                            Button(pady=1,padx=1,image=about_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda: load_script('guidesigner/cursors.py'))

                        elif entry[0] == "buttoncursor":
                            Button(pady=1,padx=1,image=about_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda: load_script('guidesigner/buttoncursors.py'))

                        elif entry[0] == "sashcursor":
                            Button(pady=1,padx=1,image=about_gif,bg='blue',text="?").rcgrid(grid_row,2)
                            do_command(lambda: load_script('guidesigner/sashcursors.py'))

                        elif entry[0] == "state":
                            if isinstance(msg,Spinbox) or isinstance(msg,Entry) : Listbox(width=8,height=3).fillList(("normal","disabled","readonly"))
                            elif isinstance(msg,Text) or isinstance(msg,Canvas): Listbox(width=8,height=2).fillList(("normal","disabled"))
                            else: Listbox(width=8,height=3).fillList(("normal","disabled","active"))
                            lbox_select(grid_row)

                        elif entry[0] == "default":
                            Listbox(width=7,height=2).fillList(("active","disabled"))
                            lbox_select(grid_row)

                        elif entry[0] == "direction":
                            Listbox(width=5,height=4).fillList(("above","below","left","right"))
                            lbox_select(grid_row)

                        elif entry[0] == "activestyle":
                            Listbox(width=9,height=3).fillList(("none","dotbox","underline"))
                            lbox_select(grid_row)

                        elif entry[0] == "wrap":
                            Listbox(width=4,height=3).fillList(("none","char","word"))
                            lbox_select(grid_row)

                        elif 'stipple' in entry[0] or 'bitmap' in entry[0]:
                            Listbox(width=9,height=13).fillList(('<=','@file','','error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question','warning'))
                            lbox_bitmap_select(grid_row)
                            #lbox_select(grid_row)
                            
                        elif entry[0] == "type":
                            Listbox(width=7,height=3).fillList(("normal","menubar","tearoff"))
                            lbox_select(grid_row)

                        elif entry[0] == "insertunfocussed":
                            Listbox(width=6,height=3).fillList(("none","hollow","solid"))
                            lbox_select(grid_row)

                        elif entry[0] == "validate":
                            Listbox(width=8,height=6).fillList(("none","focus","focusin","focusout","key",'all'))
                            lbox_select(grid_row)

                        elif entry[0] == "style" and isinstance(selected_widget,CanvasItemWidget):
                            
                            Listbox(width=8,height=3).fillList(("pieslice","chord","arc"))
                            lbox_select(grid_row)

                        elif entry[0] in ("relief","buttonuprelief","buttondownrelief","sashrelief","offrelief"):
                            Listbox(width=6,height=6).fillList(("flat","raised","sunken","groove","ridge","solid"))
                            lbox_select(grid_row)

                        elif entry[0] in ('sliderrelief',"overrelief","activerelief"):
                            Listbox(width=6,height=7).fillList(("","flat","raised","sunken","groove","ridge","solid"))
                            lbox_select(grid_row)


                        elif entry[0] =="arrow":
                            Listbox(width=5,height=4).fillList(('none','first','last','both'))
                            lbox_select(grid_row)


                        elif entry[0] =="capstyle":
                            Listbox(width=10,height=3).fillList(('butt','projecting','round'))
                            lbox_select(grid_row)

                        elif entry[0] =="joinstyle":
                            Listbox(width=5,height=3).fillList(('round','bevel','miter'))
                            lbox_select(grid_row)

                        elif entry[0] == "anchor":
                            Button(pady=0,padx=0, relief = 'flat', image=sticky_gif,text="?").rcgrid(grid_row,2)
                            do_command(lambda me = this(), root = widget('/','GuiFrame'),entry = widget('Entry'): send('SET_ANCHOR',(
                                me.winfo_rootx() - root.winfo_rootx()+me.winfo_width(),
                                me.winfo_rooty() - root.winfo_rooty(),
                                'anchor',entry
                                )))

                        elif entry[0] == "labelanchor":
                            Button(pady=0,padx=0, relief = 'flat', image=labelanchor_gif,text="?").rcgrid(grid_row,2)
                            do_command(lambda me = this(), root = widget('/','GuiFrame'),entry = widget('Entry'): send('SET_LABELANCHOR',(
                                me.winfo_rootx() - root.winfo_rootx()+me.winfo_width(),
                                me.winfo_rooty() - root.winfo_rooty(),
                                'labelanchor',entry
                                )))

                        elif entry[0] == "compound":
                            Button(pady=0,padx=0, image=compound_gif,text="?").rcgrid(grid_row,2)
                            do_command(lambda me = this(), root = widget('/','GuiFrame'),entry = widget('Entry'): send('SET_COMPOUND',(
                                me.winfo_rootx() - root.winfo_rootx()+me.winfo_width(),
                                me.winfo_rooty() - root.winfo_rooty(),
                                'config',entry
                                )))

                        elif entry[0] == 'font':
                            Button(pady=1,padx=1,image=font_gif,text="?",bg='white').rcgrid(grid_row,2)
                            do_command(lambda w_entry = widget('Entry'): DynAccess('guidesigner/FontSelect.py',(this(),w_entry)))

                        elif entry[0] =="justify":
                            justify_var.set(selected_widget['justify'])
                            justify_button(widget('Entry'))
                            rcgrid(grid_row,2)

                        elif entry[0] =="selectmode":
                            Listbox(width=8,height=4).fillList(("browse","single","multiple","extended"))
                            lbox_select(grid_row)

                        elif entry[0] =="tabstyle":
                            Listbox(width=13,height=2).fillList(("tabular","wordprocessor"))
                            lbox_select(grid_row)

                        elif entry[0] =="mode":
                            Listbox(width=13,height=2).fillList(("determinate","indeterminate"))
                            lbox_select(grid_row)

                        elif entry[0] =="orient":
                            if isinstance(selected_widget,StatTtk.PanedWindow):
                                this()['state'] = 'readonly'
                            else:
                                Listbox(width=10,height=2).fillList(("vertical","horizontal"))
                                lbox_select(grid_row)
                        
                        '''
                        elif entry[0] in ("showhandle","blockcursor","setgrid",'autoseparators','undo','exportselection','jump','tearoff',"hidemargin","columnbreak",'takefocus','opaqueresize','indicatoron'):
                            Listbox(width=4,height=2).fillList(("0","1"))
                            lbox_select()
                        '''


                    grid_row += 1
                setWidgetSelection(msg) # set selection for current user widget
                can_update(getconfdict())
                setSelection(current_selection)
                wcanvas.yview_moveto(0)

            else:
                cont.unlayout() # if the widget doesn't have a config, then disable value refresh and hide the layout options
        

    do_receive('SHOW_CONFIG',show_config,wishMessage=True)

main()

### ========================================================

goOut() # Frame
goOut() # Canvas
widget('Scrollbar').pack(side=RIGHT,fill=Y,expand=FALSE)
#widget('Canvas').pack(fill=BOTH, expand=TRUE)
widget('Canvas').pack()

### CODE ========================================================



# -------------- make a frame with a vertical scrollbar ------------------------------------

interior_id = my_canvas.create_window(0, 0, window=my_frame,anchor=NW)


# -------------- <Configure> events for the scrollbar frame ------------------------------------

def canvas_configure(me,frame,int_id = interior_id):
    if me['width'] != frame.winfo_width(): me['width'] = frame.winfo_width()
 
my_canvas.do_event("<Configure>",canvas_configure,my_frame,True)

def frame_configure(me,canvas):
    canvas.config(scrollregion="0 0 %s %s" % (me.winfo_reqwidth(), me.winfo_reqheight()))
    if me.winfo_reqwidth() != canvas['width']: canvas.config(width=me.winfo_reqwidth())
    if me.winfo_reqheight() > 400: canvas.config(height=400)
    else: canvas.config(height=me.winfo_reqheight())

my_frame.do_event("<Configure>",frame_configure,my_canvas,True)


widget("Canvas").config(yscrollcommand=widget("Scrollbar").set)
widget("Scrollbar").config(command=widget("Canvas").yview)

### ========================================================
