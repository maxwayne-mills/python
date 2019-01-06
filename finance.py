#!/usr/bin/env python3
""" Display Bills by month,current day or the next week. """

import csv
import os

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
    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)
    total = 0
    for row in lines_in_file:
        if "15" in row:
            print(row[1],row[2],row[4])
            total = total + int(float(row[4]))
    print("Total spend for the 15 is: " + str(total))

middle_month()
