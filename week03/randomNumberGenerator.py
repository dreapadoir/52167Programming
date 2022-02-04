#program to generate a random number within certain bounds
#Author: David Higgins

import random   #this imports the random package that contains the function randint
num = random.randint(0,333) #this creates a variable num and assigns it a random integer between 0 and 333

print("A random number is {}".format(num)) #this calls the variable num and enters it into the printed string