Toplevel('HelpExportTk',grid_cols='(8, 75, 0, 0)', title='Export (tk)', grid_multi_cols='[8, (0, 10, 0, 0), (7, 10, 0, 0)]', grid_rows='(21, 10, 0, 0)')
goIn()

Message('...',text='...', bg='white', anchor='w', width=500).grid(sticky='nesw', row=9, column=1, columnspan=6)
Message('after_window_name',text="The widget name is a normal tkinter parameter. And export without names don't contain this parameter.", bg='white', anchor='w', width=500).grid(sticky='nesw', row=14, column=1, columnspan=6)
Button('close',text='Close').grid(sticky='nesw', row=19, column=6)
Message('code_import1',text='import tkinter as tk', bg='white', anchor='w', fg='red', width=500, font='TkFixedFont 9 bold').grid(sticky='nesw', row=4, column=1, columnspan=6)
Message('code_import2',text='or', bg='white', anchor='w', width=500).grid(sticky='nesw', row=5, column=1, columnspan=6)
Message('code_import3',text='import DynTkExt as tk', bg='white', anchor='w', fg='red', width=500, font='TkFixedFont 9 bold').grid(sticky='nesw', row=6, column=1, columnspan=6)
Message('code_import4',text='and', bg='white', anchor='w', width=500).grid(sticky='nesw', row=7, column=1, columnspan=6)
Message('code_import5',text='#import DynTkInter as tk', bg='white', anchor='w', fg='red', width=500, font='TkFixedFont 9 bold').grid(sticky='nesw', row=8, column=1, columnspan=6)
Label('conversion',bg='white', anchor='w', text='Conversion of export with names to export without names', font='TkDefaultFont 9 bold').grid(sticky='nesw', row=16, column=1, columnspan=6)
Message('conversion_text',text='This is simple to do. Just make a copy of your source file with names and update it with an export without names.', bg='white', anchor='w', width=500).grid(sticky='nesw', row=17, column=1, columnspan=6)
Message('decide',text="Then you may decide, what to use. If you like to start the GUI designer, you have to import DynTkInter. If not, then you may use tkinter or DynTkExtend. DynTkExtend is a short module, which you need for grid tables and for menus items with names. But if you don't use this, then it's not neccessary to import DynTkExtend.\n\nThe advantage of the export using 'tkinter (names) is, that if you start the GuiDesigner, it knows the names of the widgets. In the case of 'tkinter' the GuiDesigner names all labels 'label, all buttons 'button' and so on, which isn't so much useful.\n\nWhat's the difference of export with and without names? Not very much. If you export via 'tkinter (names)' the widget has a parameter 'name' with the name combined with '#' and a number, because for tkinter it has to be a unique name.", bg='white', anchor='w', width=500).grid(sticky='nesw', row=12, column=1, columnspan=6)
Message('lead_text',text="'Export tkinter' offers a quick start for writing tkinter programs. A python source file is directly created and may be started immediatedly. It's recommended to begin with 'tkinter names'. The exported source file contains an import of 'tkinter' or 'DynTkExtend', dependent whether 'DynTkExtend' is necessary. An import for 'DynTkInter' is commented out. This import would be necessary instead of the other, if you would like to edit a tkinter GUI by using the GuiDesigner.", bg='white', anchor='w', width=500).grid(sticky='nesw', row=3, column=1, columnspan=6)
Message('mainloop1',text="#Application().mainloop('guidesigner/Guidesigner.py')", bg='white', anchor='w', fg='red', width=500, font='TkFixedFont 9 bold').grid(sticky='nesw', row=10, column=1, columnspan=6)
Message('mainloop2',text='Application().mainloop()', bg='white', anchor='w', fg='red', width=500, font='TkFixedFont 9 bold').grid(sticky='nesw', row=11, column=1, columnspan=6)
Label('title',bg='white', anchor='w', text='Export tkinter', fg='blue', font='TkDefaultFont 12 bold').grid(sticky='nesw', row=1, column=1, columnspan=6)
Message('widget_name',text="self.button = tk.Button(self, name = '#24_button', text = 'Text')", bg='white', anchor='w', fg='blue', width=500, font='TkFixedFont 9 bold').grid(sticky='nesw', row=13, column=1, columnspan=6)

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================

goOut()

