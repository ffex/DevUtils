import os

class MultiFile:
    def __init__(self,type):
        self._type=type
        path=os.path.join(os.path.realpath(__file__),type)
        if (os.path.isdir(path)):
            
        self._dir=os.path.dirname(os.path.realpath(__file__))
        self._dict={}
        
    def loadTitles(self):
        
        
    
