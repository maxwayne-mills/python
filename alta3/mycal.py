#!/usr/bin/env python3

# Module to display the month of the year
import calendar

year_input = int(input('Enter year: '))   # Convert input to an integer

# Check to ensure year_input variable has a value, else default to 2018
if year_input == '':
    year_input = 2018
    print(year_input)

# month_input = int(input('Enter the month to display'))

for month in range(1,13):   # Display all tweleve months, start at 1 as there is no '0' month
    smallcal = calendar.month(year_input, month)
    print("Calendar:")
    print(smallcal)