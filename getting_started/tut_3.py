#!/usr/bin/env python3
import fiximports
from DeclarScript.DeclarScript import Command, run_commands

### Tutorial 3 ###
### Backup Command Lists ###

# When a command fails, you can supply a backup command list to execute afterwards.
# These backup command lists will execute in a recursively, resembling a tree-like
# logical structure with different branches.

# The main branch is given the name 'root', and the other branches will be named
# automatically based on their failed command(s) that caused their execution.

# Here's an example of a tree:
#      *Note that higher level backups must be declared first since other command lists
#       reference them.

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

# test for detection of backups
the_root_command_list = [
    Command('ls', 'Listing all the files in the current directory:'),
    Command('touch SUPER_COOL_FILE.txt', 'Creating a new file...'),
    Command('ls', 'Listing all the files in the current directory:'),
    Command('AAA', "AAA has backups.", backup_command_list=AAA_backups, critical=False),
    Command('echo "Final Command!"'),
]

# Here's a visual representation for the tree of backup command lists:

# (root)
#   |____(AAA)
#          |____(BBB)
#          |      |____(CCC)
#          |      |      |____backup_list_that_critically_fail
#          |      |
#          |      |____(FFF)
#          |
#          |____(EEE)
#          |
#          |____(DDD)
#                 |____backup_list_that_succeeds

# The branch traversal order:
# (root)=>(A)=>(B)=>(C)=>(B)=>(F)=>(B)=>(A)=>(E)=>(A)=>(D)=>(A)=>(root)

# let's run it!
run_commands(the_root_command_list)

# After Running the tut_3 python script:
# Take a look at the terminal output and see if you can connect the terminal
# output with the image of the tree and the branch traveral.
