#!/usr/bin/env python3

import webbrowser as wb
import csv
import sys

# Open csv file passed in from the command line containing links
csvfile = open(sys.argv[1],'r')

# Read in all contents of the file
filereader = csv.reader(csvfile)

# Create a list of file contents
linkdata = list(filereader)

# Ignore header and get the second column from the first row of links
link = linkdata[4][1]

# Open the link in a Google chrome igconito tab
wb.get('google-chrome %s --incognito').open_new_tab(link)
