from src.process import Process

process = Process()
process.create('processes/process1.txt')







print('burst_time' + repr(process.get_burst()))
print('wait_time' + repr(process.get_wait()))
process.burst_times.appendleft(20)
print('burst_time 2 = ' + repr(process.get_burst()))
print('wait_time 2 = ' + repr(process.get_wait()))
