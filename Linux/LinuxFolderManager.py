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
        self._deleteElem(int(num))
        
    
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

    def __command(self,commands):
        commands=commands.split(",")
        com=commands[0]
        comL=len(commands)
        if com=="a":
            title=None
            content=None
            if comL==2:
                title=commands[1]
            elif comL==3:
                title=commands[1]
                content=commands[2]
            self.addfolder(title,content)
        elif com=="d":
            number=None;
            if comL==2:
                number=commands[1]
            self.deletefolder(number)
        elif com=="v":
            title=None
            if comL==2:
		title=commands[1]
            self.addfolder(title,Global.mrgclipboard.lastItem())
        elif com=="q":
            pass
        else:
            try:
                num = int(com)
                os.system("nautilus " + self._elem[num][1] + " 2>/dev/null &")
                #os.system("explorer \"" + self._elem[num][1] + "\"")
            except ValueError:
                print('Not a valid command')

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
        self.__command(action)
            # print(self._dictfolders[num][1])
            #if self.GUI:
            #    pass #TODO
            #else:
            #    os.system("explorer \"" + self._elem[num][1] + "\"")#TODO fare dei comandi esterni che a seconda dell'os scelgono il da farsi! :D
                #os.system("nautilus " + self._elem[num][1] + " 2>/dev/null &")#TODO fare dei comandi esterni che a seconda dell'os scelgono il da farsi! :D
            #os.system("clear")

