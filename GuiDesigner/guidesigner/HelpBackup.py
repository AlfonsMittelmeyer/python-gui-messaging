Toplevel('HelpBackup',**{'title': 'Backup', 'grid_cols': '(6, 75, 0, 0)', 'grid_multi_cols': '[6, (0, 10, 0, 0), (5, 10, 0, 0)]', 'grid_rows': '(9, 10, 0, 0)'})

Button('close',**{'text': 'Close'}).grid(**{'column': '4', 'sticky': 'nesw', 'row': '7'})
Message('filename',**{'text': 'Backup.py', 'pady': '10', 'font': 'TkDefaultFont 9 bold', 'width': '300', 'bd': '2', 'bg': 'white', 'fg': 'blue', 'relief': 'solid'}).grid(**{'column': '2', 'sticky': 'nesw', 'columnspan': '2', 'pady': '15', 'row': '4'})
Message('lead_text',**{'text': 'For saving a quick backup without enter a file name. The GUI will be saved as file:', 'width': '300', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '4', 'row': '3'})
LinkLabel('link',**{'text': 'Save', 'font': 'TkFixedFont 9 bold underline', 'bg': 'white', 'link': 'guidesigner/HelpSaveLoadContent.py', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '3', 'sticky': 'nesw', 'columnspan': '2', 'row': '5'})
Message('otherwise',**{'text': 'Otherwise same as:', 'width': '300', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '2', 'row': '5'})
Label('title',**{'text': 'Backup', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '4', 'row': '1'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================
