#!/usr/bin/env python3
import sys, os, pathlib, time, subprocess, datetime, io, traceback
from DeclarScript.terminal_utilities.termcolor import colored
from DeclarScript.terminal_utilities.terminalsize import get_terminal_size
from subprocess import Popen, PIPE

logfile_created = False
logfile = None

def print_and_log(list) :
    global logfile
    global logfile_created
    # each element of list is a tuple with this format: ('text', 'color')
    lstr = '' # uncolored string for logging
    pstr = '' # colored string for printing

    for tuple in list :
        text, color = tuple
        lstr += text
        pstr += colored(text, color)

    if logfile_created :
        logfile.write(lstr + os.linesep)

    print(pstr)

def print_full_bar() :
    global logfile
    global logfile_created
    # update the width in case the user changed the terminal window size
    terminalWidth, terminalHeight = get_terminal_size()
    bar = ''
    for underscore in range(terminalWidth):
        bar += '_'

    if logfile_created :
        logfile.write('______________________________________________________________________' + os.linesep) # 70 wide for the logfile

    print(colored(bar, 'green'))

def print_command_list(list, name) :
    print_and_log([('    ' + name, 'yellow'), ('(' + str(len(list)) + ' in total)', 'white')])
    for command in list:
        print_and_log([('        >>> ', 'green'), (command, 'cyan')])
    print_and_log([(' ', 'white')])

def get_name() :
    name = sys.argv[0]
    if name[0:2] == './' :
        name = name[2:]

    if name[-3:] == '.py' :
        name = name[:-3]
    return name

def set_up_logfile() :
    global logfile
    global logfile_created
    file_path = pathlib.Path(__file__).resolve()
    parent_dir = file_path.parent

    now = datetime.datetime.now()
    time_stamp = str(now.year) + '_' + str(now.month) + '_' + str(now.hour) + '_' + str(now.minute) + '_' + str(now.second) + '_' + str(now.microsecond)

    logfile_path = ''
    if sys.platform == "win32" :
        logfile_path = str(parent_dir) + "\\logs\\" + time_stamp + '.log'
    else:
        logfile_path = str(parent_dir) + "/logs/" + time_stamp + '.log'

    try:
        logfile = open(logfile_path, 'w+')
        print("Logging output to: " + logfile_path)
        logfile.write("Logfile for: " + get_name() + os.linesep)
        logfile.write("Executed on: " + time_stamp + os.linesep)
        logfile_created = True
    except Exception as e:
        print_and_log([("There was a problem setting up your logfile.", 'red')])
        print_and_log([("If you don't want to see this error message, include the parameter '", 'red'), ("create_logfile=False", 'cyan'), ("' in your run_commands() DeclarScript function like so: '", 'red'), ("run_commands(commands, create_logfile=False)", 'cyan')])
        print_and_log([(os.linesep + "Here's the error message:", 'white')])
        print_and_log([(str(traceback.print_exc()), 'white')])
        pass

# check for backups
# if backup command lists are found, recursively execute them
# First check the backups associated with the return code,
# then check if there's a default backup.
def check_and_run_backups(self, branch_name, return_code) :
    print_full_bar()
    print_and_log([(' ', 'white')])

    if self.return_code_backup_command_lists :
        for return_code_tuple in self.return_code_backup_command_lists :
            (return_code_bcl, bcl) = return_code_tuple
            if (return_code_bcl == return_code) :
                print_and_log([('Backup command list associated with return code ', 'green'), (str(return_code), 'white'), (' was detected for failed command: ', 'green'), (str(self.command), 'cyan')])
                new_branch_name = branch_name + '/(' + self.command + ' :: returncode=' + str(return_code) + ')'
                print_and_log([('Running backup commands on the backup branch: ', 'green'), (str(new_branch_name), 'green')])
                run_branch(bcl, new_branch_name)
                print_full_bar()
                print_and_log([(' ', 'white')])
                print_and_log([('Finished backup command list associated with return code ', 'green'), (str(return_code), 'white'), (' for command: ', 'green'), (str(self.command), 'cyan')])
                print_and_log([('Returning to parent branch: ', 'green'), (branch_name, 'green')])
                return

    if self.backup_command_list :
        print_and_log([('Backup command list was detected for failed command: ', 'green'), (str(self.command), 'cyan')])
        new_branch_name = branch_name + '/(' + self.command + ')'
        print_and_log([('Running backup commands on the backup branch: ', 'green'), (str(new_branch_name), 'green')])
        run_branch(self.backup_command_list, new_branch_name)
        print_full_bar()
        print_and_log([(' ', 'white')])
        print_and_log([('Finished backup command list for command: ', 'green'), (str(self.command), 'cyan')])
        print_and_log([('Returning to parent branch: ', 'green'), (branch_name, 'green')])
    else :
        print_and_log([('No backup command list detected for failed command: ', 'yellow'), (str(self.command), 'cyan')])

