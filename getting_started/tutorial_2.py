#!/usr/bin/env python3
import fiximports
from DeclarScript.DeclarScript import Command, run_commands

### Tutorial 2 ###
### Options & Defaults ###

# You have several options when declaring a single command.
# Here's some examples:

tutorial_2_commands = [
    # Just a single command with no options
    Command('echo "Hello World! :)"'),

    # providing a descriptive message for your command:
    Command('ls', message='List all the files in the current directory' ),
    # since 'message' is the 2nd parameter you can omit 'message=' if you prefer.
    # ex: Command('ls', 'List all the files in the current directory'),

    # labeling a command critical. By default, all commands are critical.
    # 'critical' commands will stop the current command list if they fail
    Command('ps', 'List the current processes', critical=False),

    # retrying a command if it fails
    Command('qwertyuiop', 'Bad command, it should fail...', retries=1, critical=False),

    # making the setup around a command invisible
    Command('echo "I\'m invisible! \\(\'o\')/"', visible=False),
    Command('sleep 5', visible=False),

    # sleeping between retries (in seconds)
    Command('asdfghjkl', 'Bad command, again.', sleep_between_retries=2, retries=3, critical=True),

    # These commands won't be executed because the 'badbutwait' command was critical and failed.
    Command('wont be executed', 'The list will terminate before this command.'),
    Command('ps', 'The list will terminate before this command.'),
    Command('sleep 9999', 'I wouldn\'t make you wait 9999 seconds. :)')
]

# There are a few more options, but they deserve their own little tutorial.
# Here's a complete list of all 8 options and their default values

# (0) command=''
# (1) message=''
# (2) critical=True
# (3) retries=0
# (4) sleep_between_retries=0
# (5) visible=True
# (6) backup_command_list=[]
# (7) return_code_backup_command_lists=[]
# (8) prompt_responses=[]

# let's run it!
run_commands(tutorial_2_commands)

# After Running the tutorial_2 python script:
# Take a look at the terminal output and see if you can follow what happened.
