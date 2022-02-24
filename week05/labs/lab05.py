#program to work through first part of week 5 lab
#Author: David Higgins

from importlib.machinery import DEBUG_BYTECODE_SUFFIXES


numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
}
]
}

print(me["teaching"][0])

months = ("January", "February", "March", "April", "May", "June", "July", "August",
 "September", "October", "November", "December")

summer = months[4:7]

for i in summer:
    print(i)

