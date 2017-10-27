import os
import folders

class LinuxFolderManager(folders.folders):
<<<<<<< HEAD

=======
    GUI=False
>>>>>>> d79e6aacc34ed0b1b0d182729da1cd1eeb721b98
    def __init__(self):
        folders.folders.__init__(self)


    # folders method
<<<<<<< HEAD
=======
    def deletefolder(self,num):
        self._deletefolder(num)
        pass #TODO
    
    def settingGUI:
        pass #TODO
>>>>>>> d79e6aacc34ed0b1b0d182729da1cd1eeb721b98
    def addfolder(self):
        title = input("title: ")
        path = input("pathname: ")
        self._addfolderfile(title, path)

    def printfolders(self):
        cnt = 0
        for elem in self._dict.values():
            print(str(cnt) + " - " + elem[0])
            cnt = cnt + 1

    def commandfolders(self):
<<<<<<< HEAD
        print("Open a folder by number")
        self.printfolders()
        print("a - add new folder")
        action = input("-> ")
        if action == "a":
            self.addfolder()
        else:
            num = int(action[0:2])
            # print(self._dictfolders[num][1])
            os.system("nautilus " + self._dict[num][1] + " 2>/dev/null &")
            os.system("clear")
=======
        print("Open a dir by number")
        if GUI:
             print("-> GUI")
        else:
             print("-> CLI")
        self.printfolders()
        print("a - add new dir")
        print("d - delete dir")
        print("t - CLI or GUI")
        print("q - quit to main menu")
        action = input("-> ")
        if action == "a":
            self.addfolder()
        elif action == "d":
            pass #TODO
        elif action == "t":
            GUI=!GUI
        elif action == "q":
            pass
        else:
            num = int(action[0:2])
            # print(self._dictfolders[num][1])
            if GUI:
                os.system("nautilus " + self._dict[num][1] + " 2>/dev/null &")
            else:
                pass #TODO
            os.system("clear")
>>>>>>> d79e6aacc34ed0b1b0d182729da1cd1eeb721b98
