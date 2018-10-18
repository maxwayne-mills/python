#!/usr/bin/env python3

#Create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

# display parts of the dictionay
print( switch['hostname'] )
print( switch['ip'] )

# request a 'fake' key
print( switch['lynx'] )

# reqiest a 'fake' key with .get() method
print( "First test - .get()" )
print( switch.get('lynx') )

print( "Second test - .get()" )
print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get('version') )
