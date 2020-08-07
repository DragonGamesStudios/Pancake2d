import ctypes, os
lib = False

def carr(arr, ctype):
    return (ctype * len(arr))(*arr)