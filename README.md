# CPU Scheduler Simulator

A simple CPU scheduler written in Python for COSCA365, Operating Systems.

### Created by: @cam-carter & @tmloupe

# Dictionary of Variables

Note that because Python does not inherently declare variable types, we will list the type of value the variables will be used according to other languages. Additionally, other variables may be necessary, such as `temp` variables, which may not be reflected in the dictionary of variables. These will be made clear inside of the code.

## Basic housekeeping variables
1. `sysclock` - this variable will take the `int` type and represent the system clock, beginning from 0.
2. `time_quantum`- this variable will take the `int` type and it will hold the Time Quantum given by a command line argument.
3. `num_jobs` - this variable will take the `int` type and it will indicate the number of jobs completed by the scheduler.
4. `turnaround_time` - this variable will take the `int` type and it will hold the average amount of time it takes to complete a process.
5. `avg_waiting` - this variable will take the `int` type and it will hold the average waiting time of each process.
6. `num_context` - this variable will take the `int` type and it will hold the total number of context switches performed.
7. `cpu_util` - this variable will take the `float` type and it will display the percentage of total time the CPU is running.
8. `sys.argv` - this variable is a special list, imported through `sys`, that returns command line arguments into an array. For example, if the number `5` was passed through the command line, `sys.argv[0]` would equal the number `5`.

## Process-specific variables
In this program, we will be creating and using a `process` object.

1. `instr[]` - this will be a list of each instruction given by the file name. This variable will not be inside of the process, but will give the process attributes. Likely to hold `int` values.
2. `pid` - this will be the Process ID, an `int`, assigned to each process uniquely.
3. `process_burst` - this variable holds the process' current burst time, an `int`. It will be utilized in the ready queue.
4. `total_cpu_time` - this variable will hold the process' total burst time, an `int`.
5. `process_exec_time` - this variable will hold the time in which the process arrives into the queue, an `int`.
6. `process_wait` - this variable, an `int`, will hold the process' current wait time, which will be decremented in the wait queue.
