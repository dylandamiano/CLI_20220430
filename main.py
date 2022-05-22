from os import path

import helpDetails
import csvHandling
import auxillary

userInput:str = input("Do you wish to continue [y/n]")

if userInput == "y":
    while True:
        userInput = input(">> ")

        if str.lower(userInput) == "exit":
            print("Closing")
            break
        
        elif str.lower(userInput) == "help":
            helpDetails.showCommands()

        elif str.lower(userInput) == "start":
            userInput = input("What do you wish to start? \n")
            csvHandling.startFile()

        elif str.lower(userInput) == "addpath":
            csvHandling.addFile()

        elif str.lower(userInput) == "removepath":
            csvHandling.removeFile()

        elif str.lower(userInput) == "notes":
            content = []
            print("When done writing to the note, type \"DONE\"")
            filename = input("Name your file: ")

            while True:
                text = input("NOTEPAD >> ")
                
                if str.lower(text) == "done":
                    break
                elif str.lower(text) != "done":
                    content.append(text + "\n")
                
            auxillary.createNote(filename, content)

        elif str.lower(userInput) == "gettime":
            print(auxillary.outputTime())

        elif str.lower(userInput) == "showfiles":
            csvHandling.showCSVContents()

        else:
            print("Command not recognized...")

elif userInput == "n":
    pass