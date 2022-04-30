import time
from os import path

def outputTime():
    return time.ctime(time.time())

def createNote(name: str, content: list):
    with open(".\\notes\\" + str(name), "x") as note:
        for i in content:
            note.write(i)