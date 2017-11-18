import os

Linuxdir=os.path.join(os.path.dirname(os.path.realpath(__file__)),"Linux")

import sys
sys.path.append(Linuxdir)
print(sys.path)

import LinuxCodeManager