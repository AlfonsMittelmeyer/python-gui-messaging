import tkinter
from tkinter import filedialog as tkFileDialog
from tkinter import constants as Tkconstants

#Tkconstants,

class TkFileDialogExample(tkinter.Frame):

  def __init__(self, root):

    tkinter.Frame.__init__(self, root)

    # options for buttons
    button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

    # define buttons
    tkinter.Button(self, text='askopenfile', command=self.askopenfile).pack(**button_opt)
    tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
    tkinter.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
    tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)
    tkinter.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)

    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    #options['initialdir'] = 'C:\\'
    options['initialfile'] = 'myfile.txt'
    options['parent'] = root
    options['title'] = 'This is a title'

    # This is only available on the Macintosh, and only when Navigation Services are installed.
    #options['message'] = 'message'

    # if you use the multiple file version of the module functions this option is set automatically.
    #options['multiple'] = 1

    # defining options for opening a directory
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'This is a title'

  def askopenfile(self):

    """Returns an opened file in read mode."""

    return tkFileDialog.askopenfile(mode='r', **self.file_opt)

  def askopenfilename(self):

    """Returns an opened file in read mode.
    This time the dialog just returns a filename and the file is opened by your own code.
    """

    # get filename
    filename = tkFileDialog.askopenfilename(**self.file_opt)

    # open file on your own
    if filename:
      return open(filename, 'r')

  def asksaveasfile(self):

    """Returns an opened file in write mode."""

    return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

  def asksaveasfilename(self):

    """Returns an opened file in write mode.
    This time the dialog just returns a filename and the file is opened by your own code.
    """

    # get filename
    filename = tkFileDialog.asksaveasfilename(**self.file_opt)

    # open file on your own
    if filename:
      return open(filename, 'w')

  def askdirectory(self):

    """Returns a selected directoryname."""

    return tkFileDialog.askdirectory(**self.dir_opt)

if __name__=='__main__':
  root = tkinter.Tk()
  TkFileDialogExample(root).pack()
  root.mainloop()
