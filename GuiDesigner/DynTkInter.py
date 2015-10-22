# encoding: UTF-8
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
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.


import tkinter as StatTkInter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from copy import copy
import traceback
import queue
import proxy as dynproxy

def dummyfunction(par):pass

class Create_Selection:

    def __init__(self,widget=None,container = None):
        if widget == None: # only for initialisation
            self._widget = None
            self._container = None
        else:
            self._widget = widget
            if container != None and container.isContainer: self._container = container
            else:
                master = widget.master
                if master == None: self._container = widget
                else: self._container = master

    def selectContainer(self): self._widget = self._container

    def selectWidget(self,widget):
        self._widget = widget
        master = widget.master
        if master == None or self._widget.isMainWindow: self._container = widget
        else: self._container = master

    def selectOut(self):
        if not self._widget.isMainWindow: self.selectWidget(self._container)

    def selectIn(self):
        if not self._widget.isLocked: self._container = self._widget
        


_Selection=Create_Selection()
_TopLevelRoot = Create_Selection()

NOLAYOUT = 0
PACKLAYOUT = 1
GRIDLAYOUT = 2
PLACELAYOUT = 4
PANELAYOUT = 8
MENUITEMLAYOUT = 16
MENULAYOUT = 32
LAYOUTNEVER = 64
LAYOUTALL = LAYOUTNEVER-1

ACTORS = {}
EXISTING_WIDGETS = {}

_AppRoot = Create_Selection()
_AppConf = None

_Application = None

     
#_queue = queue.Queue()
     
#def _execute(*args):
    #try: _queue.get()()
    #except: print("execute error")

#def execute(command):
    #_queue.put(command)
    #_Application.event_generate("<<EXEC>>", when="tail")

def widget_exists(widget): return widget in EXISTING_WIDGETS

class Dummy: pass

def grid_configure_multi(data):
    count = data[0]
    multi = []
    for i in range(count): multi.append([False,None])
    for i in range(len(data)):
        if i != 0:
            multi[data[i][0]] = [True,{'minsize':data[i][1],'pad':data[i][2],'weight':data[i][3]}]
    return multi


def grid_configure_cols(cont):

    cols = cont.grid_conf_cols[0]

    if len(cont.grid_multi_conf_cols) == 0:
        for i in range(cols): cont.grid_multi_conf_cols.append([False,None])

    to_insert =  {'minsize':cont.grid_conf_cols[1],'pad':cont.grid_conf_cols[2],'weight':cont.grid_conf_cols[3]}
    
    for col in range(cols):
        if cont.grid_multi_conf_cols[col][0] == False:
            cont.grid_multi_conf_cols[col][1] = dict(to_insert)

    for col in range(cols):
        cont.grid_columnconfigure(col,**(cont.grid_multi_conf_cols[col][1]))

def grid_configure_rows(cont):

    rows = cont.grid_conf_rows[0]

    if len(cont.grid_multi_conf_rows) == 0:
        for i in range(rows): cont.grid_multi_conf_rows.append([False,None])

    to_insert =  {'minsize':cont.grid_conf_rows[1],'pad':cont.grid_conf_rows[2],'weight':cont.grid_conf_rows[3]}
    
    for row in range(rows):
        if cont.grid_multi_conf_rows[row][0] == False: cont.grid_multi_conf_rows[row][1] = dict(to_insert)

    for row in range(rows):
        cont.grid_rowconfigure(row,**(cont.grid_multi_conf_rows[row][1]))


class GuiElement:

    def __init__(self,name="nn",select=True):

        EXISTING_WIDGETS[self] = None
        self.is_mouse_select_on = False
        
        self.reset_grid()
        
        if select: _Selection._widget = self

        if self.master != None: self.master.Dictionary.setElement(name,self)

        if self.isContainer: 
            self.Dictionary = GuiDictionary()
            self.PackList = []
            self.CODE = ""
            self.onlysavecode = False

        self.mydata = None
        self.save =True
        self.actions = {}
        self.menu_ref = None

        global NOLAYOUT
        self.Layout = NOLAYOUT
        self.hasConfig = True
        self.isMainWindow = False
        #self.isDestroyed = False
        if self.isContainer: self.isLocked=False
        else: self.isLocked = True

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
            if 'myclass' in kwargs:
                self.myclass = kwargs.pop('myclass')
            self.tkClass.config(self,**kwargs)

    def lock(): isLocked = Tue

    def myRoot(self):
        selection_before = Selection()
        setWidgetSelection(self)
        gotoRoot()
        rootwidget=this()
        setSelection(selection_before)
        return rootwidget

    def container(self): return Create_Selection(self)._container
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
        self.destroyActions()

        if self.isContainer: undo_receiveAll(self)

        if self.isMainWindow: setSelection(Create_Selection(self,_TopLevelRoot._container))
        else: setWidgetSelection(self)

        name_index = getNameAndIndex()
        if name_index[0] != None: eraseEntry(name_index[0],name_index[1])

        if self.Layout == PACKLAYOUT or self.Layout == PANELAYOUT: self._removeFromPackList()
        if self.tkClass != Dummy:
            if self.tkClass == Tk: self.quit()
            else: 
                if isinstance(self.master,MenuItem): self.master = self.myRoot()
                if widget_exists(self): self.tkClass.destroy(self)

        EXISTING_WIDGETS.pop(self,None)		
        cdApp()
        

    def destroyContent(self):
        if not self.isContainer: print("destroyContent requires a container widget")
        else:
            self.CODE = ""
            undo_receiveAll(self)
            deleteAllWidgets(self)

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
        activwidget = self.master if (isinstance(self.master,MenuItem) or isinstance(self.master,Menubutton)) else self.myRoot()
        activwidget.menu_ref = None
        activwidget.config(menu='')
        self.Layout = NOLAYOUT

    def unlayout(self):
        layout = self.Layout
        if layout == PACKLAYOUT: self.pack_forget()
        elif layout == GRIDLAYOUT: self.grid_remove()
        elif layout == PLACELAYOUT: self.place_forget()
        elif layout == PANELAYOUT: self.pane_forget()
        elif layout == MENULAYOUT: self.selectmenu_forget()

    def item_change_index(self,index):

        old_index = self.getPackListIndex()
        new_index = old_index
        try:
            new_index = int(index) -1
        except ValueError: return

        if new_index != old_index:
            limit = self.master.PackListLen()
            if new_index >= 0 and new_index < limit:
                confdict = self.getconfdict()
                confdict.pop('myclass',None)
                self.master.delete(old_index+1)
                self.master.insert(new_index+1,self.mytype,confdict)
                del self.master.PackList[old_index]
                self.master.PackList.insert(new_index,self)


    def layout(self,**kwargs):
        layout = self.Layout
        if layout == PACKLAYOUT: self.pack(**kwargs)
        elif layout == GRIDLAYOUT: self.grid(**kwargs)
        elif layout == PLACELAYOUT: self.place(**kwargs)
        elif layout == PANELAYOUT: self.master.paneconfig(self,**kwargs)
        elif layout == MENUITEMLAYOUT: self.item_change_index(**kwargs)
        elif layout == MENULAYOUT: self.select_menu(**kwargs)

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
        return dictionary


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


