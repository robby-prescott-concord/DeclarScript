#!/usr/bin/env python3
import fiximports

### Tutorial 1 ###
### Command Lists ###

# In all your python DeclarScript files, you must include the following import
from DeclarScript.DeclarScript import Command, run_commands

# DeclarScript makes it easy to run multiple commands
# This is how you declare a list:
hello_commands = [
    Command('echo "Hello World! :)"'),
    Command('ls -l'),
    Command('sleep 2'),
    Command('ps -al'),
    Command('qwertyuiop'),
]

# This is how you run a list:
run_commands(hello_commands)

# Now try executing tut_1.
# Open up a terminal and navigate to the :
# >>> cd <some_file_path>/<your_DeclarScript_root_directory>/DeclarScript/getting_started"
# Run each of these files like so:
#     Windows:          $ tutorial_1.py
#     Linux & OSX:      $ ./tutorial_1.py


# After Running the tut_1 python script:
# You witnessed each of the commands executed in succession, followed
# by a "Final Summary". Notice that 4 commands should have been successful, and
# 1 should have failed since 'qwertyuiop' isn't a standard shell command.
