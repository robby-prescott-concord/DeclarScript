#!/usr/bin/env python3
import fiximports
from DeclarScript.DeclarScript import Command, run_commands

### Tutorial 4 ###
### Return Code Triggered Backup Command Lists ###
### -plus a little bit with OS differentiation ###


# If you've been paying attention you might have noticed that after DeclarScript
# displays a "Return Code: X" after each command, where X is some number.
# By convention, a return code of 0 means the command succeeded, and all went well.
# Any other value for a return code means that something went wrong. There are
# countless internet resources that describe what each of these return codes signify.
# However, the specific return code values are not the focus of this exercise.
# For DeclarScript, all you need to know is this: given a return code, you can
# create a backup command list that will be triggered in the event of a specific
# return code. This "return_code_backup_command_lists" parameter is completely
# separate from the "backup_command_list" parameter for each Command, but they
# function nearly identially. Basically, just think of the backup_command_lists as
# a catch-all for most errors and return_code_backup_command_lists as situationally
# pertaining to specific errors.

# Let's look at an example:

# The following 12 command lists are referenced by the return_code_backup_command_list

return_code_1_backup = [
    Command('sleep 1', visible=False),
    Command('echo "A partridge in a pear tree"'),
    Command('sleep 3', visible=False)
]

return_code_2_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Two turtle doves and"', backup_command_list=return_code_1_backup, critical=False)
]

return_code_3_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Three French hens"', backup_command_list=return_code_2_backup, critical=False)
]

return_code_4_backup = [
    Command('sleep 3', visible=False),
    Command('sing "Four calling birds"', backup_command_list=return_code_3_backup, critical=False)
]

return_code_5_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Five gold rings"', backup_command_list=return_code_4_backup, critical=False)
]

return_code_6_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Six geese a laying"', backup_command_list=return_code_5_backup, critical=False)
]

return_code_7_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Seven swans a swimming"', backup_command_list=return_code_6_backup, critical=False)
]

return_code_8_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Eight maids a milking"', backup_command_list=return_code_7_backup, critical=False)
]

return_code_9_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Nine ladies dancing"', backup_command_list=return_code_8_backup, critical=False)
]

return_code_10_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Ten lords a leaping"', backup_command_list=return_code_9_backup, critical=False)
]

return_code_11_backup = [
    Command('sleep 1', visible=False),
    Command('sing "Eleven pipers piping"', backup_command_list=return_code_10_backup, critical=False)
]

# This is how you declare a return_code_backup_command_list.
# Functionally, it's a list of tuples in python, where the 1st part of the tuple
# is the return code, and the 2nd part of the tuple is the a list of commands
return_code_12_days_backups = [
    # format:
    # (return_code, backup_command_list)
    (1, return_code_1_backup),
    (2, return_code_2_backup),
    (3, return_code_3_backup),
    (4, return_code_4_backup),
    (5, return_code_5_backup),
    (6, return_code_6_backup),
    (7, return_code_7_backup),
    (8, return_code_8_backup),
    (9, return_code_9_backup),
    (10, return_code_10_backup),
    (11, return_code_11_backup),

    # You can also declare the associated backup_command_list within the
    # return_code_backup_command_list, as long as the backup_command_list
    # in question doesn't need to be referenced by anything else. This is
    # how you do it:
    (12,[
            Command('sleep 1', visible=False),
            Command('sing "Twelve drummers drumming"', backup_command_list=return_code_11_backup, critical=False)
        ]
    )
]

default_backup_list = [
    Command('echo "This is the default catch-all backup list. Try entering a number 0 through 12..."')
]

# We're running a file in a subdirectory titled 'tutorial_resources'. It is important
# to note that some operating systems denote file paths differently, namely Windows.
# For example:
#   linux & osx filepath: ./tutorial_resources/returncode.py
#   windows filepath: tutorial_resources\returncode.py
#
# The good news is we can detect which os we're using within a python script. So the most
# straightforward solution is to create different versions and run them accordingly.

# linux and osx version
the_root_command_list_linux_osx = [
    Command('cat */returncode.py', 'The contents of the python script we are calling.'),
    Command('echo "on the (return_code) day of Christmas, my true love gave to me..."'),
    Command('./tutorial_resources/returncode.py', return_code_backup_command_lists=return_code_12_days_backups, backup_command_list=default_backup_list),
    Command('echo "Success is boring! Let\'s see it fail by typing something other than 0..."')
]

# windows version
the_root_command_list_windows = [
    Command('echo "on the (return_code) day of Christmas, my true love gave to me..."'),
    Command('tutorial_resources\\returncode.py', return_code_backup_command_lists=return_code_12_days_backups, backup_command_list=default_backup_list),
    Command('echo "Success is boring! Let\'s see it fail by typing something other than 0..."')
]

# This is how you differentiate between operating systems:
from sys import platform

if platform == "linux" or platform == "linux2" :
    run_commands(the_root_command_list_linux_osx)
elif platform == "darwin" :
    run_commands(the_root_command_list_linux_osx)
elif platform == "win32" :
    run_commands(the_root_command_list_windows)
else :
    run_commands(the_root_command_list_linux_osx)
    print("weird platform: " + str(platform))

# After Running the tut_4 python script:
# Take a look at the terminal output and see if you can follow what happened.