VAR = {}

proxy = None


def this():
    global _Selection
    return _Selection._widget

def container():
    global _Selection
    return _Selection._container


def send(msgid,msgdata=None): proxy.send(msgid,msgdata)
def unregister_msgid(msgid): proxy.unregister_msgid(msgid)
def execute_lambda(cmd): proxy.send('execute_function',cmd)
def do_receive(msgid,function,parameters=None,): proxy.do_receive(container(),msgid,Callback(None,function,parameters).receive)

def undo_receive(container,msgid,receive):
    proxy.undo_receive(container,msgid,receiver)

def undo_receiveAll(cont=container()): proxy.undo_receiveAll(cont)

def activate_receive(msgid,receive,flag): proxy.activate_receive(msgid,receive,flag)




Stack = []
ObjectStack = []
SelfStack = []


def receiver(): return ObjectStack[-1]
def Par(): return receiver().parameters
def Me(): return receiver().widget
def Event(): return receiver().event
def Msg(): return receiver().event

def Self(): return SelfStack[-1]
def Data(): return Self().data

_DynLoad = None


class GuiDictionary:

    def __init__(self): self.elements = {}

    def setElement(self,name,thisone):
        if not name in self.elements: self.elements[name] = [thisone]
        else: self.elements[name].append(thisone)

    def getEntry(self,name,nr=0):
        
        if name in self.elements: return self.elements[name][nr]
        return None

def goto(name,nr=0):
    widget = _Selection._container.Dictionary.getEntry(name,nr)
    if widget != None: 
        _Selection._widget = widget

#def widget(name,nr=-1): return _Selection._container.Dictionary.getEntry(name,nr)

def widget(name,nr=0,par3=0):
    if type(name) == str or name == NONAME: return _Selection._container.Dictionary.getEntry(name,nr)
    else: return name.Dictionary.getEntry(nr,par3)

_FileImportCmdImport = EvDataCmd("""
setWidgetSelection(Data()[0])
goIn()

push(WidgetClass(Data()[0]))
if top() == "Tk" or top() == "Toplevel":
    push(copy(_AppConf))
else:
    push(eval("StatTkInter."+top()+"(container())"))
    push(top().config())
    ConfDictionaryShort(top())
    pop(-2).destroy()
Data()[0].tkClass.config(Data()[0],**pop())
pop()

DynLink(Data()[1])
goOut()
send("SELECTION_CHANGED")
""")

_FileImportCmdDestroy = EvDataCmd("""
Data()[0].destroyActions()
Data()[0].destroyContent()
send('execute_message',EvDataCmd(_FileImportCmdImport,Data()))
""")

def FileImportContainer(container):
    if container.link == "": return
    selection_before = Selection()
    setSelection(Create_Selection(container,container))
    DynLoad(container.link)
    setSelection(selection_before)
    
class Tk(GuiElement,StatTkInter.Tk):
    
    def __init__(self,myname="Application",**kwargs):

        global proxy

        self.myclass = kwargs.pop('myclass','')
        self.geometry_changed = False
        self.title_changed = False

        self.tkClass = StatTkInter.Tk 
        Stack= []
        ObjectStack = []
        SelfStack = []
        VAR.clear()
        EXISTING_WIDGETS.clear()
        ACTORS.clear()
 
        self.config_menuitems = { 'command':None,'radiobutton':None,'checkbutton':None,'separator':None,'cascade':None,'delimiter':None,'menu':None }
        
        grid_cols = kwargs.pop('grid_cols',None)
        grid_rows = kwargs.pop('grid_rows',None)
        grid_multi_rows = kwargs.pop('grid_multi_rows',None)
        grid_multi_cols = kwargs.pop('grid_multi_cols',None)
        self.link = kwargs.pop('link','')
        mytitle = kwargs.pop('title',None)
        mygeometry = kwargs.pop('geometry',None)

        self.tkClass.__init__(self,**kwargs)
        proxy = dynproxy.Proxy()

        if mytitle != None:
            self.title(mytitle)
            self.title_changed = True

        if mygeometry != None:
            self.geometry(mygeometry)
            self.geometry_changed = True

        global _Application
        _Application = self
        #_queue = queue.Queue()
        #__Application.bind("<<EXEC>>",_execute)
        
        global _AppRoot
        self.master = None
        _AppRoot = Create_Selection(self)

        global _Selection
        _Selection = copy(_AppRoot)
        
        self.master = _CreateTopLevelRoot()
        global _TopLevelRoot
        _TopLevelRoot = Create_Selection(self.master)
        _Selection = copy(_TopLevelRoot)
        self.isContainer = True
        GuiElement.__init__(self,myname)
        global LAYOUTNEVER
        self.Layout = LAYOUTNEVER

        if grid_multi_rows != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

        if grid_multi_cols != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

        if grid_cols != None:
            self.grid_conf_cols = eval(grid_cols)
            grid_configure_cols(self)

        if grid_rows != None:
            self.grid_conf_rows = eval(grid_rows)
            grid_configure_rows(self)
        
        self.master = None
        self.isMainWindow = True
        
        _Selection = copy(_AppRoot)
        
        global _AppConf
        _AppConf = self.getconfdict()
        _AppConf.pop("myclass",None)
        _AppConf.pop("title",None)
        _AppConf.pop("geometry",None)
        _AppConf.pop("link",None)
        FileImportContainer(self)
        cdApp()
        
    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = self.tkClass.config(self)
            dictionary['myclass'] = (self.myclass,)
            dictionary['title'] = (self.title(),)
            dictionary['geometry'] = (self.geometry(),)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
            grid_cols = kwargs.pop('grid_cols',None)
            grid_rows = kwargs.pop('grid_rows',None)
            grid_multi_rows = kwargs.pop('grid_multi_rows',None)
            grid_multi_cols = kwargs.pop('grid_multi_cols',None)

            if grid_multi_rows != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

            if grid_multi_cols != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

            if grid_cols != None:
                self.grid_conf_cols = eval(grid_cols)
                grid_configure_cols(self)

            if grid_rows != None:
                self.grid_conf_rows = eval(grid_rows)
                grid_configure_rows(self)

            if 'myclass' in kwargs: 
                self.myclass = kwargs.pop('myclass')
            if 'title' in kwargs: 
                self.title(kwargs['title'])
                self.title_changed = True
                kwargs.pop('title',None)
            if 'geometry' in kwargs: 
                self.geometry(kwargs['geometry'])
                self.geometry_changed = kwargs['geometry'] != ''
                kwargs.pop('geometry',None)
            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)

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


