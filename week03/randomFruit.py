#program to choose a random item from a list
#Author: David Higgins

import random                                   #imports the random package
fruits = ["Apple", 'Banana', 'Pear', 'Orange'] #creates a list called fruits with four elements
index = random.randint(0, len(fruits)-1)    #this creates an index number from a possible range starting at 0 and ending at one less than the length of list fruits. The next function will choose the item at that index or location on the list

print('This is a random fruit: {}'.format(fruits[index]))   #this uses index to choose an item from the list fruits and then print it in a string