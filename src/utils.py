from process import Process
from multiprocessing import Queue
from Queue import Empty

q = Queue()
process = Process()

def print_queue(queue):
    # TODO: print on same line
    q = queue
    copy = []
    while True:
        try:
            elem = q.get(False)
        except Empty:
            break
        else:
            copy.append(elem)

    for elem in copy:
        print('Process ' + repr(elem.pid))

def set_wait_time(wait_time, wait_queue):
    q = wait_queue
    if wait_time == None:
        try:
            process = wait_queue.get(False)
            if process.wait_times:
                wait_time = process.get_wait()
            else:
                wait_time = None
            return wait_time
        except Empty:
            return None
    else:
        wait_time -= 1
        return wait_time

def set_burst_time(burst_time, ready_queue):
    q = ready_queue
    if burst_time == None:
        try:
            process = ready_queue.get(False)
            burst_time = process.get_burst(False)
            return burst_time
        except Empty:
            return None
    else:
        burst_time -= 1
        return burst_time
