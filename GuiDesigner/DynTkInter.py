# -*- coding: utf-8 -*-
#
# Copyright 2015 Alfons Mittelmeyer
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
#
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULARF
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.


import tkinter as StatTkInter
from tkinter import *
#from tkinter import ttk
from tkinter import filedialog as tkFileDialog
from tkinter import messagebox
from tkinter import colorchooser
from copy import copy

import traceback
import queue
import Communication.proxy as dynproxy
from dyntkinter.Selection import Create_Selection
from dyntkinter.name_dictionary import GuiDictionary
from dyntkinter.layouts import *
from dyntkinter.grid_tables import *
from DynTkImports import *
#from dyntkinter.gui_element import *
#from dyntkinter.callback import *

_image_dictionary = None

def PhotoImage(**kwargs):
    img_file = kwargs['file']
    image = StatTkInter.PhotoImage(file=img_file)
    _image_dictionary[image] = img_file
    return image

def dynTkImage(widget,filename):
    if filename == "":
        widget.image = None
        image = widget.getconfig('image')
        if image:
            widget['image'] = None
    else:
        widget.image=StatTkInter.PhotoImage(file=filename)
        widget['image'] = widget.image
    widget.photoimage = filename
    

def dynTkLoadImage(widget,filename):
    widget.loadimage=StatTkInter.PhotoImage(file=filename)

# instead dynTkLoadImage is used by Canvas - create_image, get_image
'''
def dynTkActiveImage(widget,filename):
    DynTkImage.dynTkActiveImage(widget,filename)
    widget.activephotoimage = filename

def dynTkDisabledImage(widget,filename):
    DynTkImage.dynTkDisabledImage(widget,filename)
    widget.disabledphotoimage = filename
'''
'''
def dynTkBitmap(widget,filename):
    DynTkImage.dynTkBitmap(widget,filename)
    widget.bitmapfile = filename
'''

Stack = []

def pop(index=-1): return Stack.pop(index)
def push(x): Stack.append(x)
def top(): return Stack[-1]
def first(): return Stack[-1]
def second(): return Stack[-2]
def third(): return Stack[-3]

ObjectStack = []
SelfStack = []

def receiver(): return ObjectStack[-1]
def Par(): return receiver().parameters
def Me(): return receiver().widget
def Event(): return receiver().event
def Msg(): return receiver().event

def Self(): return SelfStack[-1]
def Data(): return Self().data

class CommandFromFunction:
    def __init__(self,function):
        self.execute = function
        
class CommandFromEvCode:
    def __init__(self,evcode):
        self.evcode = evcode
        
    def execute(self):
        eval(self.evcode)

class CommandFromDataEvCode:
    def __init__(self,evcode,data=None):
        self.evcode = evcode
        self.data = data
        
    def execute(self):
        SelfStack.append(self)		
        eval(self.evcode)
        SelfStack.pop()


def EvCmd(evstring): return CommandFromEvCode(compile(evstring,'<string>', 'exec'))

def EvDataCmd(evstring,data=None):
    if type(evstring) is str: return CommandFromDataEvCode(compile(evstring,'<string>', 'exec'),data)
    cmd = copy(evstring)
    cmd.data = data
    return cmd 

def dummyfunction(par):pass


class Callback:
    def __init__(self,widget,function,parameters=None,wishWidget=False,wishEvent=False,wishSelf = False):
        self.widget = widget
        self.event = None
        self.wishWidget = wishWidget
        self.wishEvent = wishEvent
        self.wishSelf = wishSelf
        self.mydata = None # may be used for many purposes. Accessible via self

        self.isFunction = False
        if type(function) is type(dummyfunction):
            self.isFunction = True
            self.function = function
            self.parameters = []
            if type(parameters) is tuple:
                for e in parameters: self.parameters.append(e)
            elif type(parameters) is list: self.parameters = parameters
            elif parameters != None: self.parameters = [parameters]
        else:
            self.parameters = parameters
            if type(function) is str: self.function = EvCmd(function)
            else:
                self.function = function

    # for execution later =======
        
    def execute(self):
        if self.isFunction:
            par = []
            if self.wishWidget: par = [self.widget]
            if self.wishEvent: par.append(self.event)
            if self.wishSelf: par.append(self)
            par += self.parameters
            return self.function(*par)
        else: 
            ObjectStack.append(self)
            self.function.execute()
            ObjectStack.pop()
        
    def setEvent(self,event = None):
        self.event = event
        return self.execute
        
    # for execution immediate =======

    def receive(self,event = None): return self.setEvent(event)()


    # for using the Callback as funcion =======

    def call(self,*args): 
        if self.isFunction: return self.function(*args) # a function cannot be copied, but a Callback can. Using different mydata, the functions can behave different.
        else: print("Please, call only functions.")


_Selection=Create_Selection()
_TopLevelRoot = Create_Selection()
_AppRoot = Create_Selection()
_AppConf = None
_Application = None
ACTORS = {}
EXISTING_WIDGETS = {}

def widget_exists(widget): return widget in EXISTING_WIDGETS


def this(): return _Selection._widget
def container(): return _Selection._container

CanvasDefaults = {}


class Dummy: pass

def set_photoimage_from_image(element,kwargs):
    if 'image' in kwargs:
        image = kwargs['image']
        if image in _image_dictionary:
            element.photoimage = _image_dictionary[image]


# wird aufgerufen von _initGuiElement und divdersen anderen Klassen
class GuiElement:

    def __init__(self,dyn_name="nn",select=True):

        self.window_item = None
        self.isDestroying = False
        name = dyn_name
        EXISTING_WIDGETS[self] = None
        self.is_mouse_select_on = False
        
        self.reset_grid()
        if select: _Selection._widget = self

        if self.master != None:
            self.master.Dictionary.setElement(name,self)

        if self.isContainer: 
            self.Dictionary = GuiDictionary()
            self.PackList = []
            self.CODE = ""
            self.onlysavecode = False

        self.mydata = None
        self.save =True
        self.actions = {}
        self.menu_ref = None

        self.Layout = NOLAYOUT
        self.hasConfig = True
        self.isMainWindow = False
        #self.isDestroyed = False
        if self.isContainer: self.isLocked=False
        else: self.isLocked = True

    # required for self['menu'] = self.menu
    def __setitem__(self, key, item):
        if key == 'menu':
            activate_menu(item,self)
        elif key == 'image':
            set_photoimage_from_image(self,{'image' :item})
        self.tkClass. __setitem__(self, key, item)


    def reset_grid(self):
        self.grid_conf_rows = None
        self.grid_conf_cols = None
        self.grid_conf_individual_wish = False
        self.grid_conf_individual_has = False
        self.grid_conf_individual_done = False
        self.grid_multi_conf_cols = []
        self.grid_multi_conf_rows = []

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = self.tkClass.config(self,**kwargs)
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'menu' in kwargs and isinstance(kwargs['menu'],Menu):
                # activate_menu(menu,menu_entry_widget)
                activate_menu(kwargs['menu'],self)
            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            if 'photoimage' in kwargs:
                dynTkImage(self,kwargs.pop('photoimage'))
            else:
                set_photoimage_from_image(self,kwargs)
                
            self.tkClass.config(self,**kwargs)

    def lock(): isLocked = Tue

    def myRoot(self):
        selection_before = Selection()
        setWidgetSelection(self)
        gotoRoot()
        rootwidget=this()
        setSelection(selection_before)
        return rootwidget

    def container(self): return _Selection._container
    def goIn(self):
        setWidgetSelection(self)
        goIn()
    
    def dontSave(self): self.save =False
    def saveOnlyCode(self): self.onlysavecode = True

    def do_action(self,actionid,function,parameters=None,wishWidget=False,wishMessage=False,wishSelf=False):
        ACTORS[self] = None
        self.actions[actionid] = [True,Callback(self,function,parameters,wishWidget,wishMessage,wishSelf)]

    def _undo_action(self,actionid):
        self.actions.pop(actionid,None)
        if len(self.actions) == 0: ACTORS.pop(self,None)

    def activateAction(self,actionid,flag):
        if actionid in self.actions: self.actions[actionid][0] = flag

    def destroyActions(self):
        self.actions.clear()
        ACTORS.pop(self,None)

    def getActionCallback(self,actionid): return self.actions[actionid][1]

    def destroy(self):
        self.isDestroying = True

        if self.menu_ref and self.menu_ref != self and widget_exists(self.menu_ref):
            self.menu_ref.unlayout()
        
        self.destroyActions()
        if self.isContainer: send("CONTAINER_DESTROYED",self)

        if self.isContainer: undo_receiveAll(self)

        if self.isMainWindow: setSelection(Create_Selection(self,_TopLevelRoot._container))
        else: setWidgetSelection(self)

        name_index = getNameAndIndex()
        if name_index[0] != None: eraseEntry(name_index[0],name_index[1])

        if self.Layout == PACKLAYOUT or self.Layout == PANELAYOUT: self._removeFromPackList()
        if self.tkClass != Dummy:
            if self.tkClass == Tk: self.quit()
            else: 
                # changed
                # if isinstance(self.master,MenuItem): self.master = self.myRoot()
                # needed for tkinter?
                if isinstance(self.master,MenuItem):
                    self.master = self.master.master
                if widget_exists(self): self.tkClass.destroy(self)
        else:
            if isinstance(self,MenuItem) and self.mytype == 'cascade':
                child_list = self.Dictionary.getChildrenList()
                for child in child_list: child.destroy()
                

        EXISTING_WIDGETS.pop(self,None)		
        cdApp()
        

    def destroyContent(self):
        if not self.isContainer: print("destroyContent requires a container widget")
        else:
            self.CODE = ""
            undo_receiveAll(self)
            deleteAllWidgets(self)
            if isinstance(self,Canvas):
                self.delete(ALL)
                self.canvas_widget = None

    def do_command(self,function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False):
        cmd = Callback(self,function,parameters,wishWidget,wishEvent,wishSelf).setEvent
        self.config(command = lambda event=None: execute_lambda(cmd(event)))
        #cmd = Callback(self,function,parameters,wishWidget,wishEvent,wishSelf).receive
        #self.config(command = cmd)

    def do_event(self,eventkey,function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False):
        cmd = Callback(self,function,parameters,wishWidget,wishEvent,wishSelf).setEvent
        self.bind(eventkey,lambda event: execute_lambda(cmd(event)))
        #cmd = Callback(self,function,parameters,wishWidget,wishEvent,wishSelf).receive
        #self.bind(eventkey,cmd)

    # used by the GUI Creator: it tries to take the name of the widget as text. So Labels, Buttons and LabelFrames may be easily identified when doing the layout
    def text(self,mytext):
        if 'text' in self.getconfdict(): self.config(text=mytext)
    
    # used by the save function: if a container doesn't have widgets then there is no need to look inside
    def hasWidgets(self):
        if self.isLocked: return False
        if isinstance(self,Canvas) and len(self.find_all()) != 0: return True
        return len(self.Dictionary.elements) != 0

    # DynTkInter records the layouts and tho order of pack layouts - without the correct pack order, pack layouts wouldn't be saved properly

    def _addToPackList(self): self.master.PackList.append(self)
        
    def PackListLen(self): return len(self.PackList)

    def getPackListIndex(self):

        index = -1
        for i in range(len(self.master.PackList)):
            if self.master.PackList[i] == self:
                index = i;
                break
        return index


    def _removeFromPackList(self):
            packlist = self.master.PackList
            packlist.pop(packlist.index(self))

    def pack(self,**kwargs):
        global PACKLAYOUT
        if self.Layout != PACKLAYOUT: self._addToPackList()
        self.Layout = PACKLAYOUT
        self.tkClass.pack(self,**kwargs)
        
    def pane(self,**kwargs):
        global PANELAYOUT
        if self.Layout != PANELAYOUT: self._addToPackList()
        self.Layout = PANELAYOUT
        self.master.tkClass.add(self.master,self,**kwargs)

    def pack_forget(self):
        global NOLAYOUT
        self._removeFromPackList()
        self.tkClass.pack_forget(self)
        self.Layout = NOLAYOUT

    def grid(self,**kwargs):
        global PACKLAYOUT
        global GRIDLAYOUT
        if self.Layout == PACKLAYOUT: self._removeFromPackList()
        self.Layout = GRIDLAYOUT
        self.tkClass.grid(self,**kwargs)

    def rcgrid(self,prow,pcolumn,**kwargs):
        kwargs["row"]=prow
        kwargs["column"]=pcolumn
        self.grid(**kwargs)

    def grid_forget(self):
        global NOLAYOUT
        self.tkClass.grid_forget(self)
        self.Layout = NOLAYOUT
    

    def grid_remove(self):
        global NOLAYOUT
        self.tkClass.grid_remove(self)
        self.Layout = NOLAYOUT

    def place(self,**kwargs):
        global PACKLAYOUT
        global PLACELAYOUT
        if self.Layout == PACKLAYOUT: self._removeFromPackList()
        self.Layout = PLACELAYOUT
        self.tkClass.place(self,**kwargs)

    def yxplace(self,y,x,**kwargs):
        kwargs["y"]=y
        kwargs["x"]=x
        self.place(**kwargs)

    def place_forget(self):
        global NOLAYOUT
        self.tkClass.place_forget(self)
        self.Layout = NOLAYOUT

    def pane_forget(self):
        global NOLAYOUT
        self._removeFromPackList()
        self.master.tkClass.remove(self.master,self)
        self.Layout = NOLAYOUT
       
    def selectmenu_forget(self):
        if not isinstance(self.master,Menu):
            activwidget = self.master
            activwidget.menu_ref = None
            activwidget.config(menu='')
            self.Layout = NOLAYOUT

    def selectmenu_forget(self):
        
        if not isinstance(self.master,Menu):
            menu_entry_widget = self.master
            if menu_entry_widget.menu_ref and widget_exists(menu_entry_widget.menu_ref):
                menu_entry_widget.menu_ref = None
            if not menu_entry_widget.isDestroying:
                menu_entry_widget.config(menu='')
        self.Layout = NOLAYOUT

    def unlayout(self):
        layout = self.Layout
        if layout == PACKLAYOUT: self.pack_forget()
        elif layout == GRIDLAYOUT: self.grid_remove()
        elif layout == PLACELAYOUT: self.place_forget()
        elif layout == PANELAYOUT: self.pane_forget()
        elif layout == MENULAYOUT: self.selectmenu_forget()

    def item_change_index(self,index):
        offset = self.master['tearoff']
        old_index = self.getPackListIndex()
        new_index = old_index
        try:
            new_index = int(index) -1
        except ValueError: return

        if new_index != old_index:
            limit = self.master.PackListLen()
            if new_index >= 0 and new_index < limit:
                confdict = self.getconfdict()
                confdict.pop('photoimage',None)
                confdict.pop('myclass',None)
                self.master.delete(old_index+offset)
                self.master.insert(new_index+offset,self.mytype,confdict)
                del self.master.PackList[old_index]
                self.master.PackList.insert(new_index,self)


    def layout(self,**kwargs):
        layout = self.Layout
        if layout == PACKLAYOUT: self.pack(**kwargs)
        elif layout == GRIDLAYOUT: self.grid(**kwargs)
        elif layout == PLACELAYOUT: self.place(**kwargs)
        elif layout == PANELAYOUT: self.master.paneconfig(self,**kwargs)
        elif layout == MENUITEMLAYOUT: self.item_change_index(**kwargs)
        elif layout == MENULAYOUT: self.select_menu()

    # layout settings with the options as a string - is used by the GUI Creator
    def setlayout(self,name,value):
        dictionary = {}
        dictionary[name]=value
        try: self.layout(**dictionary)
        except TclError: pass

    def getlayout(self,name):
        dictionary = self.layout_info()
        if name in dictionary: return dictionary[name]
        else: return ""

    def pane_info(self):
        parent = self.master
        dictionary = {}
        dictionary['width'] = parent.panecget(self,'width')
        dictionary['height'] = parent.panecget(self,'height')
        dictionary['minsize'] = parent.panecget(self,'minsize')
        dictionary['padx'] = parent.panecget(self,'padx')
        dictionary['pady'] = parent.panecget(self,'pady')
        dictionary['sticky'] = parent.panecget(self,'sticky')
        return dictionary


    def menuitem_info(self):
        dictionary = {}
        dictionary['index'] = self.getPackListIndex()+1
        return dictionary

    def layout_info(self):
        layout = self.Layout
        if layout == PACKLAYOUT: dictionary=self.pack_info()
        elif layout == GRIDLAYOUT: dictionary=self.grid_info()
        elif layout == PLACELAYOUT: dictionary = self.place_info()
        elif layout == PANELAYOUT: dictionary = self.pane_info()
        elif layout == MENUITEMLAYOUT: dictionary = self.menuitem_info()
        else: dictionary = {}
        return dictionary

    # config settings with the options as a string - is used by the GUI Creator

    def setconfig(self,name,value):
        confdict={}
        confdict[name] = value
        try: self.config(**confdict)
        except TclError: pass

    def getconfig(self,name):
        dictionary = self.getconfdict()
        if name in dictionary: return dictionary[name]
        else: return ""

    def getconfdict(self):
        dictionary = self.config()
        ConfDictionaryShort(dictionary)
        if 'image' in dictionary:
            del dictionary['image']
            dictionary['photoimage'] = self.photoimage
        if 'activeimage' in dictionary:
            del dictionary['activeimage']
            dictionary['activephotoimage'] = self.activephotoimage
        if 'disabledimage' in dictionary:
            del dictionary['disabledimage']
            dictionary['disabledphotoimage'] = self.disabledphotoimage
        return dictionary

