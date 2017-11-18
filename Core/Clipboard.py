import Global
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class Clipboard:
    def __init__(self):
        self._clipboardlist=[]

    def addelement(self,elem):
        self._clipboardlist.append(elem)

    def item(self,key):
        return self._clipboardlist[key]

    def list(self):
        return self._clipboardlist

    def empty(self):
        pass


    def setactual(self,num):

        Gtk.Clipboard.set_text(Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD),self._clipboardlist[num],len(self._clipboardlist[num]))
        self._clipboardlist.pop(num)

        #Gtk.Clipboard.set_text(self._clipboardlist[num])




