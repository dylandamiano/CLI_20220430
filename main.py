from os import path
import csv

import helpDetails
import execution

userInput = input("Do you wish to continue [y/n]")

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
            # output the list of possibilities here

        elif str.lower(userInput) == "addpath":
            pass

        elif str.lower(userInput) == "removepath":
            pass

        elif str.lower(userInput) == "notes":
            pass

        elif str.lower(userInput) == "gettime":
            pass

        else:
            print("Command not recognized...")

elif userInput == "n":
    pass