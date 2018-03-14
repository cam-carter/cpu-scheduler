from multiprocessing import Queue
from Queue import Empty
from src.process import Process

ready_queue = Queue(maxsize=3)
process = {}

number_of_processes = 3
sysclock = 0

burst_time = 0
wait_time = 0

running_process = None
waiting_process = Process()

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

    sysclock += 1


