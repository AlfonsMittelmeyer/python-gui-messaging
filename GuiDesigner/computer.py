# -*- coding: utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from PIL import Image,ImageTk


class Application(tk.Tk):

    def __init__(self,**kwargs):
        tk.Tk.__init__(self,**kwargs)
        # widget definitions ===================================
        self.button_img = ImageTk.PhotoImage(Image.open('Images/computer.png'))
        self.button = tk.Button(self,text='Computer', image=self.button_img, font='TkDefaultFont 8', compound='center')
        self.button.place(x='0', y='0')

if __name__ == '__main__':
    Application().mainloop()
