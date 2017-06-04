from appimports import *
import testgui


def MenuGUI(self):

    def test():
        testgui.TestGui(self)

    # for testing
    self.entryconfig(self.test_index,command = test)
    
    def receive_language(languages):
        
        self.entryconfig(self.languages_index,label = languages[0]) 
        publish('SUBMENU_LANGUAGES',languages[1:])

    subscribe('MENU_LANGUAGE',receive_language)

class LanguageSubmenu:

    def __init__(self,container):
        self.container = container
        self.deutsch_index = container.deutsch_index

        self.entry_count = self.deutsch_index + 1
        subscribe('SUBMENU_LANGUAGES',self.create_menu)
                  
    
    def do_action(self,language):
        publish("SELECT_LANGUAGE",language)


    def create_menu(self,languages):


        # now we delete the menu entries after deutsch
        after_deutsch = self.deutsch_index + 1
        for entries in range(after_deutsch,self.entry_count):
            self.container.delete(after_deutsch)
            
        # now we make a dynamic creation
        # first we get the style of the first command
        # this style should also be used for the other commands

        command_config = get_entryconfig(self.container,self.deutsch_index)
        
        # now we create dynamic commands

        # Example
        # languages = (('Deutsch','german'),None,('English','english'),('Spanisch','spanish'),('Franzoesisch','french'))

        entry_index = self.deutsch_index - 1 

        for language in languages:
            entry_index += 1

            if not language:
                self.container.add_separator()
                continue

            command_config['label'] = language[0]
            command_config['command'] = partial(self.do_action,language[1])
               
            if entry_index == self.deutsch_index :
                self.container.entryconfig(entry_index,**command_config)
            else:
                self.container.add_command(**command_config)

        self.entry_count = entry_index + 1
        

def PlotFrame(self):

    self.fig = Figure (figsize=(5,4), dpi=100)
    self.ax = self.fig.add_subplot(111)
    self.ax = self.fig.add_subplot(111) #fuer 2d-Plot
    self.ax.set_title('Definition der LRUGL')
    self.ax.set_xlabel('Breite y [mm]')
    self.ax.set_ylabel('Hoehe z [mm]')
    self.ax.axis([-2000,2000,0, 5000])
    self.ax.grid(True)

    self.canvas = FigureCanvasTkAgg(self.fig,self)
    self.toolbar = NavigationToolbar2TkAgg(self.canvas,self)
    self.toolbar.update()
    self.plot_widget = self.canvas.get_tk_widget()
    self.plot_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    self.ax.plot(np.zeros(100))

    def onMouseMove(event):

        self.ax.lines = [self.ax.lines[0]]
        if event.xdata and event.ydata: # python3 often has None
            self.ax.axhline(y=event.ydata, color="k") #(y=event.ydata, color="k")
            self.ax.axvline(x=event.xdata, color="k") #(x=event.xdata, color="k")   
        self.canvas.show()

    self.canvas.mpl_connect('motion_notify_event', onMouseMove)
    self.canvas.show()

    def fig_ax_request():
        publish('FIG,AX',self.fig,self.ax)

    subscribe('REQUEST_FIG,AX',fig_ax_request)

