#program to investigate the number of iterations in Collatz Conjecture
#Author: David Higgins

index = 0  
rangeCounter = 2                    #defines where number variable starts at
number = rangeCounter               #number is the variable that will be used for calculation                  
rangeCollatz = range(0,1000)        #sets the range for the for loop
outputList = {}                     #initialises a dict to hold the results

for i in rangeCollatz:
        
    startNumber = number            #creates a variable to store the start number so it can be added to the dict

    while number != 1:                              
        if number % 2 == 0:                         
            number = number // 2                    
            index = index + 1                       
        
        else:                                       
            number = (number * 3) + 1               
            index = index + 1                       
         

    if number == 1:
        outputList[startNumber] = index     #adds the start number and the number of iterations to the dict
        rangeCounter += 1                   #increments by 1 so number starts at the next value

    number = rangeCounter                   #sets number to the next start value
    index = 0                               #resets index to 0

for key, value in outputList.items():       #once the for loop finishes this line outputs the start numbers and iteration values
    print(f"{key}, {value}")