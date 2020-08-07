from ctypes import *
import os

import pancake2d.API
import pancake2d.useless
import pancake2d.window
import pancake2d.graphics

mypath = os.path.dirname(os.path.realpath(__file__))

def init():
    print(os.path.join(mypath, "Pancake2d.dll"))
    os.environ['PATH'] = os.path.join(mypath, "lib") + os.pathsep + os.environ['PATH']
    pancake2d.API.lib = cdll.LoadLibrary(os.path.join(mypath, "Pancake2d.dll"))
    pancake2d.API.lib.init()
    pancake2d.useless.init()
    pancake2d.window.init()
    pancake2d.graphics.init()