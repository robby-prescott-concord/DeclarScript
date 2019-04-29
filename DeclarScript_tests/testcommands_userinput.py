#!/usr/bin/env python
import os
from autocommand import Command
from autocommand import run_commands

# test for detection of backups
return_code_user_input_backups = [
    #(return_code, backup_command_list)
    (1, [Command('ls -l', 'Beginning backup command list if return code is 1.'), Command('sleep 2', 'End this back up list')]),
    (3, [Command('ps -a', 'Beginning backup command list if return code is 3.'), Command('sleep 2', 'End this back up list')])
]

test_commands_1 = [
    Command('ls', "List files."),
    Command('sleep 2', 'Sleep for two seconds.'),
    Command('sudo ./user-input.py', 'Run the program with user input.', prompt_responses=['5', '3'], critical=False, return_code_backup_command_lists=return_code_user_input_backups),
    Command('ls', "List files."),
    Command('ps', "List processes."),
    Command('sleep 2', 'Sleep for two seconds.'),
    Command('sudo ./user-input2.py', 'Run the program with user input.', prompt_responses=['4']),
    Command('sleep 2', 'Sleep for two seconds.')
]

print("\n\n\nRunning Test Commands 1:")
run_commands(test_commands_1)
