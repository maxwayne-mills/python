#!/usr/bin/env python3

import webbrowser as wb
import csv
import sys

# Open csv file passed in from the command line containing links
csvfile = open(sys.argv[1],'r')

linenum = int(input("Enter line number: " )) # convert string to an integer using int function

# Read in all contents of the file
filereader = csv.reader(csvfile)

# Create a list of file contents
linkdata = list(filereader)

# Ignore header and get the second column from the first row of links
link = linkdata[linenum][1] 

# Open the link in an incognito Google chrome tab
wb.get('google-chrome %s --incognito').open_new_tab(link)
