# -*- coding: utf-8 -*-
Button('english',text='english')
Button('german',text='german')

widget('german').pack(side='left')
widget('english').pack(side='left')

### CODE ===================================================

class TestApplication:

    def __init__(self,german = widget('german'), english = widget('english')):
        german['command'] = partial(self.send_language,0)
        english['command'] = partial(self.send_language,1)

    def send_language(self,index):
        language_lists = (
            ( 'Sprache',('deutsch','german'),None,('englisch','english'),('französisch','french')),
            ( 'Language',('english','english'),None,('french','french'),('german','german'))
        )
        publish('MENU_LANGUAGE',language_lists[index])

TestApplication()
            
### ========================================================
