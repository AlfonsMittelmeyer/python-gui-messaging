import DynTkInter as tk

def Access(param,tk=tk):

    filename = param[0]
    classlist = param[1]

    class_register = {}

    def class_type(myclass):
        classString = str(myclass)
        begin = classString.find(".")+1
        end = classString.find("'",begin)
        return classString[begin:end]
    
    for entry in classlist: class_register[class_type(entry)] = entry

    def create_widget(default_class,name,**kwargs):
        myclass = default_class
        if 'myclass' in kwargs:
            myclass = class_register[kwargs.pop('myclass')]
        return myclass(name,**kwargs)

    def Button(name,**kwargs): return create_widget(tk.Button,name,**kwargs)
    def Toplevel(name,**kwargs): return create_widget(tk.Topleve,name,**kwargs)
    def Message(name,**kwargs): return create_widget(tk.Message,name,**kwargs)
    def Label(name,**kwargs): return create_widget(tk.Label,name,**kwargs)
    def Checkbutton(name,**kwargs): return create_widget(tk.Checkbutton,name,**kwargs)
    def Radiobutton(name,**kwargs): return create_widget(tk.Radiobutton,name,**kwargs)
    def Entry(name,**kwargs): return create_widget(tk.Entry,name,**kwargs)
    def Text(name,**kwargs): return create_widget(tk.Text,name,**kwargs)
    def Spinbox(name,**kwargs): return create_widget(tk.Spinbox,name,**kwargs)
    def Scale(name,**kwargs): return create_widget(tk.Scale,name,**kwargs)
    def Listbox(name,**kwargs): return create_widget(tk.Listbox,name,**kwargs)
    def Scrollbar(name,**kwargs): return create_widget(tk.Scrollbar,name,**kwargs)
    def Frame(name,**kwargs): return create_widget(tk.Frame,name,**kwargs)
    def LabelFrame(name,**kwargs): return create_widget(tk.LabelFrame,name,**kwargs)
    def PanedWindow(name,**kwargs): return create_widget(tk.PanedWindow,name,**kwargs)
    def Canvas(name,**kwargs): return create_widget(tk.Canvas,name,**kwargs)
    def Menu(name,**kwargs): return create_widget(tk.Menu,name,**kwargs)
    def MenuDelimiter(name,**kwargs): return create_widget(tk.MenuDelimiter,name,**kwargs)
    def Menubutton(name,**kwargs): return create_widget(tk.Menubutton,name,**kwargs)

    def MenuItem(name,item_type,**kwargs):
        myclass = tk.MenuItem
        if 'myclass' in kwargs:
            myclass = class_register[kwargs.pop('myclass')]
        return myclass(name,item_type,**kwargs)

    exec(compile(open(filename, "r").read(), filename, 'exec'))