def add_prompt_responses_and_run_command(self, branch_name):
    if self.prompt_responses:
        print_and_log([("Automatic Terminal Prompt Responses: ", 'yellow'), (str(self.prompt_responses), 'white')])
        responses = ''
        for pr in self.prompt_responses :
            responses += str(pr) + os.linesep

        p = Popen(self.command, shell=True, stdin=PIPE, stdout=PIPE)

        out, err = p.communicate(responses.encode())
        print_and_log([(out.decode(), 'white')])
        return_code = p.wait()
        return return_code

    else:
        if logfile_created:
            p = Popen(self.command, shell=True, stdout=PIPE, bufsize=1)
            for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):
                print_and_log([(line.rstrip(), 'white')])

            return_code = p.wait()
            return return_code
        else:
            return subprocess.call(self.command, shell=True)


# constructor for each command
class Command():
    def __init__(self, command='', message='', critical=True, retries=0, sleep_between_retries=0, visible=True, backup_command_list=[], return_code_backup_command_lists=[], prompt_responses=[]):
        self.command = command
        self.message = message
        self.critical = critical
        self.retries = retries
        self.sleep_between_retries = sleep_between_retries
        self.visible = visible
        self.backup_command_list = backup_command_list
        self.return_code_backup_command_lists = return_code_backup_command_lists
        self.prompt_responses = prompt_responses


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
                print_and_log([(' ', 'white')])
                print_and_log([('Error with command: ', 'yellow'), (str(self.command), 'cyan')])
                if (self.retries != 0) :
                    print_and_log([('Command retries exceeded... times_tried: ', 'yellow'), (str(times_tried), 'white'), (', retries allotted: ', 'yellow'), (str(self.retries), 'white')])

                check_and_run_backups(self, branch_name, return_code)

                if self.critical :
                    print_and_log([(' ', 'white')])
                    print_and_log([('This failed command was flagged as critical, so the current list of commands will terminate at this command.', 'red')])
                    print_and_log([('More specifically, the branch: "', 'red'), (branch_name, 'green'), ('" ...', 'red')])
                    print_and_log([('...is terminating at command: "', 'red'), (self.command, 'cyan'), ('".', 'red')])
                    return -1

                else :
                    print_and_log([(' ', 'white')])
                    print_and_log([('This failed command was not flagged as critical, so the list of commands will now continue where it left off.', 'yellow')])
                    print_and_log([('More specifically, the branch: "', 'yellow'), (branch_name, 'green'), ('" ...', 'yellow')])
                    print_and_log([('...will continue with the following commands (if any) after the command: "', 'red'), (self.command, 'cyan'), ('".', 'yellow')])
                    return 1

            if self.visible :
                print_full_bar()
                if times_tried != 0 :
                    print_and_log([(' ', 'white')])
                    print_and_log([('Retrying... there has been ', 'yellow'), (str(times_tried), 'white'), (' unsuccessful attempts.', 'yellow')])
                    print_and_log([('Retries left: ', 'yellow'), (str(self.retries - times_tried), 'white'), ('.', 'yellow')])
                    if self.sleep_between_retries != 0 :
                        print_and_log([('sleep between retries has been set to ', 'yellow'), (str(self.sleep_between_retries), 'white'), (' seconds. Waiting to execute...', 'yellow')])
                        time.sleep(self.sleep_between_retries)

                print_and_log([(' ', 'white')])
                if self.message != '' :
                    print_and_log([("~" + self.message, 'magenta')])

                print_and_log([(branch_name + '>>> ', 'green'), (self.command, 'cyan')])

            times_tried += 1
            return_code = add_prompt_responses_and_run_command(self, branch_name)

            if self.visible :
                print_and_log([('Return Code: ', 'yellow'), (str(return_code), 'white')])

        return 0

def run_branch(commands, branch_name) :
    failed_commands = []
    successful_commands = []
    interrupted_commands = []
    interupted_command = ''
    unexecuted_commands = []
    critical_failed_commands = []

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
        print_and_log([("KeyBoardInterrupt ...Exiting", 'yellow')])
        if logfile_created :
            logfile.close()
        sys.exit(2)

    print_full_bar()
    print_and_log([(' ', 'white')])
    print_and_log([('# Final Summary for Command List Branch: ', 'yellow'), (branch_name, 'green')])
    print_and_log([(' ', 'white')])
    print_command_list(successful_commands,'Successful Commands: ')
    print_command_list(interrupted_commands,'Interrupted Commands: ')
    print_command_list(unexecuted_commands,'Unexecuted Commands: ')
    print_command_list(failed_commands,'Failed Commands: ')
    print_command_list(critical_failed_commands,'Critical Failed Commands: ')

def run_commands(commands, branch_name='(root)', create_logfile=False):
    global logfile
    global logfile_created
    if create_logfile :
        set_up_logfile()

    run_branch(commands, branch_name)

    print_full_bar()
    print_and_log([(' ', 'white')])
    print_and_log([('DeclarScript file "', 'green'), (get_name(), 'white'), ('" has completed execution.', 'green')])
    print_full_bar()

    if logfile_created :
        logfile.close()