# hier mit master noch ueberlegen =================================

class Toplevel(GuiElement,StatTkInter.Toplevel):

    def __init__(self,myname="Toplevel",**kwargs):

        self.myclass = kwargs.pop('myclass','')

        self.tkClass = StatTkInter.Toplevel
        self.title_changed = False
        self.geometry_changed = False

        master,myname,select = _getMasterAndNameAndSelect(myname,"Toplevel")
        kwargs["master"] = master

        grid_cols = kwargs.pop('grid_cols',None)
        grid_rows = kwargs.pop('grid_rows',None)
        grid_multi_rows = kwargs.pop('grid_multi_rows',None)
        grid_multi_cols = kwargs.pop('grid_multi_cols',None)

        self.link = ""
        if "link" in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)

        mytitle = None
        mygeometry = None
        if "title" in kwargs:
            mytitle = kwargs['title']
            self.title_changed = True
            kwargs.pop('title',None)

        if "geometry" in kwargs:
            mygeometry = kwargs['geometry']
            self.geometry_changed = True
            kwargs.pop('geometry',None)

        self.tkClass.__init__(self,**kwargs)

        if mytitle != None:
            self.title(mytitle)
            self.title_changed = True
        if mygeometry != None: self.geometry(mygeometry)

        global _TopLevelRoot
        self.isContainer = True
        master = self.master		
        self.master = _TopLevelRoot._container
        GuiElement.__init__(self,myname,select)

        if grid_multi_rows != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

        if grid_multi_cols != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

        if grid_cols != None:
            self.grid_conf_cols = eval(grid_cols)
            grid_configure_cols(self)

        if grid_rows != None:
            self.grid_conf_rows = eval(grid_rows)
            grid_configure_rows(self)

        global LAYOUTNEVER

        self.Layout = LAYOUTNEVER
        self.isMainWindow = True
        self.master = master
        goIn()
        FileImportContainer(self)

    def destroy(self):
        selection = Selection()
        if widget_exists(self): GuiElement.destroy(self)
        send('TOPLEVEL_CLOSED',selection)

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = self.tkClass.config(self)
            dictionary['title'] = (self.title(),)
            dictionary['geometry'] = (self.geometry(),)
            dictionary['link'] = (self.link,)
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            grid_cols = kwargs.pop('grid_cols',None)
            grid_rows = kwargs.pop('grid_rows',None)
            grid_multi_rows = kwargs.pop('grid_multi_rows',None)
            grid_multi_cols = kwargs.pop('grid_multi_cols',None)

            if grid_multi_rows != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

            if grid_multi_cols != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

            if grid_cols != None:
                self.grid_conf_cols = eval(grid_cols)
                grid_configure_cols(self)

            if grid_rows != None:
                self.grid_conf_rows = eval(grid_rows)
                grid_configure_rows(self)
 
            if 'myclass' in kwargs: 
                self.myclass = kwargs.pop('myclass')

            if 'title' in kwargs:
                self.title(kwargs['title'])
                self.title_changed = True
                kwargs.pop('title',None)

                kwargs.pop('title',None)
            if 'geometry' in kwargs: 
                self.geometry(kwargs['geometry'])
                self.geometry_changed = kwargs['geometry'] != ''
                kwargs.pop('geometry',None)

            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)

    def pack(self,**kwargs): print("Sorry, no pack for a Toplevel!")
    def grid(self,**kwargs): print("Sorry, no grid for a Toplevel!")
    def place(self,**kwargs): print("Sorry, no place for a Toplevel!")


# Achtung, auch App muss einen Namen haben, wegen Toplevel Fenstern

NONAME = -1

def _getMasterAndNameAndSelect(name,altname):
    global NONAME
    if type(name) == str or name == NONAME: return _Selection._container,name,True
    elif type(name) == tuple: return name[0],name[1],False
    else: return name,altname,False


