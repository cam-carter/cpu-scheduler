# import the queue library
from src.utils import *
from multiprocessing import Queue
from Queue import Empty
from collections import deque
from src.process import Process

number_of_processes = 3
ready_queue = Queue()
wait_queue = Queue()
done = Queue()

# declare process dictionary
process = {}

# for loop from 1 to 4 crates processes from file
for i in range(1, number_of_processes + 1):
    process[i] = Process()
    process[i].create('processes/process%d.txt' % (i))
    # ready_queue.put(process[i])

sysclock = 0
i = 1
time_quantum = 5

burst_time
burst_time is None
wait_time = None
running_process = None
waiting_process = None

while True:

    # checks arrival time of each process against the system clock
    # if sysclock == arrival_time add process to ready_queue
    for j in range (1, number_of_processes + 1):
        if sysclock == process[j].arrival_time:
            ready_queue.put(process[j])
        j += 1

    # check if there is a running process, if not get one from the ready_queue
    if running_process == None:
        try:
            running_process = ready_queue.get(False)
        except Empty:
            running_process = None

    if waiting_process == None:
        try:
            waiting_process = wait_queue.get(False)
        except Empty:
            waiting_process = None

    # check if there is a currently assigned burst_time, if not get one from the running_process
    # check if burst_time == 0, if so puts the running_process into the wait_queue
    #   also performs a context switch
    # else decrement burst_time
    if burst_time is None:
        try:
            burst_time = 0
            burst_time = running_process.get_burst()
        except Empty:
            if running_process.wait_times:
                pass
            else:
                print('Process ' + repr(running_process.pid) + ' terminated at sysclock ' + repr(sysclock))
    elif burst_time == 0:
        wait_queue.put(running_process)
        sysclock += 5
        burst_time = None
        running_process = None
    elif time_quantum == 0:
        running_process.burst_times.appendleft(burst_time)
        ready_queue.put(running_process)
        try:
            running_process = ready_queue.get()
        except Empty:
            running_process = None
        try:
            burst_time = runing_process.get_burst()
        except Empty:
            burst_time = None
    else:
        burst_time -= 1
        time_quantum -= 1

    if wait_time == None:
        try:
            wait_time = waiting_process.get_wait()
        except Empty:
            if waiting_process.burst_times:
                pass
            else:
                print('Process ' + repr(waiting_process.pid) + ' terminated at sysclock ' + repr(sysclock))
    elif wait_time == 0:
        ready_queue.put(waiting_process)
        sysclock += 5
        wait_time = None
        waiting_process = None
    else:
        wait_time -= 1
    
    sysclock += 1
