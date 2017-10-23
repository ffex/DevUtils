import os
import folders

class LinuxFolderManager(folders.folders):

    def __init__(self):
        folders.folders.__init__(self)


    # folders method
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