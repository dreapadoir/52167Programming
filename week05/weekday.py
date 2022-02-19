#program to test ideas for week 5 task
#Author: David Higgins

from datetime import datetime

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
weekend = ('Saturday', 'Sunday')

day = datetime.today().strftime('%A')

if day in weekdays:
    print('Today is {}, it is a weekday'.format(day))

elif day in weekend:
    print('Today is {}, it is the weekend'.format(day))