class GuiContainer(GuiElement):

    def __init__(self,dyn_name="nn",select=True,mayhave_grid=False,isMainWindow=False,tk_master = None,**kwargs):

        name = dyn_name
        if isMainWindow:

            self.title_changed = False
            self.geometry_changed = False

            mytitle = None
            mygeometry = None
            if "title" in kwargs:
                mytitle = kwargs.pop('title')
                self.title_changed = True

            if "geometry" in kwargs:
                mygeometry = kwargs.pop('geometry')
                self.geometry_changed = True
        else:
            kwargs.pop('title',None)
            kwargs.pop('geometry',None)


        self.link = kwargs.pop('link',"")

        self.mayhave_grid = mayhave_grid
        if mayhave_grid: grids = (kwargs.pop('grid_rows',None),kwargs.pop('grid_cols',None),kwargs.pop('grid_multi_rows',None),kwargs.pop('grid_multi_cols',None))

        mymaster = self.master
        self.master = tk_master

        if isinstance(self,Tk):

            self.tkClass.__init__(self,**kwargs)
            
            global _Application
            _Application = self
            
            global _AppRoot
            self.master = None
            _AppRoot = Create_Selection(self)

            global _Selection
            _Selection = copy(_AppRoot)
     
            self.master = _CreateTopLevelRoot()
            global _TopLevelRoot
            _TopLevelRoot = Create_Selection(self.master)
            _Selection = copy(_TopLevelRoot)
            
            GuiElement.__init__(self,name)
            _Selection = copy(_AppRoot)

            global _AppConf
            _AppConf = self.getconfdict()
            _AppConf.pop("title",None)
            _AppConf.pop("geometry",None)
            _AppConf.pop("link",None)
            
            self.master = None

        else:
            
            self.tkClass.__init__(self,tk_master,**kwargs)
            self.master = mymaster
            GuiElement.__init__(self,name,select)

        self.isMainWindow = isMainWindow
        if isMainWindow:
            self.Layout = LAYOUTNEVER
            if mytitle != None: self.title(mytitle)
            if mygeometry != None: self.geometry(mygeometry)
        
        if mayhave_grid: grid_table(self,*grids)
        FileImportContainer(self) # if link != ""

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = GuiElement.config(self,**kwargs)
            dictionary['link'] = (self.link,)
            if self.isMainWindow:
                dictionary['title'] = (self.title(),)
                dictionary['geometry'] = (self.geometry(),)
            
            return dictionary
        else:
            if self.mayhave_grid:
                grids = (kwargs.pop('grid_rows',None),kwargs.pop('grid_cols',None),kwargs.pop('grid_multi_rows',None),kwargs.pop('grid_multi_cols',None))
                grid_table(self,*grids)
        
            if self.isMainWindow:
                if 'title' in kwargs:
                    self.title(kwargs.pop('title'))
                    self.title_changed = True

                if 'geometry' in kwargs: 
                    self.geometry_changed = kwargs['geometry'] != ''
                    self.geometry(kwargs.pop('geometry'))
            else:
                kwargs.pop('geometry',None)
                kwargs.pop('title',None)

            if 'link' in kwargs:
                self.link = kwargs.pop('link')
                kwargs.pop('link',None)
                if len(kwargs) != 0: GuiElement.config(self,**kwargs)
                FileImportContainer(self)

            else: GuiElement.config(self,**kwargs)


def ConfDictionaryShort(dictionary):

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


#  doing layouts for the currently selected element

def pack(**kwargs): this().pack(**kwargs)
def grid(**kwargs): this().grid(**kwargs)
def place(**kwargs): this().place(**kwargs)
def pane(*args): this().pane(*args)

# for convenience
def rcgrid(prow,pcolumn,**kwargs): this().rcgrid(prow,pcolumn,**kwargs)
def yxplace(y,x,**kwargs): this().yxplace(y,x,**kwargs)

def unlayout(): this().unlayout()
def remove(): unlayout()


def pack_forget(): this().pack_forget()
def grid_forget(): this().grid_forget()
def grid_remove(): this().grid_remove()
def place_forget(): this().place_forget()

def config(**kwargs): 
    if len(kwargs) == 0: return this().config()
    else: this().config(**kwargs)

def getconfdict(): return this().getconfdict()
def getconfig(name): return this().getconfig(name)
def setconfig(name,value): this().setconfig(name,value)

def layout(**kwargs): this().layout(**kwargs)
def setlayout(name,value): this().setlayout(name,value)
def getlayout(name): return this().getlayout(name)
def layout_info(): return this().layout_info()

def text(mytext): this().text(mytext)

def Reference():
    selection_before = Selection()
    path_name = ']'
 
    if this() == container(): goOut()

    while not isinstance(container(),_CreateTopLevelRoot):

        if this().isMainWindow: _Selection._container = _TopLevelRoot._container

        name_index = getNameAndIndex()
        if name_index[1] == -1: name = "'"+name_index[0]+"'"
        else: name = "('"+name_index[0]+"',"+str(name_index[1])+")"
        path_name = ',' + name + path_name

        goOut()
    
    path_name = eval("['//'"+path_name)
    setSelection(selection_before)
    return path_name




VAR = {}

proxy = None


def send(msgid,msgdata=None): proxy.send(msgid,msgdata)
def send_immediate(msgid,msgdata=None): proxy.send_immediate(msgid,msgdata)
def unregister_msgid(msgid): proxy.unregister_msgid(msgid)
def execute_lambda(cmd): proxy.send('execute_function',cmd)
def do_receive(msgid,function,parameters=None,): proxy.do_receive(container(),msgid,Callback(None,function,parameters).receive)

def undo_receive(container,msgid,receive):
    proxy.undo_receive(container,msgid,receiver)

def undo_receiveAll(cont=container()): proxy.undo_receiveAll(cont)

def activate_receive(msgid,receive,flag): proxy.activate_receive(msgid,receive,flag)


_DynLoad = None

