import csv
import subprocess
import os

fileIndex = []

def addFile():
    file_name = input("File name: ")
    print("NOTE: YOUR FILE PATH MUST HAVE \\\\ IN PLACE OF / OR \\")
    file_path = input("File path: ")

    headings = ["FILE_NAME", "FILE_PATH"]
    
    with open("file_paths.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headings)
        writer.writerow({"FILE_NAME": file_name, "FILE_PATH": file_path})

def removeFile():
    pass

def showCSVContents():
    global fileIndex
    fileIndex = []

    with open("file_paths.csv", 'r', newline='') as csvfile:
        csvContents = csv.DictReader(csvfile)
        iterator: int = 0

        for row in csvContents:
            print("Access Code: " + str(iterator) + " ... Name: " + row["FILE_NAME"], " ... Path: " + row["FILE_PATH"])
            fileIndex.append([row["FILE_NAME"], row["FILE_PATH"]])
            iterator += 1

def startFile():

    showCSVContents()
    
    '''
        # fileIndex works as the following:
            1. Nested list added
                a. Access the file name from CSV
                b. Access the file path from CSV

            2. When going to start you must:
                a. Specify the index key, will present options
    '''
    
    print("\n Which file do you want to access? [example: 0]\n")
    print("File access code: ")

    prompt_input: int = int(input()) # Will add syntax-checking for this later
    
    print("Starting: " + fileIndex[prompt_input][0] + " from " + fileIndex[prompt_input][1])

    process = None

    try:
        process = subprocess.Popen(['start', fileIndex[prompt_input][1]], shell=True)
    except FileNotFoundError:
        print("Cannot find file, try checking the file path for this entry!")
    except PermissionError:
        print("You may need to elevate permissions before launching this file, or lift the permissions!")
    except Exception as e:
        print("Error ", e, " has occured!")
    finally:
        print("Returning to command prompt...")