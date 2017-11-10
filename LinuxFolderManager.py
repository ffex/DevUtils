import os
import SingleFile

class LinuxFolderManager(SingleFile.SingleFile):

    GUI=False

    def __init__(self):
        super(LinuxFolderManager,self).__init__("folder")




    # folders method

    def deletefolder(self,num):
        self._deleteElem(num)
        pass #TODO
    
    def settingGUI(self):
        pass #TODO

    def addfolder(self):
        title = input("title: ")
        content = input("pathname: ")
        self._addElem(title, content)

    def printfolders(self):
        cnt = 0
        for elem in self._dict.values():
            print(str(cnt) + " - " + elem[0])
            cnt = cnt + 1

    def commandfolders(self):
        print("Open a dir by number")
        if self.GUI:
             print("-> GUI")
        else:
             print("-> CLI")
        self.printfolders()
        print("-------------------->>>")
        print("a - add new dir")
        print("d - delete dir")
        print("t - CLI or GUI")
        print("q - quit to main menu")
        action = input("-> ")
        if action == "a":
            self.addfolder()
        elif action == "d":
            num1=input("Which one? > ")
            self.deletefolder(int(num1))
        elif action == "t":
            self.GUI= not self.GUI
        elif action == "q":
            pass
        else:
            num = int(action[0:2])
            # print(self._dictfolders[num][1])
            if self.GUI:
                os.system("nautilus " + self._dict[num][1] + " 2>/dev/null &")
            else:
                pass #TODO
            os.system("clear")

