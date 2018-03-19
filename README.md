# CPU Scheduler Simulator

A simple CPU scheduler written in Python for COSCA365, Operating Systems.  This simulation implements a FCFS scheduling algorithm.

# Dictionary of Variables

Note that because Python does not inherently declare variable types, we will list the type of value the variables will be used according to other languages. Additionally, other variables may be necessary, such as `temp` variables, which may not be reflected in the dictionary of variables. These will be made clear inside of the code.

## Basic housekeeping variables
1. `sysclock` - this variable will take the `int` type and represent the system clock, beginning from 0.
2. `time_quantum`- time quantum for the program. Givin by a command line argument to the scheduler, ex. `python scheduler.py 10` where the number `10` is the program `time_quantum`
3. `number_of_processes` - total number of processes for the scheduler.  Hard-coded into the pogram and is decremented whenever a process is terminated; once `number_of_processes == 0` the main loop breaks and the program is halted.
4. `total_processes` - set equal to the `number_of_processes` in the beginning of the pogram.  Since `number_of_processes` is decremented, `total_processes` is used make runtime calculations after main loop is broken.
5. `avg_waiting` - this variable will take the `int` type and it will hold the average waiting time of each process.
6. `num_context` - this variable will take the `int` type and it will hold the total number of context switches performed.
7. `cpu_util` - this variable will take the `float` type and it will display the percentage of total time the CPU is running.
8. `parser` - the `ArgumentParser` object imported from Python's `argparse` module. Allows the use of command line arguments, so the user can input `time_quantum`
9. `args` - arguments parsed by the `parser`.
 
## Process-specific variables
In this program, we will be creating and using a `process` object.

1. `process[]` - process dictionary that holds a `process[i]` where `i = pid`; the dictionary contains `Process` objects. Used to iterate through while creating the processes from the text files provided.
2. `pid` - this will be the Process ID, an `int`, assigned to each process uniquely.
3. `burst_times` - deque containing individual `burst_time` variables. Used to pop and append `burst_time` for running or waiting process.
4. `wait_times` - deque containing individual `wait_time` variables. Used to pop and append `wait_time` for running or waiting process.
5. `arrival_time` - time at which the process arrives in the program.  Checked in the beginning of the program with a loop testing `arrival_time` against `sysclock`.
6. `inputfile` - file to create the process from.

## Queues

1. `ready` - this queue will be the "ready" queue for `process` objects that are ready to be run by the CPU.
2. `wait` - this queue will be the "wait" queue for `process` objects that are waiting for their wait time to decrease.
