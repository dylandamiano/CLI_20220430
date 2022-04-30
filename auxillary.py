import time
from os import path

def outputTime():
    return time.ctime(time.time())

def createNote(name: str, content: list):
    with open(".\\notes\\name.txt", "x", encoding="UTF-8") as note:
        print("WRITING...")