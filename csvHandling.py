import csv

def addFile():
    file_name = input("File name: ")
    file_path = input("File path: ")

    headings = ["FILE_NAME", "FILE_PATH"]
    
    with open("file_paths.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headings)
        writer.writerow({"FILE_NAME": file_name, "FILE_PATH": file_path})

def removeFile():
    pass

def showCSVContents():
    with open("file_paths.csv", 'r', newline='') as csvfile:
        csvContents = csv.DictReader(csvfile)
        for row in csvContents:
            print("Name: " + row["FILE_NAME"], " ... Path: " + row["FILE_PATH"])

def startFile():
    pass