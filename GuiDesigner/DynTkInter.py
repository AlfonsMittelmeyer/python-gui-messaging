import tkinter as StatTkInter
from tkinter import *
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
LAYOUTNEVER = 16

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

class GuiElement:

    def __init__(self,name="nn",select=True):

        EXISTING_WIDGETS[self] = None
    
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

        global NOLAYOUT
        self.Layout = NOLAYOUT
        self.hasConfig = True
        self.isMainWindow = False
        #self.isDestroyed = False
        if self.isContainer: self.isLocked=False
        else: self.isLocked = True


    def myRoot(self):
        push(Selection())
        setWidgetSelection(self)
        gotoRoot()
        rootwidget=this()
        setSelection(pop())
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

        push(getNameAndIndex())
        if top()[0] != None: eraseEntry(top()[0],top()[1])
        pop()

        if self.Layout == PACKLAYOUT or self.Layout == PANELAYOUT: self._removeFromPackList()
        self.tkClass.destroy(self)

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
        try: self.config(text=mytext)
        except TclError: pass
    
    # used by the save function: if a container doesn't have widgets then there is no need to look inside
    def hasWidgets(self):
        if self.isLocked: return False
        return len(self.Dictionary.elements) != 0

    # DynTkInter records the layouts and tho order of pack layouts - without the correct pack order, pack layouts wouldn't be saved properly

    def _addToPackList(self): self.master.PackList.append(self)
        
    def _removeFromPackList(self):
            packlist = self.master.PackList
            packlist.pop(packlist.index(self))

    def pack(self,**kwargs):
        global PACKLAYOUT
        if self.Layout != PACKLAYOUT: self._addToPackList()
        self.Layout = PACKLAYOUT
        self.tkClass.pack(self,**kwargs)
        
    def pane(self,*args):
        global PANELAYOUT
        if self.Layout != PANELAYOUT: self._addToPackList()
        self.Layout = PANELAYOUT
        self.master.tkClass.add(self.master,self)

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

    def unlayout(self):
        layout = self.Layout
        if layout == PACKLAYOUT: self.pack_forget()
        elif layout == GRIDLAYOUT: self.grid_remove()
        elif layout == PLACELAYOUT: self.place_forget()
        elif layout == PANELAYOUT: self.pane_forget()

    def layout(self,**kwargs):
        layout = self.Layout
        if layout == PACKLAYOUT: self.pack(**kwargs)
        elif layout == GRIDLAYOUT: self.grid(**kwargs)
        elif layout == PLACELAYOUT: self.place(**kwargs)
        elif layout == PANELAYOUT: self.master.paneconfig(self,**kwargs)

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

    def layout_info(self):
        layout = self.Layout
        if layout == PACKLAYOUT: dictionary=self.pack_info()
        elif layout == GRIDLAYOUT: dictionary=self.grid_info()
        elif layout == PLACELAYOUT: dictionary = self.place_info()
        elif layout == PANELAYOUT: dictionary = self.pane_info()
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
    dictionary['bd'] = dictionary['borderwidth']
    dictionary.pop('borderwidth',None)
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

    def getEntry(self,name,nr=-1):
        
        if name in self.elements: return self.elements[name][nr]
        return None

def goto(name,nr=-1):
    widget = _Selection._container.Dictionary.getEntry(name,nr)
    if widget != None: 
        _Selection._widget = widget

def widget(name,nr=-1): return _Selection._container.Dictionary.getEntry(name,nr)


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
    DynLink(container.link)
    
    #filename = container.link
    #print(filename)
    #try: handle = open(filename,"r")
    #except IOError:
    #	print("Sorry, the File '"+filename+"' doesn't exist") 
    #	return
    #handle.close()
    #send('execute_message',EvDataCmd(_FileImportCmdDestroy,(container,container.link)))

