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

# Display Bills for the current day
def current_day():
    #  Get today's date
    today = datetime.datetime.now()
    todays_date = (today.day)

    # Open and read contents from the file
    file = open(path_to_file, newline='')
    next(file)                                  # Skip the header
    lines_in_file = csv.reader(file)            # load contents of file into a variable in a list format

    # Search each row of the file for content that match's today's date
    total = 0
    for row in lines_in_file:
        if str(todays_date) in row[2]:
            print(row[1],row[2],row[4])
            total = total + int(float(row[4]))

    print("Total spend for " + str(todays_date) + " is: " + str(total))

def user_menu():
        print("A. Current Day")
        print("B. End of the month")
        user_input = input("Make a selection a or b: ")

        if user_input == "a":
                current_day()
        else:
                list_bills()

user_menu()
