config(**{'title': 'Save & Load', 'grid_cols': '(8, 75, 0, 0)', 'grid_multi_cols': '[8, (0, 10, 0, 0), (7, 10, 0, 0)]', 'grid_rows': '(20, 10, 0, 0)'})

Button('close',**{'text': 'Close', 'bd': '2'}).grid(**{'column': '6', 'sticky': 'nesw', 'row': '18'})
Label('load_destructive',**{'text': 'Are Load & Edit (part) and Load & Run (part) destructive?', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '15'})
Message('load_destructive_text',**{'text': 'These load functions are not indended to delete something. But if you would load more than one GUI scripts into one container widget and if these GUI scripts would contain code blocks, then only the code block of the last loaded script would persist for this container widget. In such a case you should copy the missing code block into the source file manually.', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '16'})
Label('load_edit',**{'text': 'Load & Edit, Load & Edit (part)', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '9'})
Message('load_edit_text',**{'text': "The meaning of Load & Edit is: if a GUI script contains marked code blocks, this code blocks are not executed. So we get simply the widgets without a running code.\n\nThe difference between Load & Edit and Load & Edit (part) is: Load & Edit always deletes the content of the current window and loads the GUI into the root of the current window, which may be an Application window or a Toplevel window. Load & Edit (part) don't delete something. And it loads the GUI into the currently selected container widget, which may be the Application window, a Toplevel window, a Frame, a LabelFrame, a Canvas, a PanedWindow, a Menu, a Menubutton or a cascade.\n\nLoad & Edit (part) is ideal for putting a GUI together. It may be, that you have designed a GUI in the application window. But then you have the idea to put it in a Frame. How to do this? Simply make a Frame and load the saved GUI into the Frame.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '10'})
Label('load_run',**{'text': 'Load & Run, Load & Run (part)', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '12'})
Message('load_run_text',**{'text': 'The difference to Load & Edit is: if a GUI script contains marked code blocks, this code will be executed.', 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '13'})
Label('save',**{'text': 'Save', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '3'})
Label('save_part',**{'text': 'Save (part)', 'font': 'TkDefaultFont 9 bold', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '6'})
Message('save_part_text',**{'text': "Save (part) in File->Split & Join->Save (part) is ideal for saving GUI parts, e.g. of a splitted GUI or for splitting a GUI. But this save function has to be used carefully. It doesn't save whole the GUI, but only, what is selected. If somebody has selected a button without taking care, then only this button is saved. Or if somebody had modified a splitted GUI part, separated by a link, but saves the root, then the modifications will not be saved. So it's recommended, always to control, what was saved.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '7'})
Message('save_text',**{'text': "Save in File->Save is easy to use. It saves the whole content of the currently edited Window. A Toplevel window is saved as a Toplevel widget. But an Application window will not be saved as a Tk() object. It's expected, that the application window already exists. And so only the content of the application window and it's config will be saved.\n\nFor a complex large GUI, which is splitted into different GUI scripts, it's not always so a good idea to use this save function. This save function doesn't save the config option link entries, but saves whole the GUI. So for example, if we would save the GuiDesigner via this save function, it would become one large file of more than 3400 lines. Not easy to overlook.", 'width': '500', 'bg': 'white', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '4'})
Label('title',**{'text': 'Save & Load', 'font': 'TkDefaultFont 12 bold', 'bg': 'white', 'fg': 'blue', 'anchor': 'w'}).grid(**{'column': '1', 'sticky': 'nesw', 'columnspan': '6', 'row': '1'})

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================
