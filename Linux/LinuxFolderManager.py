import os
import Global
from Core import SingleFile



class LinuxFolderManager(SingleFile.SingleFile):

    GUI=False

    def __init__(self):
        super(LinuxFolderManager,self).__init__("folder")




    # folders method

    def deletefolder(self,num):
	    #retest
        if num==None:
            num=input("Which one? > ")
        self._deleteElem(num)
        
    
    def settingGUI(self):
        pass #TODO
	
    def addfolder(self,title=None,content=None):
        if title == None:
            title = input("title: ")
        if content == None:
            content = input("pathname: ")
        self._addElem(title, content)
		
    #def addfolder(self):
    #    title = input("title: ")
    #    content = input("pathname: ")
    #    self._addElem(title, content)

    #def addfolderclip(self,content):
    #    title = input("title: ")
    #    self._addElem(title, content)

    def printfolders(self):
        cnt = 0
        for elem in self._elem:
            print(str(cnt) + " - " + elem[0])
            cnt = cnt + 1
#commands!
        # a
        # a,title
        # a,title,path
        # d
        # dnum
        # v
        # v,title
        # num -> se nel campo d'azione
        #
        #
    def __command(self,commands):
        commands=commands.split(",")
        com=commands[0]
        comL=len(commands)
        if com=="a":
            title=None
            tent=None
            if comL==2:
                title=commands[1]
            elif comL==3:
                title=commands[1]
                folderdir=commands[2]
            f.addfolder(title,content)
        elif com=="d":
            number=None;
            if comL==2:
                number=commands[1]
            self.deletefolder(number)
        elif com=="v":
            self.addfolder(None,Global.mrgclipboard.lastItem())
        else:
            pass

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
        print("v - copy from clip")
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
        elif action == "v":
            self.addfolderclip(Global.mrgclipboard.lastItem())

        elif action == "q":
            pass
        else:
            num = int(action[0:2])
            # print(self._dictfolders[num][1])
            if self.GUI:
                pass #TODO
            else:
                #os.system("explorer /select,\"" + self._elem[num][1] + "\"")#TODO fare dei comandi esterni che a seconda dell'os scelgono il da farsi! :D
                os.system("nautilus " + self._elem[num][1] + " 2>/dev/null &")#TODO fare dei comandi esterni che a seconda dell'os scelgono il da farsi! :D
            os.system("clear")