class Tk(GuiElement,StatTkInter.Tk):
    
    def __init__(self,myname="Application",**kwargs):

        global proxy

        self.tkClass = StatTkInter.Tk 
        Stack= []
        ObjectStack = []
        SelfStack = []
        VAR.clear()
        EXISTING_WIDGETS.clear()
        ACTORS.clear()
        self.link = ""
        
        if "link" in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)

        mytitle = None
        mygeometry = None
        if "title" in kwargs:
            mytitle = kwargs['title']
            kwargs.pop('title',None)

        if "geometry" in kwargs:
            mygeometry = kwargs['geometry']
            kwargs.pop('geometry',None)

        self.tkClass.__init__(self,**kwargs)
        proxy = dynproxy.Proxy(self)

        if mytitle != None: self.title(mytitle)
        if mygeometry != None: self.geometry(mygeometry)

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

        self.master = None
        self.isMainWindow = True
        
        _Selection = copy(_AppRoot)
        
        global _AppConf
        _AppConf = self.getconfdict()
        _AppConf.pop("title",None)
        _AppConf.pop("geometry",None)
        _AppConf.pop("link",None)
        self.geometry_changed = False
        self.title_changed = False

        FileImportContainer(self)
        cdApp()
        
    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = self.tkClass.config(self)
            dictionary['title'] = (self.title(),)
            dictionary['geometry'] = (self.geometry(),)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
            if 'title' in kwargs: 
                self.title(kwargs['title'])
                kwargs.pop('title',None)
            if 'geometry' in kwargs: 
                self.geometry(kwargs['geometry'])
                kwargs.pop('geometry',None)
            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)

    def mainloop(self,load_file = None):
        if load_file != None:
            _Application.after(1000,_DynLoad,load_file)

        cdApp()
        StatTkInter.Tk.mainloop(self)


    def pack(self,**kwargs): print("Sorry, no pack for the Application!")
    def grid(self,**kwargs): print("Sorry, no grid for the Application!")
    def place(self,**kwargs): print("Sorry, no place for the Application!")


class _CreateTopLevelRoot(GuiElement):
    def __init__(self):
        self.isContainer = True
        self.master = None
        GuiElement.__init__(self,"TopLevel")
        self.hasConfig = False
        global LAYOUTNEVER
        self.Layout = LAYOUTNEVER
        
    def pack(self,**kwargs): print("Sorry, no pack for the Toplevel Root!")
    def grid(self,**kwargs): print("Sorry, no grid for the Toplevel Root!")
    def place(self,**kwargs): print("Sorry, no place for the Toplevel Root!")


# hier mit master noch ueberlegen =================================

class Toplevel(GuiElement,StatTkInter.Toplevel):

    def __init__(self,myname="Toplevel",**kwargs):

        self.tkClass = StatTkInter.Toplevel

        master,myname,select = _getMasterAndNameAndSelect(myname,"Toplevel")
        kwargs["master"] = master

        self.link = ""
        if "link" in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)

        mytitle = None
        mygeometry = None
        if "title" in kwargs:
            mytitle = kwargs['title']
            kwargs.pop('title',None)

        if "geometry" in kwargs:
            mygeometry = kwargs['geometry']
            kwargs.pop('geometry',None)

        self.tkClass.__init__(self,**kwargs)

        if mytitle != None: self.title(mytitle)
        if mygeometry != None: self.geometry(mygeometry)

        global _TopLevelRoot
        self.isContainer = True
        master = self.master		
        self.master = _TopLevelRoot._container
        GuiElement.__init__(self,myname,select)
        global LAYOUTNEVER
        self.Layout = LAYOUTNEVER
        self.isMainWindow = True
        self.master = master
        goIn()
        FileImportContainer(self)
        self.geometry_changed = False
        self.title_changed = False

    def destroy(self):
        selection = Selection()
        GuiElement.destroy(self)
        send('TOPLEVEL_CLOSED',selection)

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = self.tkClass.config(self)
            dictionary['title'] = (self.title(),)
            dictionary['geometry'] = (self.geometry(),)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
            if 'title' in kwargs: 
                self.title(kwargs['title'])
                kwargs.pop('title',None)

                kwargs.pop('title',None)
            if 'geometry' in kwargs: 
                self.geometry(kwargs['geometry'])
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


