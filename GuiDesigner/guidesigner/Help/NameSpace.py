Toplevel('HelpNameSpace',**{'title': 'Namespace of Scripts', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(10, 10, 0, 0)'})

Button('close',**{'text': 'Close'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '8'})
Message('dyntkinter_text',**{'text': "In the main script the global name space is the name space of the main script itself. So there is the need to import DynTkInter. But in a script, which is loaded via a load option of DynTkInter the global name space is DynTkInter. So there is normally no import of DynTkInter in these scripts and no expression like tk.Button() but only Button().\n\nAnd because the global name space is DynTkInter, so only in the DynTkInter module or what's imported by this module, global definitions may be done, but not in a script, which is loaded.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Label('dyntkinter_title',**{'text': 'Global Namespace is DynTkInter', 'font': 'TkDefaultFont 10 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Message('lead_text',**{'text': "What you define in a script isn't defined in a global name space, but only in a local one and will vanish and be garbage collected after the end of the script, if not referenced by some object, which will then still exist.\n\nBut should there not be also a global name space? Of course there is one.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('title',**{'text': 'Namespace of Scripts', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================

