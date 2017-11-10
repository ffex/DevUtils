import os

class MultiFile:
    def __init__(self,type):
        self._type=type
        path=os.path.join(os.path.dirname(os.path.realpath(__file__)),type)
        if not(os.path.isdir(path)):
            os.makedirs(path)
        self._type=type
        self._dir=path
        self._titles=[]
        self._loadTitles()
        
        
    def _loadTitles(self):
        
        dirs = os.listdir(self._dir)
        for file in dirs:
            self._titles.append(file)
                
	
    def _getTitles(self):
        if len(self._titles)>0:
            return self._titles
        else:
            return 0
			
    def _addFile(self,title):
        self._titles.append(title)
        #salvataggio del file
        if not os.path.isfile(os.path.join(self._dir,title)):
            file = open(os.path.join(self._dir,title), "w")
            file.close()
	    
        
    def _deleteFile(self,num):
        os.remove(os.path.join(self._dir,self._titles[num]))
        #da guardare
        titles._self.remove(num)
