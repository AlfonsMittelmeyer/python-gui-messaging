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

# ======= Grid Table ======================================================

def grid_configure_multi(data):
    count = data[0]
    multi = []
    for i in range(count): multi.append([False,None])
    for i in range(len(data)):
        if i != 0:
            multi[data[i][0]] = [True,{'minsize':data[i][1],'pad':data[i][2],'weight':data[i][3]}]
    return multi

def grid_configure_cols(container,grid_conf_cols,grid_multi_conf_cols,isColumns=True):

    cols = grid_conf_cols[0]

    if len(grid_multi_conf_cols) == 0:
        for i in range(cols): grid_multi_conf_cols.append([False,None])

    to_insert =  {'minsize':grid_conf_cols[1],'pad':grid_conf_cols[2],'weight':grid_conf_cols[3]}
    
    for col in range(cols):
        if grid_multi_conf_cols[col][0] == False:
            grid_multi_conf_cols[col][1] = dict(to_insert)

    for col in range(cols):
        if isColumns:
            container.grid_columnconfigure(col,**(grid_multi_conf_cols[col][1]))
        else:
            container.grid_rowconfigure(col,**(grid_multi_conf_cols[col][1]))

def grid_table(container,grid_rows = None, grid_cols = None, grid_multi_rows = None, grid_multi_cols = None):

    grid_multi_conf_cols = []
    grid_multi_conf_rows = []

    if grid_multi_rows != None:
        grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

    if grid_multi_cols != None:
        grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

    if grid_cols != None:
        grid_conf_cols = eval(grid_cols)
        grid_configure_cols(container,grid_conf_cols,grid_multi_conf_cols)

    if grid_rows != None:
        grid_conf_rows = eval(grid_rows)
        grid_configure_cols(container,grid_conf_rows,grid_multi_conf_rows,False)

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