def goto(name,nr=0):
    widget = _Selection._container.Dictionary.getEntry(name,nr)
    if widget != None: 
        _Selection._widget = widget

#def widget(name,nr=-1): return _Selection._container.Dictionary.getEntry(name,nr)

#def widget(name,nr=0,par3=0):
def widget(*args):

    name = args[0]
    nr = 0 if len(args) < 2 else args[1]
    par3 = 0 if len(args) < 3 else args[2]
    
    if type(name) == str:
        if name in ('//','/','.'):
            if name == '//': my_widget = _TopLevelRoot._container
            elif name == '/': my_widget = container().myRoot()
            else: my_widget = container()
            for element in args[1:]:
                if type(element) is tuple:
                    my_widget = my_widget.Dictionary.getEntry(element[0],element[1])
                else:
                    my_widget = my_widget.Dictionary.getEntry(element,0)
            return my_widget
        else:
            return container().Dictionary.getEntry(name,nr)
        
    elif name == NONAME: return container().Dictionary.getEntry(name,nr)
    else: return name.Dictionary.getEntry(nr,par3)


def FileImportContainer(container):
    if container.link == "": return
    selection_before = Selection()
    setSelection(Create_Selection(container,container))
    DynLoad(container.link)
    setSelection(selection_before)
    
NONAME = -1


def _getMasterAndNameAndSelect(name_or_master,altname,kwargs):

    # if the name is a string or NONAME, the master is the current container
    if type(name_or_master) == str or name_or_master == NONAME: return _Selection._container,name_or_master,True
    
    # if there isn't a name, the master is the current container
    elif name_or_master == None: return _Selection._container,altname,True

    # if the name is a tuple, ther master is the first element
    elif type(name_or_master) == tuple: return name_or_master[0],name_or_master[1],False
    else:
        # otherwise the master is name_or_master
        if 'name' in kwargs:
            altname = kwargs['name']
            if altname and altname[0] == '#' and '_' in altname: 
                altname = altname.split('_')[1]
                
            
        return name_or_master,altname,False

def _initGuiElement(kwargs,tkClass,element,myname,altname,isContainer=False):
    element.photoimage=kwargs.pop('photoimage','')
    element.myclass = kwargs.pop('myclass','')
    element.tkClass = tkClass
    master,myname,select = _getMasterAndNameAndSelect(myname,altname,kwargs)
    element.tkClass.__init__(element,master,**kwargs)
    element.master = master
    element.isContainer = isContainer
    GuiElement.__init__(element,myname,select)
    if 'menu' in kwargs and isinstance(kwargs['menu'],Menu):
        # activate_menu(menu,menu_entry_widget)
        activate_menu(kwargs['menu'],self)
    if element.photoimage:
        element.config(photoimage = element.photoimage)
    else:
        set_photoimage_from_image(element,kwargs)
    


def _initGuiContainer(kwargs,tkClass,element,myname,altname,mayhave_grid=False,isMainWindow=False,tk_master = None,self_master = None):
    element.photoimage=kwargs.pop('photoimage','')
    element.myclass = kwargs.pop('myclass','')
    element.tkClass = tkClass
    master,myname,select = _getMasterAndNameAndSelect(myname,altname,kwargs)

    # changed - only one line of code
    # tkmaster = None
    # if tk_master == 'Application': tkmaster = None
    # else: tkmaster = master if tk_master == None else tk_master
    tkmaster = None if tk_master == 'Application' else master if tk_master == None else tk_master
    element.master = master if self_master == None else self_master
    element.isContainer = True
    GuiContainer.__init__(element,myname,select,mayhave_grid,isMainWindow,tkmaster,**kwargs)
    if 'menu' in kwargs and isinstance(kwargs['menu'],Menu):
        activate_menu(self,kwargs['menu'])
    if element.photoimage:
        element.config(photoimage = element.photoimage)
    else:
        set_photoimage_from_image(element,kwargs)
    return tkmaster

class Tk(GuiContainer,StatTkInter.Tk):

    def __init__(self,myname=None,**kwargs):

        global proxy,_image_dictionary,Stack,SelfStack,ObjectStack,CanvasDefaults
        _image_dictionary = {}
        Stack= []
        ObjectStack = []
        SelfStack = []
        VAR.clear()
        EXISTING_WIDGETS.clear()
        ACTORS.clear()
        self.config_menuitems = { 'command':None,'radiobutton':None,'checkbutton':None,'separator':None,'cascade':None,'delimiter':None,'menu':None }
        proxy = dynproxy.Proxy()
        self.master = None
        _initGuiContainer(kwargs,StatTkInter.Tk,self,myname,"Application",True,True,'Application')
        cdApp()

        menu = Menu(self)
        self.config_menuitems['menu'] = menu.config()
        
        for item in self.config_menuitems:
            if item == 'delimiter':
                delim = MenuDelimiter(menu)
                self.config_menuitems['delimiter'] = delim.config()
            elif item == 'menu':
                pass
            else:
                menitem = MenuItem(menu,item)
                self.config_menuitems[item] = menitem.config()
        menu.destroy()

        # create default attributes for Canvas
        canvas = Canvas(self)
        
        item = canvas.create_line(0,0,0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['line'] = config

        item = canvas.create_rectangle(0,0,0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['rectangle'] = config

        item = canvas.create_polygon(0,0,0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['polygon'] = config

        item = canvas.create_oval(0,0,0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['oval'] = config

        item = canvas.create_arc(0,0,0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['arc'] = config

        item = canvas.create_text(0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['text'] = config

        item = canvas.create_bitmap(0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['bitmap'] = config

        item = canvas.create_image(0,0)
        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        CanvasDefaults['image'] = config

        CanvasDefaults['window'] = { 'tag':'','state':'normal','width':'0','height':'0','anchor':'center' }

        canvas.destroy()

    def geometry(self,geometry=None):
        if geometry:
            self.geometry_changed = True
            return StatTkInter.Tk.geometry(self,geometry)
        else:
            return StatTkInter.Tk.geometry(self)

    def title(self,text=None):
        if text:
            self.title_changed = True
        if text:
            return StatTkInter.Tk.title(self,text)
        else:
            return StatTkInter.Tk.title(self)

    def mainloop(self,load_file = None):

        if load_file != None:
            _Application.after(100,_DynLoad,load_file)

        cdApp()
        StatTkInter.Tk.mainloop(self)


    def pack(self,**kwargs): print("Sorry, no pack for the Application!")
    def grid(self,**kwargs): print("Sorry, no grid for the Application!")
    def place(self,**kwargs): print("Sorry, no place for the Application!")


class _CreateTopLevelRoot(GuiElement,Dummy):
    def __init__(self):
        self.tkClass = Dummy
        self.isContainer = True
        self.master = None
        GuiElement.__init__(self,"TopLevel")
        self.hasConfig = False
        self.Layout = LAYOUTNEVER
        
    def pack(self,**kwargs): print("Sorry, no pack for the Toplevel Root!")
    def grid(self,**kwargs): print("Sorry, no grid for the Toplevel Root!")
    def place(self,**kwargs): print("Sorry, no place for the Toplevel Root!")


class Toplevel(GuiContainer,StatTkInter.Toplevel):

    def __init__(self,myname=None,**kwargs):
        master = _initGuiContainer(kwargs,StatTkInter.Toplevel,self,myname,"toplevel",True,True,None,_TopLevelRoot._container)
        goIn()
        self.master = master

    def title(self,text=None):
        if text:
            self.title_changed = True
        if text:
            return StatTkInter.Toplevel.title(self,text)
        else:
            return StatTkInter.Toplevel.title(self)

    def geometry(self,geometry=None):
        if geometry:
            self.geometry_changed = True
            return StatTkInter.Toplevel.geometry(self,geometry)
        else:
            return StatTkInter.Toplevel.geometry(self)

    def destroy(self):
        send_immediate('THIS_TOPLEVEL_CLOSED',self)
        selection = Selection()
        GuiElement.destroy(self)
        send('TOPLEVEL_CLOSED',selection)

    def pack(self,**kwargs): print("Sorry, no pack for a Toplevel!")
    def grid(self,**kwargs): print("Sorry, no grid for a Toplevel!")
    def place(self,**kwargs): print("Sorry, no place for a Toplevel!")

    def geometry(self,geometry=None):
        if geometry:
            self.geometry_changed = True
        return StatTkInter.Toplevel.geometry(self,geometry)




class Menu(GuiContainer,StatTkInter.Menu):

    def __init__(self,myname=None,**kwargs):

        self.title_changed = False
        master,altname,select = _getMasterAndNameAndSelect(myname,"menu",kwargs)
        # changed
        # tk_master = master.myRoot() if isinstance(master,MenuItem) else master
        tk_master = master.master if isinstance(master,MenuItem) else master
        _initGuiContainer(kwargs,StatTkInter.Menu,self,myname,altname,tk_master = tk_master)

        # get default configuration for menu if it was the first call
        if _Application.config_menuitems['menu'] == None:
            tk_menu = StatTkInter.Menu(_Application)
            _Application.config_menuitems['menu'] = tk_menu.config()
            tk_menu.destroy()

    def add(self,itemtype,**kwargs):
        MenuItem(self,itemtype,**kwargs)

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
        if not len(kwargs): return StatTkInter.Menu.entryconfig(self,index)

        if index == 0 and self['tearoff'] and not self._delimiter_exists():
            MenuDelimiter(self,**kwargs)
        else:
            if 'image' in kwargs:
                pack_offset = index - self['tearoff']
                widget = self.PackList[pack_offset]
                set_photoimage_from_image(widget,kwargs)

            StatTkInter.Menu.entryconfig(self,index,**kwargs)

    def _delimiter_exists(self):

        child_list = self.Dictionary.getChildrenList()
        for child in child_list:
            if isinstance(child,MenuDelimiter):
                return True
        return False

    def select_menu(self):
        if not isinstance(self.master,Menu):
            menu_entry_widget = self.master

            if menu_entry_widget.menu_ref != None:
                if widget_exists(menu_entry_widget.menu_ref):
                    menu_entry_widget.menu_ref.unlayout()

            if isinstance(menu_entry_widget,MenuItem):
                menu_entry_widget.set_menu(self)
            else:
                menu_entry_widget.tkClass.config(menu_entry_widget,menu=self)
            
            menu_entry_widget.menu_ref = self
            self.Layout = MENULAYOUT


class Canvas(GuiContainer,StatTkInter.Canvas):
    def __init__(self,myname=None,**kwargs):
        _initGuiContainer(kwargs,StatTkInter.Canvas,self,myname,"canvas",True)

        self.canvas_pyimages = {}
        self.canvas_image_files = {}
        self.canvas_widget = None
        
    def delete(self,item):

        # selete items
        self.tkClass.delete(self,item)

        # delete images
        item_list = self.find_all()
        img_copy = dict(self.canvas_pyimages)
        for entry in item_list:
            if self.type(entry) == 'image':
                img_copy.pop(self.itemcget(entry,'image'),None)
                img_copy.pop(self.itemcget(entry,'activeimage'),None)
                img_copy.pop(self.itemcget(entry,'disabledimage'),None)
        for entry,filename in img_copy.items():
            del self.canvas_pyimages[entry]
            del self.canvas_image_files[filename]

        # update Layout
        for name,entries in self.Dictionary.elements.items():
            for x in entries:
                if x.Layout == WINDOWLAYOUT and x.window_item != None and not x.window_item in item_list:
                    x.Layout = NOLAYOUT
                    x.window_item = None
        
        for name,entries in dict(self.Dictionary.elements).items():
            for x in entries:
                if isinstance(x,CanvasItemWidget) and x.item_id not in item_list: GuiElement.destroy(x)
                

    def create_window(self,*coords,**kwargs):
        if 'window' in kwargs:
            kwargs['window'].Layout = WINDOWLAYOUT
        return self.tkClass.create_window(self,*coords,**kwargs)

    def create_image(self,*coords,**kwargs):
        if 'photoimage' in kwargs: kwargs['image'] = self.get_image(kwargs.pop('photoimage'))
        if 'activephotoimage' in kwargs: kwargs['activeimage'] = self.get_image(kwargs.pop('activephotoimage'))
        if 'disabledphotoimage' in kwargs: kwargs['disabledimage'] = self.get_image(kwargs.pop('disabledphotoimage'))
        return self.tkClass.create_image(self,*coords,**kwargs)

    def itemconfig(self,item,**kwargs):
        if 'photoimage' in kwargs: kwargs['image'] = self.get_image(kwargs.pop('photoimage'))
        if 'activephotoimage' in kwargs: kwargs['activeimage'] = self.get_image(kwargs.pop('activephotoimage'))
        if 'disabledphotoimage' in kwargs: kwargs['disabledimage'] = self.get_image(kwargs.pop('disabledphotoimage'))
        if 'window' in kwargs: kwargs['window'].Layout = WINDOWLAYOUT
        if 'tags' in kwargs: send('CANVAS_TAGCHANGED',item)
        self.tkClass.itemconfig(self,item,**kwargs)

    def destroy(self):
        self.delete(ALL)
        GuiElement.destroy(self)

    def get_image(self,filename):
        if filename in self.canvas_image_files: return self.canvas_image_files[filename]
        dynTkLoadImage(self,filename)
        self.canvas_image_files[filename] = self.loadimage
        self.canvas_pyimages[str(self.loadimage)] = filename
        loadimage = self.loadimage
        self.loadimage = None
        return loadimage


    def get_itemconfig(self,item_id):
        dictionary = {}
        for entry in (
'anchor',
'height',
'state',
'tags',
'width',
'window',
'activefill',
'activestipple',
'disabledfill',
'disabledstipple',
'fill',
'font',
'justify',
'offset',
'stipple',
'text',
'activedash',
'activeoutline',
'activeoutlinestipple',
'activewidth',
'dash',
'dashoffset',
'default',
'relief',
'overrelief',
'disableddash',
'disabledoutline',
'disabledoutlinestipple',
'disabledwidth',
'outline',
'outlineoffset',
'outlinestipple',
'joinstyle',
'smooth',
'splinesteps',
'arrow',
'arrowshape',
'capstyle',
'activeimage',
'disabledimage',
'image',
'activebackground',
'activebitmap',
'activeforeground',
'background',
'bitmap',
'disabledbackground',
'disabledbitmap',
'disabledforeground',
'foreground',
'extent',
'start',
'style'):

            try:
                option = self.itemcget(item_id,entry)
                if entry == 'state' and option == "": option='normal'
                dictionary[entry] = (option,)
            except TclError: pass
        return dictionary

                
class Frame(GuiContainer,StatTkInter.Frame):
    def __init__(self,myname=None,**kwargs):
        _initGuiContainer(kwargs,StatTkInter.Frame,self,myname,"frame",True)

class LabelFrame(GuiContainer,StatTkInter.LabelFrame):

    def __init__(self,myname=None,**kwargs):
        _initGuiContainer(kwargs,StatTkInter.LabelFrame,self,myname,"labelframe",True)

class Button(GuiElement,StatTkInter.Button):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Button,self,myname,"button")

class Checkbutton(GuiElement,StatTkInter.Checkbutton):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Checkbutton,self,myname,"checkbutton")

class Entry(GuiElement,StatTkInter.Entry):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Entry,self,myname,"entry")

class Label(GuiElement,StatTkInter.Label):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Label,self,myname,"label")

class Message(GuiElement,StatTkInter.Message): # similiar Label

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Message,self,myname,"message")

class Radiobutton(GuiElement,StatTkInter.Radiobutton):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Radiobutton,self,myname,"radiobutton")

class Scale(GuiElement,StatTkInter.Scale):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Scale,self,myname,"scale")

