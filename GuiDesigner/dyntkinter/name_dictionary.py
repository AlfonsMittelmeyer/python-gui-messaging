class NONAMES:
    pass

NONAME = NONAMES()
NONAMECANVAS = NONAMES()
NONAME2 = NONAMES()
NONAME_HILI = NONAMES()
NONAME_MOVE = NONAMES()


class GuiDictionary:

    def __init__(self): self.elements = {}

    def setElement(self,name,thisone):
        if not name in self.elements: self.elements[name] = [thisone]
        else: self.elements[name].append(thisone)

    def getEntry(self,name,nr=0):
        if name in self.elements: return self.elements[name][nr]
        return None

    def eraseEntry(self,name,index):
        dictionary=self.elements	
        if name in dictionary:
            elist = dictionary[name]
            e = elist[index]
            elist.pop(index)
            if len(elist)==0: dictionary.pop(name,None)
            return e
        else: return None

    def getChildrenList(self):
        element_list = []
        for name,entry in self.elements.items():
            for x in entry: element_list.append(x)
        return element_list

    def getChildDictionary(self):
        children = {}
        for name,entry in self.elements.items():
            if not isinstance(name,NONAMES): 
                for x in entry: children[x] = name
        return children

    def getChildDictionaryWith(self,withname):
        children = {}
        for name,entry in self.elements.items():
            if name == withname or not isinstance(name,NONAMES): 
                for x in entry: children[x] = name
        return children


    def getEntryByStringAddress(self,refstring):
        for name,entry in self.elements.items():
            for x in entry:
                if str(x) == refstring: return x
        return None

    def getNameAndIndex(self,reference):
        for name,entry in self.elements.items():
            for index in range(len(entry)):
                if entry[index] == reference:
                    if len(entry) == 1: return name,-1
                    else: return name,index
        return None,None

    def getNameAndIndexByStringAddress(self,reference_string):
        for name,entry in self.elements.items():
            for index in range(len(entry)):
                if str(entry[index]) == reference_string:
                    if len(entry) == 1: return name,-1
                    else: return name,index
        return None,None