class Button(GuiElement,StatTkInter.Button):

    def __init__(self,myname="Button",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Button
        master,myname,select = _getMasterAndNameAndSelect(myname,"Button")
        kwargs["master"] = master
        StatTkInter.Button.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Canvas(GuiElement,StatTkInter.Canvas):
    def __init__(self,myname="Canvas",**kwargs):

        self.myclass = kwargs.pop('myclass','')

        self.tkClass = StatTkInter.Canvas
        master,myname,select = _getMasterAndNameAndSelect(myname,"Canvas")
        kwargs["master"] = master
        StatTkInter.Canvas.__init__(self,**kwargs)
        self.isContainer = True
        GuiElement.__init__(self,myname,select)

        grid_cols = kwargs.pop('grid_cols',None)
        grid_rows = kwargs.pop('grid_rows',None)
        grid_multi_rows = kwargs.pop('grid_multi_rows',None)
        grid_multi_cols = kwargs.pop('grid_multi_cols',None)

        if grid_multi_rows != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

        if grid_multi_cols != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

        if grid_cols != None:
            self.grid_conf_cols = eval(grid_cols)
            grid_configure_cols(self)

        if grid_rows != None:
            self.grid_conf_rows = eval(grid_rows)
            grid_configure_rows(self)


class Checkbutton(GuiElement,StatTkInter.Checkbutton):
    def __init__(self,myname="Checkbutton",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Checkbutton
        master,myname,select = _getMasterAndNameAndSelect(myname,"Checkbutton")
        kwargs["master"] = master
        StatTkInter.Checkbutton.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Entry(GuiElement,StatTkInter.Entry):

    def __init__(self,myname="Entry",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Entry
        master,myname,select = _getMasterAndNameAndSelect(myname,"Entry")
        kwargs["master"] = master
        StatTkInter.Entry.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Frame(GuiElement,StatTkInter.Frame):

    def __init__(self,myname="Frame",**kwargs):

        self.myclass = kwargs.pop('myclass','')

        grid_cols = kwargs.pop('grid_cols',None)
        grid_rows = kwargs.pop('grid_rows',None)
        grid_multi_rows = kwargs.pop('grid_multi_rows',None)
        grid_multi_cols = kwargs.pop('grid_multi_cols',None)

        self.link = ""
        if "link" in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)

        self.tkClass = StatTkInter.Frame
        master,myname,select = _getMasterAndNameAndSelect(myname,"Frame")
        kwargs["master"] = master
        StatTkInter.Frame.__init__(self,**kwargs)
        self.isContainer = True
        GuiElement.__init__(self,myname,select)

        if grid_multi_rows != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

        if grid_multi_cols != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

        if grid_cols != None:
            self.grid_conf_cols = eval(grid_cols)
            grid_configure_cols(self)

        if grid_rows != None:
            self.grid_conf_rows = eval(grid_rows)
            grid_configure_rows(self)

        FileImportContainer(self)

    def config(self,**kwargs):
        if len(kwargs) == 0: 
            dictionary = self.tkClass.config(self)
            dictionary['link'] = (self.link,)
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            grid_cols = kwargs.pop('grid_cols',None)
            grid_rows = kwargs.pop('grid_rows',None)
            grid_multi_rows = kwargs.pop('grid_multi_rows',None)
            grid_multi_cols = kwargs.pop('grid_multi_cols',None)

            if grid_multi_rows != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

            if grid_multi_cols != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))
            
            if grid_cols != None:
                self.grid_conf_cols = eval(grid_cols)
                grid_configure_cols(self)

            if grid_rows != None:
                self.grid_conf_rows = eval(grid_rows)
                grid_configure_rows(self)

            if 'myclass' in kwargs: 
                self.myclass = kwargs.pop('myclass')
            if 'title' in kwargs: kwargs.pop('title')
            if 'geometry' in kwargs: kwargs.pop('geometry')
            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)


class Label(GuiElement,StatTkInter.Label):

    def __init__(self,myname="Label",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Label
        master,myname,select = _getMasterAndNameAndSelect(myname,"Label")
        kwargs["master"] = master
        StatTkInter.Label.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)


def link_command(me):
    mylink = me.getconfig('link')
    if mylink != "":
        mymaster = me.master
        mymaster.destroyContent()
        row_conf = mymaster.grid_conf_rows
        col_conf = mymaster.grid_conf_cols
        
        old_rows = row_conf[0]
        old_cols = col_conf[0]
            
        unconf_rows = old_rows
        unconf_cols = old_cols
        
        if mymaster.grid_conf_individual_done:
            unconf_rows += 1
            unconf_cols += 1
        
        for i in range(unconf_rows):
            mymaster.grid_rowconfigure(i,minsize = 0,pad=0,weight=0)

        for i in range(unconf_cols):
            mymaster.grid_columnconfigure(i,minsize = 0,pad=0,weight=0)
        
        mymaster.reset_grid()
        mymaster.setconfig('link',mylink)
        if not widget_exists(this()): cdApp() # this is a secure place

class LinkLabel(Label):

    def __init__(self,myname="LinkLabel",**kwargs):
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

    def __init__(self,myname="LinkButton",**kwargs):
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
      
class LabelFrame(GuiElement,StatTkInter.LabelFrame):

    def __init__(self,myname="LabelFrame",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        grid_cols = kwargs.pop('grid_cols',None)
        grid_rows = kwargs.pop('grid_rows',None)
        grid_multi_rows = kwargs.pop('grid_multi_rows',None)
        grid_multi_cols = kwargs.pop('grid_multi_cols',None)

        self.link = ""
        if "link" in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)

        self.tkClass = StatTkInter.LabelFrame
        master,myname,select = _getMasterAndNameAndSelect(myname,"LabelFrame")
        kwargs["master"] = master
        StatTkInter.LabelFrame.__init__(self,**kwargs)
        self.isContainer = True
        GuiElement.__init__(self,myname,select)

        if grid_multi_rows != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

        if grid_multi_cols != None:
            self.grid_conf_individual_has = True
            self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

        if grid_cols != None:
            self.grid_conf_cols = eval(grid_cols)
            grid_configure_cols(self)

        if grid_rows != None:
            self.grid_conf_rows = eval(grid_rows)
            grid_configure_rows(self)

        FileImportContainer(self)

    def config(self,**kwargs):
        if len(kwargs) == 0: 
            dictionary = self.tkClass.config(self)
            dictionary['link'] = (self.link,)
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:

            grid_cols = kwargs.pop('grid_cols',None)
            grid_rows = kwargs.pop('grid_rows',None)
            grid_multi_rows = kwargs.pop('grid_multi_rows',None)
            grid_multi_cols = kwargs.pop('grid_multi_cols',None)

            if grid_multi_rows != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

            if grid_multi_cols != None:
                self.grid_conf_individual_has = True
                self.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))
            
            if grid_cols != None:
                self.grid_conf_cols = eval(grid_cols)
                grid_configure_cols(self)

            if grid_rows != None:
                self.grid_conf_rows = eval(grid_rows)
                grid_configure_rows(self)

            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            if 'title' in kwargs: kwargs.pop('title',None)
            if 'geometry' in kwargs: kwargs.pop('geometry',None)
            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)