class Scrollbar(GuiElement,StatTkInter.Scrollbar):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Scrollbar,self,myname,"scrollbar")


class Text(GuiElement,StatTkInter.Text):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Text,self,myname,"text")


class Spinbox(GuiElement,StatTkInter.Spinbox):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Spinbox,self,myname,"spinbox")


class Menubutton(GuiElement,StatTkInter.Menubutton):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.Menubutton,self,myname,"menubutton",True)

class PanedWindow(GuiElement,StatTkInter.PanedWindow):

    def __init__(self,myname=None,**kwargs):
        _initGuiElement(kwargs,StatTkInter.PanedWindow,self,myname,"panedwindow",True)

    def trigger_sash_place(self,time,index,x_coord,y_coord):
        self.after(time,lambda pwin = self, i = index, x = x_coord, y=y_coord, function = self.tkClass.sash_place: function(pwin,i,x,y))

    def add(self,child,**kwargs):
        global PANELAYOUT
        if child.Layout != PANELAYOUT: child._addToPackList()
        child.Layout = PANELAYOUT
        self.tkClass.add(self,child,**kwargs)

class Listbox(GuiElement,StatTkInter.Listbox):

    def __init__(self,myname=None,**kwargs):
        hastext = kwargs.pop('text',None)
        _initGuiElement(kwargs,StatTkInter.Listbox,self,myname,"listbox")
        if hastext != None: self.fillString(hastext)

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = self.tkClass.config(self)
            dictionary['text'] = (self.getString(),)
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            if 'text' in kwargs: 
                self.fillString(kwargs['text'])
                kwargs.pop('text',None)
            self.tkClass.config(self,**kwargs)

    def fillString(self,string):
        self.delete(0,END)		
        for e in string.split("\n"): self.insert(END,e)

    def fillList(self,elements):
        self.delete(0,END)		
        for e in elements: self.insert(END,e)


    def getString(self): return "\n".join(self.get(0,END))

    def getStringIndex(self,string): return self.get(0,END).index(str(string))


def link_command(me):
    mylink = me.getconfig('link')
    if mylink != "":
        mymaster = me.master
        mymaster.destroyContent()
        clear_grid(mymaster)
        mymaster.setconfig('link',mylink)
        if not widget_exists(this()): cdApp() # this is a secure place

class LinkLabel(Label):

    def __init__(self,myname="linklabel",**kwargs):
        self.link=""		
        if 'link' in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)
        if not 'font' in kwargs: kwargs['font'] = 'TkFixedFont 9 normal underline'
        if not 'fg' in kwargs: kwargs['fg'] = 'blue'
        Label.__init__(self,myname,**kwargs)
        self.do_event('<Button-1>',link_command,wishWidget = True)

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = Label.config(self,**kwargs)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
            if 'link' in kwargs: 
                self.link = kwargs['link']
                kwargs.pop('link',None)
            Label.config(self,**kwargs)

class LinkButton(Button):

    def __init__(self,myname="linkbutton",**kwargs):
        self.link=""		
        if 'link' in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)
        Button.__init__(self,myname,**kwargs)
        # not a command, because this would be a problem in the GUI Designer
        self.do_event('<ButtonRelease-1>',link_command,wishWidget = True)

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = Button.config(self)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
            if 'link' in kwargs: 
                self.link = kwargs['link']
                kwargs.pop('link',None)
            Button.config(self,**kwargs)

class CanvasItemWidget(GuiElement):

    def __init__(self,master,item_id,do_append = True):
        if master.canvas_widget != None: master.canvas_widget.dummy_destroy()
        name = master.type(item_id)
        self.master = master
        self.item_id = item_id
        self.tkClass = Dummy
        self.isContainer = False
        GuiElement.__init__(self,name,True)
        _Selection._container = master
        self.Layout = LAYOUTNEVER
        master.canvas_widget = self
        if do_append and name == 'image':
            self.config(photoimage = 'guidesigner/images/butterfly.gif')
            self.activephotoimage = ''
            self.disabledphotoimage = ''
 
    def destroy(self):
        self.master.canvas_widget = None
        self.master.delete(self.item_id)
        GuiElement.destroy(self)
        #setSelection(Create_Selection(self.master,self.master))
        
    def dummy_destroy(self):
        self.master.canvas_widget = None
        '''
        if self.master.type(self.item_id) == 'image':
            self.master.canvas_images[self.item_id] = self
            setWidgetSelection(self)
            name_index = getNameAndIndex()
            if name_index[0] != None: eraseEntry(name_index[0],name_index[1])
            cdApp()
        else: GuiElement.destroy(self)
        '''
        GuiElement.destroy(self)


    def config(self,**kwargs):
        if len(kwargs) == 0:
    
            if self.master.type(self.item_id) == 'image':
               self.photoimage = '' 
               self.activephotoimage = '' 
               self.disabledphotoimage = ''
               img = self.master.itemcget(self.item_id,'image')
               if img in self.master.canvas_pyimages: self.photoimage = self.master.canvas_pyimages[img]
               img = self.master.itemcget(self.item_id,'activeimage')
               if img in self.master.canvas_pyimages: self.activephotoimage = self.master.canvas_pyimages[img]
               img = self.master.itemcget(self.item_id,'disabledimage')
               if img in self.master.canvas_pyimages: self.disabledphotoimage = self.master.canvas_pyimages[img]

            return self.master.get_itemconfig(self.item_id)
        else:
            if 'photoimage' in kwargs:
                self.photoimage = kwargs['photoimage']
            if 'activephotoimage' in kwargs:
                self.activephotoimage = kwargs['activephotoimage']
            if 'disabledphotoimage' in kwargs:
                self.disabledphotoimage = kwargs['disabledphotoimage']

            self.master.itemconfig(self.item_id,**kwargs)


def CanvasItem(master,item_id,do_append = True):
    return CanvasItemWidget(master,item_id,do_append)
    '''
    if do_append or master.type(item_id) != 'image': return CanvasItemWidget(master,item_id,do_append)
    if master.canvas_widget != None: master.canvas_widget.dummy_destroy()
    this_widget = master.canvas_images.pop(item_id)
    master.canvas_widget = this_widget
    master.Dictionary.setElement('image',this_widget)
    _Selection._container = master
    _Selection._widget = this_widget
    '''

class MenuDelimiter(GuiElement):
    def __init__(self,myname="menu_delimiter",**kwargs):
        self.photoimage = kwargs.pop('photoimage','')
        self.myclass = kwargs.pop('myclass','')
        master,myname,select = _getMasterAndNameAndSelect(myname,"MenuItem",kwargs)
        self.master = master
        kwargs.pop('name',None)
        StatTkInter.Menu.entryconfig(self.master,0,**kwargs)
        self.tkClass = Dummy
        self.isContainer = False
        GuiElement.__init__(self,myname,select)
        self.Layout = LAYOUTNEVER
        if _Application.config_menuitems['delimiter'] == None:
            self.config()


    def config(self,**kwargs):
        index = 0

        if len(kwargs) == 0:
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
                    dictionary[entry] = (self.master.entrycget(index,entry),)
                except TclError: pass

            if _Application.config_menuitems['delimiter'] == None:
                base_dict = dict(dictionary)
                _Application.config_menuitems['delimiter'] = base_dict

            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            if 'photoimage' in kwargs: dynTkImage(self,kwargs.pop('photoimage'))
            StatTkInter.Menu.entryconfig(self.master,0,**kwargs)


