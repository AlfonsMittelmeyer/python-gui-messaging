from functools import partial
from Imports.communication import publish,subscribe

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
    


def short_dictionary(dictionary):

    # reduce tuple to last entry
    for n,e in dictionary.items():
        dictionary[n] = e[-1]

    # erase doubles
    if "bd" in dictionary:	
        dictionary['bd'] = dictionary['borderwidth']
        dictionary.pop('borderwidth',None)
    if "bg" in dictionary:	
        dictionary['bg'] = dictionary['background']
        dictionary.pop('background',None)
    if "fg" in dictionary:	
        dictionary['fg'] = dictionary['foreground']
        dictionary.pop('foreground',None)
    if "validatecommand" in dictionary:
        dictionary['vcmd'] = dictionary['validatecommand']
        dictionary.pop('validatecommand',None)
    if "invalidcommand" in dictionary:
        dictionary['invcmd'] = dictionary['invalidcommand']
        dictionary.pop('invalidcommand',None)

    # changing not allowed after widget definition - maybe I should save it?. But then I would need the default value.
    dictionary.pop('colormap',None)
    dictionary.pop('screen',None)
    dictionary.pop('visual',None)
    dictionary.pop('class',None)
    dictionary.pop('use',None)
    dictionary.pop('container',None)
    return dictionary


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

    return short_dictionary(dictionary)
