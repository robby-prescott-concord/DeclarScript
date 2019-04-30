#!/usr/bin/env python3
import fiximports
from DeclarScript.DeclarScript import Command
from DeclarScript.DeclarScript import run_commands

# test for a single command
test_commands_1 = [Command('ls', "listing all the files in the current directory:")]

# test for multiple commands
test_commands_2 = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 5', visible=False),
    Command('touch dummyfile.txt', '~creating a new file'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 5', visible=False),
    Command('rm dummyfile.txt', '~removing the created file'),
    Command('ls -l', '~listing all the files in the current directory:')
]

# test to make sure aaaaa command fails and stops
test_commands_3 = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 5', visible=False),
    Command('aaaaa', '~bad input'),
    Command('ps -al', '~listing all the processes:')
]

# test to make sure jibberish command fails and continues
test_commands_4 = [
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 5', visible=False),
    Command('touch dummyfile.txt', '~creating a new file'),
    Command('ls -l', '~listing all the files in the current directory:'),
    Command('sleep 5', visible=False),
    Command('jibberish', '~this should fail 4 times and continue', retries=3, critical=False),
    Command('rm dummyfile.txt', '~removing the created file'),
    Command('ls -l', '~listing all the files in the current directory:')
]

print("\n\n\nRunning Test Commands 1:")
run_commands(test_commands_1)

print("\n\n\nRunning Test Commands 2:")
run_commands(test_commands_2)

print("\n\n\nRunning Test Commands 3:")
run_commands(test_commands_3)

print("\n\n\nRunning Test Commands 4:")
run_commands(test_commands_4)
