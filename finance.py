#!/usr/bin/env python3
""" Display Bills by month,current day or the next week. """

import csv
import os
import datetime

path_to_file = "/home/cmills/Dropbox/personal/bill_list.csv"

# Display contents of the Bills file
def list_bills():
    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)
    for row in lines_in_file:
        print(row[1], row[2], row[4], row[0]) 

# Display Bills for the 15, middle of the month
def middle_month():
    today = datetime.datetime.now()
    todays_date = (today.day)

    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)
    total = 0
    for row in lines_in_file:
        if str(todays_date) in row[2]:
            print(row[1],row[2],row[4])
            total = total + int(float(row[4]))

    print("Total spend for " + str(todays_date) + " is: " + str(total))

def user_menu():
        print("A. Mid month")
        print("B. End of the month")
        user_input = input("Make a selection a or b: ")

        if user_input == "a":
                middle_month()
        else:
                list_bills()

user_menu()
