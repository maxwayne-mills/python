#!/usr/bin/env python3
import calendar

year_input = input('Enter year')
if year_input == '':
    year_input = 2018

print(year_input)
month_input = int(input('Enter the month to display'))

lilcal = calendar.month(year_input, month_input)
print("Here is a tiny calendar:")
print(lilcal)