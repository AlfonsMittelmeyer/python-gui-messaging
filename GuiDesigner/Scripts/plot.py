config(text='Madplotlib')


### CODE ===================================================

class Plot_Frame:
    
    def __init__(self,container=container()):
        self.container = container

        self.fig = Figure (figsize=(5,4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax = self.fig.add_subplot(111) #für 2d-Plot
        self.ax.set_title('Definition der LRUGL')
        self.ax.set_xlabel('Breite y [mm]')
        self.ax.set_ylabel('Hoehe z [mm]')
        self.ax.axis([-2000,2000,0, 5000])
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig,container)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas,container)
        self.toolbar.update()
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.lineVal, = self.ax.plot(np.zeros(100))
        self.canvas.mpl_connect('motion_notify_event', self.onMouseMove)
        self.canvas.show()

        subscribe('REQUEST_FIG,AX',self.fig_ax_request)

    def onMouseMove(self, event):

        self.ax.lines = [self.ax.lines[0]]
        if event.xdata and event.ydata: # python3 often has None
            self.ax.axhline(y=event.ydata, color="k") #(y=event.ydata, color="k")
            self.ax.axvline(x=event.xdata, color="k") #(x=event.xdata, color="k")   
        self.canvas.show()

    def fig_ax_request(self):
        publish('FIG,AX',self.fig,self.ax)

Plot_Frame()

### ========================================================
