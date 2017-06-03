from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import numpy as np

from functools import partial
from Imports.communication import publish,subscribe

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

def shorten_dictionary(dictionary):

    # reduce tuple to last entry
    for n,e in dictionary.items():
        dictionary[n] = e[-1]

    # erase doubles
    for entry in (('bd','borderwidth'),('bg','background'),('fg','foreground')):
        if entry[0] in dictionary:
            dictionary[entry[0]] = dictionary.pop(entry[1])

    for entry in (('vcmd','validatecommand'),('invcmd','invalidcommand')):
        if entry[1] in dictionary:
            dictionary[entry[0]] = dictionary.pop(entry[1])

    # changing not allowed after widget definition
    for entry in ('colormap','screen','visual','class','use','container'):
        dictionary.pop(entry,None)


def get_entryconfig(menu,index):

    index = 0
    dictionary = {}
    for entry in (
'activebackground',
'activeforeground',
'accelerator',
'background',
'bitmap',
'columnbreak',
'command',
'font',
'foreground',
'hidemargin',
'image',
'indicatoron',
'label',
'menu',
'offvalue',
'onvalue',
'selectcolor',
'selectimage',
'state',
'underline',
'value',
'variable'
):

        try:
            dictionary[entry] = (menu.entrycget(index,entry),)
        except tk.TclError: pass

    shorten_dictionary(dictionary)
    return dictionary
