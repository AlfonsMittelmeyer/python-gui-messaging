Toplevel('test',**{'call Code(self)': 'appcode.TestGUI', 'title': 'Testing', 'myclass': 'TestGui'})
goIn()

Button('english',**{'text': 'english'})
Button('german',**{'text': 'german'})
Button('plot',**{'text': 'plot'})

widget('german').pack(side='left')
widget('english').pack(side='left')
widget('plot').pack(side='left')

goOut()

