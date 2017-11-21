import os


class SingleFile:


    def __init__(self,type):
        self._elem = []
        nameproj="";

        self._type=type
        self.__dir_path = os.path.dirname(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'Projects',nameproj))

        self._loadFile()

    def _deleteElem(self, num):
        # del self._dict[num]
        #TODO ci son degli errori! e grossi anche!
        self._elem.remove(self._elem[num])
        #del self._dict.items()[self._dict[num]]
        pass

    def _addElem(self, title, content):

        # out_file=open(self.__dir_path + "/folders","a")
        # out_file.write(title + "\n")
        # out_file.write(path + "\n")
        # out_file.close()
        self._elem.append([title, content])


    def _saveFile(self):
        os.remove(self.__dir_path + "/" + self._type)
        out_file = open(self.__dir_path + "/" + self._type, "a")
        for x in self._elem:
            out_file.write(str(x[0]) + "\n")
            out_file.write(str(x[1]) + "\n")
        out_file.close()

    def _loadFile(self):
        if os.path.isfile(self.__dir_path + "/" + self._type):
            in_file = open(self.__dir_path + "/" + self._type, "r")
            line1 = "temp"

            while line1 != "":
                line1 = in_file.readline()
                line2 = in_file.readline()
                if line1 != "":
                    self._elem.append([line1.replace("\n", ""), line2.replace("\n", "")])

            in_file.close()

        else:
            in_file = open(self.__dir_path + "/" + self._type, "w")
        in_file.close()

    def getElem(self):
        return self._elem





