from ctypes import *

import pancake2d.API

def init():
    pancake2d.API.lib.setBackgroundColorRGB.argtypes = [c_float, c_float, c_float]
    pancake2d.API.lib.setBackgroundColorRGBA.argtypes = [c_float, c_float, c_float, c_float]

def setBackgroundColor(r: int, g:int, b:int, a=False):
    if not a:
        pancake2d.API.lib.setBackgroundColorRGB(r/255, g/255, b/255)
    else:
        pancake2d.API.lib.setBackgroundColorRGBA(r/255, g/255, b/255, a/255)