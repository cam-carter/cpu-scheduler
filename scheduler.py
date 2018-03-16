#!/usr/bin/env python2

# import Queue class from multiprocessing module
from multiprocessing import Queue
# import Empty class from Queue module
from Queue import Empty
# import Process class from ./src/process/
from src.process import Process
# import utils.py from ./src/
from src.utils import *

# initialize queues
ready_queue = Queue()
wait_queue = Queue()

# initialize process dictionary
process = {}

# initialize number_of_processes
number_of_processes = 3

# initialize time variables
sysclock = 0
burst_time = 0
wait_time = 0
time_quantum = 5
switch_counter = 0

# initialize temp processes
running_process = None
waiting_process = None

# initialize booleans
cpu_busy = False
context_switch = False

# creates Processes and puts them into process[] dictionary
for i in range(1, number_of_processes + 1):
    process[i] = Process()
    process[i].create('processes/process%d.txt' % i)

# while True will loop until a break message is sent
# loop will break when number_of_processes == 0
# number_of_porcesses is decremented whenever process is terminated
while True:
    # adds processes to the ready queue at there specified arrival times
    for i in range (1, number_of_processes + 1):
        # if sysclock is the same as arrival_time, add process[i] to ready_queue
        if sysclock == process[i].arrival_time:
            # put process to back of ready_queue
            ready_queue.put(process[i])
            # process arrival message
            print('Process ' + repr(process[i].pid) + ' has arrived at ' + repr(sysclock))

    # check if context_switch == True
    if context_switch == True:
        # increment switch_counter
        switch_counter += 1
        # increment sysclock
        sysclock += 1
        # when switch_counter == 5 halt context_switch
        if switch_counter == 5:
            # set context_switch flag to False
            context_switch = False
            # reset switch_counter
            switch_counter = 1
        continue

    # check to see if waiting_process == None
    if waiting_process == None:
        # try to get waiting_process from wait_queue, catch Empty exception and pass
        try:
            # get waiting_process from front of wait_queue
            waiting_process = wait_queue.get(False)
            # set wait_time from waiting_process, will pull from front of wait_times deque
            wait_time = waiting_process.get_wait()
        except Empty:
            pass

    # check to see if cpu_busy flag == False
    if cpu_busy == False:
        # try to get running_process from ready_queue, catch Empty exception and pass
        try:
            # get running_process from front of ready_queue
            running_process = ready_queue.get(False)
            # set burst_time from running_process, will pull from front of burst_times deque
            burst_time = running_process.get_burst()
            # set cpu_busy flag to True
            cpu_busy = True
        except Empty:
            pass
    else:
        # decrement time_quantum
        time_quantum -= 1
        # decrement burst_time
        burst_time -= 1

    if waiting_process != None:
        wait_time -= 1
    
    # check to see if wait_time == 0
    if wait_time == 0:
        # check if waiting_process is not None
        if waiting_process != None:
            # check to see if waiting_process has any burst_times left
            if waiting_process.burst_times:
                # put waiting_process to back of ready_queue
                ready_queue.put(waiting_process)
                # set context_switch flag to True
                context_switch = True
                # set waiting_process = None
                waiting_process = None
            else:
                # process termination message
                print('Process ' + repr(waiting_process.pid) + ' has been terminated at time ' + repr(sysclock))
                # set waiting_process to None
                waiting_process = None
                # decrement number of processes
                number_of_processes -= 1
    
    # check if running_process is not None
    if running_process != None:
        # check to see if time_quantum == 0 and burst_time > 0
        if time_quantum == 0 and burst_time > 0:
            # set cpu_busy flag to True
            cpu_busy = False
            # set context_switch flag to True
            context_switch = True
            # storing ongoing burst_time to front of burst_time deque
            running_process.burst_times.appendleft(burst_time)
            # put running_process to back of ready_queue
            ready_queue.put(running_process)
            # reset time_quantum
            time_quantum = 5
        
        # check to see if time_quantum == 0 and burst_time == 0
        if time_quantum == 0 and burst_time == 0:
            # set cpu_busy flag to False
            cpu_busy = False
            # set context_switch flag to True
            context_switch = True
            # check if running_process is not None
            if running_process != None:
                # check to see if running_process has any wait_times
                if running_process.wait_times:
                    # put running_process to back of wait_queue
                    wait_queue.put(running_process)
                    # set running_process = None
                    running_process = None
                else:
                    # termination message
                    print('Process ' + repr(waiting_process.pid) + ' has been terminated at time ' + repr(sysclock))
                    # set waiting_process = None
                    waiting_process = None
                    # decrement number_of_processes
                    number_of_processes -= 1
            # print_queue
            # reset time_quantum
            time_quantum = 5
        
        # check to see if time_quantum > 0 and burst_time == 0
        if time_quantum > 0 and burst_time == 0:
            # set cpu_busy flag to False
            cpu_busy = False
            # set context_switch flag to True
            context_switch = True
            # check if running_process is not None
            if running_process != None:
                # check to see if running_process has any wait_times
                if running_process.wait_times:
                    # put running_process to back of wait_queue
                    wait_queue.put(running_process)
                    # set running_process = None
                    running_process = None
                else:
                    # termination message
                    print('Process ' + repr(waiting_process.pid) + ' has been terminated at time ' + repr(sysclock))
                    # set waiting_process = None
                    waiting_process = None
                    # decrement number_of_processes
                    number_of_processes -= 1

    # breaks loop when number_of_processes == 0
    if number_of_processes == 0:
        break
    # increment sysclock
    sysclock += 1
# end of while True
