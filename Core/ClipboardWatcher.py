import sys
import threading
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class ClipboardWatcher(threading.Thread):
    def __init__(self,clipboard):
        super(ClipboardWatcher,self).__init__()
        #self._predicate=predicate
        #self._callback=callback
        #self._pause=pause
        self._stopping =False
        self._clipboard =clipboard
        self._clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self._clip.connect('owner-change', self.callBack)



    def callBack(self, *args):
        self._clipboard.addelement(self._clip.wait_for_text())

    def run(self):

        Gtk.main()
    def stop(self):
        Gtk.main_quit()



