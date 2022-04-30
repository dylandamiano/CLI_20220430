commands = {
    "help": "Shows you all commands pertaining to this application",
    "exit": "Exits the application",
    "addpath": "Adds an executable to the CSV log file",
    "removepath": "Removes an executable from the CSV log file",
    "notes": "Create a note file spanning one or multiple lines",
    "gettime": "Gets the system time",
}

def showCommands():
    print("\n")

    for x in commands:
        print(str(x) + ": " +  str(commands[x]))

    print("\n")