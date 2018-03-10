# import the queue library
from Queue import *

# max amount of time for CPU to burst, with a temporary holding value
time_quantum = 5
time_quantum_temp = 0

# creating the ready queue with a max size of 1
ready = Queue(maxsize=1)

# process id is uniquely assigned to each process
pid = 1
# process araival time
# TODO: rename this variable to process_arrival_time? Makes more sense.
process_exec_time = 5
# process burst time
process_burst = 10

# Puts the process burst into the queue, for testing purposes
ready.put(process_burst)

# Defines a test variable for burst time to use in queue
burst_time = ready.get()

# system clock
sysclock = 0
# infinite loop, breaks when process_burst is decremented to 0
while True:
    # checks process arrival time against the system clock
    if sysclock >= process_exec_time:
        burst_time -= 1
        time_quantum_temp += 1

    # increments system clock
    sysclock += 1
    
    # performs a context switch once the time_quantum_temp becomes greater than
    # the time quantum
    # TODO: utilize one time quantum and not two variables
    if time_quantum_temp > time_quantum:
        sysclock += 5
        time_quantum_temp = 0
        continue

    # checks it process_burst has reached zero and breaks the loop
    if burst_time == 0:
        break

# prints termination status of process and the amount of time it took to execute
print('Process ' + repr(pid) + ' has been terminated.')
print('Finishing at system time: ' + repr(sysclock))
