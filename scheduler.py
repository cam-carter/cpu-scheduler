# process id is uniquely assigned to each process
pid = 1
# process araival time
# TODO: rename this variable to process_arrival_time? Makes more sense.
process_exec_time = 5
# process burst time
process_burst = 10

# system clock
sysclock = 0
# infinite loop, breaks when process_burst is decremented to 0
while True:
    # checks process arrival time against the system clock
    if sysclock >= process_exec_time:
        process_burst -= 1
    
    # increments system clock
    sysclock += 1
    # checks it process_burst has reached zero and breaks the loop
    if process_burst == 0:
        break

# prints termination status of process and the amount of time it took to execute
print('Process ' + repr(pid) + ' has been terminated.')
print('Finishing at system time: ' + repr(sysclock))
