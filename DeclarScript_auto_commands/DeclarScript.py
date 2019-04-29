#!/usr/bin/env python
import os
import time
import subprocess
from . terminal_utilities import termcolor
from termcolor import colored
from terminal_utilities import terminalsize
from . terminalsize import get_terminal_size
from subprocess import Popen, PIPE

terminalWidth, terminalHeight = get_terminal_size()

def print_full_bar():
    # update the width in case the user changed the terminal window size
    terminalWidth, terminalHeight = get_terminal_size()
    bar = ''
    for underscore in range(terminalWidth):
        bar += '_'
    print(colored(bar, 'green'))

def print_command_list(list, name) :
    print('    ' + colored(name, 'yellow') + '(' + str(len(list)) + ' in total)')
    for command in list:
        print(colored('        >>> ', 'green') + colored(command, 'cyan'))
    print(' ')

# check for backups
# if backup command lists are found, recursively execute them
# First check the backups associated with the return code,
# then check if there's a default backup.
def check_and_run_backups(self, branch_name, return_code) :
    print_full_bar()
    print(' ')

    if self.return_code_backup_command_lists :
        for return_code_tuple in self.return_code_backup_command_lists :
            (return_code_bcl, bcl) = return_code_tuple
            if (return_code_bcl == return_code) :
                print(colored('Backup command list associated with return code ', 'green') + str(return_code) + colored(' was detected for failed command: ', 'green') + colored(str(self.command), 'cyan'))
                new_branch_name = branch_name + '/(' + self.command + ' :: returncode=' + str(return_code) + ')'
                print(colored('Running backup commands on the backup branch: ', 'green') + colored(str(new_branch_name), 'green'))
                run_commands(bcl, new_branch_name)
                print_full_bar()
                print(' ')
                print(colored('Finished backup command list associated with return code ', 'green') + str(return_code) + colored(' for command: ', 'green') + colored(str(self.command), 'cyan'))
                print(colored('Returning to parent branch: ', 'green') + colored(branch_name, 'green'))
                return

    if self.backup_command_list :
        print(colored('Backup command list was detected for failed command: ', 'green') + colored(str(self.command), 'cyan'))
        new_branch_name = branch_name + '/(' + self.command + ')'
        print(colored('Running backup commands on the backup branch: ', 'green') + colored(str(new_branch_name), 'green'))
        run_commands(self.backup_command_list, new_branch_name)
        print_full_bar()
        print(' ')
        print(colored('Finished backup command list for command: ', 'green') + colored(str(self.command), 'cyan'))
        print(colored('Returning to parent branch: ', 'green') + colored(branch_name, 'green'))
    else :
        print(colored('No backup command list detected for failed command: ', 'yellow') + colored(str(self.command), 'cyan'))

def check_and_run_backupsOLD_FOR_REFERENCE_DELETE_LATER(self, branch_name) :
    print_full_bar()
    print(' ')
    if self.backup_command_list :
        print(colored('Backup command list was detected for failed command: ', 'green') + colored(str(self.command), 'cyan'))
        new_branch_name = branch_name + '/(' + self.command + ')'
        print(colored('Running backup commands on the backup branch: ', 'green') + colored(str(new_branch_name), 'green'))
        run_commands(self.backup_command_list, new_branch_name)
        print_full_bar()
        print(' ')
        print(colored('Finished backup command list for command: ', 'green') + colored(str(self.command), 'cyan'))
        print(colored('Returning to parent branch: ', 'green') + colored(branch_name, 'green'))
    else :
        print(colored('No backup command list detected for failed command: ', 'yellow') + colored(str(self.command), 'cyan'))


def add_prompt_responses_and_run_command(self, branch_name) :
    if self.prompt_responses :
        print(colored("Automatic Terminal Prompt Responses: ", 'yellow') + str(self.prompt_responses))
        responses = ''
        for pr in self.prompt_responses :
            responses += pr + os.linesep

        p = Popen(self.command, shell=True, stdin=PIPE)
        p.stdin.write(responses)
        return_code = p.wait()
        return return_code

    else :
        return subprocess.call(self.command, shell=True)