def _getMasterAndNameAndSelect(name,altname):
    if type(name) == str: return _Selection._container,name,True
    elif type(name) == tuple: return name[0],name[1],False
    else: return name,altname,False


class Button(GuiElement,StatTkInter.Button):

    def __init__(self,myname="Button",**kwargs):
        self.tkClass = StatTkInter.Button
        master,myname,select = _getMasterAndNameAndSelect(myname,"Button")
        kwargs["master"] = master
        StatTkInter.Button.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Canvas(GuiElement,StatTkInter.Canvas):
    def __init__(self,myname="Canvas",**kwargs):
        self.tkClass = StatTkInter.Canvas
        master,myname,select = _getMasterAndNameAndSelect(myname,"Canvas")
        kwargs["master"] = master
        StatTkInter.Canvas.__init__(self,**kwargs)
        self.isContainer = True
        GuiElement.__init__(self,myname,select)

class Checkbutton(GuiElement,StatTkInter.Checkbutton):
    def __init__(self,myname="Checkbutton",**kwargs):
        self.tkClass = StatTkInter.Checkbutton
        master,myname,select = _getMasterAndNameAndSelect(myname,"Checkbutton")
        kwargs["master"] = master
        StatTkInter.Checkbutton.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Entry(GuiElement,StatTkInter.Entry):

    def __init__(self,myname="Entry",**kwargs):
        self.tkClass = StatTkInter.Entry
        master,myname,select = _getMasterAndNameAndSelect(myname,"Entry")
        kwargs["master"] = master
        StatTkInter.Entry.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Frame(GuiElement,StatTkInter.Frame):

    def __init__(self,myname="Frame",**kwargs):

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
        FileImportContainer(self)

    def config(self,**kwargs):
        if len(kwargs) == 0: 
            dictionary = self.tkClass.config(self)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
            if 'title' in kwargs: kwargs.pop('title',None)
            if 'geometry' in kwargs: kwargs.pop('geometry',None)
            if 'link' in kwargs:
                self.link = kwargs['link']
                kwargs.pop('link',None)
                self.tkClass.config(self,**kwargs)
                FileImportContainer(self)
            else: self.tkClass.config(self,**kwargs)


class Label(GuiElement,StatTkInter.Label):

    def __init__(self,myname="Label",**kwargs):
        self.tkClass = StatTkInter.Label
        master,myname,select = _getMasterAndNameAndSelect(myname,"Label")
        kwargs["master"] = master
        StatTkInter.Label.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)


class LinkLabel(Label):

    def __init__(self,myname="LinkLabel",**kwargs):
        self.link=""		
        if 'link' in kwargs:
            self.link = kwargs['link']
            kwargs.pop('link',None)
        Label.__init__(self,myname="LinkLabel",**kwargs)
        self.config(font='TkFixedFont 9 normal underline',fg="blue")
        self.do_event('<Button-1>',"Me().container().setconfig('link',Me().getconfig('link'))")

    def config(self,**kwargs):
        if len(kwargs) == 0:
            dictionary = Label.config(self)
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
        Button.__init__(self,myname="LinkButton",**kwargs)
        self.do_command("Me().container().setconfig('link',Me().getconfig('link'))")


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
        FileImportContainer(self)

    def config(self,**kwargs):
        if len(kwargs) == 0: 
            dictionary = self.tkClass.config(self)
            dictionary['link'] = (self.link,)
            return dictionary
        else:
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
            return dictionary
        else:
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
        self.tkClass = StatTkInter.Menubutton
        master,myname,select = _getMasterAndNameAndSelect(myname,"Menubutton")
        kwargs["master"] = master
        StatTkInter.Menubutton.__init__(self,**kwargs)
        self.isContainer = True  # Achtung, kann nur ein Menue aufnehmen, dh wir brauchen hierzu ein flag oder eine Kennung fuer die Elemente
        GuiElement.__init__(self,myname,select)


