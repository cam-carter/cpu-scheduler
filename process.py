from collections import deque

class Process:
    def __init__(self, pid, arrival_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_times = deque([])
        self.wait_times = deque([])

    def create_process(filename):
        inputfile = open(filename)
        lines = inputfile.readlines()
        self.pid = lines[0]
        self.arrival_time = lines[1]
        self.burst_times = deque([lines[2], lines[4]])
        self.wait_times = deque([lines[3], lines[5]])

    def get_burst():
        burst_time = self.burst_times.popleft()
        return burst_time

    def get_wait():
        wait_time = self.wait_times.popleft()
        return wait_time
