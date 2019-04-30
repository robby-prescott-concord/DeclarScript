#!/usr/bin/env python3
import fiximports
from sys import platform
from DeclarScript.DeclarScript import Command
from DeclarScript.DeclarScript import run_commands

# test for detection of backups
return_code_user_input_backups = [
    #(return_code, backup_command_list)
    (2, [Command('ls -l', 'Beginning backup command list if return code is 2.'),
         Command('sleep 2', 'End this back up list')]),
    (3, [Command('ps -a', 'Beginning backup command list if return code is 3.'),
         Command('echo "Howdy Partner"'),
         Command('sleep 2', 'End this back up list')]),
]

default_backup_list = [
    Command('echo "Yup, this one\'s the default backup list. try entering 2 or 3 for the return code."', 'Beginning of the default')
]

test_commands_linux = [
    Command('ls', "List files."),
    Command('sleep 1', 'Sleep for 1 second.'),
    Command('./examples/returncode.py', 'Run the program with user input.', critical=False, return_code_backup_command_lists=return_code_user_input_backups, backup_command_list=default_backup_list),
    Command('ps', "List processes.")
]

test_commands_windows = [
    Command('ls', "List files."),
    Command('sleep 1', 'Sleep for 1 second.'),
    Command('examples\\returncode.py', 'Run the program with user input.', critical=False, return_code_backup_command_lists=return_code_user_input_backups, backup_command_list=default_backup_list),
    Command('ps', "List processes.")
]

# how to differentiate between platforms

print("\n\nRunning Custom Return Codes:")
if platform == "linux" or platform == "linux2" :
    run_commands(test_commands_linux)
elif platform == "darwin" :
    run_commands(test_commands_linux)
elif platform == "win32" :
    run_commands(test_commands_windows)
else :
    run_commands(test_commands_linux)
    print("weird platform: " + str(platform))
