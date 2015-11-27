# if you have PIL or Pillow, you may include it here
from tkinter import PhotoImage

def dynTkImage(widget,filename):
    widget.image=PhotoImage(file=filename)
    widget.setconfig('image',widget.image)

def dynTkLoadImage(widget,filename):
    widget.loadimage=PhotoImage(file=filename)

