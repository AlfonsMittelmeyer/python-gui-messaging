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
