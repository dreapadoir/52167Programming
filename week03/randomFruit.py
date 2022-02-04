#program to choose a random item from a list
#Author: David Higgins

import random
fruits = ["Apple", 'Banana', 'Pear', 'Orange']
index = random.randint(0, len(fruits)-1)

print('This is a random fruit: {}'.format(fruits[index]))