#program to break down list of random numbers
#Author: David Higgins
import random 

queue = []
rangeTo = 100
numberOfNumbers = 10

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print(f"queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print("Current Number is {}. Queue is {}".format(currentNumber, queue))

print("Queue is now empty.")