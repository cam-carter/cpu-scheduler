from multiprocessing import Queue
from Queue import Empty
from src.process import Process
from src.utils import *

ready_queue = Queue()
wait_queue = Queue()

process = {}
number_of_processes = 3

# create processes from text files
for i in range(1, number_of_processes + 1):
    process[i] = Process()
    process[i].create('processes/process%d.txt' % i )

wait_time = 0
time_quantum = 5
burst_time = 4
sysclock = 1
terminated = 0
context_switch = False
switch_counter = 1

running_process = Process()
waiting_process = Process()

j = 0
while True:
    # WORKS
    # adds processes to the ready_queue at there specified arrival_time
    for i in range(1, number_of_processes + 1):
        if sysclock == process[i].arrival_time:
            ready_queue.put(process[i])
            print('Process ' + repr(process[i].pid) + ' has arrived at time ' + repr(process[i].arrival_time))
            print('burst ' + repr(process[i].get_burst()))
    if context_switch == True:
        switch_counter += 1
        sysclock += 1
        if switch_counter > 5:
            context_switch = False
            switch_counter = 1
    else:
        try: 
            running_process = ready_queue.get(False)
        except Empty:
            pass

        if running_process.burst_times:
            burst_time = running_process.get_burst()

        while True:
            time_quantum -= 1
            burst_time -= 1

            if burst_time == 0:
                wait_queue.put(running_process)
                context_switch = True
                running_process = wait_queue.get()
                terminated += 1
                break
            elif time_quantum == 0:
                ready_queue.put(running_process)
                running_process.burst_times.appendleft(burst_time)
                running_process = ready_queue.get()
                time_quantum = 5
                context_switch = True

        if running_process.burst_times:
            print('burst_time ' + repr(running_process.get_burst()))
        else:
            print('burst empty')
        if terminated >= number_of_processes:
            print(terminated)
            break
    sysclock += 1
    j += 1
    if j == 1000:
        break
