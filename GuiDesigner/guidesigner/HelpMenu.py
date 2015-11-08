Toplevel('HelpMenu',**{'title': 'Menu Entries', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(10, 10, 0, 0)'})

Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '8'})
Label('item_index',**{'text': 'get_index()', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '5'})
Message('item_index_text',**{'text': "It's useful to have menu item widgets. But there are also tkinter functions, which you would like to use for menu entries, like invoke and others. Therefore you need the index of the menu item. You get it via the method get_index for the menu item widgets. This method isn't available for the 'delimiter'. But if it exists (tearoff is 1), then its index is 0.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('lead_text',**{'text': "The menu entries didn't fit in the concept only widgets, config and layout and no other functions. So the menu entries became widgets. It's easier to have widgets instead of some menu entries, for which the exact index sometimes isn't known for sure. And sometimes programmers look for the label text of the entries for identifying them. But what, if somebody likes to write a program in different languages.\n\nWidgets are easy to use. And a command callback may be made in the normal way for widgets.\n\nSo command, checkbutton, radiobutton, cascade and separator became widgets. But what's about the delimiter, which you also detect, when you design a menu?\n\nI didn't know the name, when I detected it. And it's not really creating a menu entry, when you create this pseudo widget. It's only the access to the tearoff. When the tearoff is set to 1 for a menu, then you may tear off the menu as a window and move it somewhere. And there is a small separator at the begin of the menu. When you click it, the menu will tear off.\n\nWhen tearoff is set to 1, you may change the 'background' of this tearoff. This is all what you may do with this 'delimiter'. If tearoff is set to 0 this 'delimiter' points to the first menu entry. Then don't use it. You also cannot define a command callback for this tearoff the same way as for the other menu entries.\n\nA command callback for the tearoff has to be done using 'tearoffcommand' in the menu options.\n\n", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('title',**{'text': 'Menu Entries', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================


