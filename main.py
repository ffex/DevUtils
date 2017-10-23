import os
import LinuxFolderManager

class main:
    __mrgfolder=LinuxFolderManager.LinuxFolderManager()



    def start(self):
        run=True
        while run:
            print("Welcome to ffex console. What do you need?")
            print("1 - Open favorite folder")
            print("2 - Take a note")
            print("3 - Take a link")
            print("4 - Take a Code")
            print("5 - List of clipboard")
            print("d - Debug command")
            print("q - quit")
            print("")
            action = input("-> ")
            os.system("clear")
            if action == "1":
                self.__mrgfolder.commandfolders()
            elif action == "d":
                print(self.__mrgfolder.getdict())
            elif action=="q":
                os.system("clear")
                run=False


m=main()
m.start()


#def Command(action):
#    if action==1:
