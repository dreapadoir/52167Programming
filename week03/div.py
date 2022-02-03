#program to divide two numbers
#Author: David Higgins

x = int(input('Enter a number: ')) #int() is used to turn the input into an integer
y = int(input('Enter another number: '))
answer = x//y    #// returns an integer instead of a float
remainder = x%y #% returns the remainder of dividing two integers

print('{} divided by {} is equal to {} with remainder {}'.format(x, y, answer, remainder))
