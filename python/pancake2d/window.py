from ctypes import *

import pancake2d.API

function_empty = CFUNCTYPE(None)

def init():
    pancake2d.API.lib.createWindow.restype = c_void_p

    pancake2d.API.lib.deleteWindow.argtypes = [c_void_p]

    pancake2d.API.lib.closeWindow.argtypes = [c_void_p]

    pancake2d.API.lib.runWindow.argtypes = [c_void_p, function_empty, function_empty]

    pancake2d.API.lib.getWidthWindow.argtypes = [c_void_p]
    pancake2d.API.lib.getWidthWindow.restype = c_int

    pancake2d.API.lib.getHeightWindow.argtypes = [c_void_p]
    pancake2d.API.lib.getHeightWindow.restype = c_int

    pancake2d.API.lib.setFullscreenWindow.argtypes = [c_void_p, c_bool]

    pancake2d.API.lib.isFullscreenWindow.argtypes = [c_void_p]
    pancake2d.API.lib.isFullscreenWindow.restype = c_bool

class Window:
    def __init__(self, width: int = 500, height: int = 500, caption: str = "Pancake2d Project", flags = []):
        cflags = []
        # flags.append("pchdr")
        pancake2d.API.lib.createWindow.argtypes = [c_int, c_int, c_char_p, c_char_p * len(flags), c_int]
        for flag in flags:
            cflags.append(c_char_p(bytes(flag, encoding="UTF-8")))

        cflags = pancake2d.API.carr(cflags, c_char_p)
        self.obj = pancake2d.API.lib.createWindow(width, height, c_char_p(bytes(caption, encoding="UTF-8")), cflags, len(flags))

    def close(self):
        pancake2d.API.lib.closeWindow(self.obj)

    def run(self, updatefunction=lambda: None, drawfunction=lambda: None):
        pancake2d.API.lib.runWindow(self.obj, function_empty(updatefunction), function_empty(drawfunction))

    def isFullscreen(self):
        return pancake2d.API.lib.isFullscreenWindow(self.obj)

    def setFullscreen(self, fullscreen:bool = True):
        pancake2d.API.lib.setFullscreenWindow(self.obj, fullscreen)

    def getWidth(self):
        return pancake2d.API.lib.getWidthWindow(self.obj)

    def getHeight(self):
        return pancake2d.API.lib.getHeightWindow(self.obj)