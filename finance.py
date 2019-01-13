#!/usr/bin/env python3
""" Display Bills by month,current day or the next week. """

import csv
import os
import datetime
import sys

os.system("clear")
path_to_file = "/home/cmills/Dropbox/personal/bill_list.csv"
now = datetime.datetime.now()
todays_date = (now.day)

# Display contents of the Bills file

def list_bills():
    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)
    for row in lines_in_file:
        print(row[1], row[2], row[4], row[0])

def due_today():
    file = open(path_to_file, newline='')
    next(file)
    lines_in_file = csv.reader(file)

    now = datetime.datetime.now()
    todays_date = (now.day)
    month = (now.month)
    print(todays_date)

    total = 0
    for row in lines_in_file:
        if todays_date in row:
            print(row[1], row[2], row[4])
            total = total + int(float(row[4]))

    print("Total spend for " + str(month) + " " + str(todays_date) + " is: " + str(total))


# Display Bills for the 15, middle of the month
def middle_month():
    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)

    total = 0
    for row in lines_in_file:
        if "15" in row:
            print(row[1], row[2], row[4])
            total = total + int(float(row[4]))

    print("Total spend for the 15 is: " + str(total))

# Display Bills for the 30, end of the month
def end_of_month():
    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)

    total = 0
    for row in lines_in_file:
        if "30" in row:
            print(row[1], row[2], row[4])
            total = total + int(float(row[4]))

    print("Total spend for the 30 is: " + str(total))

if int(len(sys.argv)) == 1:                     # Check if an option was passed
    print(sys.argv[0] + " options: day,middle,month")
elif sys.argv[1] == "day":
    due_today()
elif sys.argv[1] == "middle":
    middle_month()
elif sys.argv[1] == "month":
    end_of_month()
else:
    list_bills()