class Listbox(GuiElement,StatTkInter.Listbox):

    def __init__(self,myname="Listbox",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Listbox
        master,myname,select = _getMasterAndNameAndSelect(myname,"Listbox")
        kwargs["master"] = master

        hastext = None
        if "text" in kwargs: 
            hastext = kwargs.pop('text')
        StatTkInter.Listbox.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)
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
                



class Menubutton(GuiElement,StatTkInter.Menubutton):

    def __init__(self,myname="Menubutton",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Menubutton
        master,myname,select = _getMasterAndNameAndSelect(myname,"Menubutton")
        kwargs["master"] = master
        StatTkInter.Menubutton.__init__(self,**kwargs)
        self.isContainer = True  # Achtung, kann nur ein Menue aufnehmen, dh wir brauchen hierzu ein flag oder eine Kennung fuer die Elemente
        GuiElement.__init__(self,myname,select)


class MenuDelimiter(GuiElement):
    def __init__(self,myname="MenuDelimiter",**kwargs):

        self.myclass = kwargs.pop('myclass','')
        master,myname,select = _getMasterAndNameAndSelect(myname,"MenuItem")
        self.master = master
        self.master.entryconfig(0,**kwargs)

        self.tkClass = Dummy

        self.isContainer = False
        GuiElement.__init__(self,myname,select)
        self.Layout = LAYOUTNEVER

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
                _Application.config_menuitems['delimiter'] = dict(dictionary)

            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            self.master.entryconfig(0,**kwargs)


class MenuItem(GuiElement):
    def __init__(self,myname="MenuItem",mytype='command',**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.mytype = mytype
        master,myname,select = _getMasterAndNameAndSelect(myname,"MenuItem")
        self.master = master
        self._addToPackList()
        master.add(mytype,**kwargs)
        #container().add(mytype,**kwargs)

        self.tkClass = Dummy

        self.isContainer = mytype == 'cascade'
        GuiElement.__init__(self,myname,select)
        self.Layout = MENUITEMLAYOUT

    def destroy(self):
         index = self.getPackListIndex()
         self.master.delete(index+1)
         self._removeFromPackList()
         GuiElement.destroy(self)

    def config(self,**kwargs):
        index = self.getPackListIndex() + 1
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
            if _Application.config_menuitems[self.mytype] == None:
                base_dict = dict(dictionary)
                base_dict.pop('label',None)
                _Application.config_menuitems[self.mytype] = base_dict
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            self.master.entryconfig(index,**kwargs)
                

class Menu(GuiElement,StatTkInter.Menu):

    def __init__(self,myname="Menu",**kwargs):

        self.myclass = kwargs.pop('myclass','')

        self.title_changed = False

        self.tkClass = StatTkInter.Menu
        master,myname,select = _getMasterAndNameAndSelect(myname,"Menu")
 
        if isinstance(master,MenuItem): kwargs["master"] = master.myRoot()
        else: kwargs["master"] = master
            
        '''
        if isinstance(container(),MenuItem):
            push(Selection())
            setWidgetSelection(container())
            gotoRoot()
            rootwidget=this()
            setSelection(pop())
            kwargs["master"] = rootwidget
        else: kwargs["master"] = master
        '''


        self.link = ""
        if "link" in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)

        StatTkInter.Menu.__init__(self,**kwargs)
        #self.master = container()
        self.master = master
        self.isContainer = True
        GuiElement.__init__(self,myname,select)

        if _Application.config_menuitems['menu'] == None:
            _Application.config_menuitems['menu'] = self.config()

        FileImportContainer(self)

    def select_menu(self,**kwargs):
        activwidget = self.master if (isinstance(self.master,MenuItem) or isinstance(self.master,Menubutton)) else self.myRoot()
        if activwidget.menu_ref != None:
            activwidget.menu_ref.unlayout()
        activwidget.config(menu=self)
        activwidget.menu_ref = self
        self.Layout = MENULAYOUT

    def config(self,**kwargs):
        if len(kwargs) == 0: 
            dictionary = self.tkClass.config(self)
            dictionary['link'] = (self.link,)
            dictionary['myclass'] = (self.myclass,)
            return dictionary
        else:
            if 'myclass' in kwargs: self.myclass = kwargs.pop('myclass')
            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)