class Menu(GuiElement,StatTkInter.Menu): # Achtung, Master darf vielleicht nur ein Menuebutton sein?

    def __init__(self,myname="Menu",**kwargs):
        self.tkClass = StatTkInter.Menu
        master,myname,select = _getMasterAndNameAndSelect(myname,"Menu")
        kwargs["master"] = master
        StatTkInter.Menu.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)
        self.Layout = LAYOUTNEVER

class Message(GuiElement,StatTkInter.Message): # similiar Label

    def __init__(self,myname="Message",**kwargs):
        self.tkClass = StatTkInter.Message
        master,myname,select = _getMasterAndNameAndSelect(myname,"Message")
        kwargs["master"] = master
        StatTkInter.Message.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Radiobutton(GuiElement,StatTkInter.Radiobutton):

    def __init__(self,myname="Radiobutton",**kwargs):
        self.tkClass = StatTkInter.Radiobutton
        master,myname,select = _getMasterAndNameAndSelect(myname,"Radiobutton")
        kwargs["master"] = master
        StatTkInter.Radiobutton.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Scale(GuiElement,StatTkInter.Scale):

    def __init__(self,myname="Scale",**kwargs):
        self.tkClass = StatTkInter.Scale
        master,myname,select = _getMasterAndNameAndSelect(myname,"Scale")
        kwargs["master"] = master
        StatTkInter.Scale.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class Scrollbar(GuiElement,StatTkInter.Scrollbar):

    def __init__(self,myname="Scrollbar",**kwargs):
        self.tkClass = StatTkInter.Scrollbar
        master,myname,select = _getMasterAndNameAndSelect(myname,"Scrollbar")
        kwargs["master"] = master
        StatTkInter.Scrollbar.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)


class Text(GuiElement,StatTkInter.Text):

    def __init__(self,myname="Text",**kwargs):
        self.tkClass = StatTkInter.Text
        master,myname,select = _getMasterAndNameAndSelect(myname,"Text")
        kwargs["master"] = master
        StatTkInter.Text.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)


class Spinbox(GuiElement,StatTkInter.Spinbox):

    def __init__(self,myname="Spinbox",**kwargs):
        self.tkClass = StatTkInter.Spinbox
        master,myname,select = _getMasterAndNameAndSelect(myname,"Spinbox")
        kwargs["master"] = master
        StatTkInter.Spinbox.__init__(self,**kwargs)
        self.isContainer = False
        GuiElement.__init__(self,myname,select)

class PanedWindow(GuiElement,StatTkInter.PanedWindow):

    def __init__(self,myname="PanedWindow",**kwargs):
        self.tkClass = StatTkInter.PanedWindow
        master,myname,select = _getMasterAndNameAndSelect(myname,"PanedWindow")
        kwargs["master"] = master
        StatTkInter.PanedWindow.__init__(self,**kwargs)
        self.isContainer = True
        GuiElement.__init__(self,myname,select)
        
    def trigger_sash_place(self,time,index,x_coord,y_coord):
        self.after(time,lambda pwin = self, i = index, x = x_coord, y=y_coord, function = self.tkClass.sash_place: function(pwin,i,x,y))

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

# File saving: sollte überarbeitet und gekürzt werden

def WidgetClass(widget):
    classString = str(widget.tkClass)
    begin = classString.find(".")+1
    end = classString.find("'",begin)
    return classString[begin:end]


# ====================================

# herausspringen, wenn es nicht gesaved werden soll.

# config dictionary holen und herauslöschen, was wir nicht saven sollen

# Widget Klasse als Text bestimmen 

# Ein Compare Widget erzeigen zum Vergleich der Config
# dann aus der Config des aktuellen Element herauslöschen, was mit dem Compare Widget übereinstimmt
#
# wenn es sich um einen Container handelt, der Widgets hat, hineingehen und diesen sichern

