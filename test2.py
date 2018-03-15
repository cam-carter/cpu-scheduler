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

print(process[1].pid)
print(process[2].pid)
print(process[3].pid)

wait_time = 0
time_quantum = 5
burst_time = 4
sysclock = 1

running_process = Process()
waiting_process = Process()

j = 0
while True:
    # WORKS
    # adds processes to the ready_queue at there specified arrival_time
    for i in range(1, number_of_processes + 1):
        if sysclock == process[i].arrival_time:
            ready_queue.put(process[i])
            print('Process ' + repr(process[i].pid) + ' has arrived.')
    try: 
        running_process = ready_queue.get(False)
    except Empty:
        pass

    while True:
        time_quantum -= 1
        burst_time -= 1

        if burst_time == 0:
            wait_queue.put(running_process)
            sysclock += 5
            print('test')
            burst_time = 4

            break
        elif time_quantum == 0:
            ready_queue.put(running_process)
            running_process.burst_times.appendleft(burst_time)
            time_quantum = 5
            sysclock += 5
            break

    sysclock += 1
    j += 1
    print(sysclock)
