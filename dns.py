#!/usr/bin/env python3

import os
from subprocess import call

server = str("www.clarencemills.com")

def resolv_ip(server_name):
    answer = call(['dig', server_name, '+short'])
    return answer

resolv_ip(server)
