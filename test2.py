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
burst_time = 5
sysclock = 0

running_process = Process()
waiting_process = Process()

j = 0
while True:
    # WORKS
    # adds processes to the ready_queue at there specified arrival_time
    for i in range(i, number_of_processes + 1):
        if sysclock == process[i].arrival_time:
            ready_queue.put(process[i])
            print('Process ' + repr(process[i].pid) + ' has arrived.')
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
            try:
                running_process = ready_queue.get(False)
            except Empty:
                pass
            sysclock += 5
            print('test')
            break
        elif time_quantum == 0:
            time_quantum = 5
            sysclock += 5
            break

    sysclock += 1
    j += 1
    if i == 10:
        break
