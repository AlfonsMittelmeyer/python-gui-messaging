config(myclass='MenuGUI')

MenuItem('languages','cascade',label='Sprachen')
goIn()

Menu('language_submenu',link='Scripts/languages.py').select_menu()

goOut()

MenuItem('test','command',label='Test')

widget('languages').layout(index=1)
widget('test').layout(index=2)

### CODE ===================================================


class MainMenu:

    def __init__(self,language = widget('languages'),test=widget('test')):
        self.language = language
        subscribe('MENU_LANGUAGE',self.receive_language)

        # for testing
        test['command'] = self.test

    def receive_language(self,languages):
        self.language['label'] = languages[0] # this should be written as entryconfig for tkinter
        publish('SUBMENU_LANGUAGES',languages[1:])

    def test(self):
        current_selection = Selection() # for GuiDesigner the selection shouldn't change
        Toplevel('test',title = 'Testing',link='Scripts/tests.py')
        setSelection(current_selection) # for GuiDesigner the selection shouldn't change

MainMenu()

### ========================================================
