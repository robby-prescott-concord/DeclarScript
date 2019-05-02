#!/usr/bin/env python3
import fiximports
from DeclarScript.DeclarScript import Command, run_commands

hello_commands = [
    Command('echo "Hello World! :)"'),
    Command('ls -l'),
    Command('sleep 2', visible=False),
    Command('ps -al'),
    Command('cool')
]

run_commands(hello_commands)
