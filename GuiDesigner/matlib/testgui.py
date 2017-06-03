try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


import testcode

class TestGui(tk.Toplevel):

    def __init__(self,master,**kwargs):
        tk.Toplevel.__init__(self,master,**kwargs)
        self.title('Testing')
        # widget definitions ===================================
        self.english = tk.Button(self,text='english')
        self.german = tk.Button(self,text='german')
        self.plot = tk.Button(self,text='plot')
        self.german.pack(side='left')
        self.english.pack(side='left')
        self.plot.pack(side='left')
        # call Code ===================================
        testcode.TestGUI(self)

