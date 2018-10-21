#!/usr/bin/env python3
# Author: Clarence Mils

''' Backup local Google drive to cloud ''' 

import os
import subprocess

user_dirs = ['/home/cmills/Documents/google_drive_clarence_mills','/home/cmills/Documents/google_drive_oss']

def main():
    for x in user_dirs:
        subprocess.call('clear')
        print('Backuping up google drive: ' + x )
        os.chdir(user_dirs[0])
        #subprocess.Popen('make')
        subprocess.call('make')

main()