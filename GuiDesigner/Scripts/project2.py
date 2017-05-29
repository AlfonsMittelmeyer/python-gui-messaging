Menu('mainmenu',myclass='MenuGUI')
goIn()

MenuItem('cascade','cascade',label='Symbolleisten')
goIn()

Menu('symbolleisten',tearoff=0)
goIn()

MenuItem('analyse','checkbutton',label='Analyse')
MenuItem('auswertung','checkbutton',label='Auswertung')
MenuItem('datenbank','checkbutton',label='Datenbank')
MenuItem('export','checkbutton',label='Export')

widget('datenbank').layout(index=1)
widget('analyse').layout(index=2)
widget('auswertung').layout(index=3)
widget('export').layout(index=4)

goOut()
select_menu()

goOut()


widget('cascade').layout(index=1)

goOut()
select_menu()
