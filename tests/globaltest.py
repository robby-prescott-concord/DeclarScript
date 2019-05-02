#!/usr/bin/env python3
import sys

logfile_created = False
logfile = None

def set_up_logfile() :
    global logfile
    logfile = 'LOGFILE'
    global logfile_created
    logfile_created = True

def run() :
    global logfile
    global logfile_created
    if logfile_created :
        print('run: ' + logfile)
    else :
        print('the logfile was not created')

def run_commands(create_logfile=True) :
    if create_logfile :
        set_up_logfile()

    run()

run_commands()

# global
if logfile_created :
    print("global scope: " + logfile)
else :
    print('the logfile was not created')

logfile = 'Stop logfile'
print(logfile)
