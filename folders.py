import os
class folders:
    _dict={}
    _last=0
    __dir_path =""
    def _deletefolderfile(self, num):
        _dict.pop(num,None)
    
    def _addfolderfile(self,title,path):

        #out_file=open(self.__dir_path + "/folders","a")
        #out_file.write(title + "\n")
        #out_file.write(path + "\n")
        #out_file.close()
        self._dict.update({self._last :[title,path]})
        self._last=self._last+1
    def _savefile(self):
        out_file=open(self.__dir_path + "/folders","a")
        for x in _dict.items:
            out_file.write(x[0] + "\n")
            out_file.write(x[1] + "\n")
        out_file.close()
    def _loadfolders(self):

        in_file= open(self.__dir_path + "/folders","r")
        line1="temp"
        cnt=0
        while line1!= "":
            line1 = in_file.readline()
            line2 = in_file.readline()
            if line1!="":
                self._dict[cnt]=[line1.replace("\n",""),line2.replace("\n","")]
            cnt=cnt+1
        in_file.close()
        self._last=cnt-1

    def getdict(self):
        return self._dict

    def __init__(self):
        self.__dir_path=os.path.dirname(os.path.realpath(__file__))
        self._loadfolders()

