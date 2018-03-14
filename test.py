from multiprocessing import Queue
from Queue import Empty
from src.process import Process

ready_queue = Queue(maxsize=3)
wait_queue = Queue(maxsize=3)
process = {}

number_of_processes = 3
sysclock = 0

burst_time = 0
is_declared = False
wait_declared = False
wait_time = 0

running_process = None
waiting_process = None

for i in range(1, number_of_processes + 1):
    process[i] = Process()
    process[i].create('processes/process%d.txt' % i)

while True:
    # adds processes to the ready queue at there specified arrival times
    for i in range (1, number_of_processes + 1):
        if sysclock == process[i].arrival_time:
            ready_queue.put(process[i])
            print('Process ' + repr(process[i].pid) + ' has arrived.')
    
    # if running_process is empty pull process from ready_queue
    # if ready_queue is empty pass
    if running_process is None:
        try:
            running_process = ready_queue.get(False)
            print('Currently running process: ' + repr(running_process.pid))
        except Empty:
            pass

    # if waiting_process is empty pull process from wait_queue
    # if wait_queue is empty pass
    if waiting_process is None:
        try:
            waiting_process = wait_queue.get(False)
            print('Currently waiting process: ' + repr(waiting_process.pid))
        except Empty:
            pass
    
    # check is there is a running_process
    if running_process != None:
        # if the burst_time is = 0 and hasn't been declared yet then pull burst_time from 
        if burst_time == 0 and is_declared is False:
            # check if there's burst_times in the running_process
            if running_process.burst_times:
                # if there is pull burst_time from left of burst_times
                burst_time = running_process.get_burst()
            # if no burst times check and see if the running_process has any wait times
            else:
                # if the running process has wait_times but no burst_times put it in the wait_queue
                if running_process.wait_times:
                    wait_queue.put(running_process)
                # else pull in a new running_process and the currently running_process is terminated
                else:
                    running_process = ready_queue.get()
                    continue
            is_declared = True
            print(burst_time)
        # if burst_time is = 0 and has already been declared then put running_process in wait_queue
        elif burst_time == 0 and is_declared is True:
            wait_queue.put(running_process)
            # perform context switch and pull in new running process from ready_queue
            sysclock += 5
            running_process = ready_queue.get()
            # if running_process has burst_times get new burst_time
            if running_process.burst_times:
                burst_time = running_process.get_burst()
            # else pull in new process from ready_queue and get new burst_time
            else:
                running_process = ready_queue.get()
                burst_time = running_process.get_burst()
        # if time_quantum = 0 add current burst_time to the left side of its deque
        elif time_quantum == 0:
            running_process.burst_times.appendleft(burst_time)
            # pull in new _prcess from ready_queue
            ready_queue.put(running_process)
            # perform context switch
            sysclock += 5
            burst_time = 0
            is_declared = False
            running_process = None
            time_quantum = 5
        else:
            bust_time -= 1
            time_quantum -= 1

    if waiting_process != None:
        if wait_time == 0 and wait_declared is False:
            wait_time = waiting_process.get_wait()
            wait_declared = True
            print('wait time: ' + repr(wait_time))
        elif wait_time == 0 and wait_declared is True:
            ready_queue.put(waiting_process)
            sysclock += 5
            waiting_process = wwait_queue.get()
            if waiting_process.wait_times:
                wait_time = waiting_process.get_wait()
            else:
                sysclock += 5
                print('Process ' + repr(waiting_process.pid) + ' terminated at ' + repr(sysclock))
        else:
            wait_time -= 1

    if ready_queue.empty() is True and wait_queue.empty() is True:
        break
    sysclock += 1


