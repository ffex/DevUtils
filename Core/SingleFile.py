import os


class SingleFile:


    def __init__(self,type):
        self._dict = {}
        nameproj="";
        self._last = 0
        self._type=type
        self.__dir_path = os.path.dirname(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'Projects',nameproj))

        self._loadFile()

    def _deleteElem(self, num):
        # del self._dict[num]
        #TODO ci son degli errori! e grossi anche!
        self._dict.pop(num, None)
        self._last = self._last -1

    def _addElem(self, title, content):

        # out_file=open(self.__dir_path + "/folders","a")
        # out_file.write(title + "\n")
        # out_file.write(path + "\n")
        # out_file.close()
        self._dict.update({self._last: [title, content]})
        self._last = self._last + 1

    def _saveFile(self):
        os.remove(self.__dir_path + "/" + self._type)
        out_file = open(self.__dir_path + "/" + self._type, "a")
        for x in self._dict.items():
            out_file.write(str(x[1][0]) + "\n")
            out_file.write(str(x[1][1]) + "\n")
        out_file.close()

    def _loadFile(self):
        if os.path.isfile(self.__dir_path + "/" + self._type):
            in_file = open(self.__dir_path + "/" + self._type, "r")
            line1 = "temp"
            cnt = 0
            while line1 != "":
                line1 = in_file.readline()
                line2 = in_file.readline()
                if line1 != "":
                    self._dict[cnt] = [line1.replace("\n", ""), line2.replace("\n", "")]
                cnt = cnt + 1
            in_file.close()
            self._last = cnt - 1
        else:
            in_file = open(self.__dir_path + "/" + self._type, "w")
        in_file.close()

    def getdict(self):
        return self._dict





