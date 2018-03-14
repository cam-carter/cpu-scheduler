from collections import deque

class Process:
    def __init__(self):
        self.burst_times = deque([])
        self.wait_times = deque([])

    def create(self, filename):
        inputfile = open(filename)
        lines = inputfile.readlines()
        self.pid = int(lines[0].rstrip('\n'))
        self.arrival_time = int(lines[1].rstrip('\n'))
        self.burst_times = deque([int(lines[2].rstrip('\n')), int(lines[4].rstrip('\n'))])
        self.wait_times = deque([int(lines[3].rstrip('\n')), int(lines[5].rstrip('\n'))])

    def get_burst(self):
        burst_time = self.burst_times.popleft()
        return burst_time

    def get_wait(self):
        wait_time = self.wait_times.popleft()
        return wait_time
