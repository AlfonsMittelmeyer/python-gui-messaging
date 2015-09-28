Button('Menu',text="""Menu""",width=14).pack()

widget('Menu').do_command(lambda: send('CREATE_CLASS_SELECTED','Menu')) # button send message with class name 'Menu'