class MenuItem(GuiElement):
    def __init__(self,myname="menuitem",mytype='command',**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.photoimage=kwargs.pop('photoimage','')
        

        self.mytype = mytype
        master,myname,select = _getMasterAndNameAndSelect(myname,"menuitem",kwargs)
        self.master = master
        self._addToPackList()
        kwargs.pop('name',None)
        StatTkInter.Menu.add(master,mytype,**kwargs)
        self.tkClass = Dummy

        self.isContainer = mytype == 'cascade'
        GuiElement.__init__(self,myname,select)
        self.Layout = MENUITEMLAYOUT
        if self.photoimage:
            kwargs['photoimage'] = self.photoimage
        self.config(**kwargs)

    # required for dynTkImage
    def __setitem__(self, key, item): 
        confdict = { key : item }
        self.config(**confdict)

    # required for dynTkImage
    def __delitem__(self, key, item): 
        confdict = { key : item }
        self.config(**confdict)


    def get_index(self):
        offset = self.master['tearoff']
        return self.master.get_item_index(self) + offset

    def destroy(self):
        offset = self.master['tearoff']
        index = self.getPackListIndex()
        self.master.delete(index+offset)
        self._removeFromPackList()
        GuiElement.destroy(self)



    def config(self,**kwargs):
        offset = self.master['tearoff']
        index = self.getPackListIndex() + offset
        if len(kwargs) == 0:
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
'indicatoron',
'image',
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
                    dictionary[entry] = (self.master.entrycget(index,entry),)
                except TclError: pass
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'myclass' in kwargs:
                self.myclass = kwargs.pop('myclass')

            if 'photoimage' in kwargs:
                dynTkImage(self,kwargs.pop('photoimage',''))
            else:
                set_photoimage_from_image(self,kwargs)
               
            if 'menu' in kwargs and isinstance(kwargs['menu'],Menu):
                # activate_menu(menu,menu_entry_widget)
                activate_menu(kwargs['menu'],self)
            StatTkInter.Menu.entryconfig(self.master,index,**kwargs)
                
    def set_menu(self,menu):
        offset = self.master['tearoff']
        index = self.getPackListIndex() + offset
        StatTkInter.Menu.entryconfig(self.master,index,menu=menu)        

def goIn():_Selection.selectIn()
def goOut(): _Selection.selectOut()

def cdDir():_Selection.selectContainer()
def cdApp(): setSelection(_AppRoot)

def gotoRoot():
    while not this().isMainWindow: goOut()

def gotoTop(): setSelection(_TopLevelRoot)

def Selection(): return copy(_Selection)

def setSelection(thisSelection):
    _Selection._container = thisSelection._container
    _Selection._widget = thisSelection._widget

def setWidgetSelection(widget,container=None): setSelection(Create_Selection(widget,container))
    

def do_command(function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False): this().do_command(function,parameters,wishWidget,wishEvent,wishSelf)
def do_event(eventstr,function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False): this().do_event(eventstr,function,parameters,wishWidget,wishEvent,wishSelf)
def do_receive(msgid,function,parameters=None,wishWidget=False,wishMessage=False): proxy.do_receive(container(),msgid,Callback(None,function,parameters,wishWidget,wishEvent=wishMessage).receive)


def ls():
    if _Selection._container is _Selection._widget:
        print("=> "+"\\.")
    else:
        print("   "+"\\.")

    for n,e in _Selection._container.Dictionary.elements.items():
        isNameSelected = False
        number = len(e)
        if _Selection._widget in e:
            print("=>",end=" ")
            isNameSelected = True
        else:
            print("  ",end=" ")

        if number == 1: print (n)
        else:
            if isNameSelected:
                i = 0
                while i < number and not e[i] is _Selection._widget: i = i+1
                print (n + " : " + str(i+1) + " of " + str(number) + " => index ["+str(i)+"]")
    
            else: print (n + " : " + str(number))

def showconf():
    dictionary = getconfdict()
    for n,e in dictionary.items():
        print(n,end=" : ")
        print(e)


def get(): return this().get()

def Selection(): return copy(_Selection)


'''
def allDictEntries(dictionary,cmd,data=None):
    for n,e in dictionary.items():
        ObjectStack.append((e,n,data))
        cmd()
        ObjectStack.pop()
'''
    
'''
GetContLayoutsCmd = EvCmd("Stack[-1] |= this().Layout")

def allContainerEntries(container,cmd=EvCmd("pass")):
    SelectionBefore=Selection()
    dictionary=container.Dictionary.elements
    elementlist = []
    values=dictionary.values()	

    for e in values:
        for n in e:
            elementlist.append(n)
    for e in elementlist:
        setWidgetSelection(e)
        cmd.execute()
    
    setSelection(SelectionBefore)
'''

def getNameAndIndex():
    name,index = container().Dictionary.getNameAndIndex(this())
    return (name,index) # todo, because not nice

def getContLayouts(container):
    children_list = container.Dictionary.getChildrenList()
    layout = 0
    for x in children_list: layout |= x.Layout
    return layout

def getAllWidgetsWithoutNoname(containerWidget):
    dictionary=containerWidget.Dictionary.elements
    elementlist = []
    for key,entry in dictionary.items():
        if key != NONAME:
            for x in entry:
                elementlist.append(x)
    return elementlist

def deleteAllWidgets(containerWidget):
    SelectionBefore=Selection()
    dictionary=containerWidget.Dictionary.elements
    elementlist = []
    values=dictionary.values()	

    for e in values:
        for x in e:
            elementlist.append(x)

    dictionary.clear()

    for x in elementlist: x.destroy()
    setSelection(SelectionBefore)

def deleteWidgetsForName(containerWidget,name):
    SelectionBefore=Selection()
    dictionary=containerWidget.Dictionary.elements
    elementlist=dictionary.pop(name,None)
    if elementlist != None:
        for x in elementlist: x.destroy()
    setSelection(SelectionBefore)

def eraseEntry(name,index):
    return _Selection._container.Dictionary.eraseEntry(name,index)

def destroyElement(name,index):
    OurSelection = Create_Selection(_Selection._container,_Selection._container)
    e = eraseEntry(name,index)
    if e != None: e.destroy()
    setSelection(OurSelection)

def renameElement(oldname,index,newname):
    e = eraseEntry(oldname,index)
    if e != None:
        dictionary=_Selection._container.Dictionary.elements	
        if not newname in dictionary: dictionary[newname] = [e]
        else: dictionary[newname].append(e)

        
def nl(): return "\n"

def Data(): return Self().data

def EraseNames():
    cdDir()
    container().Dictionary.elements.clear()

def Lock(): this().isLocked=True

# ============= New Save Functions ===================================================================

indent = ""

SAVE_ALL = False

def class_type(myclass):
    classString = str(myclass)
    begin = classString.find(".")+1
    end = classString.find("'",begin)
    return classString[begin:end]


def WidgetClass(widget):
    if isinstance(widget,MenuItem): return 'MenuItem'
    elif isinstance(widget,MenuDelimiter): return 'MenuDelimiter'
    elif isinstance(widget,LinkButton): return 'LinkButton'
    elif isinstance(widget,LinkLabel): return 'LinkLabel'
    else: return class_type(widget.tkClass)

def del_config_before_compare(dictionaryWidget):

    # delete what we don't want
    for entry in ("command","variable","image","menu"): dictionaryWidget.pop(entry,None)

    # delete empty or unchanged special cases
    if 'title' in dictionaryWidget and not isinstance(this(),Menu):
        if not this().title_changed: del dictionaryWidget['title']
    if 'geometry' in dictionaryWidget:
        if not this().geometry_changed: del dictionaryWidget['geometry']
    if 'link' in dictionaryWidget:
        if dictionaryWidget['link'] == '': del dictionaryWidget['link']
    if 'cursor' in dictionaryWidget:
        if dictionaryWidget['cursor'] == '': del dictionaryWidget['cursor']
    if 'myclass' in dictionaryWidget:
        if dictionaryWidget['myclass'] == '': del dictionaryWidget['myclass']
    if 'photoimage' in dictionaryWidget:
        if dictionaryWidget['photoimage'] == '': del dictionaryWidget['photoimage']
    #dictionaryWidget.pop('link',None) # links shouldn'd be saved. Otherwise we would have the widgets twice
    if isinstance(this(),Listbox) and dictionaryWidget['text'] == '': del dictionaryWidget['text']
    
def get_config_compare():

    if this().isMainWindow:
        dictionaryCompare = _AppConf
    elif isinstance(this(),MenuItem):
        dictionaryCompare = dict(_Application.config_menuitems[this().mytype])
        ConfDictionaryShort(dictionaryCompare)
    elif isinstance(this(),MenuDelimiter):
        dictionaryCompare = dict(_Application.config_menuitems['delimiter'])
        ConfDictionaryShort(dictionaryCompare)
    elif isinstance(this(),Menu):
        dictionaryCompare = dict(_Application.config_menuitems['menu'])
        ConfDictionaryShort(dictionaryCompare)
    else:
        if isinstance(this(),MenuItem): print("Shoudn't be")
        CompareWidget = this().tkClass(container())
        #CompareWidget = eval("StatTkInter."+thisClass+"(container())")
        dictionaryCompare = dict(CompareWidget.config())
        CompareWidget.destroy()
        ConfDictionaryShort(dictionaryCompare)

    return dictionaryCompare


def get_layout_dictionary():

    CompareWidget=StatTkInter.Frame(container(),width=0,height=0)
    if this().Layout == GRIDLAYOUT:
        CompareWidget.grid()
        layoutCompare = dict(CompareWidget.grid_info())
    else: 
        CompareWidget.place(x=-53287,y=-43217)
        layoutCompare = dict(CompareWidget.place_info())
    CompareWidget.destroy()

    layoutDict = layout_info()
    layoutDict.pop(".in",None)
    for n,e in dict(layoutDict).items():
        if e == layoutCompare[n]: layoutDict.pop(n,None)

    # Causes bug for tuple - padx, do we have some pixel object?
    #for n,e in layoutDict.items(): layoutDict[n] = str(e)

    for n,e in layoutDict.items():
        if class_type(type(e)) == "Tcl_Obj":
            layoutDict[n] = str(e)

    return layoutDict

def is_immediate_layout(): return this().Layout & (GRIDLAYOUT | PLACELAYOUT | MENULAYOUT)

def generate_keyvalues(dictionary):
    result = []
    for key, value in dictionary.items():
        if key == 'image':
            result.append("{}={}".format(key, value))
        else:
            result.append("{}={!r}".format(key, value))
    return ", ".join(result)

def save_immediate_layout(filehandle):
    if not is_immediate_layout(): return

    if this().Layout == GRIDLAYOUT:
        filehandle.write(indent+"grid(")
        layout = get_layout_dictionary()
    elif this().Layout == PLACELAYOUT:
        filehandle.write(indent+"place(")
        layout = get_layout_dictionary()
    elif this().Layout == MENULAYOUT:
        filehandle.write(indent+"select_menu(")
        layout = {}
        
    if len(layout) != 0: filehandle.write(generate_keyvalues(layout))
    filehandle.write(")")

def save_pack_entries(filehandle):

    packlist = container().PackList
    if len(packlist) == 0: return

    filehandle.write("\n")
    item_index = 1
    for e in packlist:
        filehandle.write(indent+"widget('")
        setWidgetSelection(e)
        nameAndIndex = getNameAndIndex()
        if nameAndIndex[1] == -1: filehandle.write(nameAndIndex[0]+"')")
        else: filehandle.write(nameAndIndex[0]+"',"+str(nameAndIndex[1])+")")

        if this().Layout == MENUITEMLAYOUT:
            filehandle.write(".layout(index="+str(item_index)+")\n")
            item_index += 1
        else:
       
            layoutWidget = layout_info()

            if this().Layout == PACKLAYOUT:
                CompareWidget=StatTkInter.Frame(container(),width=0,height=0)
                layoutWidget.pop(".in",None)
                filehandle.write(".pack(")
                CompareWidget.pack()
                layoutCompare = dict(CompareWidget.pack_info())
                CompareWidget.destroy()
            elif this().Layout == PANELAYOUT:
                filehandle.write(".pane(")
                layoutCompare = {'sticky': 'nesw', 'minsize': 0, 'width': '', 'pady': 0, 'padx': 0, 'height': ''}

            for n,e in dict(layoutWidget).items():
                if e == layoutCompare[n]: layoutWidget.pop(n,None)
            
            if len(layoutWidget) != 0:
                for n,e in layoutWidget.items():
                    if class_type(type(e)) == "Tcl_Obj":
                        layoutWidget[n] = str(e)
                filehandle.write(generate_keyvalues(layoutWidget))
           
            filehandle.write(")\n")
        
    if container().tkClass == StatTkInter.PanedWindow:

        index = 0
        sash_list = []
        while True:
            try:
                sash_list.append(container().sash_coord(index))
                index += 1
            except: break
        for i in range(len(sash_list)):
            filehandle.write(indent+"container().trigger_sash_place("+str((i+1)*500)+","+str(i)+","+str(sash_list[i][0])+","+str(sash_list[i][1])+")\n")

def save_sub_container(filehandle):
    if not this().isContainer: return False
    if not this().hasWidgets() and len(this().CODE) == 0: return False

    filehandle.write("\n"+indent+"goIn()\n\n")

    # entweder nur der Code des Untercontainers
    if (not this().hasWidgets() or this().onlysavecode) and len(this().CODE) != 0:
        filehandle.write("### CODE ===================================================\n")
        filehandle.write(this().CODE)
        filehandle.write("### ========================================================\n")

    # oder den ganzen Container sichern
    else:

        goIn()
        saveContainer(filehandle)
        goOut()

    filehandle.write("\n"+indent+"goOut()\n")
    return True

def check_individual_grid(multi_list):
    is_individual = False
    for entry in multi_list:
        if entry[0]:
            is_individual = True
            break
    return is_individual

def get_save_config():

    dictionaryConfig = getconfdict()
    del_config_before_compare(dictionaryConfig)
    dictionaryCompare = get_config_compare()

    for n,e in dict(dictionaryConfig).items():
        if n in dictionaryCompare:
            if e == dictionaryCompare[n]: dictionaryConfig.pop(n,None)

    for n,e in dictionaryConfig.items():
        if class_type(type(e)) == "Tcl_Obj":
            dictionaryConfig[n] = str(e)

    if this().grid_conf_rows != None:
        if this().grid_conf_rows[0] != 0:
            if this().grid_conf_individual_has:
                if check_individual_grid(this().grid_multi_conf_rows):
                    conf_list = [len(this().grid_multi_conf_rows)]
                    index = 0
                    for entry in this().grid_multi_conf_rows:
                        if entry[0]: conf_list.append((index,entry[1]['minsize'],entry[1]['pad'],entry[1]['weight']))
                        index += 1
                    dictionaryConfig['grid_multi_rows'] = repr(conf_list)
            dictionaryConfig['grid_rows'] =repr(this().grid_conf_rows)

    if this().grid_conf_cols != None:
        if this().grid_conf_cols[0] != 0:
            if this().grid_conf_individual_has:
                if check_individual_grid(this().grid_multi_conf_cols):
                    conf_list = [len(this().grid_multi_conf_cols)]
                    index = 0
                    for entry in this().grid_multi_conf_cols:
                        if entry[0]: conf_list.append((index,entry[1]['minsize'],entry[1]['pad'],entry[1]['weight']))
                        index += 1
                    dictionaryConfig['grid_multi_cols'] = repr(conf_list)
            dictionaryConfig['grid_cols'] = repr(this().grid_conf_cols)
            
    return dictionaryConfig

def save_widget(filehandle,name):
    if not this().save: return
    if isinstance(this(),CanvasItemWidget): return

    # write name ================================
    thisClass = WidgetClass(this())
 
    if isinstance(this(),MenuItem):
        filehandle.write(indent+thisClass+"('"+name+"','"+this().mytype+"'")
    else:
        filehandle.write(indent+thisClass+"('"+name+"'")

    conf_dict = get_save_config()
    
    if not (isinstance(this(),LinkLabel) or isinstance(this(),LinkButton)):
        if SAVE_ALL:
            conf_dict.pop('link',None)
        elif 'link' in conf_dict:
            mylink = conf_dict['link']
            conf_dict.clear()
            conf_dict['link'] = mylink
    
    if len(conf_dict) != 0:
        filehandle.write(","+generate_keyvalues(conf_dict)+")")
    else:
         filehandle.write(")")

    if 'link' in conf_dict and not (isinstance(this(),LinkLabel) or isinstance(this(),LinkButton)):
        if is_immediate_layout(): filehandle.write('.')
    else:
        if not save_sub_container(filehandle) and is_immediate_layout(): filehandle.write('.')
    save_immediate_layout(filehandle)
    filehandle.write("\n")


def save_canvas(filehandle):

    canvas = container()
    item_list = canvas.find_all()
    if len(item_list) == 0: return

    filehandle.write("\ncanvas=container()\n\n")
    for item in item_list:
        coords = canvas.coords(item)
        filehandle.write('coords = (')
        begin = True
        for entry in coords:
            if begin: begin = False
            else: filehandle.write(',')
            filehandle.write(str(entry))
        filehandle.write(')\n')
        filehandle.write('item = canvas.create_')
        filehandle.write(canvas.type(item))
        filehandle.write('(*coords)\n')

        config = canvas.get_itemconfig(item)
        ConfDictionaryShort(config)
        
        dictionaryCompare = CanvasDefaults[canvas.type(item)]

        for n,e in dict(config).items():
            if n in dictionaryCompare:
                if e == dictionaryCompare[n]: config.pop(n,None)

        if canvas.type(item) == 'image':

            img = canvas.itemcget(item,'image')
            if img in canvas.canvas_pyimages:
               config['photoimage'] = canvas.canvas_pyimages[img]
               
            img = canvas.itemcget(item,'activeimage')
            if img in canvas.canvas_pyimages:
               config['activephotoimage'] = canvas.canvas_pyimages[img]

            img = canvas.itemcget(item,'disabledimage')
            if img in canvas.canvas_pyimages:
               config['disabledphotoimage'] = canvas.canvas_pyimages[img]

            config.pop('image',None)
            config.pop('activeimage',None)
            config.pop('disabledimage',None)

        elif canvas.type(item) == 'window':
            window = canvas.itemcget(item,'window')
            if window != "":
                name,index = canvas.Dictionary.getNameAndIndexByStringAddress(window)
                if name != None:
                    if index == -1:
                        config['window'] = "widget('"+name+"')"
                    else:
                        config['window'] = "widget('"+name+"',"+str(index)+')'
            
        conf_copy = dict(config)
        for key,value in conf_copy.items():
            if value == '': del config[key]
            
        if len(config) != 0:
            filehandle.write('canvas.itemconfig(item,**{')
            begin = True
            for key,value in config.items():
                if begin: begin = False
                else: filehandle.write(',')
                if key == 'window':
                    filehandle.write("'"+key+"':"+value)
                else:
                    filehandle.write("'"+key+"':"+repr(value))
            filehandle.write("})\n\n")
        
        

def saveContainer(filehandle):

    dictionary = container().Dictionary.elements
 
    # sorted name list
    namelist = []
    for name in dictionary:
        if name != NONAME: namelist.append(name)
    namelist.sort()

    # now we save the widgets in the container
    for name in namelist:
        e = dictionary[name]
        for x in e:
            setWidgetSelection(x)
            save_widget(filehandle,name)

    save_pack_entries(filehandle)

    if isinstance(container(),Canvas): save_canvas(filehandle)

    # was ist mit gelocktem code? Der Code sollte geschrieben werden, nur die widgets nicht
    code_len = len(container().CODE)
    if code_len != 0:
        filehandle.write("\n### CODE ===================================================\n")
        if container().CODE[code_len-1] != '\n': container().CODE = container().CODE + '\n'
        filehandle.write(container().CODE)
        
        filehandle.write("### ========================================================\n")

def saveWidgets(filehandle,withConfig=False,saveAll=False):

    global SAVE_ALL
    if not this().save: return	# if this shouldn't be saved

    SAVE_ALL = saveAll

    if this() == container():
        
        if saveAll and isinstance(this(),Toplevel):
            _Selection._container = _TopLevelRoot._container
            save_widget(filehandle,getNameAndIndex()[0])
        else:

            if withConfig:
                conf_dict = get_save_config()
                conf_dict.pop('link',None)
                #if len(conf_dict) != 0: filehandle.write('config(**'+str(conf_dict)+")\n\n")
                if len(conf_dict) != 0: filehandle.write('config('+generate_keyvalues(conf_dict)+")\n\n")
            saveContainer(filehandle)

    else: 
        save_widget(filehandle,getNameAndIndex()[0])
        
    SAVE_ALL = False

# ========== End save functions ===========================================================

# ========== Save Access ===========================================================


AccessDictionary = {}
CamelCaseDictionary = {}


ACCESS_DEPTH_WIDGET = False

def set_AccessDepth_Widgets(flag):
    global ACCESS_DEPTH_WIDGET
    ACCESS_DEPTH_WIDGET = flag

def saveAccessSubContainer(filehandle):
    if not this().hasWidgets(): return False

    filehandle.write("        goIn()\n")

    # entweder nur der Code des Untercontainers
    if this().onlysavecode and len(this().CODE) != 0: pass
    else:
        goIn()
        saveAccessContainer(filehandle)
        goOut()

    filehandle.write("        goOut()\n")
    return True

def getCamelCaseName(name):
    newname = name
    
    if newname in CamelCaseDictionary or newname in globals():
        nr = 1
        while True:
            newname = name+'_'+ str(nr)
            if newname not in CamelCaseDictionary:
                break
            nr+=1
    CamelCaseDictionary[newname] = None
    return newname


def getAccessName(name):
    newname = name
    if newname in AccessDictionary:
        nr = 1
        while True:
            newname = name+'_'+ str(nr)
            if newname not in AccessDictionary:
                break
            nr+=1

    AccessDictionary[newname] = None
    return newname



def saveAccessWidget(filehandle,name_index):
    if not this().save: return
    if isinstance(this(),CanvasItemWidget): return

    # write name ================================
    
    savename = getAccessName(name_index[0])
    if this().isContainer:
        if name_index[1] == -1:
            filehandle.write("        goto('"+name_index[0]+"')\n")
        else:
            filehandle.write("        goto('"+name_index[0]+"',"+str(name_index[1])+")\n")
        filehandle.write("        self."+savename+" = this()\n")
        saveAccessSubContainer(filehandle)
    else:
        if name_index[1] == -1:
            filehandle.write('        self.'+savename+" = widget('"+name_index[0]+"')\n")
        else:
            filehandle.write('        self.'+savename+" = widget('"+name_index[0]+"',"+str(name_index[1])+")\n")

def saveAccessContainer(filehandle):

    dictionary = container().Dictionary.elements
 
    # sorted name list
    namelist = []
    for name in dictionary:
        if name != NONAME: namelist.append(name)
    namelist.sort()
    # now we save the widgets in the container
    for name in namelist:
        e = dictionary[name]
        index = 0
        for x in e:
            if x.isContainer or ACCESS_DEPTH_WIDGET:
                setWidgetSelection(x)
                if len(e) == 1: saveAccessWidget(filehandle,(name,-1))
                else:saveAccessWidget(filehandle,(name,index))
            index += 1
 
def saveAccess(filehandle,isWidgets=False):
    global ACCESS_DEPTH_WIDGET

    if not this().save: return	# if this shouldn't be saved

    ACCESS_DEPTH_WIDGET = isWidgets
    AccessDictionary.clear()

    filehandle.write('class Access:\n\n    def __init__(self):\n\n')
   
    if this() == container():
        saveAccessContainer(filehandle)
    else:
        if isinstance(container(),_CreateTopLevelRoot):
            filehandle.write('        gotoTop()\n')
            
        saveAccessWidget(filehandle,getNameAndIndex())

    AccessDictionary.clear()
    ACCESS_DEPTH_WIDGET = False
    
# ========== End save Access ===========================================================

# ========== Save Export ===========================================================

def saveExport(readhandle,writehandle,flag=False):

    EXPORT_NAME = flag # export with or without names
    export_info = { 'NameNr': 0 , 'need_ext' : False }

    # ExportNames contains the widgwet names {widget : (name,nameCamelCase)}
    # entries are made by exportContainer
    # and the first one by saveExport_intern 
    ExportNames = {} 

    def getAccessAllName(name):
        newname = '#{}_{}'.format(export_info['NameNr'],name)
        export_info['NameNr'] += 1
        return newname



    # ExportBuffer for writing to memory, later write to file
    # used by ExportList and and by saveExport_intern as exphandle
    class ExportBuffer:
        
        def __init__(self):
            self.stringbuffer = []
            
        def write(self,text):
            self.stringbuffer.append(text)
            
        def get(self):
            return ''.join(self.stringbuffer)
            
        def reset(self):
            self.stringbuffer = []

    # ExportList used for checking, whether classnames are double
    # Created in saveExport_intern, which writes the contents to file
    # used also by exportSubcontainer, which opens a list entry
    # for each container
    class ExportList(ExportBuffer):
        
        def __init__(self):
            ExportBuffer.__init__(self)
            self.export_list = []
            self.name = None
            
        def close(self):
            if self.name != None:
                self.export_list.append((self.name,self.get()))
                self.name = None
            self.reset()
        
        def open(self,name):
            self.close()
            self.name = name
            
        def getlist(self):
            return self.export_list
   

    # makeCamelCase used by exportContainer for creating CamelCase names
    # for container classes
    def makeCamelCase(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

    # name_expr used by exportWidget for EXPORT_NAMES
    # the name of a widget shall not be captalisized in tkinter
    def name_expr(name):
        return "name='{}'".format(name)

    # get_grid_dict used by exportWidget
    # delivers a dictionary with grid_cols, grid_rows, grid_multi_cols,grid_multi_rows
    def get_grid_dict(confdict):
        grid_dict = {}
        for entry in ('grid_cols','grid_rows','grid_multi_cols','grid_multi_rows'):
            value = confdict.pop(entry,None)
            if value != None: grid_dict[entry] = value
        return grid_dict

    def write_config_parameters(filehandle,colon,var_name):
        # generate other config parameters
        conf_dict = get_save_config()

        # delete what can't be generated by export
        conf_dict.pop('link',None)
        conf_dict.pop('myclass',None)

        # save what has to be treated after regular parameters
        photoimage = conf_dict.pop('photoimage',None)
        if photoimage:
            conf_dict['image'] = 'self.' + var_name + '_img'
        lbtext = None
        if isinstance(this(),Listbox): lbtext = conf_dict.pop('text',None)
        grid_dict = get_grid_dict(conf_dict)

        # generate regular parameters
        if len(conf_dict) != 0:
            filehandle.write(colon + generate_keyvalues(conf_dict)+")\n")
        else:
             filehandle.write(")\n")

        # !!! Achtung grid sollte im container behandelt werden und nicht zweimal
        # add irregular parameters as additionale functions
        if len(grid_dict) != 0:
            export_info['need_ext'] = True
            filehandle.write('        tk.grid_table(self.'+var_name+','+generate_keyvalues(grid_dict)+')\n')
        if lbtext:
            export_info['need_ext'] = True
            filehandle.write('        tk.fill_listbox_with_string(self.'+var_name+','+repr(lbtext)+')\n')
        # if photoimage: filehandle.write('        ext.dynTkImage(self.'+var_name+",'"+photoimage+"')\n")


    # export_immediate_layout used by exportWidget
    # a immediate layout shall be done immediately after creating the widget
    # these layouts are GRID, PLACE and MENU
    def export_immediate_layout(filehandle,name):
        if not is_immediate_layout(): return

        filehandle.write('        self')

        if this().Layout == GRIDLAYOUT:
            filehandle.write('.'+name+".grid(")
            layout = get_layout_dictionary()
        elif this().Layout == PLACELAYOUT:
            filehandle.write('.'+name+".place(")
            layout = get_layout_dictionary()
        elif this().Layout == MENULAYOUT:
            filehandle.write("['menu'] = self."+name+"\n")
            return
            
        if len(layout) != 0: filehandle.write(generate_keyvalues(layout))
        filehandle.write(")\n")

    def get_write_expression(var_name,class_name,optional,widget_name=None):
        if widget_name:
            return '        self.' + var_name + ' = ' + class_name + '(self' + optional + ',' + name_expr(widget_name)
        else:
            return '        self.' + var_name + ' = ' + class_name + '(self' + optional

    def get_write_add_menuitem(item_type,widget_name):
        if widget_name:
            export_info['need_ext'] = True
            return '        self.add_' + item_type + '(' + name_expr(widget_name)
        else:
            return '        self.add_' + item_type + '('

    def export_menu_entry(filehandle,var_name,class_name):
        optional = ''
        filehandle.write(get_write_expression(var_name,class_name,optional,getAccessAllName(var_name)))
        write_config_parameters(filehandle,",",var_name)

    def call_write_menu(filehandle,widget,widget_name):

        setWidgetSelection(widget)
        var_name = getAccessName(widget_name)
        camelcase_name = makeCamelCase(var_name)
        camelcase_name = getCamelCaseName(camelcase_name)
        ExportNames[this()] = (var_name,camelcase_name)
        export_menu_entry(filehandle,var_name,camelcase_name)
        return var_name if widget.Layout==MENULAYOUT else None , camelcase_name

    def generate_menu_entries(filehandle):
        activemenu_varname = None
        create_class_list = []

        dictionary = this().Dictionary.elements
        # sorted name list
        namelist = []

        # alphabetical order
        for name in dictionary:
            if name != NONAME: namelist.append(name)
        namelist.sort()

        for widget_name in namelist:
            e = dictionary[widget_name]
            for widget in e:
                var_name,camelcase_name = call_write_menu(filehandle,widget,widget_name)
                create_class_list.append((camelcase_name,widget))
                if var_name:
                    activemenu_varname = var_name
        return activemenu_varname,create_class_list
                    

        


    # exportWidget called by exportContainer
    # generates a widget and maybe an immediate layout
    def exportWidget(filehandle,var_name,camelcase_name,uni_name):

        create_menu_list = []

        
        # ================== return for not saving or still not implemented ==================
        #if the widget is marked for not saving, then don't do it
        if not this().save: return create_menu_list
        # Canvas Items not implemented now
        if isinstance(this(),CanvasItemWidget): return create_menu_list
       

        # ================== write widget definition ==========================================
         
        # class of widget
        thisClass = WidgetClass(this())

        # own class name, if has widgets
        if this().hasWidgets():
            class_name = camelcase_name
        else:
            class_name = 'tk.'+thisClass
 
        if isinstance(this(),LinkLabel):
            class_name = 'tk.Label'
        elif isinstance(this(),LinkButton):
            class_name = 'tk.Button'


        optional = ''
        colon = ','
        if isinstance(this(),MenuItem):
            optional = "'"+this().mytype

        if this().photoimage:
            filehandle.write('        self.' + var_name+"_img = tk.PhotoImage(file = '" + this().photoimage + "')\n")

        if isinstance(this(),MenuDelimiter):
            if EXPORT_NAME:
                export_info['need_ext'] = True
                filehandle.write('        self.entryconfig(0' + ',' + name_expr(uni_name))
            else:
                filehandle.write('        self.entryconfig(0')
            
        elif isinstance(this(),MenuItem):
            if this().mytype == 'cascade' :
                # die Menus in der Cascade abarbeiten
                # Schritt 1:
                #   wir erzeugen Menudefinitionen, etwa:
                # self.menu_x = tk.Menu(self,optional name, optional cascade = cascadenname,existing parameters)
                #
                # Schritt 2:
                #   Ruckübergabe zu erzeugender ContainerClassen
                #

                # Implementierung in Form einer speziellen Container Funktion
                this_widget = this()
                active_menu,create_classes = generate_menu_entries(filehandle)
                create_menu_list.extend(create_classes)
                setWidgetSelection(this_widget)
                filehandle.write(get_write_add_menuitem(this().mytype,uni_name))
                if not uni_name: colon = ''
                if active_menu:
                    filehandle.write(colon + 'menu=self.' +active_menu)
                    colon = ','
            else:
                filehandle.write(get_write_add_menuitem(this().mytype,uni_name))
                if not uni_name: colon = ''

        else:
            filehandle.write(get_write_expression(var_name,class_name,optional,uni_name))


        # ================== write config parameters ==========================================
        write_config_parameters(filehandle,colon,var_name)

        # ================ write immediate layout ==================================================
        export_immediate_layout(filehandle,var_name)

        return create_menu_list

    # export_pack_entries called by exportContainer
    # at the end of the container generation pach und menuitem laqyout has to be done
    def export_pack_entries(filehandle):

        # not neccessary, because now MenuItems in correct order
        if isinstance(container(),Menu):
            return

        # packlist, return if empty
        packlist = container().PackList
        if len(packlist) == 0: return

        item_index = 1

        for e in packlist:

            setWidgetSelection(e)
            name = ExportNames[this()][0]


            filehandle.write(indent+"        self.")

            # no name for PANELAYOUT, because there has to be self.add
            if this().Layout != PANELAYOUT: filehandle.write(name)

            if this().Layout == MENUITEMLAYOUT:
                filehandle.write(".layout(index="+str(item_index)+")\n")
                item_index += 1
            else: # Packlayout and Panelayout
           
                layoutWidget = layout_info()

                if this().Layout == PACKLAYOUT:
                    CompareWidget=StatTkInter.Frame(container(),width=0,height=0)
                    layoutWidget.pop(".in",None)
                    filehandle.write(".pack(")
                    CompareWidget.pack()
                    layoutCompare = dict(CompareWidget.pack_info())
                    CompareWidget.destroy()
                elif this().Layout == PANELAYOUT:
                    filehandle.write("add(self."+name) # point already written 'self.'
                    layoutCompare = {'sticky': 'nesw', 'minsize': 0, 'width': '', 'pady': 0, 'padx': 0, 'height': ''}

                for n,e in dict(layoutWidget).items():
                    if e == layoutCompare[n]: layoutWidget.pop(n,None)
     
                if len(layoutWidget) != 0:
                    if this().Layout == PANELAYOUT: filehandle.write(",")
                    
                    for n,e in layoutWidget.items():
                        if class_type(type(e)) == "Tcl_Obj":
                            layoutWidget[n] = str(e)
     
                    filehandle.write(generate_keyvalues(layoutWidget))

                filehandle.write(")\n")

            
        # if the container is a PanedWindow, we add the sashes and trigger, that they update correct after 500 ms
        if container().tkClass == StatTkInter.PanedWindow:

            index = 0
            sash_list = []
            while True:
                try:
                    sash_list.append(container().sash_coord(index))
                    index += 1
                except: break

            for i in range(len(sash_list)):
                export_info['need_ext'] = True
                filehandle.write("        tk.trigger_sash_place(self,"+str((i+1)*500)+","+str(i)+","+str(sash_list[i][0])+","+str(sash_list[i][1])+")\n")

    def get_key_of_value(value,dictionary):
        for key,widgetlist in dictionary.items():
            for widget in widgetlist:
                if value == widget:
                    return key
        return None


    def call_exportWidget(filehandle,widget,widget_name):
        if isinstance(widget,CanvasItemWidget): return []

        setWidgetSelection(widget)
        var_name = (widget_name)

        camelcase_name = None
        if this().hasWidgets():
            camelcase_name = makeCamelCase(var_name)
            camelcase_name = getCamelCaseName(camelcase_name)

        
        uni_name = getAccessAllName(widget_name) if EXPORT_NAME else None
        ExportNames[this()] = (var_name,camelcase_name)
        return exportWidget(filehandle,var_name,camelcase_name,uni_name)


    # exportContainer called by exportSubcontainer
    # calls exportWidget for the widgets in this container
    # calls after this exportSubcontainer for the widgets, which are containers and have widgets
    def exportContainer(filehandle):

        create_menu_list=[]

        dictionary = container().Dictionary.elements
        AccessDictionary.clear()

        # sorted name list
        namelist = []

        # alphabetical order
        for name in dictionary:
            if name != NONAME: namelist.append(name)
        namelist.sort()
 
        # for MenuDelimiter and MenuItems
        if isinstance(container(),Menu):
            accesslist = []

            # first look for MenuDelimiter
            if container()['tearoff']:
                ready = FALSE
                for name,widgetlist in dictionary.items():
                    if name != NONAME:
                        for widget in widgetlist:
                            if isinstance(widget,MenuDelimiter):
                                accesslist.append((name,widget))
                                ready = True
                            break
                    if ready: break

            # now append MenuItems in Layout order
            packlist = container().PackList
            for widget in packlist:
                foundname = get_key_of_value(widget,dictionary)
                if foundname and foundname != NONAME:
                    accesslist.append((foundname,widget))

            for item in accesslist:
                widget_name = item[0]
                widget = item[1]
                create_menu_list.extend(call_exportWidget(filehandle,widget,widget_name))

        else:

            # now we save the widgets in the container
            for widget_name in namelist:
                e = dictionary[widget_name]
                for widget in e:
                    call_exportWidget(filehandle,widget,widget_name)

            export_pack_entries(filehandle)

        # now we save sub containers ==============================================

    
        # first export menus

        for menu in create_menu_list:
            setWidgetSelection(menu[1]) # widget
            exportSubcontainer(filehandle,menu[0]) # camelcase_name

        # then export other classes
        for widget_name in namelist:
            e = dictionary[widget_name]
            for x in e:
                setWidgetSelection(x)
                # shall not be called for MenuItem type 'cascade', which has widgets
                if this().hasWidgets() and not isinstance(this(),MenuItem): exportSubcontainer(filehandle,ExportNames[this()][1]) # camelcase_name

        AccessDictionary.clear()

    # exportSubcontainer called by exportContainer and saveExport_intern
    # defines a class for a container widget, which haas widgets
    def exportSubcontainer(filehandle,class_name):

        filehandle.open(class_name)
        
        thisClass = WidgetClass(this())
        
        if isinstance(this(),Tk): thisMaster = ''
        else: thisMaster = ',master'
            
        filehandle.write('class '+class_name+'(tk.'+thisClass+'):\n\n')
        filehandle.write('    def __init__(self'+thisMaster+',**kwargs):\n')
        filehandle.write('        tk.'+thisClass+'.__init__(self'+thisMaster+',**kwargs)\n')
     
        # only for Application or Toplevel 
        if isinstance(this(),Tk) or isinstance(this(),Toplevel):
            conf_dict = get_save_config()
            conf_dict.pop('link',None)
            conf_dict.pop('myclass',None)

            tit = conf_dict.pop('title',None)
            if tit: filehandle.write('        self.title('+repr(tit)+")\n")
            geo = conf_dict.pop('geometry',None)
            if geo: filehandle.write('        self.geometry('+repr(geo)+")\n")
            
            grid_dict = get_grid_dict(conf_dict)
            if len(grid_dict) != 0:
                filehandle.write('        tk.grid_table(self,'+generate_keyvalues(grid_dict)+')\n')
                print("gridtable in Class Definition")

            if len(conf_dict) != 0: filehandle.write('        self.config('+generate_keyvalues(conf_dict)+")\n")

        # after class definition export the content     
        goIn()
        exportContainer(filehandle)
        goOut()
        
    def saveExport_intern(readhandle,writehandle):

        export_info['NameNr'] = 0
        export_info['need_ext'] = False

        # clear global dictionary
        CamelCaseDictionary.clear()

        # writehandle to empty buffer
        exphandle = ExportBuffer()

        # name of application or toplevel
        name = getNameAndIndex()[0]
        name = getCamelCaseName(name)
        ExportNames[this()] = (name,name)

        # generate the GUI 
        exp_list = ExportList()
        exportSubcontainer(exp_list,name)
        exp_list.close()

        # check for double class names and return an error, if ths had happened
        class_list = exp_list.getlist()
        class_dict = {}
        for entry in class_list:

            if entry[0] in class_dict:
                error = "Error: class name '" + entry[0] + "' is double!"
                CamelCaseDictionary.clear()
                ExportNames.clear()
                return error
            class_dict[entry[0]] = entry[1]
            
        # write imports
        if export_info['need_ext']:
            writehandle.write('import DynTkExtend as tk\n')
        else:
            writehandle.write('import tkinter as tk\n')
        writehandle.write('#import DynTkInter as tk # for GuiDesigner\n\n')


        # if no readhandle then write the generated GUI to file
        if readhandle == None:
            writehandle.write(exphandle.get())
            for entry in class_list:
                writehandle.write(entry[1]+"\n")
            if this() == _Application:
                writehandle.write("#"+name+"().mainloop('guidesigner/Guidesigner.py') # for GuiDesigner\n")
                writehandle.write(name+"().mainloop()\n")

        # if readhandle then merge the generated GUI with file
        else:
            isEnd = False
            while True:
                line = readhandle.readline()
                if line.find("mainloop(") >= 0:
                    if len(class_dict) != 0:
                        writehandle.write("# =======  New GUI Container Widgets ======================\n\n")
                        
                        for entry in class_list:
                            if entry[0] in class_dict:
                                writehandle.write(entry[1])
                                class_dict.pop(entry[0],None)
                        writehandle.write("\n# =======  End New GUI Container Widgets ==================\n\n")
                            
                if not line:
                    isEnd = True
                    break
                if line[0:5] == "class":
                    end = line.find("(")
                    if end >= 0:
                        class_name = line[5:end].strip()
                        if class_name in class_dict:
                            while readhandle.readline().find('__init__') < 0: pass
                            
                            while True:
                                rl=readhandle.readline()
                                if not rl:
                                    isEnd = True
                                    break
                                else:
                                   if rl.strip() == '': break
                            if isEnd: break
                            writehandle.write(class_dict[class_name])
                            class_dict.pop(class_name,None)
                            line = "\n"
                writehandle.write(line)

        
        # clear global dictionary
        CamelCaseDictionary.clear()


        return 'OK'

    return saveExport_intern(readhandle,writehandle)

def decapitalize(name):
    return name[0].lower()+name[1:]


# ========== Save Export ===========================================================
   

def DynImportCode(filename):
    global LOADforEdit

    ĥandle = None
    try:
        handle = open(filename,'r')
    except: 
        print("Couldn't open file: " + filename)
        return

    guicode = ""
    while True:
        isEnd = False
        while True:
            line = handle.readline()
            if not line:
                isEnd = True
                break
            if line[0:9] == "### CODE ": break

            guicode+=line

        evcode = compile(guicode,filename,'exec')
        eval(evcode)
        if isEnd: break

        code = ""	
        while True:
            line = handle.readline()
    
            if not line or line[0:5] == "### =":
                if not line: print("Code end '### =' missing in file: ",filename)
                container().CODE = code
                if not LOADforEdit:	
                    evcode = compile(code,filename,'exec')
                    eval(evcode)
                break

            code+=line
        guicode = ""
    handle.close()

LOADwithCODE = False
LOADforEdit = False

def setLoadForEdit(flag):
    global LOADwithCODE
    global LOADforEdit
    LOADwithCODE = flag;
    LOADforEdit = flag

def setLoadWithCode(flag):
    global LOADwithCODE
    LOADwithCODE = flag;

def DynLoad(filename):
    if LOADwithCODE: DynImportCode(filename)
    else:
        try:
            handle = open(filename,'r')
        except: 
            print("Couldn't open file: " + filename)
            return
        code = handle.read()
        evcode = compile(code,filename,'exec')
        exec(evcode)

_DynLoad = DynLoad

def DynAccess(filename,par=None,parent=None):
    selection_before = Selection()
    if parent != None: setSelection(Create_Selection(parent,parent))
    exec(compile(open(filename, "r").read(), filename, 'exec'))
    if par == None: retval = locals()['Access']()
    elif type(par) is tuple or type(par) is list: retval = locals()['Access'](*par)
    else: retval = locals()['Access'](par)
    setSelection(selection_before)
    return retval

def load_script(filename,classlist = None, parent=None):
    if type(classlist) is list or type(classlist) is tuple: DynAccess('dyntkinter/LoadScript.py',(filename,classlist),parent)
    myparent = classlist
    selection_before = Selection()
    if myparent != None: setSelection(Create_Selection(myparent,myparent))
    exec(compile(open(filename, "r").read(), filename, 'exec'))
    setSelection(selection_before)

def DynLink(filename):
    goIn()
    retval = DynLoad(filename)
    goOut()
    return retval

def quit(): _Application.quit()

def do_action(actionid,function,parameters=None,wishWidget=False,wishMessage=False,wishSelf=False): this().do_action(actionid,function,parameters,wishWidget,wishMessage,wishSelf)
def activateAction(actionid,flag): this().activateAction(actionid,flag)
def getActionCallback(actionid): return this().getActionCallback(actionid)


def undo_action(widget,actionid):
    if widget in ACTORS: widget._undo_action(actionid)


def informImmediate(widget,actionid,msg=None):
    if widget in ACTORS:
        if actionid in widget.actions:
            if widget.actions[actionid][0] == True:
                widget.actions[actionid][1].receive(msg)

def inform(widget,actionid,message=None): execute_lambda(lambda wi = widget, actid=actionid, msg=message, funct=informImmediate: funct(wi,actid,msg))
def _informLater(cmd): execute_lambda(cmd)
def informLater(ms,widget,actionid,message=None): _Application.after(ms,_informLater,lambda wi = widget, actid=actionid, msg=message, funct=informImmediate: funct(wi,actid,msg))

def gui(): DynLoad("guidesigner/Guidesigner.py")

def select_menu(): this().select_menu()


def get_entry_as_string(value):
    if type(value) is tuple:
        tlist=[]
        for entry in value: tlist.append(str(entry))
        return ' '.join(tlist)
    else: return str(value)
    

# ========== For Compatibility with Export with Names =============

def trigger_sash_place(pane_window,time,index,x_coord,y_coord):
    pane_window.after(time,lambda i = index, x = x_coord, y=y_coord, function = pane_window.sash_place: function(i,x,y))

def fill_listbox_with_string(listbox,string):
    listbox.delete(0,END)		
    for e in string.split("\n"): listbox.insert(END,e)

# ======== refresh of top window ===================================

class Geometry_Refresh():

    def __init__(self,time,widget):
        self.widget = widget
        widget.after(time,self.call)

    def call(self):
        my_geo = self.widget.geometry()
        find_plus = my_geo.find("+")
        find_minus = my_geo.find("-")
        if find_plus < 0: begin = find_minus
        elif find_minus < 0: begin = find_plus
        else: begin = min(find_plus,find_minus)
        my_geo = my_geo[begin:]

        self.widget.geometry('') # refresh the geometry of the GUI Designer
        self.widget.withdraw()
        self.widget.geometry(my_geo)
        self.widget.deiconify()
        
def relocate_widget(widget,new_destination):
    name,index = widget.master.Dictionary.getNameAndIndex(widget)
    widget.master.Dictionary.eraseEntry(name,index)
    new_destination.Dictionary.setElement(name,widget)
    widget.master = new_destination

def activate_menu(menu,menu_entry_widget):
    if menu.master != menu_entry_widget:
        relocate_widget(menu,menu_entry_widget)
    menu.select_menu()
    
