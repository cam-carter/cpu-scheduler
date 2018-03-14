from multiprocessing import Queue
from Queue import Empty
from src.process import Process

ready_queue = Queue(maxsize=3)
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
    for i in range (1, number_of_processes + 1):
        if sysclock == process[i].arrival_time:
            ready_queue.put(process[i])
            print('Process ' + repr(process[i].pid) + ' has arrived.')
    
    if running_process is None:
        try:
            running_process = ready_queue.get(False)
            print('Currently running process: ' + repr(running_process.pid))
        except Empty:
            pass

    if wait_process is None:
        try:
            waiting_process = waiting_queue.get(False)
            print('Currently waiting process: ' + repr(waiting_process.pid))
        except Empty:
            pass

    if running_process != None:
        if burst_time == 0 and is_declared is False:
            burst_time = running_process.get_burst()
            is_declared = True
            print(burst_time)
        elif burst_time == 0 and is_declared is True:
            wait_queue.put(running_process)
            sysclock += 5
            burst_time = 0
            is_decalred = False
            running_process = None
        elif time_quantum == 0:
            running_process.burst_times.appendleft(burst_time)
            ready_queue.put(running_process)
            sysclock += 5
            burst_time = 0
            is_decalred = False
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
            burst_time = 0
            wait_declared = False
            waiting_process = None
        else:
            wait_time -= 1


    sysclock += 1


