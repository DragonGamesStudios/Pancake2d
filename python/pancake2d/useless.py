import ctypes

import pancake2d.API

def init():
    pancake2d.API.lib.version.restype = ctypes.c_char_p

def version():
    print(pancake2d.API.lib.version().decode("utf-8"))