### CODE ===================================================

def main():
    
    # =============================================================
    # color yellow
    # =============================================================
    # in:
    # - for_a_name - 2 times: when more same names or only one name
    # - for_names: when the container is selected
    # - for_basement
    # - look_up_refs

    # for each yellow a function has to be called with reference to the button

    Lock()

    RefDict = {}
    RefCont = [_Application]
    Default_bg = ['grey']

    class Var:
        def __init__(self):
            self.value = False

    ALPHABET = 0
    BASEMENT = 1
    INDEX = 2

    sort_order = Var()
    sort_order.value = ALPHABET

    def button_select(selection):
        if widget_exists(selection._widget): setSelection(selection)
        send("SELECTION_CHANGED")

    def do_button_command(selection,button_press=button_select):
        do_command(button_press,selection)
        widget = selection._widget
        if widget.hasConfig and widget_exists(widget):
        #if widget.hasConfig and widget_exists(widget) and ('DynTtk' in str(type(widget)) or widget.getconfig("highlightthickness")):
            try:
                a = widget.winfo_x()
                b = widget.winfo_width()
                do_event("<Button-1>",highlight_widget,widget,wishWidget=True)
            except: pass


    class DynTk_HighLight:

        def __init__(self,me):
            self.me = me
            dyntk_highlight(me)

        def restore(self):
            selection_before = Selection()
            deleteWidgetsForName(self.me.myRoot(),NONAME_HILI)
            setSelection(selection_before)

    def highlight_widget(button,widget):
        button.dyntk_highlight = DynTk_HighLight(widget)
        button.do_event('<ButtonRelease-1>',highlight_mouse_up,button)

    def highlight_mouse_up(me):
        me.unbind('<ButtonRelease-1>')
        me.dyntk_highlight.restore()
        me.dyntk_highlight = None


    def for_a_name(row,name,entry,selection,anchor = 'center',padx=6, button_command = do_button_command,RefDict=RefDict):
        current_this = None
        Button(text=name,anchor = anchor, padx = padx) # create a button, text is the name of the widget
        button_command(Create_Selection(entry[0],selection._container))
        config(font = "TkDefaultFont 8 normal roman",height = 1) # user smaler font
        rcgrid(row+1,1,sticky=W+E) # layout

        if len(entry) > 1:

            # create a label with text "-"
            Label(text="-")
            rcgrid(row+1,2)

            column=0 # index for while loop
            # for each widget in the list
            while column < len(entry):

                Button(text=str(column)) # create a button, which text of it's index
                RefDict[entry[column]] = this()
                # bind command for pressing this button: selection for this widget
                button_command(Create_Selection(entry[column],selection._container))
                rcgrid(row+1,column+3,sticky=W+E) # layout

                # if this widget is the selected one, the bg color shall be yellow
                if entry[column] is selection._widget:
                    config(bg="yellow")
                    scroll_button(this())
                    current_this = selection._widget

                # if the widget doesn't have a layout, the font shall be italic and otherwise normal
                if entry[column].Layout == NOLAYOUT: config(font = "TkDefaultFont 8 normal italic")
                else: config(font = "TkDefaultFont 8 normal roman")

                column += 1

            if current_this != None:
                if not current_this.isLocked:
                    Label(text="-").rcgrid(row+1,column+3)
                    Button(text="=>",font = "TkDefaultFont 8 normal roman",bg="orange").rcgrid(row+1,column+4)
                    button_command(Create_Selection(current_this,current_this))

        else:   # if there is only one widget for this name

            # if this widget is the selected one, the bg color shall be yellow
            if entry[0] is selection._widget:
                config(bg="yellow")
                scroll_button(this())
            RefDict[entry[0]] = this()

            # if the widget doesn't have a layout, the font shall be italic and otherwise normal
            if entry[0].Layout == NOLAYOUT: config(font = "TkDefaultFont 8 normal italic")
            else: config(font = "TkDefaultFont 8 normal roman")

            if entry[0].hasConfig and entry[0].isContainer and len(entry[0].CODE) != 0: config(highlightthickness=1, highlightbackground = "blue", relief="solid")

            # if the widget is a container widget, then create label "-" and button "=>" in orange for goIn()
            if not entry[0].isLocked:
                Label(text="-").rcgrid(row+1,2) # 
                Button(text="=>",font = "TkDefaultFont 8 normal roman",bg="orange").rcgrid(row+1,3)
                button_command(Create_Selection(entry[0],entry[0]))



    def start_show_selection(frame_Selection = Selection(),button_command = do_button_command,for_entries = for_a_name,RefDict=RefDict,Default_bg=Default_bg,RefCont=RefCont):
        RefDict.clear() # clear the reference dictionary (buttons which already exists)
        RefCont[0] = container()
        
        selection_before = Selection() # save the user selection
        setSelection(frame_Selection) # set the selection to inside Frame SelectionShow (container is selected)
        unlayout()
        deleteAllWidgets(this()) # delete all widgets in Frame SelectionShow

        # go out button =========================
        Button(text="<=") # create the button for goOut()
        Default_bg[0] = this()['bg']

        def do_goOut():
            goOut()
            send("SELECTION_CHANGED")

        do_command(do_goOut)
        config(font = "TkDefaultFont 8 normal roman") # use a smaller font
        rcgrid(0,0) # layout
        # =====================================================

        # container button =========================
        Button(text='.',padx=11) # create the button for selecting the container
        RefDict[selection_before._container] = this()
        button_command(Create_Selection(selection_before._container,selection_before._container))
        config(font = "TkDefaultFont 8 normal roman") # use a smaller font
        rcgrid(0,1,sticky=W) # layout

        if selection_before._container is selection_before._widget:
            config(bg="yellow") # if the container is already selected, mark it with yellow background
            scroll_button(this()) # if is yellow, then scroll
        # =====================================================
            
        # if container contains code, thenh mark id with blue margin ==================
        if len(selection_before._container.CODE) != 0:
            config(highlightthickness=1, highlightbackground = "blue", relief="solid")
        # =====================================================




    def for_names(for_entries = for_a_name):

        selection_before = Selection() # save the user selection
        start_show_selection()

        # sorted names
        namelist = []
        for name in selection_before._container.Dictionary.elements:
            if not isinstance(name,NONAMES): namelist.append(name)
        namelist.sort()

        row = 0
        for name in namelist:
            entry = selection_before._container.Dictionary.elements[name]
            for_entries(row,name,entry,selection_before)
            row += 1

        #frame_Selection._container.pack(anchor='nw')	
        setSelection(selection_before) # restore the user selection


    def for_basement(for_entries = for_a_name):

        selection_before = Selection() # save the user selection
        start_show_selection()

        # names sorted by basement
        namelist = []
        this_container = selection_before._container
        
        children = this_container.winfo_children()
        children_copy = list(children)
        for child in children_copy:
            if isinstance(child,StatTkInter.Toplevel) or not isinstance(child,GuiElement):
                children.pop(children.index(child))
            
        for child in children[::-1]:
            name,index = this_container.Dictionary.getNameAndIndex(child)
            if name and not isinstance(name,NONAMES):
                if index != -1:
                    name += '.' + str(index)
                namelist.append((name,child))
       

        row = 0
        index = 0
        for name_child in namelist:
            if isinstance(name_child[1],Menu):
                for_entries(row,name_child[0],[name_child[1]],selection_before)
            else:
                for_entries(row,'{0:{width}}: {1}'.format(-index,name_child[0],width=2),[name_child[1]],selection_before,anchor = 'w')
                index += 1
            row += 1

        #frame_Selection._container.pack(anchor='nw')	
        setSelection(selection_before) # restore the user selection


    def for_index(for_entries = for_a_name):

        selection_before = Selection() # save the user selection
        start_show_selection()


        # before wo do the following, first we should get the MenuDelimiters and show them first
        
        this_container = selection_before._container

        children_list = this_container.Dictionary.getChildrenList()
        children = []

        if isinstance(this_container,Menu):
            # Menu Tearoffs ====================================
            for child in children_list:
                if isinstance(child,MenuDelimiter):
                    children.append(child)

        # names sorted by index ===============================
        
        
        if isinstance(this_container,(PanedWindow,ttk.PanedWindow)):
            index_list = [ this_container.nametowidget(element) for element in this_container.panes() ]
        if isinstance(this_container,ttk.Notebook):
            index_list = [ this_container.nametowidget(element) for element in this_container.tabs() ]
        else:
            index_list = this_container.PackList

        children.extend(index_list)

        # sorted names for remaining elements
        namelist = []
        for name in selection_before._container.Dictionary.elements:
            if not isinstance(name,NONAMES): namelist.append(name)
        namelist.sort()

        for name in namelist:
            entry = selection_before._container.Dictionary.elements[name]
            for x in entry:
                if x not in children:
                    children.append(x)
        
        namelist = []

        for child in children:
            name,index = this_container.Dictionary.getNameAndIndex(child)
            if name and not isinstance(name,NONAMES):
                if index != -1:
                    name += '.' + str(index)
                namelist.append((name,child))
        # =====================================================
       

        row = 0
        index = 0
        if isinstance(this_container,Menu):
            index = this_container['tearoff']

        for name_child in namelist:

            if isinstance(name_child[1],MenuDelimiter):
                for_entries(row,'{0:{width}}: {1}'.format(0,name_child[0],width=2),[name_child[1]],selection_before,anchor = 'w')
            elif name_child[1] in index_list:
                for_entries(row,'{0:{width}}: {1}'.format(index,name_child[0],width=2),[name_child[1]],selection_before,anchor = 'w')
                index += 1
            else:
                for_entries(row,name_child[0],[name_child[1]],selection_before)

            row += 1

        #frame_Selection._container.pack(anchor='nw')	
        setSelection(selection_before) # restore the user selection




    def check_for_names(for_names=for_names,for_basement = for_basement):
        
        if isinstance(container(),(Menu,PanedWindow,ttk.PanedWindow,ttk.Notebook)):
            for_index()
        elif sort_order.value == INDEX:
            for_index()
        elif sort_order.value == ALPHABET:
            for_names()
        elif isinstance(container(),(Tk,Toplevel,Frame,LabelFrame,ttk.Frame,ttk.LabelFrame)):
            for_basement()
        else:
            for_names()


    def look_up_refs(RefDict=RefDict,for_names=for_names,Default_bg=Default_bg,RefCont=RefCont,for_basement = for_basement, check_for_names = check_for_names):
        if not this() in RefDict or container() != RefCont[0]:
            check_for_names()
        else:
            for element in RefDict:
                if not widget_exists(element):
                    if sort_order.value == BASEMENT:
                        for_basement()
                    else:
                        for_names()
                    return
            for element,button in RefDict.items():
                if element == this():
                    button['bg'] = 'yellow'
                    scroll_button(button)
                    button['font'] = "TkDefaultFont 8 normal italic" if element.Layout == NOLAYOUT else "TkDefaultFont 8 normal roman"
                else:
                    button['bg'] = Default_bg[0]




    def check_for_menu(for_names=for_names,look_up_refs = look_up_refs):
        look_up_refs()
        '''
        if isinstance(container(),Menu): for_names()
        else: look_up_refs()
        '''

    do_receive('SHOW_SELECTION',check_for_menu)
    do_receive('SHOW_SELECTION_UPDATE',check_for_names)


    def select_alphabetical(for_names = for_names):
        sort_order.value = ALPHABET
        for_names()

    def select_basement(check_for_names = check_for_names):
        sort_order.value = BASEMENT
        check_for_names()

    def level_changed(for_basement = for_basement):
        if sort_order.value == BASEMENT:
            for_basement()

    def select_index(check_for_names = check_for_names):
        sort_order.value = INDEX
        check_for_names()


    def refresh_index():
        if isinstance(container(),(Menu,PanedWindow,ttk.PanedWindow,ttk.Notebook)) or sort_order.value == INDEX:
            for_index()
         

    do_receive('REFRESH_INDEX_ORDER',refresh_index)
    do_receive('SELECT_INDEX_ORDER',select_index)
    do_receive('SELECT_ALPHABETICAL',select_alphabetical)
    do_receive('SELECT_BASEMENT',select_basement)
    do_receive('BASEMENTLEVEL_CHANGED',level_changed)

    def show_scroll_button(widget):
        if widget_exists(widget):
            bottom_y = widget.winfo_rooty()+widget.winfo_height()-1 - widget.master.winfo_rooty()
            frame_height = widget.master.winfo_height()
            canvas = widget.master.master
            if bottom_y < 400:
                canvas.yview_moveto(0)
            else:
                end_view = bottom_y + 200
                if end_view > frame_height:
                    end_view = frame_height
                start_view = end_view - 400
                offset = start_view/frame_height
                canvas.yview_moveto(offset)

    def scroll_button(widget):
        widget.master.after(100,show_scroll_button,widget)
        
main()


### ========================================================

