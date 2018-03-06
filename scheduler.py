class Process(object):
    def __init__(self, arrival_time, total_cpu_time, cpu_burst, cpu_wait, pid):
        self.arrival_time = arrival_time
        self.total_cpu_time = total_cpu_time
        self.cpu_burst = cpu_burst
        self.cpu_wait = cpu_wait
        slef.pid = pid
