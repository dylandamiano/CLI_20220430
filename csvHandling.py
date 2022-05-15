import csv
import subprocess
#import os --will be implemented at a later time

fileIndex: list = []
headings: list = ["FILE_NAME", "FILE_PATH"]

def addFile() -> None:
    '''
        Add a file to a CSV document. Allows you to name as well.
    '''

    file_name: str = input("File name: ")
    print("NOTE: YOUR FILE PATH MUST HAVE \\\\ IN PLACE OF / OR \\")
    file_path: str = input("File path: ")
    
    with open("file_paths.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headings)
        writer.writerow({"FILE_NAME": file_name, "FILE_PATH": file_path})

def removeFile() -> None:
    '''
        There is apparently no way to explicity remove a certain part of the CSV document without having to rewrite the whole file
        We will do this as such:
            1. Copy the file into a list format
            2. Query the file name
            3. Delete the list element
            4. Rewrite to the CSV file

        Output of DictReader as implied by logic:
            - Outputted as a list
            - Rows are formatted as KEY, VALUE pairs (DICT datatype)
    '''

    showCSVContents()
    print("Which data do you wish to remove (ex: 0): ")

    selector:int = int(input())
    fileIndex.pop(selector)

    with open("file_paths.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headings)

        writer.writeheader()

        for data in fileIndex:
            print(data)
            writer.writerow({"FILE_NAME": data[0], "FILE_PATH": data[1]})


def showCSVContents() -> None:
    global fileIndex
    fileIndex = []

    with open("file_paths.csv", 'r', newline='') as csvfile:
        csvContents = csv.DictReader(csvfile)
        iterator: int = 0

        for row in csvContents:
            print("Access Code: " + str(iterator) + " ... Name: " + row["FILE_NAME"], " ... Path: " + row["FILE_PATH"])
            fileIndex.append([row["FILE_NAME"], row["FILE_PATH"]])
            iterator += 1

    print(fileIndex)

def startFile() -> None:

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
    print("File access code (any integer greater than or equal to zero): ")

    prompt_input: int = int(input()) # Will add syntax-checking for this later

    print("Starting: " + fileIndex[prompt_input][0] + " from " + fileIndex[prompt_input][1])

    process: subprocess.Popen = None

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