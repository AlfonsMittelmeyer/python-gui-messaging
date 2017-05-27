# python-gui-messaging
Tkinter GUI Designer, the only one with advanced Grid Design
and individual table settings per row and column

very new:
- ttk widgets (which also exist in tkinter)
- you may experiment with TtkSyles.styles.py. This file may be loaded by the GuiDesigner

- bug fixing for PhotoImages (were not deletable, didn't show in menu intems)
- bug fixing for PanedWindow (was not stable, exceptions could happen)

relative new:

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


The GUI Designer includes Help pages and an introduction

- The introduction you start with: python3 intro.py
- The GuiDesigner you start with: python3 main.py
