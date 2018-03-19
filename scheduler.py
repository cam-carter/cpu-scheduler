import argparse
from multiprocessing import Queue
from Queue import Empty
from src.process import Process

# Parses arguments from the command line
parser = argparse.ArgumentParser(description='Take time quantum')
parser.add_argument('time_quantum', type=int, help='time quantum')
args = parser.parse_args()

# Initialize the queues and the process
ready_queue = Queue(maxsize=3)
wait_queue = Queue(maxsize=3)
process = {}

# Variables used for the program
time_quantum = args.time_quantum
sysclock = 0
number_of_processes = 3
total_processes = number_of_processes
burst_time = 0
wait_time = 0
switch_counter = 1

# Variables for output calculations
total_runtime = 0
total_waiting = 0
total_context = 0

# Flags for processes
running_process = None
waiting_process = None
cpu_busy = False
context_switch = False

# Creates processes from the text files in the processes folder
for i in range(1, number_of_processes + 1):
	process[i] = Process()
	process[i].create('processes/process%d.txt' % i)

while True:
	# adds processes to the ready queue at their specified arrival times
	for i in range (1, number_of_processes + 1):
		if sysclock == process[i].arrival_time:
			ready_queue.put(process[i])
			print('Process ' + repr(process[i].pid) + ' has arrived.')

	print('Time %d' % sysclock + ': ')

	# Display the running and waiting processes.
	if running_process != None:
		print('Currently running process ' + repr(running_process.pid) + '.')
	else:
		print('There is no running process.')
	if waiting_process != None:
		print('Currently process ' + repr(waiting_process.pid) + ' is waiting.')
	else:
		print('There is no waiting process.')

	# If there is a context switch, increment the sysclock and
	# check for process arrivals.
	if context_switch == True:
		if switch_counter == 1:
			print('Performing context switch.')
		switch_counter += 1
		sysclock += 1
		if switch_counter > 5:
			context_switch = False
			switch_counter = 1
			print('Context switch is ending.')
			#halt = input('...') # Comment/uncomment this line for halting.
		continue

	# If there is no waiting process, check if there are any in the wait
	# queue. Otherwise, pass.
	if waiting_process == None:
		try:
			waiting_process = wait_queue.get(False)
			wait_time = waiting_process.get_wait()
		except Empty:
			pass

	# If the CPU is not busy running a process, try to grab a new process
	# from the ready queue. If the CPU is busy, then decrement the time quantum
	# and the burst time.
	if cpu_busy == False:
		try:
			running_process = ready_queue.get(False)
			burst_time = running_process.get_burst()
			cpu_busy = True
		except Empty:
			pass
	else:
		time_quantum -= 1
		burst_time -= 1

	# Decrements the wait times for processes.
	if waiting_process != None:
		wait_time -= 1

	# When the wait time for a process hits 0, if there are burst times left,
	# context switch it to the ready queue. Otherwise, terminate the process.
	if wait_time == 0:
		if waiting_process != None:
			if waiting_process.burst_times:
				ready_queue.put(waiting_process)
				context_switch = True
				waiting_process = None
			else:
				print('Process %d' % waiting_process.pid, end = '')
				waiting_process = None
				print(' terminated at system time %d' % sysclock + '.')
				number_of_processes -= 1

	# If the time quantum is zero and the burst time is greater than zero,
	# and there is a running process, store the burst time back into the process
	# and perform a context switch back into the ready queue and reset
	# the time quantum.
	if running_process != None:
		if time_quantum == 0 and burst_time > 0:
			cpu_busy = False
			context_switch = True
			running_process.burst_times.appendleft(burst_time)
			ready_queue.put(running_process)
			time_quantum = args.time_quantum

		# If the time quantum and burst times are both zero, context switch
		# If there is a running process, put it in the wait queue. Otherwise,
		# terminate the process. Reset the time quantum.
		if time_quantum == 0 and burst_time == 0:
			cpu_busy = False
			context_switch = True
			if running_process != None:
				if running_process.wait_times:
					wait_queue.put(running_process)
					running_process = None
				else:
					print('Process %d' % waiting_process.pid, end = '')
					print(' terminated at system time %d' % sysclock + '.')
					waiting_process = None
					number_of_processes -= 1
			time_quantum = args.time_quantum

		# If the time quantum is greater than zero and the burst time is equal
		# to zero, and if there is a running process with wait times,
		# put the process into the wait queue. Otherwise, terminate the process.
		if time_quantum > 0 and burst_time == 0:
			cpu_busy = False
			context_switch = True
			if running_process != None:
				if running_process.wait_times:
					wait_queue.put(running_process)
					running_process = None
				else:
					print('Process %d' % waiting_process.pid, end = '')
					print(' terminated at system time %d' % sysclock + '.')
					waiting_process = None
					number_of_processes -= 1

	# Once the number of processes reaches zero, break.
	if number_of_processes == 0:
		break

	# Incrementing the variables required for calculations
	sysclock += 1
	if (cpu_busy == True):
		total_runtime += 1
	if (cpu_busy == False):
		total_waiting += 1
	if (context_switch):
		total_context += 1

	#halt = input('...') # Comment/uncomment this line for halting.

# Final output calculations
cpu_util = (total_runtime / sysclock) * 100
average_runtime = total_runtime / total_processes
average_wait = total_waiting / total_processes

# Final output
print('System terminated at time %d units' % sysclock)
print('Number of processes: %d' % total_processes)
print('Time quantum used: %d' % args.time_quantum) # this should be the arg
print('Total time spent waiting: %d units (average: %f)' % (total_waiting, average_wait))
print('Total system run time: %d units (average: %f)' % (total_runtime, average_runtime))
print('Total context switches: %d' % total_context)
print('CPU Utilization: %f' % cpu_util + '%')

halt = input('Press any key to continue.')
