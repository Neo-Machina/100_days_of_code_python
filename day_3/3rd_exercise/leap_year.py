# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. 

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print('Leap year.')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Leap year.')
    else:
        print('Not leap year.')
else:
    print('Not leap year.')