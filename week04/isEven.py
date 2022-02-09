#isEven.py
#program to determine if a number is even
#Author: David Higgins

num = int(input("Enter a number: ")) #creates a variable num and assigns it a number taken in from the user. int converts it to an integer

if (num%2 == 0): #this test checks if num is divisible by two 
    print("{} is an even number".format(num)) #this is the statement that will run if the statement above is true

else: #this block contains the code that will run if the boolean test above is false
    print("{} is an odd number".format(num))