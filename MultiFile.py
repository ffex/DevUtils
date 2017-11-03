import os

class MultiFile:
    def __init__(self,type):
        self._type=type
        path=os.path.join(os.path.realpath(__file__),type)
        if !(os.path.isdir(path)):
            os.makedirs(path)
        self._dir=os.path.dirname(os.path.realpath(__file__))
        self._titles=[]
        self.loadTitles()
        
        
    def loadTitles(self):
        if os.path.isdir(self._dir):
            dirs = os.listdir(path)
            for file in dirs:
                self._titles.append(file)
                
    
    def getTitles(self):
        if len(self._titles)>0:
            return self._titles
        else
            return 0
    def addFile(self):
        
    def deleteFile(self):
        
