# import the queue library
from queue import *
from collections import deque
from process import Process

number_of_processes = 3
ready_queue = Queue()
wait_queue = Queue()
done = Queue()

process = {}
for i in range(1, number_of_processes + 1):
    process[i] = Process()
    process[i].create('processes/process%d.txt' % (i))
    ready_queue.put(process[i])

# system clock
sysclock = 0
time_quantum = 5
time_quantum_temp = 0
# infinite loop, breaks when process_burst is decremented to 0
wait_time = None

i = 1
while True:
    sysclock += 1
    if i > number_of_processes:
        break

    pid = process[i].pid
    arrival_time = process[i].arrival_time
     
    if i > 1 and process[i - 1].wait_times:
        wait_time = process[i - 1].get_wait()
    if wait_time != None:
        wait_time -= 1
        if wait_time == 0:
            ready_queue.put(wait_queue.get())

    if process[i].burst_times:
        burst_time = process[i].get_burst()
    else:
        i += 1
        sysclock += 1
        continue

    if process[i].burst_times and process[i].wait_times is None:
        done.put(process[i])
        i += 1
        sysclock += 1
        continue

    # checks process arrival time against the system clock
    if sysclock >= arrival_time:
        burst_time -= 1
        time_quantum -= 1

    # decrements time_quantum
    # increments system clock
    
    # checks it process_burst has reached zero and breaks the loop
    if burst_time == 0:
        wait_queue.put(process[i])
        i += 1

    # performs a context switch once the time_quantum reaches 0
    if time_quantum == 0:
        sysclock += 5
        time_quantum = 5
    
    if ready_queue.empty() and wait_queue.empty():
        break

# prints termination status of process and the amount of time it took to execute
print('Process ' + repr(pid) + ' has been terminated.')
print('Finishing at system time: ' + repr(sysclock))
