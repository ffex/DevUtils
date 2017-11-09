import os

class MultiFile:
    def __init__(self,type):
        self._type=type
        path=os.path.join(os.path.realpath(__file__),type)
        if !(os.path.isdir(path)):
            os.makedirs(path)
	    self._type=type
        self._dir=os.path.dirname(path)
        self._titles=[]
        self._loadTitles()
        
        
    def _loadTitles(self):
        
        dirs = os.listdir(self._dir)
        for file in dirs:
            self._titles.append(file)
                
	
    def _getTitles(self):
        if len(self._titles)>0:
            return self._titles
        else
            return 0
			
    def _addFile(self,title):
	    self._titles.append(title)
		#salvataggio del file
	    
        
    def _deleteFile(self,title):
		os.remove(os.path.join(self._dir,title))
	#da guardare
        self._titles.remove(title)
