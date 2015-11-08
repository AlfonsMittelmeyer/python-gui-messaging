Toplevel('HelpDynAccess',**{'title': 'DynAccess - Loading Scripts and passing Parameters', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(22, 10, 0, 0)'})

Message('call_dyn',**{'text': "access = DynAccess('myscript.py')", 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '11'})
Message('call_dyn_parameters',**{'text': "DynAccess('myscript.py,parameter) # if one parameter\nDynAccess('myscript.py,(par1,par2,par3)) # if more parameters\nDynAccess('myscript.py,(list,)) # if one parameter but a list or tuple", 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '13'})
Message('call_dyn_text',**{'text': 'And you will get back a return value, if it was a function or an instance of a class, if it was a class.\n\nAlso passing parameters is possible:', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '12'})
Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '20'})
Message('lead_text',**{'text': "Function 'load_script' simply loads and executes a script, without opportunity to get a return value or to pass parameters. But function 'DynAccess' makes this possible.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('load_into',**{'text': 'Load Widgets into Container Widgets', 'font': 'TkDefaultFont 11 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '15'})
Message('load_into_code',**{'text': "DynAccess('myscript',parameter,parent) # if you pass parameters\nDynAccess('myscript',None,parent) # without parameters\nDynAccess('myscript',(None,),parent) # with parameter None", 'font': 'TkfixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '18'})
Message('load_into_text',**{'text': 'When you use load_script, you may load widgets from a script not only into the application window, but in every container widget. This also may be done, when you use DynAccess.', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '17'})
Message('pre_class',**{'text': '# in your script there has to be such a class', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('pre_class_code',**{'text': 'class Access:', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Message('pre_function',**{'text': '# or such a function', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '8'})
Message('pre_function_code',**{'text': 'def Access():\n    ...\n    return value', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '9'})
Label('precondition_title',**{'text': "Precondition: a class or a function with name 'Access'", 'font': 'TkDefaultFont 11 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Label('title',**{'text': 'DynAccess - Loading Scripts and passing Parameters', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})
Label('use_dynaccess',**{'text': 'Then use DynAccess', 'font': 'TkDefaultFont 11 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '10'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================

