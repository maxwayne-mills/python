#!/usr/bin/python
import calendar

user_input = input('Enter the month to display')

lilcal = calendar.month(2018, user_input)
print("Here is a tiny calendar:")
print(lilcal)