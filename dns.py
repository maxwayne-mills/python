#!/usr/bin/env python3

import os
import sys
from subprocess import call

# Get arguments passed into script
server = sys.argv[1]

# Define functions

# Function to resolve hostname to IP address
def resolve_to_ip(server_name):
    resolve_to_ip_answer = call(['dig', server_name, '+short'])
    return resolve_to_ip
    
def ping_server(server_name):
    response = call(['ping', '-c 3', server_name])
    return response

def reverse_ip(server_name):
    ip = resolve_to_ip(server)
    reverse_ip = call(['dig', '-x',int(ip) , '+short'])
    #print(reverse_ip)
    #return reverse_ip

#resolve_to_ip(server)
#ping_server(server)
reverse_ip(server)