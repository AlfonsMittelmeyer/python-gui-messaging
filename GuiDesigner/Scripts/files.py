Menu('mainmenu')
goIn()

MenuItem('close','command',label='close')
MenuItem('open','command',label='open')

widget('open').layout(index=1)
widget('close').layout(index=2)

goOut()
select_menu()
Label('status',bg='white', height=3, text='status\n', width=40)

widget('status').pack()
