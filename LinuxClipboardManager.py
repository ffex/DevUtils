import Clipboard
import os

class LinuxClipboardManager(Clipboard.Clipboard):

    def command(self):
        cnt=0
        for elem in self._clipboardlist:
            print(cnt, " - ",elem )
            cnt = cnt+1
        print("q - quit to main menu")
        action= input("Which one would you set in clipboard? > ")


        if action == "q":
            os.system("clear")
        else:
            self.setactual(int(action))
