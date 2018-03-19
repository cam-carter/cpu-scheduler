import argparse
from multiprocessing import Queue
from Queue import Empty
from src.process import Process

ready_queue = Queue(maxsize=3)
wait_queue = Queue(maxsize=3)
process = {}

parser = argparse.ArgumentParser(description='Take time quantum')
parser.add_argument('time_quantum', type=int, help='time quantum')
args = parser.parse_args()

number_of_processes = 3
sysclock = 0
burst_time = 0
wait_time = 0
time_quantum = args.time_quantum
switch_counter = 1

running_process = None
waiting_process = None
cpu_busy = False
context_switch = False

for i in range(1, number_of_processes + 1):
    process[i] = Process()
    process[i].create('processes/process%d.txt' % i)

while True:
    # adds processes to the ready queue at there specified arrival times
    for i in range (1, number_of_processes + 1):
        if sysclock == process[i].arrival_time:
            ready_queue.put(process[i])
            print('Process ' + repr(process[i].pid) + ' has arrived.')

    print(sysclock)
    print('cpu flag = ' + repr(cpu_busy))
    print('context switch = ' + repr(context_switch))
    print('time quantum = ' + repr(time_quantum))
    print('burst time = ' + repr(burst_time))
    print('wait time = ' + repr(wait_time))
    if running_process != None:
        print('running process = ' + repr(running_process.pid))
    else:
        print('running process is none')
    if waiting_process != None:
        print('waiting process = ' + repr(waiting_process.pid))
    else:
        print('waiting_process is none')


    if sysclock > 350:
        halt = input('press any to continue')
    # if running_process is empty pull process from ready_queue
    # if ready_queue is empty pass
    if context_switch == True:
        switch_counter += 1
        sysclock += 1
        if switch_counter > 5:
            context_switch = False
            switch_counter = 1
        continue

    if waiting_process == None:
        try:
            waiting_process = wait_queue.get(False)
            wait_time = waiting_process.get_wait()
        except Empty:
            pass

    if cpu_busy == False:
        try:
            running_process = ready_queue.get(False)
            burst_time = running_process.get_burst()
            cpu_busy = True
            print('Currently running process: ' + repr(running_process.pid))
        except Empty:
            pass
    else:
        time_quantum -= 1
        burst_time -= 1

    if waiting_process != None:
        wait_time -= 1

    if wait_time == 0:
        if waiting_process != None:
            if waiting_process.burst_times:
                print('Moving waiting process into ready queue')
                ready_queue.put(waiting_process)
                context_switch = True
                waiting_process = None
            else:
                print('x')
                waiting_process = None
                number_of_processes -= 1

    if running_process != None:
        if time_quantum == 0 and burst_time > 0:
            cpu_busy = False
            context_switch = True
            running_process.burst_times.appendleft(burst_time)
            print('moving running process into ready queue')
            ready_queue.put(running_process)
            time_quantum = 5

        if time_quantum == 0 and burst_time == 0:
            cpu_busy = False
            context_switch = True
            if running_process != None:
                if running_process.wait_times:
                    print('moving running process to wait queue')
                    wait_queue.put(running_process)
                    running_process = None
                else:
                    print('y')
                    waiting_process = None
                    number_of_processes -= 1
            time_quantum = 5

        if time_quantum > 0 and burst_time == 0:
            cpu_busy = False
            context_switch = True
            if running_process != None:
                print('Running process before context switch = ' + repr(running_process.pid))
                if running_process.wait_times:
                    print('moving running process to wait queue')
                    wait_queue.put(running_process)
                    running_process = None
                else:
                    print('z')
                    waiting_process = None
                    number_of_processes -= 1

    print('# of processes ' + repr(number_of_processes))
    if number_of_processes == 0:
        break
    sysclock += 1
