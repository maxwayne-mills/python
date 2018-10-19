#!/usr/bin/env python3
# Author: Clarence Mills

# Module to display the month of the year
import calendar

# Collect year from user input
year_input = int(input('Enter year: '))   # Convert input to an integer

# Check if the year is a leap year
verify_leap_year = calendar.isleap(year_input)

if verify_leap_year == False:
    is_leap_year = "Not a leap year"
else:
    is_leap_year = "Leap year"

for month in range(1,13):   # Display all tweleve months, start at 1 as there is no '0' month
    smallcal = calendar.month(year_input, month)
    print("Calendar: "  + is_leap_year )
    print(smallcal)