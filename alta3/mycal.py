#!/usr/bin/env python3
import calendar

year_input = input('Enter year')
if year_input == '':
    year_input = 2018
    print(year_input)

# month_input = int(input('Enter the month to display'))

for month in range(1,13):
    lilcal = calendar.month(year_input, month)
    print("Calendar:")
    print(lilcal)