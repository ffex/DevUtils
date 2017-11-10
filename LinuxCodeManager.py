import os
import MultiFile

class LinuxCodeManager(MultiFile.MultiFile):
    def __init__(self):
        super(LinuxCodeManager,self).__init__("Code")
	
    def deleteCode(self,num):
	    
        self._deleteFile(num)
        pass #TODO
		
    def addCode(self):
        title = input("title: ")
        self._addFile(title)
        #aprire il nano
        os.system("nano " + os.path.join(self._dir,title))
		
    def printCodeList(self):
        cnt = 0
        for elem in self._titles:
            print(str(cnt) + " - " + elem)
            cnt = cnt + 1
		
    def commandCode(self):
        print("Open a piece of Code by number")
        self.printCodeList()

        #print(os.listdir(self._dir))
        print("-------------------->>>")
        print("a - add new Code")
        print("d - delete Code")
        print("q - quit to main menu")
        action = input("-> ")
        if action == "a":
            self.addCode()
        elif action == "d":
            num1 = input("Which one? > ")
            self.deleteCode(int(num1))
        elif action == "q":
            pass
        else:
            num = int(action[0:2])
            #TODO aprire appunti
            os.system("clear")
