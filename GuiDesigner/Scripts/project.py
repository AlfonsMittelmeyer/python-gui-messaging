config(myclass='BOStrab_Fahrzeugeinschraenkung')

Menu('MainMenu',myclass='MenuGUI')
goIn()

MenuItem('languages','cascade',label='Sprachen')
goIn()

Menu('language_submenu',myclass='LanguageSubmenu', tearoff=0)
goIn()

MenuItem('deutsch','command',label='deutsch')

widget('deutsch').layout(index=1)

### CODE ===================================================

# this shall later be exported in another form from widgets in tkinter style
# later the GuiDesigner should be able to create such a code

# this name doesn't matter. Only for better recognition
class LanguageSubmenu:
    def __init__(self):

        self._start()
        self._dont_save_dynamically_created()

    def _start(self,container = container()):
        self.container = container
        self.deutsch_index = self.container['tearoff']
        self._create_menu()
               

    def _create_menu(self):
        current_selection = Selection()
        self.create_menu()
        setSelection(current_selection)

        # here should follow own code in tkinter style
        # later the GuiDesigner should be able to export this code

# EXPORT =============================

    # after GUI definition: the Code ===========================
    # this code may also be inserted in GuiDesigner Scripts
    

    def create_menu(self):    


        # for calling more times, delete the menu, which existed before,
        # except the first command

        # for marking the end
        
        self.container.add_checkbutton()

        # now we delete the menu entries after deutsch
        after_deutsch = self.deutsch_index + 1
        while True:
            itemtype = self.container.type(after_deutsch)
            self.container.delete(after_deutsch)
            if itemtype == 'checkbutton':
                break
 
        # now we make a dynamic creation
        # first we get the style of the first command
        # this style should also be used for the other commands

        command_config = get_entryconfig(self.container,self.deutsch_index)
        
        # we dont't use some now not defined languagefile[i]
        # we can think later of this

        # now we create dynamic commands

        languages = ('deutsch','english','russisch','polnisch','italienisch',None,'spanisch','französisch',None,'dänisch')

        for index,language in enumerate(languages):

            if not language:
                self.container.add_separator()
                continue

            command_config['label'] = language
            command_config['command'] = partial(self.do_action,language)
                
            try:
                self.container.entryconfig(index+self.deutsch_index,**command_config)
            except IndexError:
                self.container.add_command(**command_config)
                 
    def do_action(self,language):
        publish("SELECT_LANGUAGE",language)
            
# /EXPORT =============================

    # we don't want to save dynamically created widgets after self.deutsch_index
    # by the GuiDesigner
    def _dont_save_dynamically_created(self):
        start_index = self.deutsch_index - self.container['tearoff']
        for element in self.container.PackList[start_index+1:]:
            element.dontSave()
        
        
LanguageSubmenu()

### ========================================================

goOut()
select_menu()

goOut()


widget('languages').layout(index=1)

goOut()
select_menu()