# constructor for each command
class Command():
    def __init__(self, command='', message='', retries=0, critical=True, visible=True, sleep_between_retries=0, backup_command_list=[], prompt_responses=[], return_code_backup_command_lists=[]):
        self.command = command
        self.message = message
        self.retries = retries
        self.critical = critical
        self.visible = visible
        self.sleep_between_retries = sleep_between_retries
        self.backup_command_list = backup_command_list
        self.prompt_responses = prompt_responses
        self.return_code_backup_command_lists = return_code_backup_command_lists

    # runs an individual command
    # returns 0 on success
    # returns 1 on non-critical failure
    # returns -1 on critical failure
    def run(self, branch_name):
        return_code = 1
        times_tried = 0

        while return_code != 0 :
            if times_tried > self.retries :
                print_full_bar()
                print(' ')
                print(colored('Error with command: ', 'yellow') + colored(str(self.command), 'cyan'))
                if (self.retries != 0) :
                    print(colored('Command retries exceeded... times_tried: ', 'yellow') + str(times_tried) + colored(', retries allotted: ', 'yellow') + str(self.retries))

                check_and_run_backups(self, branch_name, return_code)

                if self.critical :
                    print(' ')
                    print(colored('This failed command was flagged as critical, so the current list of commands will terminate at this command.', 'red'))
                    print(colored('More specifically, the branch: "', 'red') + colored(branch_name, 'green') + colored('" ...', 'red'))
                    print(colored('...is terminating at command: "', 'red') + colored(self.command, 'cyan') + colored('".', 'red'))
                    return -1

                else :
                    print(' ')
                    print(colored('This failed command was not flagged as critical, so the list of commands will now continue where it left off.', 'yellow'))
                    print(colored('More specifically, the branch: "', 'yellow') + colored(branch_name, 'green') + colored('" ...', 'yellow'))
                    print(colored('...will continue with the following commands (if any) after the command: "', 'yellow') + colored(self.command, 'cyan') + colored('".', 'yellow'))
                    return 1

            if self.visible :
                print_full_bar()
                if times_tried != 0 :
                    print(' ')
                    print(colored('Retrying... there has been ', 'yellow') + str(times_tried) + colored(' unsuccessful attempts.', 'yellow'))
                    print(colored('Retries left: ', 'yellow') + str(self.retries - times_tried) + colored('.', 'yellow'))
                    if self.sleep_between_retries != 0 :
                        print(colored('sleep between retries has been set to ', 'yellow') + str(self.sleep_between_retries) + colored(' seconds. Waiting to execute...', 'yellow'))
                        time.sleep(self.sleep_between_retries)

                print(colored("\n~" + self.message, 'magenta') + colored('\n' + branch_name + '>>> ', 'green') + colored(self.command, 'cyan'))

            times_tried += 1

            return_code = add_prompt_responses_and_run_command(self, branch_name)
            print(colored('\nReturn Code: ', 'yellow') + str(return_code))


        return 0

def run_commands(commands, branch_name='(root)'):
    critical_failed_commands = []
    failed_commands = []
    successful_commands = []
    interrupted_commands = []
    interupted_command = ''
    unexecuted_commands = []

    # generate list of call the text versions of commands for them to be removed once executed
    for command in commands :
        unexecuted_commands.append(command.command)

    # execute the commands
    try:
        for command in commands:
            interupted_command = command.command
            unexecuted_commands.pop(0)
            return_code = command.run(branch_name)

            if return_code == -1 :
                critical_failed_commands.append(command.command)
                break
            elif return_code == 1 :
                failed_commands.append(command.command)
            else :
                successful_commands.append(command.command)

    except KeyboardInterrupt:
        interrupted_commands.append(interupted_command)
        print(colored("...Exiting", 'yellow'))
        pass

    print_full_bar()
    print(' ')
    print(colored('# Final Summary for Command List Branch: ', 'yellow') + colored(branch_name, 'green'))
    print(' ')
    print_command_list(successful_commands,'Successful Commands: ')
    print_command_list(interrupted_commands,'Interrupted Commands: ')
    print_command_list(unexecuted_commands,'Unexecuted Commands: ')
    print_command_list(failed_commands,'Failed Commands: ')
    print_command_list(critical_failed_commands,'Critical Failed Commands: ')
