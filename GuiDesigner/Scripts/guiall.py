Toplevel('HelpExportTk',grid_multi_cols='[8, (0, 10, 0, 0), (7, 10, 0, 0)]', grid_rows='(20, 10, 0, 0)', grid_cols='(8, 75, 0, 0)', title='Export (tk)')
goIn()

Message('after_window_name',width=500, anchor='w', text="The window name is a normal tkinter parameter. And export without names doesn't contain this parameter.", bg='white').grid(column=1, sticky='nesw', columnspan=6, row=10)
Button('close',text='Close').grid(column=6, sticky='nesw', row=18)
Message('code_import',width=500, anchor='w', font='TkFixedFont 9 bold', text='import DynTkInter as tk\nimport DynTkInter as ext', fg='blue', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=4)
Message('code_loop',width=500, anchor='w', font='TkFixedFont 9 bold', text="...\n\nApplication().mainloop('guidesigner/Guidesigner.py')", bg='white').grid(column=1, sticky='nesw', columnspan=6, row=6)
Message('code_unimport',width=500, anchor='w', font='TkFixedFont 9 bold', text='#import tkinter as tk\n#import DynTkExtend as ext', fg='red', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=5)
Message('code_unloop',width=500, anchor='w', font='TkFixedFont 9 bold', text='#Application().mainloop()', fg='red', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=7)
Label('conversion',text='Conversion export with names to export without names', anchor='w', font='TkDefaultFont 9 bold', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=15)
Message('conversion_text',width=500, anchor='w', text='This is simple to do. Just make a copy of your source file with names and update it with an export without names.', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=16)
Message('decide',width=500, anchor='w', text="Then you may decide, what to use. If you like to start the GUI designer, you have to import DynTkInter. If not, then you may use tkinter. DynTkExtend is a short module, which you need for grid tables and for menus. But if you didn't use this, then it's not neccessary to import DynTkExtend.\n\nThe export without names contains what's commented in the export with names. It doesn't make much sense to start the GuiDesigner, when the names are missing.\n\nThe advantage of the export with names is, that you may modify parameters of the widgets in your source code without using the GuiDesigner. When you start the GuiDesigner at the end of your program it automatically catches your modifications and you don't need to modify your GUI script each time, when you make changes.\n\nWhat's the difference between export with and without names? Not very much. The export with names contains the window name:", bg='white').grid(column=1, sticky='nesw', columnspan=6, row=8)
Message('lead_text',width=500, anchor='w', text="Export (tk) offers a quick start for writing tkinter programs. A python source file is directly created and may be started immediatedly. It's recommended to begin with Export (tk) with names. The exported source file (with names) contains imports for DynTkInter and commented imports for tkinter and DynTkExtend. And also two versions for the mainloop:", bg='white').grid(column=1, sticky='nesw', columnspan=6, row=3)
Label('title',text='Export (tk)', anchor='w', font='TkDefaultFont 12 bold', bg='white', fg='blue').grid(column=1, sticky='nesw', columnspan=6, row=1)
Label('update',text='Export Update', anchor='w', font='TkDefaultFont 9 bold', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=12)
Message('update_text',width=500, anchor='w', text="After you have added your code for callbacks (commands and events), classes and anything else you could have the idea to modify the GUI again by using the GuiDesigner. But how can you do this?\n\nIt's simple. Just export the modified GUI again and overwrite your source file with the modified GUI.\n\nOh, sounds terrible? No, you will find a backup of your old source file, the name beginning with '~'. And the export will not overwrite your source file completely, but only exchange the __init__ definitions for the GUI. You only have to take care, that you let an empty line after the widget definitions, which the GuiDesigner made. The __init__ definitions only will be exchanged until the first empty line. If you add other container widgets, which didn't exist before, you will find these classes at the end of the source file just before mainloop.", bg='white').grid(column=1, sticky='nesw', columnspan=6, row=13)
Message('window_name',width=500, anchor='w', font='TkFixedFont 9 bold', text="self.Button = tk.Button(self,name = 'button',**{'text': 'Button'})", fg='blue', bg='white').grid(column=1, sticky='nesw', columnspan=6, row=9)

### CODE ===================================================
def do_close(cont=container()):
    cont.destroy()

widget('close').do_command(do_close)
### ========================================================

goOut()

