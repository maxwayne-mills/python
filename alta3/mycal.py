#!/usr/bin/python
import calendar

year_input = input('Enter year')
month_input = input('Enter the month to display')

lilcal = calendar.month(year_input, month_input)
print("Here is a tiny calendar:")
print(lilcal)