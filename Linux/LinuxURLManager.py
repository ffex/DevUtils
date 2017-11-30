import os
import Global

from Core import SingleFile


class LinuxURLManager(SingleFile.SingleFile):
    def __init__(self):
        super(LinuxURLManager, self).__init__("URLS")

    def deleteURL(self,num):
        self._deleteElem(num)
        pass #TODO
		
    def addURL(self):
        title = input("title: ")
        content = input("pathname: ")
        self._addElem(title, content)

    def addURLclip(self,content):
        title = input("title: ")
        self._addElem(title, content)
		
    def printURLS(self):
        cnt = 0
        for elem in self._elem:
            print(str(cnt) + " - " + elem[0])
            cnt = cnt + 1
    def commandURL(self):
        print("Open a URL by number")
        self.printURLS()
        print("-------------------->>>")
        print("a - add new URL")
        print("d - delete URL")
        print("v - copy from clip")
        print("q - quit to main menu")
        action = input("-> ")
        if action == "a":
            self.addURL()
        elif action == "d":
            num1 = input("Which one? > ")
            self.deleteURL(int(num1))
        elif action == "v":
            self.addURLclip(Global.mrgclipboard.lastItem())

        elif action == "q":
            pass
        else:
            num = int(action[0:2])
            #TODO aprire browser
            os.system("clear")
