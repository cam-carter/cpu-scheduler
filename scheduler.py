# import the queue library
from queue import *
from collections import deque
from process import Process

number_of_processes = 3
process_list = deque([])
ready = Queue(maxsize=1)
process1 = Process()
process1.create('process1.txt')

pid = process1.pid
# process arrival time
process_arrival_time = 5
# process burst time
process_burst = 10

burst_time = process1.get_burst()
# Defines a test variable for burst time to use in queue
# burst_time = ready.get()

# system clock
sysclock = 0
time_quantum = 5
time_quantum_temp = 0
# infinite loop, breaks when process_burst is decremented to 0
i = 1
while True:
    # checks process arrival time against the system clock
    if sysclock >= process_arrival_time:
        burst_time -= 1
        time_quantum -= 1

    # decrements time_quantum
    # increments system clock
    sysclock += 1
    
    # checks it process_burst has reached zero and breaks the loop
    if burst_time == 0:
        break

    # performs a context switch once the time_quantum reaches 0
    if time_quantum == 0:
        sysclock += 5
        time_quantum = 5

# prints termination status of process and the amount of time it took to execute
print('Process ' + repr(pid) + ' has been terminated.')
print('Finishing at system time: ' + repr(sysclock))
