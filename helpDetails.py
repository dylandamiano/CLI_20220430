commands = {
    "help": "Shows you all commands pertaining to this application",
    "exit": "Exits the application",
}

def showCommands():
    print("\n")

    for x in commands:
        print(str(x) + ": " +  str(commands[x]))

    print("\n")