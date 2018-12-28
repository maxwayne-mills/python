#!/usr/bin/env python3
# Author: Clarence Mills
''' Download python script to control dropbox daemon '''

import urllib.request
import os

#  Define variables
url = 'https://www.dropbox.com/download?dl=packages/dropbox.py' 
file_download_dest = '/home/cmills/Downloads/dropbox.py'
dir_dest = '/home/cmills/bin'
file_dest = '/home/cmills/bin/dropbox.py'

# Download Dropbox app
print('Downloading Drobox python script from ' + url  + ' to ' + file_download_dest + '\n')
urllib.request.urlretrieve(url,file_download_dest)

# Create bin directory within user home.
if not os.path.isdir(dir_dest):         #check if directory exists first
    print('Creating bin directory' + dir_dest )
    os.mkdir(dir_dest)                  # Create directory
else:
    print(dir_dest + ' direectory exists')
    print('Moving python script to: ' + dir_dest)
    os.rename(file_download_dest,file_dest) # move file to bin directory
