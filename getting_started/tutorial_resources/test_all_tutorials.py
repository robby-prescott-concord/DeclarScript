#!/usr/bin/env python3
# fix imports
import sys, os
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[3]
print("sys.path set to: " + str(root))
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

# run the program normally
from DeclarScript.DeclarScript import Command, run_commands
from sys import platform

print('\n\n\n     #####     Test 1     #####')
tut_1 = [
    Command('echo "Hello World! :)"'),
    Command('ls -l'),
    Command('sleep 2'),
    Command('ps -al'),
    Command('qwertyuiop'),
]

run_commands(tut_1)

print('\n\n\n     #####     Test 2     #####')
tut_2 = [
    Command('echo "Hello World! :)"'),
    Command('ls', message='List all the files in the current directory' ),
    Command('ps', 'List the current processes', critical=False),
    Command('qwertyuiop', 'Bad command, it should fail...', retries=1, critical=False),
    Command('echo "I\'m invisible! \\(\'o\')/"', visible=False),
    # Command('sleep 5', visible=False),
    Command('asdfghjkl', 'Bad command, again.', sleep_between_retries=2, retries=3, critical=True),
    Command('wont be executed', 'The list will terminate before this command.'),
    Command('ps', 'The list will terminate before this command.'),
    # Command('sleep 9999', 'I wouldn\'t make you wait 9999 seconds. :)')
]

run_commands(tut_2)

print('\n\n\n     #####     Test 3     #####')
DDD_backups = [
    Command('echo "We\'re in DDD\'s backup command list"', 'Begin the backup command list:'),
    Command('ls', 'Listing all the files in the current directory:'),
    Command('rm SUPER_COOL_FILE.txt', 'Removing the created file...'),
    Command('ls', 'Listing all the files in the current directory:'),
]

CCC_backups = [
    Command('echo "We\'re in CCC\'s backup command list"', '~Begin the backup command list:')
]

BBB_backups = [
    Command('echo "We\'re in BBB\'s backup command list"', 'Begin the backup command list:'),
    Command('CCC', 'CCC has backups', retries=2, backup_command_list=CCC_backups, critical=True),
    Command('FFF', "Should not execute anything past this since CCC is critical"),
    Command('ls -l'),
    Command('ps -l'),
    Command('ls -l'),
    Command('ps -l'),
    Command('ls -l')

]

AAA_backups = [
    Command('echo "We\'re in AAA\'s backup command list"', 'Begin the backup command list:'),
    Command('ps', 'Listing all the current processes:'),
    Command('BBB', 'BBB has backups.', backup_command_list=BBB_backups, critical=False),
    Command('EEE', 'No backups for this guy!', critical=False),
    Command('DDD', 'DDD has backups.', backup_command_list=DDD_backups, critical=False)
]

tut_3 = [
    Command('ls', 'Listing all the files in the current directory:'),
    Command('touch SUPER_COOL_FILE.txt', 'Creating a new file...'),
    Command('ls', 'Listing all the files in the current directory:'),
    Command('AAA', "AAA has backups.", backup_command_list=AAA_backups, critical=False),
    Command('echo "Final Command!"'),
]

run_commands(tut_3)

print('\n\n\n     #####     Test 4     #####')
return_code_1_backup = [
    Command('sleep 1', visible=False),
    Command('echo "A partridge in a pear tree"')
]

return_code_2_backup = [
    Command('sleep 1', visible=False),
    Command('echo "Two turtle doves and"')
]

return_code_3_backup = [
    Command('sleep 1', visible=False),
    Command('echo "Three French hens"')
]

return_code_4_backup = [
    Command('sleep 1', visible=False),
    Command('echo "Four calling birds"')
]

return_code_5_backup = [
    Command('sleep 1', visible=False),
    Command('echo "Five gold rings"')
]

return_code_12_days_backups = [
    (1, return_code_1_backup),
    (2, return_code_2_backup),
    (3, return_code_3_backup),
    (4, return_code_4_backup),
    (5, return_code_5_backup),

    (6, [ Command('sleep 1', visible=False),
          Command('echo "Six geese a laying"') ]),

    (7, [ Command('sleep 1', visible=False),
          Command('echo "Seven swans a swimming"') ]),

    (8, [ Command('sleep 1', visible=False),
          Command('echo "Eight maids a milking"') ]),

    (9, [ Command('sleep 1', visible=False),
          Command('echo "Nine ladies dancing"') ]),

    (10, [ Command('sleep 1', visible=False),
           Command('echo "Ten lords a leaping"') ]),

    (11, [ Command('sleep 1', visible=False),
           Command('echo "Eleven pipers piping"') ]),

    (12, [ Command('sleep 1', visible=False),
           Command('echo "Twelve drummers drumming"') ])
]


default_backup_list = [
    Command('echo "This is the default catch-all backup list. Try entering a number 0 through 12..."')
]

tut_4_linux_osx = [
    Command('cat returncode.py', 'The contents of the python script we are calling.'),
    Command('echo "on the (return_code) day of Christmas, my true love gave to me..."'),
    Command('./returncode.py', return_code_backup_command_lists=return_code_12_days_backups, backup_command_list=default_backup_list),
    Command('echo "Success is boring! Let\'s see it fail by typing something other than 0..."')
]

tut_4_windows = [
    Command('cat returncode.py', 'The contents of the python script we are calling.'),
    Command('echo "on the (return_code) day of Christmas, my true love gave to me..."'),
    Command('returncode.py', return_code_backup_command_lists=return_code_12_days_backups, backup_command_list=default_backup_list),
    Command('echo "Success is boring! Let\'s see it fail by typing something other than 0..."')
]

if platform == "win32" :
    run_commands(tut_4_windows)
else :
    run_commands(tut_4_linux_osx)

print('\n\n\n     #####     Test 5     #####')

userinput0_responses = [17, 16, 18, 288, 289, 17]
userinput1_responses = [3]
userinput2_responses = ['Y', 'Y', '100', 'N', 'N', '6', 'Y', 'N', 'purple', '17']

tut_5_linux_osx = [
    Command('echo "DeclarScript is running, everything is going dandy."'),
    Command('sleep 2', visible=False),
    Command('echo "Oh, gee whiz. User Input. Just my luck. :("'),
    Command('./userinput0.py', prompt_responses=userinput0_responses),
    Command('./userinput1.py', prompt_responses=userinput1_responses),
    Command('./userinput2.py', prompt_responses=userinput2_responses),
    Command('./returncode.py', prompt_responses=['0'])
]

# windows version
tut_5_windows = [
    Command('echo "DeclarScript is running, everything is going dandy."'),
    Command('sleep 2', visible=False),
    Command('echo "Oh, gee whiz. User Input. Just my luck. :("'),
    Command('userinput0.py', prompt_responses=userinput0_responses),
    Command('userinput1.py', prompt_responses=userinput1_responses),
    Command('userinput2.py', prompt_responses=userinput2_responses),
    Command('returncode.py', prompt_responses=['0'])
]

if platform == "win32" :
    run_commands(tut_5_windows)
else :
    run_commands(tut_5_linux_osx)
