config(**{'myclass': 'BOStrab_Fahrzeugeinschraenkung'})

Menu('MainMenu',**{'myclass': 'MenuGUI', 'call Code(self)': 'appcode.MenuGUI'})
goIn()

MenuItem('languages','cascade',**{'label': 'Sprachen'})
goIn()

Menu('language_submenu',**{'myclass': 'LanguageSubmenu', 'call Code(self)': 'appcode.LanguageSubmenu', 'tearoff': 0})
goIn()

MenuItem('deutsch','command',**{'label': 'deutsch'})

widget('deutsch').layout(index=1)

goOut()
select_menu()

goOut()

MenuItem('test','command',**{'label': 'Test'})

widget('languages').layout(index=1)
widget('test').layout(index=2)

goOut()
select_menu()
LabelFrame('plotframe',**{'myclass': 'PlotFrame', 'call Code(self)': 'appcode.PlotFrame', 'text': 'Madplotlib'})
goIn()

goOut()

widget('plotframe').pack()
