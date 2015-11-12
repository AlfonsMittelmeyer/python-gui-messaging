Toplevel('HelpImport',**{'title': 'Imports in Scripts', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(13, 10, 0, 0)'})

Message('better_code',**{'text': 'def main():\n\n    from functools import partial\n    ....\n\n\nmain()\n\n', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '9'})
Message('better_comment',**{'text': '# or may be better this way?', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '8'})
Message('class_code',**{'text': 'from functools import partial\n\ndef main(partial=partial):\n\n    class Test:\n\n        def __init__(self):\n            basetwo = partial(int, base=2)\n            print(basetwo)\n    \n    Test()\n\nmain()', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Message('class_comment',**{'text': '# how to use imports in classes', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '11'})
Message('function_code',**{'text': 'from functools import partial\n\ndef main(partial=partial):\n\n\n    def function_a():\n        basetwo = partial(int, base=2)\n        print(basetwo)\n\n    function_a()\n\nmain()', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Message('function_comment',**{'text': '# how to use imports in functions', 'font': 'TkFixedFont 9 bold', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '4'})
Message('lead_text',**{'text': "You are used to do imports. When you expect, this will work in the same way as in the main script, then your expectation isn't correct. What applies to functions applies to imports too. The imported module isn't known inside of functions, if you don't make it known or if you don't import inside the function.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('title',**{'text': 'Imports in Scripts', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
widget('close').do_command(lambda cont = container(): cont.destroy())
### ========================================================
