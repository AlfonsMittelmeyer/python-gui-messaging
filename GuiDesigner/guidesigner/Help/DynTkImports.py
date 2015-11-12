Toplevel('HelpDynTkImports',**{'title': 'DynTkImports.py', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(11, 10, 0, 0)'})

Button('close',**{'text': 'Code', 'bd': '2'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '9'})
Message('feel_free',**{'text': 'Feel free to adapt DynTkImports.py to your needs.', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Message('lead_text',**{'text': "Because it's not convenient to do imports in a little complicated way, there is the module DynTkImports.py. We have included there:", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Message('partial_code',**{'text': 'def test():\n    basetwo = partial(int, base=2)\n    print(basetwo)\n\ntest()', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('partial_include',**{'text': 'from functools import partial', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '4'})
Message('partial_script',**{'text': "DynTkImports.py is imported by DynTkInter and what's defined there may be used by scripts. So in scripts it's sufficient to write:", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Label('title',**{'text': 'DynTkImports.py', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================
