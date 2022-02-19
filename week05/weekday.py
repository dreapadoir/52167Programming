#program to test ideas for week 5 task
#Author: David Higgins

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
weekend = ('Saturday', 'Sunday')

day = input("Enter a weekday: ")

if day.capitalize() in weekdays:
    print('It is a weekday')

elif day.capitalize() in weekend:
    print('It is the weekend')

else:
    print('Error: what you entered is not a day')