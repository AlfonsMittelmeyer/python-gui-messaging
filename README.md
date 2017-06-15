# DynTkInter GuiDesigner

DynTkinter GUI Designer, the only one with advanced Grid Design
and individual table settings per row and column

The GUI Designer includes Help pages and an introduction

- The introduction you start with: python3 intro.py
- The GuiDesigner you start with: python3 main.py

![enter image description here](https://www2.pic-upload.de/img/33340088/guidesigner.gif)

brand-new:

- an easy to use eventbroker in directory Utilities

- distinguishing between imports by baseclass ond those of call Code

- automatic generation of imports for export

- file export, save and load utf-8 encoded for Windows

very new:

- bug fixing for geometry: was not saved and not exported
- export of same names for local widgets self.name as self.names_nr
- implementation of forget() for pack layout
- minsize, maxsize and resizable for Main Window and Toplevel

relative new:

- saving and export of Text widget text
- ttk.Notebook now available and full functioning
- all ttk Widgets are available
  but Treeview and Sizegrip without further functionality

- two new ttk widgets: ttk.Separator and ttk.Combobox

- a new module Export/tk_extend.py for fixing a tkinter problem with entryconfig

- a new option 'baseclass' allows inheritance from your own base classes instead of tkinter ort ttk widget classes.
  So it's simple now to implement complex guis in tkinter

- a new option 'call Code(self)' allows to generate a function or a class call in the exported source.
  So now it's possible to separate gui and code so that a new export may be taken as it is, because
  it already contains calls of code, which shall be in other modules
  Only you have to insert your imports for your code modules

- improvements for PanedWindow and ttk.PanedWindow
- sashpos and sash_coord will only be saved and exported, if manually changed
- may be reset by changing a layout option
- weight may be changed for ttk.PanedWindow panes also afterwards as a layout option

- ttk widgets (which also exist in tkinter)
- you may experiment with TtkSyles.styles.py. This file may be loaded by the GuiDesigner

- bug fixing for PhotoImages (were not deletable, didn't show in menu intems)
- bug fixing for PanedWindow (was not stable, exceptions could happen)

- full support for PIL Image and PIL ImageTk
  (if you import "from DynTkInter import Image, ImageTk"
  then you may use all functions of Image or ImageTk)
- Export of Menus and PhotoImages in tkinter style
- better name export and reimport for export 'tk (names)' 
- indexes for menu entries for easy entryconfig later
- class names for export
- overwriting files instead of merging when exporting
- export and reimport of grid tables in tkinter style
  via rowconfigure and columnconfigure
- Export of Canvas Items

to do:

- GuiDesigner and DynTkInter work now also with Python 2.7 instead only with Python 3
    but this doen't work correct now. str() doesn't work as in python3. Before str is used
    the data have to be encoded for not standard ascii characters



> Written with [StackEdit](https://stackedit.io/).