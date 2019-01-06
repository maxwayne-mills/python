#!/usr/bin/env python3

import csv
import os

def list_bills():
    path_to_file = "/home/cmills/Dropbox/personal/bill_list.csv"
    file = open(path_to_file, newline='')
    next(file)  # Skip the header
    lines_in_file = csv.reader(file)
    for row in lines_in_file:
        print(row[1], row[2], row[4], row[0]) 

def middle_month():
    os.popen("clear")   # Clear the screen
    path_to_file = "/home/cmills/Dropbox/personal/bill_list.csv"
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
