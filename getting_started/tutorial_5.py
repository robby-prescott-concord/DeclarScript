#!/usr/bin/env python3
import fiximports
from DeclarScript.DeclarScript import Command, run_commands
import sys
from sys import platform

### Tutorial 5 ###
### Automatically respond to terminal prompts ###

# In the last tutorial, we got a taste of how the entire DeclarScript can be halted
# if the program prompts for user input. This need for the user to enter in information
# goes against the 'one-and-done' theme of DeclarScript, so there's a way to automate
# it. Here's how it's done:

# First, let's feed the program some empty lists so it doesn't break.
# ***(1)*** Try running the program now in this state

userinput0_responses = []
userinput1_responses = []
userinput2_responses = []

# ***(2)*** Once you've gotten sick of entering user input, run the code again
# with the auto-respond flag. This is how the command should look:

#   linux & osx: './tutorial_5.py --auto-respond'
#   windows:     'tutorial_5.py --auto-respond'

# This checks to see if "--auto-respond" second command line argument
if  len(sys.argv) > 1 and sys.argv[1] == '--auto-respond' :
    userinput0_responses = [17, 16, 18, 288, 289, 17] # numbers can be strings, ints, or floats
    userinput1_responses = [3]
    userinput2_responses = ['Y', 'Y', '100', 'N', 'N', '6', 'Y', 'N', 'purple', '17']


# linux and osx version
the_root_command_list_linux_osx = [
    Command('echo "DeclarScript is running, everything is going dandy."'),
    Command('sleep 2', visible=False),
    Command('echo "Oh, gee whiz. User Input. Just my luck. :("'),
    Command('./tutorial_resources/userinput0.py', prompt_responses=userinput0_responses),
    Command('./tutorial_resources/userinput1.py', prompt_responses=userinput1_responses),
    Command('./tutorial_resources/userinput2.py', prompt_responses=userinput2_responses),

    # you can also insert the user input in directly:
    Command('./tutorial_resources/returncode.py', prompt_responses=['0'])
]

# windows version
the_root_command_list_windows = [
    Command('echo "DeclarScript is running, everything is going dandy."'),
    Command('sleep 2', visible=False),
    Command('echo "Oh, gee whiz. User Input. Just my luck. :("'),
    Command('tutorial_resources\\userinput0.py', prompt_responses=userinput0_responses),
    Command('tutorial_resources\\userinput1.py', prompt_responses=userinput1_responses),
    Command('tutorial_resources\\userinput2.py', prompt_responses=userinput2_responses),

    # you can also insert the user input in directly:
    Command('tutorial_resources\\returncode.py', prompt_responses=['0'])
]

if platform == "linux" or platform == "linux2" :
    run_commands(the_root_command_list_linux_osx)
elif platform == "darwin" :
    run_commands(the_root_command_list_linux_osx)
elif platform == "win32" :
    run_commands(the_root_command_list_windows)
else :
    run_commands(the_root_command_list_linux_osx)
    print("weird platform: " + str(platform))

# After Running the tutorial_5 python script:
# Take a look at the terminal output and see if you can follow what happened.
