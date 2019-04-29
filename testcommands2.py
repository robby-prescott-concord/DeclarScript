#!/usr/bin/env python
import os
from ..DeclarScript_auto_commands import DeclarScript
from DeclarScript import Command
from DeclarScript import run_commands

dddd_backups = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('touch dummyfile.txt', '~creating a new file'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('rm dummyfile.txt', '~removing the created file'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 2', '~sleep for 2 seconds:')
]

cccc_backups = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 2', '~sleep for 2 seconds:')
]

bbbb_backups = [
    Command('sleep 2', '~sleep for 2 seconds:'),
    Command('cccc', '~cccc has backups', retries=2, sleep_between_retries=1, backup_command_list=cccc_backups, critical=True),
    Command('should not execute anything past this since cccc is critical.', ";)"),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ls -l', '~listing all the files in the current directory:')
]

aaaa_backups = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('ps -al', '~listing all the current processes:'),
    Command('bbbb', '~cccc has backups', retries=2, sleep_between_retries=1, backup_command_list=bbbb_backups, critical=False),
    Command('jibberish with no backups', '~no backups!', retries=2, sleep_between_retries=1, critical=False),
    Command('dddd', '~cccc has backups', backup_command_list=dddd_backups, critical=False)
]

# test for detection of backups
test_commands_1 = [
    Command('aaaa', "~dummy thing to test if there are backups", retries=2, sleep_between_retries=3, backup_command_list=aaaa_backups, critical=False),
    Command('sleep 2', '~final sleep')
]

# test for multiple commands
test_commands_2 = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('touch dummyfile.txt', '~creating a new file'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('rm dummyfile.txt', '~removing the created file'),
    Command('ls -l', '~listing all the files in the current directory:')
]

print("\n\n\nRunning Test Commands 1:")
run_commands(test_commands_1)
