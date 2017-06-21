#config(**{'bd': 2, 'height': 100, 'width': 300})
config(**{'bd': 2})
config(**{'grid_rows': '(3, 0, 0, 1)', 'grid_cols': '(1, 0, 0, 1)'})

LabelFrame('baselayout',**{'link': 'guidesigner/BaseLayout.py'}).grid(pady=7, row=1,sticky='ew')
LabelFrame('widgetclass',**{'link': 'guidesigner/WidgetClass.py'}).grid(sticky='ew', row=0)
