#!/usr/bin/env python3
# Author: Clarence Mills
''' How to use mix lists '''

protocols = ['ssh', 'http','https']
print(protocols)
print(protocols[1])
protocols.append('dns') # This will add another item to the end of the list protcol
print(protocols)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports
protocols.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (protocols)
protocols.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protocols)