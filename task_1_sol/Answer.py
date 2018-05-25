# Haomin Shi
# 05/25/2018
# Response to the assignment 2, task 1

import os
import subprocess
import pandas as pd
import time as t
from subprocess import Popen

"""
    Take in a list of commands,
    execute the commands in the list:
        - Then:
            A. Display report:
                1. total elapsed time,
                2. avg, max, min execution time among all commands
"""


def solution(commands_list):
    # concurent, all the commands executed at the same time
    process_list = []
    time_dict = {}
    time_list = []

    FNULL = open(os.devnull, 'w')

    print("++++++++++++++++++++++++++++++++++++++++")

    for str_element in commands_list:
        # break down the command provided into arg section and command section
        # each command be come a list, e.g: ["ls","-l", "/"]
        command_args = str_element.split(' ')
        print("Executing cmd ---> " + str(commands_list.index(str_element)) +
              " ---> " + str_element)
        process_list.append(subprocess.Popen(
            command_args, stdout=FNULL, stderr=subprocess.STDOUT))
        time_dict[process_list[-1]] = t.time()

    while process_list:
        for process in process_list:
            if process.poll() != None:
                # time recorded
                time_dict[process] = t.time() - time_dict[process]
                # take finished process out
                process_list.remove(process)
                break
            else:  # do nothing if process not done yet
                continue

    for key in time_dict:  # convert dict to list for easy dataframe construct
        time_list.append(time_dict[key])

    return time_list


def main():
    """functions will be called here"""
    # ------- commands var given by the assignment
    commands = ['sleep 3', 'ls -l /', 'find /', 'sleep 4',
                'find /usr', 'date', 'sleep 5', 'uptime']
    # my_test_commands = ['sleep 3', 'date', 'uptime', 'echo 11111', 'sleep 4']
    # ----------------------------------------------------------------------
    log_list = []
    # run 3 times since scientific method requires to run test at least 3 times
    total_elapsed_time = t.time()
    """If you want to run more than 3 test, just call and append more"""
    log_list.append(solution(commands))
    log_list.append(solution(commands))
    log_list.append(solution(commands))
    # e.g: log_list.append(solution(commands))
    # if you want to add more run follow the above example

    """DO NOT edit codes below"""
    total_elapsed_time = (t.time() - total_elapsed_time)/len(log_list)
    # ----------------------------------------------------------------------
    final_report = pd.DataFrame(log_list)
    print("------------ Total Elapsedtime ------------")
    print("The avg total elapsed time when execute these cmds concurrently is: ")
    print(total_elapsed_time)
    print("The avg total elapsed time when execute these cmds one by one is: ")
    print(final_report.sum(axis=1).mean())
    print("------------ Overview ------------")
    print(final_report)
    print("* vertical index indicates each run")
    print("* column index indicates each command")
    print("------------ Final Report ------------")
    print(final_report.describe())
    print("NOTE 1: mean is avg elapsed time")
    print("NOTE 2: min is minimum elapsed time")
    print("NOTE 3: max is maximum elapsed time")


if __name__ == "__main__":
    main()