# wenn der Container aber nur zu sichernden Code enthält, dann nicht hineingehen und nur diesen Code sichern
# Neue Zeile für nach Container berücksichtigen

# dann bei grid oder pack das Layout schreiben

# ====================================

# Wie es jetzt sein soll:

# Widget Klasse bestimmen
#
# Wenn es kein Container ist, dann beim Create gleichb den Config machen.
# Wenn es ein Container ist, dann den Config erst im Container vornehmen
#
# Das Layout gehört nicht zum Element sondern zum Container

# ====================================


def getModifiedConfig():

    # get a reduced config only with entries, which were modified
    thisClass = WidgetClass(this())
    CompareWidget = eval("StatTkInter."+thisClass+"(container())")
    dictionaryCompare = CompareWidget.config()
    ConfDictionaryShort(dictionaryCompare)
    CompareWidget.destroy()
    
    dictionaryWidget = getconfdict()
    dictionaryWidget.pop("command",None)
    dictionaryWidget.pop("variable",None)
    dictionaryWidget.pop("image",None)
    
    dictionaryCopy = copy(dictionaryWidget)
    
    for n,e in dictionaryCopy.items():
        if e == dictionaryCompare[n]: dictionaryWidget.pop(n,None)
    return dictionaryWidget
    
    
    
def writeConfig(filehandle,dictionaryWidget,colon):
        
    for n,e in dictionaryWidget.items():
        if colon: filehandle.write(",")
        colon = True
        if n == "text":
            filehandle.write(n + '="""'+str(e)+'"""')
        else: 
            if n == "from": n = "from_"			
            filehandle.write(n + "='"+str(e)+"'")
    filehandle.write(")")
        
indent = ""

def saveElement(filehandle):
    name = getNameAndIndex()[0]
    thisClass = WidgetClass(this())
    filehandle.write(indent+thisClass+"('"+name+"'")

    if this().isContainer:
        filehandle.write(")\n\n"+indent+"goIn()\n\n")
        goIn()
        saveContainer(filehandle)
        goOut()
        filehandle.write("\n"+indent+"goOut()\n")
        return True
        
    writeConfig(filehandle,getModifiedConfig(),True)
    return False
    

def saveContainer(filehandle): pass



# ====================================


def saveOneElement(filehandle,name):

    if not this().save : return

    wasInContainer = False	
    addNl = False

    dictionaryWidget = getconfdict()
    dictionaryWidget.pop("command",None)
    dictionaryWidget.pop("variable",None)
    dictionaryWidget.pop("image",None)

    thisClass = WidgetClass(this())
    CompareWidget = eval("StatTkInter."+thisClass+"(container())")
    dictionaryCompare = CompareWidget.config()
    ConfDictionaryShort(dictionaryCompare)

    dictionaryCopy = copy(dictionaryWidget)

    for n,e in dictionaryCopy.items():
        if n == 'title':
            if e =="": dictionaryWidget.pop(n,None)
        elif n == 'link':
             if e =="": dictionaryWidget.pop(n,None)
        elif n == 'geometry':
             if e =="": dictionaryWidget.pop(n,None)
        elif n == 'text':
            if thisClass =="Listbox" and e =="": dictionaryWidget.pop(n,None)
        elif e == dictionaryCompare[n]: dictionaryWidget.pop(n,None)

    filehandle.write(indent+thisClass+"('"+name+"'")
    for n,e in dictionaryWidget.items():
        if n == "text":
            filehandle.write("," + n + '="""'+str(e)+'"""')
        else: 
            if n == "from": n = "from_"			
            filehandle.write("," + n + "='"+str(e)+"'")
    filehandle.write(")")

    CompareWidget.destroy()
    CompareWidget=StatTkInter.Frame(container(),width=0,height=0)

    wasInside = False
    if this().hasWidgets():
        wasInside = True
        filehandle.write("\n"+indent+"goIn()\n\n")

        if this().onlysavecode and len(this().CODE) != 0:
            filehandle.write("### CODE ===================================================\n")
            filehandle.write(this().CODE)
            filehandle.write("### ========================================================\n")
        else:
            goIn()
            saveContainerOld(filehandle)
            goOut()

        filehandle.write("\n"+indent+"goOut()\n")
        if this().Layout != PACKLAYOUT and this().Layout != PANELAYOUT: addNl=True
        wasInContainer = True

    if this().Layout & 6: # GRID OR PLACE
        layoutWidget = layout_info()
        layoutWidget.pop(".in",None)

        first = True
        layoutCompare=None
        if this().Layout == GRIDLAYOUT:
            if wasInside: filehandle.write(indent+"grid(")
            else: filehandle.write(".grid(")
            CompareWidget.grid()
            layoutCompare = CompareWidget.grid_info()
        else: 
            if wasInside: filehandle.write(indent+"place(")
            else: filehandle.write(".place(")
            CompareWidget.place(x=-1,y=-1)
            layoutCompare = CompareWidget.place_info()
        
        layoutCopy = copy(layoutWidget)
        for n,e in layoutCopy.items():
            if e == layoutCompare[n]: layoutWidget.pop(n,None)

        for n,e in layoutWidget.items():
            if not first: filehandle.write(",")			
            filehandle.write(n+"='"+str(e)+"'")
            first=False
        filehandle.write(")\n")
    else: filehandle.write("\n")

    if addNl: filehandle.write("\n")
    CompareWidget.destroy()
    return wasInContainer

    
