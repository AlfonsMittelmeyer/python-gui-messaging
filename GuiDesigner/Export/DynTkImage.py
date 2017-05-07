# if you have PIL or Pillow, you may include it here
from tkinter import PhotoImage

def dynTkImage(widget,filename):
    widget.image=PhotoImage(file=filename)
    widget['image'] = widget.image

def dynTkLoadImage(widget,filename):
    widget.loadimage=PhotoImage(file=filename)

def dynTkLoadImageObject(filename):
    obj = Object()
    obj.loadimage=PhotoImage(file=filename)
    return obj
