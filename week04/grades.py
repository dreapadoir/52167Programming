#program to classify a percentage result as a grade
#Author: David Higgins

score = int(input("Enter your test score: "))

if score > 100 or score < 0:
    print("Score must be between 0 and 100")

elif score < 40:
    print("Fail")

elif score < 50:
    print("Pass")

elif score < 60:
    print("Merit 1")

elif score < 70:
    print("Merit 2")

else:
    print("Distinction")