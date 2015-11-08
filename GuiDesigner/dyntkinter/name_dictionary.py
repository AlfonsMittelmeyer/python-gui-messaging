class GuiDictionary:

    def __init__(self): self.elements = {}

    def setElement(self,name,thisone):
        if not name in self.elements: self.elements[name] = [thisone]
        else: self.elements[name].append(thisone)

    def getEntry(self,name,nr=0):
        if name in self.elements: return self.elements[name][nr]
        return None
