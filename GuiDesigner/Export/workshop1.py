# -*- coding: utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class Application(tk.Tk):

    def __init__(self,**kwargs):
        tk.Tk.__init__(self,**kwargs)
        self.minsize(500, 400)
        # widget definitions ===================================
        self.frame_guinotes = FrameGuinotes(self)
        self.frame_menunotes = FrameMenunotes(self)
        self.frame_toolbarnotes = FrameToolbarnotes(self)
        self.label_PS = tk.Label(self,font='TkFixedFont 10 bold', anchor='w', relief='solid', text='Welches Layout soll man nehmen?\nUnd soll man einen GuiBuilder nehmen?\nWenn ja, welchen?', pady='4', padx='4', fg='#a90000', justify='left', bd='4')
        self.frame_menunotes.pack(fill='x')
        self.frame_toolbarnotes.pack(fill='x')
        self.frame_guinotes.pack(expand=1, fill='both')
        self.label_PS.pack(pady=3, fill='x')

class FrameGuinotes(tk.Frame):

    def __init__(self,master,**kwargs):
        tk.Frame.__init__(self,master,**kwargs)
        self.config(highlightthickness=7, highlightcolor='#a90000', highlightbackground='#a90000')
        # widget definitions ===================================
        self.notes_gui = tk.Text(self,font='TkFixedFont 12 bold', width=1, height=1, pady=8, padx=8)
        self.notes_gui.delete(1.0, tk.END)
        self.notes_gui.insert(tk.END,'Und da kommt die eigentlich GUI Anwendung')
        self.notes_gui.pack(expand=1, fill='both')

class FrameMenunotes(tk.Frame):

    def __init__(self,master,**kwargs):
        tk.Frame.__init__(self,master,**kwargs)
        self.config(highlightthickness=7, highlightcolor='blue', highlightbackground='blue')
        # widget definitions ===================================
        self.notes_menu = tk.Text(self,font='TkFixedFont 12 bold', height=1, pady=8, padx=8, fg='blue')
        self.notes_menu.delete(1.0, tk.END)
        self.notes_menu.insert(tk.END,'Oben soll ein Menü sein')
        self.notes_menu.pack(expand=1, fill='both')

class FrameToolbarnotes(tk.Frame):

    def __init__(self,master,**kwargs):
        tk.Frame.__init__(self,master,**kwargs)
        self.config(relief='sunken', highlightthickness=7, highlightcolor='#008900', highlightbackground='#008900')
        # widget definitions ===================================
        self.notes_toolbar = tk.Text(self,font='TkFixedFont 12 bold', height=1, pady=8, padx=8, fg='#008900')
        self.notes_toolbar.delete(1.0, tk.END)
        self.notes_toolbar.insert(tk.END,'Darunter kommt eine Toolbar mit Photoimages')
        self.notes_toolbar.pack(expand=1, fill='both')

if __name__ == '__main__':
    Application().mainloop()
