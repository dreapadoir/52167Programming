import json
filename="testdict.json"
sample= dict(name='fred', age=31, grades=[1,34,55])
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)
#test the function
writeDict(sample)

filename="testdict.json"
def readDict():
# this will throw an error if the file does not exist
# it should readly just return an empty dict
# we can do this later
    with open(filename) as f:
        return json.load(f)
# test the function
somedict = readDict()

print(somedict)