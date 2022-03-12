#program to test counter in persistent memory
#Author: David Higgins

import os.path
filename = "count.txt"

def readCount():
    with open(filename, "rt") as f:
        count = int(f.read())
        return count

def writeCount(number):
    with open(filename, "wt") as f:
        f.write(str(number))

if not os.path.isfile(filename):
    print ("File does not exist")
#initialise file here
    writeCount(0)

num = readCount()
num += 1
writeCount(num)

print("We have run this program {} times".format(num))

