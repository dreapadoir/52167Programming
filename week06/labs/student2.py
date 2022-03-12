#program to create and view student records
#Author: David Higgins

import json

students = []

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")

    choice = input("Type one letter (a/v/s/q):").strip()
    return choice

#test the function
choice = displayMenu()

def doAdd():
    print("in adding")

def doView():
    print("in viewing")

def doSave():
    filename = "studentData.json"
    def saveDict(obj):
        with open(filename, 'wt') as f:
            json.dump(obj,f)
    saveDict(students)
    print("in save")

choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 's':
        doSave()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
