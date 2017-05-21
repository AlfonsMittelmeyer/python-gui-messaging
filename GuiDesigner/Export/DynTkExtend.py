# encoding: UTF-8
#
# Copyright 2017 Alfons Mittelmeyer
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter import *
from functools import partial

# == Fill Listbox with Text ==============================================

def fill_listbox_with_string(listbox,string):
    listbox.delete(0,'end')		
    for e in string.split("\n"): listbox.insert('end',e)

# =========  Trigger sash_place in a PanedWindow after some time ==========================

def trigger_sash_place(pane_window,time,index,x_coord,y_coord):
    pane_window.after(time,partial(pane_window.sash_place,index,x_coord,y_coord))

# =========  Menu  ===================================================

class Menu(tk.Menu):

    def __init__(self,master,**kwargs):
        kwargs.pop('name',None)        
        tk.Menu.__init__(self,master,**kwargs)

    def add(self,itemtype,**kwargs):
        kwargs.pop('name',None)
        tk.Menu.add(self,itemtype,**kwargs)

    def add_command(self,**kwargs):
        self.add('command',**kwargs)

    def add_separator(self,**kwargs):
        self.add('separator',**kwargs)

    def add_checkbutton(self,**kwargs):
        self.add('checkbutton',**kwargs)

    def add_radiobutton(self,**kwargs):
        self.add('radiobutton',**kwargs)

    def add_cascade(self,**kwargs):
        self.add('cascade',**kwargs)

    def entryconfig(self,index,**kwargs):
        kwargs.pop('name',None)
        tk.Menu.entryconfig(self,index,**kwargs)