class Message(GuiElement,StatTkInter.Message): # similiar Label

    def __init__(self,myname="Message",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Message
        master,myname,select = _getMasterAndNameAndSelect(myname,"Message")
        kwargs["master"] = master
        StatTkInter.Message.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Radiobutton(GuiElement,StatTkInter.Radiobutton):

    def __init__(self,myname="Radiobutton",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Radiobutton
        master,myname,select = _getMasterAndNameAndSelect(myname,"Radiobutton")
        kwargs["master"] = master
        StatTkInter.Radiobutton.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Scale(GuiElement,StatTkInter.Scale):

    def __init__(self,myname="Scale",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Scale
        master,myname,select = _getMasterAndNameAndSelect(myname,"Scale")
        kwargs["master"] = master
        StatTkInter.Scale.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Scrollbar(GuiElement,StatTkInter.Scrollbar):

    def __init__(self,myname="Scrollbar",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Scrollbar
        master,myname,select = _getMasterAndNameAndSelect(myname,"Scrollbar")
        kwargs["master"] = master
        StatTkInter.Scrollbar.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)


class Text(GuiElement,StatTkInter.Text):

    def __init__(self,myname="Text",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Text
        master,myname,select = _getMasterAndNameAndSelect(myname,"Text")
        kwargs["master"] = master
        StatTkInter.Text.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)


class Spinbox(GuiElement,StatTkInter.Spinbox):

    def __init__(self,myname="Spinbox",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.Spinbox
        master,myname,select = _getMasterAndNameAndSelect(myname,"Spinbox")
        kwargs["master"] = master
        StatTkInter.Spinbox.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class PanedWindow(GuiElement,StatTkInter.PanedWindow):

    def __init__(self,myname="PanedWindow",**kwargs):
        self.myclass = kwargs.pop('myclass','')
        self.tkClass = StatTkInter.PanedWindow
        master,myname,select = _getMasterAndNameAndSelect(myname,"PanedWindow")
        kwargs["master"] = master
        StatTkInter.PanedWindow.__init__(self,**kwargs)
        self.isContainer = True
        GuiElement.__init__(self,myname,select)
        
    def trigger_sash_place(self,time,index,x_coord,y_coord):
        self.after(time,lambda pwin = self, i = index, x = x_coord, y=y_coord, function = self.tkClass.sash_place: function(pwin,i,x,y))

    def add(self,child,**kwargs):
        global PANELAYOUT
        if child.Layout != PANELAYOUT: child._addToPackList()
        child.Layout = PANELAYOUT
        self.tkClass.add(self,child,**kwargs)


def goIn():_Selection.selectIn()
def goOut(): _Selection.selectOut()

def cdDir():_Selection.selectContainer()
def cdApp():
    global _Selection
    global _AppRoot
    _Selection = copy(_AppRoot)

def gotoRoot():
    while not this().isMainWindow: goOut()

def gotoTop():
    global _Selection
    global _TopLevelRoot
    _Selection = copy(_TopLevelRoot)


def Selection():
    global _Selection
    return copy(_Selection)

def setSelection(thisSelection):
    global _Selection
    _Selection=copy(thisSelection)

def setWidgetSelection(widget,container=None):
    global _Selection
    _Selection = Create_Selection(widget,container)

def text(mytext): this().text(mytext)

def do_command(function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False): this().do_command(function,parameters,wishWidget,wishEvent,wishSelf)
def do_command(function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False): this().do_command(function,parameters,wishWidget,wishEvent,wishSelf)
def do_event(eventstr,function,parameters=None,wishWidget=False,wishEvent=False,wishSelf=False): this().do_event(eventstr,function,parameters,wishWidget,wishEvent,wishSelf)
def do_receive(msgid,function,parameters=None,wishWidget=False,wishMessage=False): proxy.do_receive(container(),msgid,Callback(None,function,parameters,wishWidget,wishEvent=wishMessage).receive)


def pop(index=-1): return Stack.pop(index)
def push(x): Stack.append(x)
def top(): return Stack[-1]
def first(): return Stack[-1]
def second(): return Stack[-2]
def third(): return Stack[-3]


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

def getContainer():
    global _Selection
    return _Selection._container


def allDictEntries(dictionary,cmd,data=None):
    for n,e in dictionary.items():
        ObjectStack.append((e,n,data))
        cmd()
        ObjectStack.pop()


GetNameAndIndexCmd = EvCmd("""
push(0)
push(None)
for Stack[-1] in receiver()[0]:
    if top() is receiver()[2]:
        Stack[-4] = second()
        Stack[-3] = receiver()[1]
    Stack[-2] +=1
pop()
pop()
""")


def getNameAndIndex():
    push(None)
    push(None)
    dictionary=Selection()._container.Dictionary.elements
    allDictEntries(dictionary,GetNameAndIndexCmd.execute,Selection()._widget)
    if top() != None:	
        if len(dictionary[top()]) == 1: Stack[-2] = -1
    return (pop(),pop())
    

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


def getContLayouts(container):
    push(0)
    allContainerEntries(container,GetContLayoutsCmd)
    return pop()

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
    dictionary=_Selection._container.Dictionary.elements	
    if name in dictionary:
        elist = dictionary[name]
        e = elist[index]
        elist.pop(index)
        if len(elist)==0: dictionary.pop(name,None)
        return e
    else: return None

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

def WidgetClass(widget):
    if isinstance(widget,MenuItem): return 'MenuItem'
    elif isinstance(widget,MenuDelimiter): return 'MenuDelimiter'
    elif isinstance(widget,LinkButton): return 'LinkButton'
    elif isinstance(widget,LinkLabel): return 'LinkLabel'
    else: classString = str(widget.tkClass)
    begin = classString.find(".")+1
    end = classString.find("'",begin)
    return classString[begin:end]

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
        if isinstance(this(),MenuItem): print("Kann nicht sein")
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
        CompareWidget.place(x=-1,y=-1)
        layoutCompare = dict(CompareWidget.place_info())
    CompareWidget.destroy()

    layoutDict = layout_info()
    layoutDict.pop(".in",None)
    for n,e in dict(layoutDict).items():
        if e == layoutCompare[n]: layoutDict.pop(n,None)

    # Causes bug for tuple - padx, do we have some pixel object?
    #for n,e in layoutDict.items(): layoutDict[n] = str(e)

    return layoutDict

def is_immediate_layout(): return this().Layout & (GRIDLAYOUT | PLACELAYOUT | MENULAYOUT)

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
        
    if len(layout) != 0: filehandle.write("**"+repr(layout))
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
                filehandle.write('**'+repr(layoutWidget))
           
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
            filehandle.write(indent+"container().trigger_sash_place("+str(i*500)+","+str(i)+","+str(sash_list[i][0])+","+str(sash_list[i][1])+")\n")

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

    # get config ===============================
    dictionaryConfig = getconfdict()
    del_config_before_compare(dictionaryConfig)

    dictionaryCompare = get_config_compare()

    for n,e in dict(dictionaryConfig).items():
        if n in dictionaryCompare:
            if e == dictionaryCompare[n]: dictionaryConfig.pop(n,None)

    for n,e in dictionaryConfig.items(): dictionaryConfig[n] = str(e)

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

    # write name ================================
    thisClass = WidgetClass(this())
 
    if isinstance(this(),MenuItem):
        filehandle.write(indent+thisClass+"('"+name+"','"+this().mytype+"'")
    else:
        filehandle.write(indent+thisClass+"('"+name+"'")

    conf_dict = get_save_config()
    if SAVE_ALL and not (isinstance(this(),LinkLabel) or isinstance(this(),LinkButton)):
        conf_dict.pop('link',None)
    
    if len(conf_dict) != 0:
        filehandle.write(",**"+repr(conf_dict)+")")
    else:
         filehandle.write(")")

    if 'link' in conf_dict:
        if is_immediate_layout(): filehandle.write('.')
    else:
        if not save_sub_container(filehandle) and is_immediate_layout(): filehandle.write('.')
    save_immediate_layout(filehandle)
    filehandle.write("\n")


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
                if len(conf_dict) != 0: filehandle.write('config(**'+str(conf_dict)+")\n\n")
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
    if newname in CamelCaseDictionary:
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

EXPORT_NAME = False
ExportNames = {}

class ExportBuffer:
    
    def __init__(self):
        self.stringbuffer = []
        
    def write(self,text):
        self.stringbuffer.append(text)
        
    def get(self):
        return ''.join(self.stringbuffer)
        
    def reset(self):
        self.stringbuffer = []

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

 
def get_grid_dict(confdict):
    grid_dict = {}
    for entry in ('grid_cols','grid_rows','grid_multi_cols','grid_multi_rows'):
        value = confdict.pop(entry,None)
        if value != None: grid_dict[entry] = value
    return grid_dict


def makeCamelCase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

def export_pack_entries(filehandle):

    packlist = container().PackList
    if len(packlist) == 0: return

    item_index = 1
    for e in packlist:
        filehandle.write(indent+"        self.")
        setWidgetSelection(e)
        name = ExportNames[this()][0]

        if this().Layout != PANELAYOUT: filehandle.write(name)

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
                filehandle.write("add(self."+name) # point already written 'self.'
                layoutCompare = {'sticky': 'nesw', 'minsize': 0, 'width': '', 'pady': 0, 'padx': 0, 'height': ''}

            for n,e in dict(layoutWidget).items():
                if e == layoutCompare[n]: layoutWidget.pop(n,None)
 
            if len(layoutWidget) != 0:
                if this().Layout == PANELAYOUT: filehandle.write(",")
                filehandle.write('**'+repr(layoutWidget))

            filehandle.write(")\n")

        
    if container().tkClass == StatTkInter.PanedWindow:

        index = 0
        sash_list = []
        while True:
            try:
                sash_list.append(container().sash_coord(index))
                index += 1
            except: break

        if EXPORT_NAME:
            for i in range(len(sash_list)):
                filehandle.write("        tk.trigger_sash_place(self,"+str(i*500)+","+str(i)+","+str(sash_list[i][0])+","+str(sash_list[i][1])+")\n")
        else:
            for i in range(len(sash_list)):
                filehandle.write("        ext.trigger_sash_place(self,"+str(i*500)+","+str(i)+","+str(sash_list[i][0])+","+str(sash_list[i][1])+")\n")

def export_immediate_layout(filehandle,name):
    if not is_immediate_layout(): return

    filehandle.write('        self.'+name+'.')

    if this().Layout == GRIDLAYOUT:
        filehandle.write("grid(")
        layout = get_layout_dictionary()
    elif this().Layout == PLACELAYOUT:
        filehandle.write("place(")
        layout = get_layout_dictionary()
    elif this().Layout == MENULAYOUT:
        filehandle.write("select_menu(")
        layout = {}
        
    if len(layout) != 0: filehandle.write("**"+repr(layout))
    filehandle.write(")\n")

def exportWidget(filehandle,name,widgetname=None,camelcase_name = None):
    if not this().save: return

    if widgetname == None: widgetname = name

    # write name ================================
    thisClass = WidgetClass(this())

    if this().hasWidgets(): class_name = camelcase_name
    else: class_name = 'tk.'+thisClass
    
    if EXPORT_NAME:
        if isinstance(this(),MenuItem): filehandle.write('        self.'+name+' = '+class_name+"((self,'"+widgetname+"'),'"+this().mytype+"'")
        #elif isinstance(this(),MenuDelimiter): filehandle.write('        self.entryconfig(0')
        else: filehandle.write('        self.'+name+' = '+class_name+"((self,'"+widgetname+"')")
    else:
        if isinstance(this(),MenuItem):
            if this().hasWidgets(): filehandle.write('        self.'+name+' = '+class_name+"(self,'"+this().mytype+"'")
            else: filehandle.write('        self.'+name+' = ext.'+thisClass+"(self,'"+this().mytype+"'")
        elif isinstance(this(),Menu) and not this().hasWidgets(): filehandle.write('        self.'+name+' = ext.'+thisClass+"(self")
        elif isinstance(this(),MenuDelimiter):
            #filehandle.write('        self.entryconfig(0')
            filehandle.write('        self.'+name+' = ext.'+thisClass+"(self")
        elif isinstance(this(),LinkLabel):
            filehandle.write('        self.'+name+' = tk.Label(self)')
        elif isinstance(this(),LinkButton):
            filehandle.write('        self.'+name+' = tk.Button(self)')
        else: filehandle.write('        self.'+name+' = '+class_name+"(self")

    conf_dict = get_save_config()
    if SAVE_ALL and not (isinstance(this(),LinkLabel) or isinstance(this(),LinkButton)):
        conf_dict.pop('link',None)
    
    lbtext = None
    if isinstance(this(),Listbox): lbtext = conf_dict.pop('text',None)

    grid_dict = get_grid_dict(conf_dict)

    if not EXPORT_NAME:
        conf_dict.pop('myclass',None)
        conf_dict.pop('link',None) # also for LinkLabel and LinkButton (only Label and Button for without Names)

    if len(conf_dict) != 0:
        filehandle.write(",**"+repr(conf_dict)+")\n")
    else:
         filehandle.write(")\n")

    if EXPORT_NAME:
        if len(grid_dict) != 0: filehandle.write('        tk.grid_table(self.'+name+',**'+repr(grid_dict)+')\n')
        if lbtext != None: filehandle.write('        tk.fill_listbox_with_string(self.'+name+','+repr(lbtext)+')\n')
    else:
        if len(grid_dict) != 0: filehandle.write('        ext.grid_table(self.'+name+',**'+repr(grid_dict)+')\n')
        if lbtext != None: filehandle.write('        ext.fill_listbox_with_string(self.'+name+','+repr(lbtext)+')\n')

    export_immediate_layout(filehandle,name)


def exportContainer(filehandle):

    dictionary = container().Dictionary.elements
    AccessDictionary.clear()
    
    # sorted name list
    namelist = []
    for name in dictionary:
        if name != NONAME: namelist.append(name)
    namelist.sort()

    # now we save the widgets in the container
    for widget_name in namelist:
        e = dictionary[widget_name]
        for x in e:
            setWidgetSelection(x)
            var_name = getAccessName(widget_name)
            camelcase_name = None
            if this().hasWidgets():
                camelcase_name = makeCamelCase(var_name)
                camelcase_name = getCamelCaseName(camelcase_name)
                
            ExportNames[this()] = (var_name,camelcase_name)
            exportWidget(filehandle,var_name,widget_name,camelcase_name)

    export_pack_entries(filehandle)

    # now we save sub containers
    for widget_name in namelist:
        e = dictionary[widget_name]
        for x in e:
            setWidgetSelection(x)
            if this().hasWidgets(): exportSubcontainer(filehandle,ExportNames[this()][1]) # camelcase_name

    AccessDictionary.clear()

def exportSubcontainer(filehandle,class_name):

    filehandle.open(class_name)
    
    thisClass = WidgetClass(this())
    
    if isinstance(this(),Tk): thisMaster = ''
    else: thisMaster = ',master'
        

    if isinstance(this(),MenuItem):
        if EXPORT_NAME:
            filehandle.write('class '+class_name+'(tk.'+thisClass+'):\n\n')
        else:
            filehandle.write('class '+class_name+'(ext.'+thisClass+'):\n\n')

        filehandle.write('    def __init__(self'+thisMaster+',item,**kwargs):\n')
        if EXPORT_NAME:
            filehandle.write('        tk.'+thisClass+'.__init__(self'+thisMaster+',item,**kwargs)\n')
        else:
            filehandle.write('        ext.'+thisClass+'.__init__(self'+thisMaster+',item,**kwargs)\n')
    elif isinstance(this(),Menu) and not EXPORT_NAME:
        filehandle.write('class '+class_name+'(ext.'+thisClass+'):\n\n')
        filehandle.write('    def __init__(self'+thisMaster+',**kwargs):\n')
        filehandle.write('        ext.'+thisClass+'.__init__(self'+thisMaster+',**kwargs)\n')
    else:
        filehandle.write('class '+class_name+'(tk.'+thisClass+'):\n\n')
        filehandle.write('    def __init__(self'+thisMaster+',**kwargs):\n')
        filehandle.write('        tk.'+thisClass+'.__init__(self'+thisMaster+',**kwargs)\n')
 
    if isinstance(this(),Tk) or isinstance(this(),Toplevel):
        conf_dict = get_save_config()
        conf_dict.pop('link',None)

        tit = conf_dict.pop('title',None)
        if tit != None: filehandle.write('        self.title('+repr(tit)+")\n")
        geo = conf_dict.pop('geometry',None)
        if geo != None: filehandle.write('        self.geometry('+repr(geo)+")\n")
        
        grid_dict = get_grid_dict(conf_dict)
        if EXPORT_NAME:
            if len(grid_dict) != 0: filehandle.write('        tk.grid_table(self,**'+repr(grid_dict)+')\n')
        else:
            if len(grid_dict) != 0: filehandle.write('        ext.grid_table(self,**'+repr(grid_dict)+')\n')
            conf_dict.pop('myclass',None)

        if not EXPORT_NAME: conf_dict.pop('myclass',None)
        if len(conf_dict) != 0: filehandle.write('        self.config(**'+repr(conf_dict)+")\n")
 
    goIn()
    exportContainer(filehandle)
    goOut()
    
def saveExport(readhandle,writehandle,flag=False):

    global SAVE_ALL
    global EXPORT_NAME
    
    EXPORT_NAME = flag
    SAVE_ALL = True
    
    CamelCaseDictionary.clear()
    ExportNames.clear()
    exphandle = ExportBuffer()

    if EXPORT_NAME:
        exphandle.write('import DynTkInter as tk\n\n')
    else:
        exphandle.write('import tkinter as tk\n')
        exphandle.write('import DynTkExtend as ext\n\n')

    name = getNameAndIndex()[0]
    name = getCamelCaseName(name)
    ExportNames[this()] = (name,name)

    exp_list = ExportList()
    exportSubcontainer(exp_list,name)
    exp_list.close()

    class_list = exp_list.getlist()
    
    class_dict = {}
    for entry in class_list:

        if entry[0] in class_dict:
            error = "Error: class name '" + entry[0] + "' is double!"
            CamelCaseDictionary.clear()
            ExportNames.clear()
            return error
        class_dict[entry[0]] = entry[1]
        
    if readhandle == None:
        writehandle.write(exphandle.get())
        for entry in class_list:
            writehandle.write(entry[1]+"\n")
        if this() == _Application: writehandle.write(name+'().mainloop()\n')
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

    CamelCaseDictionary.clear()
    ExportNames.clear()

    EXPORT_NAME = False
    SAVE_ALL = False
    return('OK')
 
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

'''

def clean_eval(evcode):
    glob_before = globals().keys()
    eval(evcode)
    glob_after = globals().keys()
    for element in glob_after:
        if element not in glob_before: del globals()[element]


def DynImport(filename):
    global LOADwithCODE
    if LOADwithCODE: DynImportCode(filename)
    else:
        dynfile = filename
        try:
            handle = open(dynfile,'r')
        except: 
            print("Couldn't open file: " + dynfile)
            return
        code = handle.read()
        handle.close()
        evcode = compile(code,filename,'exec')
        eval(evcode)
'''

def DynLoad(filename):
    global LOADwithCODE
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

# ========== For Compatibility with Export with Names =============

def trigger_sash_place(pane_window,time,index,x_coord,y_coord):
    pane_window.after(time,lambda i = index, x = x_coord, y=y_coord, function = pane_window.sash_place: function(i,x,y))

def fill_listbox_with_string(listbox,string):
    listbox.delete(0,END)		
    for e in string.split("\n"): listbox.insert(END,e)
    
def grid_table(container,grid_rows = None, grid_cols = None, grid_multi_rows = None, grid_multi_cols = None):
    if grid_multi_rows != None:
        container.grid_conf_individual_has = True
        container.grid_multi_conf_rows = grid_configure_multi(eval(grid_multi_rows))

    if grid_multi_cols != None:
        container.grid_conf_individual_has = True
        container.grid_multi_conf_cols = grid_configure_multi(eval(grid_multi_cols))

    if grid_cols != None:
        container.grid_conf_cols = eval(grid_cols)
        grid_configure_cols(container)

    if grid_rows != None:
        container.grid_conf_rows = eval(grid_rows)
        grid_configure_rows(container)


