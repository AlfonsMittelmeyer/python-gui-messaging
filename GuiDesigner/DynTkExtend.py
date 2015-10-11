# encoding: UTF-8
#
# Copyright 2015 Alfons Mittelmeyer
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
    pane_window.after(time,lambda i = index, x = x_coord, y=y_coord, function = pane_window.sash_place: function(i,x,y))


# =========  Menu and MenuItem ==========================

def find_root(begin):
    root = begin
    while not (isinstance(root,tk.Tk) or isinstance(root,tk.Toplevel)):
        root = root.master
    return root

class Menu(tk.Menu):

    def __init__(self,master,**kwargs):
 
        if isinstance(master,MenuItem):
            tk.Menu.__init__(self,find_root(master),**kwargs)
        else:
            tk.Menu.__init__(self,master,**kwargs)
        self.master = master
        self.itemlist = []



    def select_menu(self):
        menubase = self.master if (isinstance(self.master,MenuItem) or isinstance(self.master,tk.Menubutton)) else find_root(self)
        menubase.config(menu=self)

    def selectmenu_forget(self):
        menubase = self.master if (isinstance(self.master,MenuItem) or isinstance(self.master,tk.Menubutton)) else find_root(self)
        menubase.config(menu='')

    def layout(self): self.select_menu()
    def unlayout(self): self.selectmenu_forget()

    def add_to_itemlist(self,menu_item):
        self.itemlist.append(menu_item)

    def get_item_index(self,menu_item):

        index = -1
        for i in range(len(self.itemlist)):
            if self.itemlist[i] == menu_item:
                index = i;
                break
        return index

    def remove_from_itemlist(self,menu_item):
        self.itemlist.pop(self.itemlist.index(menu_item))

    def item_list_len(self):
        return len(self.itemlist)

    def destroy(self):
        if isinstance(self.master,MenuItem): self.master = find_root(self)
        tk.Menu.destroy(self)



class MenuItem:

    def __init__(self,master,mytype='command',**kwargs):

        self.mytype = mytype
        self.master = master
        master.add_to_itemlist(self)
        master.add(mytype,**kwargs)

    def destroy(self):
         index = self.master.get_item_index(self)
         self.master.delete(index+1)
         self.master.remove_from_itemlist(self)

    def layout(self,**kwargs):
        self.item_change_index(**kwargs)

    def item_change_index(self,index):

        old_index = self.master.get_item_index(self)
        new_index = old_index
        try:
            new_index = int(index) -1
        except ValueError: return

        if new_index != old_index:
            limit = self.master.item_list_len()
            if new_index >= 0 and new_index < limit:

                confdict = dict(self.get_confdict())
                self.master.delete(old_index+1)
                self.master.insert(new_index+1,self.mytype,confdict)
                del self.master.itemlist[old_index]
                self.master.itemlist.insert(new_index,self)

    def config(self,**kwargs):
        index = self.master.get_item_index(self) + 1
        self.master.entryconfig(index,**kwargs)

    def get_confdict(self):
        index = self.master.get_item_index(self) + 1
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
                dictionary[entry] = self.master.entrycget(index,entry)
            except tk.TclError: pass
        return dictionary

class MenuDelimiter():
    def __init__(self,master,**kwargs):

        self.master = master
        self.master.entryconfig(0,**kwargs)

    def config(self,**kwargs):
        self.master.entryconfig(0,**kwargs)

