# if you have PIL or Pillow, you may include it here
from tkinter import PhotoImage

def dynTkImage(widget,filename):
    widget.image=PhotoImage(file=filename)
    widget['image'] = widget.image
    