def saveContainerOld(filehandle):
    dictionary = container().Dictionary.elements
    
    for n,e in dictionary.items():
        for x in e:
            setWidgetSelection(x)
            saveOneElement(filehandle,n)

    packlist = container().PackList
    if len(packlist) != 0:
        filehandle.write("\n")
        for e in packlist:
            filehandle.write(indent+"widget('")
            setWidgetSelection(e)
            nameAndIndex = getNameAndIndex()
            if nameAndIndex[1] == -1: filehandle.write(nameAndIndex[0]+"')")
            else: filehandle.write(nameAndIndex[0]+"',"+str(nameAndIndex[1])+")")

            layoutWidget = layout_info()

            if this().Layout == PACKLAYOUT:
                CompareWidget=StatTkInter.Frame(container(),width=0,height=0)
                layoutWidget.pop(".in",None)
                filehandle.write(".pack(")
                CompareWidget.pack()
                layoutCompare = dict(CompareWidget.pack_info())
                CompareWidget.destroy()
            else:
                filehandle.write(".pane(")
                layoutCompare = {'sticky': 'nesw', 'minsize': 0, 'width': '', 'pady': 0, 'padx': 0, 'height': ''}

            layoutCopy = copy(layoutWidget)
            first = True
            for n,e in layoutCopy.items():
                if e == layoutCompare[n]: layoutWidget.pop(n,None)

            for n,e in layoutWidget.items():
                if not first: filehandle.write(",")			
                filehandle.write(n+"='"+str(e)+"'")
                first=False
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
                filehandle.write(indent+"container().trigger_sash_place("+str(i*100)+","+str(i)+","+str(sash_list[i][0])+","+str(sash_list[i][1])+")\n")

    cdDir()

    # was ist mit gelocktem code? Der Code sollte geschrieben werden, nur die widgets nicht
    if len(container().CODE) != 0:
        filehandle.write("\n### CODE ===================================================\n")
        filehandle.write(container().CODE)
        filehandle.write("### ========================================================\n")
        

# ===================================================
#    Sicherung Container oder einzelnes Element
#
# Wenn wir es mit config sichern, dann ist nochmals dasselbe zu tun,
# wie wir es beim Einzelelement hatten, doch warum?
#
# ===================================================


