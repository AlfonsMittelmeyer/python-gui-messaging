config(myclass='BOStrab_Fahrzeugeinschraenkung')

Menu('MainMenu',link='Scripts/menu.py').select_menu()
LabelFrame('plotframe',link='Scripts/plot.py')

widget('plotframe').pack()

