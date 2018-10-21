#!/usr/bin/env python3
''' This program accepts 4 parameters passed in from the command line '''
import sys

args = sys.argv
print("Username: " + args[0])
print("Password: " + args[1])
print("IP Address: " + args[2])
print("Gateway: " + args[3])