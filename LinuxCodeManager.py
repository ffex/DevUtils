import os
import MultiFile

class LinuxCodeManager(MultiFile.MultiFile):
	def __init__(self):
		super(LinuxCodeManager,self).__init__("Code")
		