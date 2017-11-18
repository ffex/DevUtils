import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Core"))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Linux"))

import LinuxNoteManager
import LinuxFolderManager
import LinuxURLManager

from Core import ClipboardWatcher
from Core.ClipboardWatcher import ClipboardWatcher
from Linux import LinuxClipboardManager


class main:

    def __init__(self):

        self.__mrgfolder = LinuxFolderManager.LinuxFolderManager()
        self.__mrgclipboard= LinuxClipboardManager.LinuxClipboardManager()
        self.__mrgurl= LinuxURLManager.LinuxURLManager()
        self.__mrgcode= LinuxNoteManager.LinuxNoteManager('Code')
        self.__mrgnote= LinuxNoteManager.LinuxNoteManager('Note')


        self._thread = ClipboardWatcher(self.__mrgclipboard)
        self._thread.start()


    def start(self):
        run=True


        while run:
            os.system("clear")
            print("Welcome to ffex console. What do you need?")
            print("1 - Open favorite folder")
            print("2 - Take a note")
            print("3 - Take a link")
            print("4 - Take a code")
            print("5 - List of clipboard")
            print("d - Debug command")
            print("q - quit")
            print("")
            action = input("-> ")
            os.system("clear")
            if action == "1":
                self.__mrgfolder.commandfolders()
                self.__mrgfolder._saveFile()
            elif action == "2":
                self.__mrgnote.commandCode()

            elif action =="3":
                self.__mrgurl.commandURL()
                self.__mrgurl._saveFile()
            elif action=="4":
                self.__mrgcode.commandCode()
				
            elif action == "5":
                self.__mrgclipboard.command()
	
            elif action == "d":
                print(self.__mrgfolder.getdict())
            elif action=="q":
                os.system("clear")
                run=False
                self._thread.stop()


m=main()
m.start()


#def Command(action):
#    if action==1:
