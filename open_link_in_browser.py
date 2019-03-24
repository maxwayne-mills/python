#!/usr/bin/env python3
""" Author: Clarence Mills """
""" Script to open a URL contained within a file """
""" expects a csv file in a three column format, first field cateogory of the link, second field link, third field describes the link"""

import webbrowser as wb
import os
import csv
import sys

def get_link():
    os.popen("clear")  # Clear the screen
    # Open csv file passed in from the command line as the first argument
    csvfile = open(sys.argv[1], "r")

    # Read in contents of the file
    filereader = csv.reader(csvfile)
    next(filereader)  # Skip the header

    # Create a list of file contents
    link_data = list(filereader)

    n = 0
    for row_in_file in link_data:
        print(
            n, row_in_file[1], row_in_file[2]
        )  # Print line number and a row from the file
        n = n + 1  # increment counter by 1
    
    linenum = int(input("Enter line number: ")
    )  # convert string to an integer using the int function

    # load link variable based on line number entered by user and selecting the second column
    link = link_data[linenum][
        1
    ]  # number 1 indicates to use the second column that contains the link

    return link

# Open the link in Google chrome tab in incognito mode
wb.get("google-chrome %s --incognito").open_new_tab(get_link())

user_input = input("continue: y or n ")
while user_input != "n":
    wb.get("google-chrome %s --incognito").open_new_tab(get_link())