def saveWidgets(filehandle,withConfig=False):
    if not this().save: return	
    wasInContainer = False
    if this() == container():
        if withConfig:
            dictionaryCompare = None
            CompareWidget = None
            wdestroy = False
            if this().isMainWindow:
                dictionaryCompare = _AppConf
            else:
                thisClass = WidgetClass(this())
                CompareWidget = eval("StatTkInter."+thisClass+"(container())")
                dictionaryCompare = CompareWidget.config()
                ConfDictionaryShort(dictionaryCompare)
                wdestry = True
            
            dictionaryWidget = getconfdict()
            dictionaryWidget.pop("command",None)
            dictionaryWidget.pop("variable",None)
            dictionaryCopy = copy(dictionaryWidget)

            for n,e in dictionaryCopy.items():
                if n == 'title':
                    if e =="" or not this().title_changed: dictionaryWidget.pop(n,None)
                elif n == 'link':
                     if e =="": dictionaryWidget.pop(n,None)
                elif n == 'geometry':
                     if e =="" or not this().geometry_changed: dictionaryWidget.pop(n,None)
                elif n == 'text':
                    if thisClass =="Listbox" and e =="": dictionaryWidget.pop(n,None)
                elif e == dictionaryCompare[n]: dictionaryWidget.pop(n,None)

            if len(dictionaryWidget) != 0:
                filehandle.write(indent+"config(")
                first = True

                for n,e in dictionaryWidget.items():
                    if not first: filehandle.write(",")
                    first = False
                    if n == "text":
                        filehandle.write(n + '="""'+str(e)+'"""')
                    else: 
                        if n == "from": n = "from_"			
                        filehandle.write(n + "='"+str(e)+"'")
                filehandle.write(")\n")

            if wdestroy: CompareWidget.destroy()
            
        saveContainerOld(filehandle)
    else: 
        wasInContainer = saveOneElement(filehandle,getNameAndIndex()[0])
        if this().Layout == PACKLAYOUT or this().Layout == PANELAYOUT: 
            CompareWidget=StatTkInter.Frame(container(),width=0,height=0)
            layoutWidget = layout_info()
            if this().Layout == PACKLAYOUT:
                layoutWidget.pop(".in",None)
                filehandle.write(indent+"pack(")
                CompareWidget.pack()
                layoutCompare = CompareWidget.pack_info()
            else:
                filehandle.write(indent+"pane(")
                container().add(CompareWidget)
                layoutCompare = GuiElement.pane_info(CompareWidget)
            layoutCopy = copy(layoutWidget)
            first = True
            for n,e in layoutCopy.items():
                if e == layoutCompare[n]: layoutWidget.pop(n,None)

            for n,e in layoutWidget.items():
                if not first: filehandle.write(",")			
                filehandle.write(n+"='"+str(e)+"'")
                first=False
            filehandle.write(")\n")
            if wasInContainer: filehandle.write("\n")
    

_code_list = []

def _store_code():
    container().CODE = _code_list.pop(0)

def DynImportCode(filename):
    global LOADforEdit
    global _code_list
    _code_list = []
    #print("DynImport")

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
        if isEnd: break

        guicode+="\t_store_code()\n"	

        code = ""	
        while True:
            line = handle.readline()
            if not line:
                handle.close()
                print("Code end '### ' missing")
    

            if line[0:4] == "### ": break
            code+=line

        if not LOADforEdit:	
            guicode += code
        _code_list.append(code)
        code = ""
            
    handle.close()
    evcode = compile(guicode,filename,'exec')
    eval(evcode)
    _code_list = []




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



def clean_eval(evcode):
    glob_before = globals().keys()
    eval(evcode)
    glob_after = globals().keys()
    for element in glob_after:
        if element not in glob_before: del globals()[element]


'''
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

'''
def load_Script(parent,filename):
    try:
        handle = open(filename,'r')
    except: 
        print("Couldn't open file: " + filename)
        return
    code = handle.read()
    handle.close()
    evcode = compile(code,filename,'exec')
    exec(evcode)
'''

def DynLink(filename):
    goIn()
    DynLoad(filename)
    goOut()

def quit(): _AppRoot._widget.quit()


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
