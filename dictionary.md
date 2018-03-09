# Dictionary of Variables

Note that because Python does not inherently declare variable types, we will list the type of value the variables will be used according to other languages.

Basic housekeeping variables
-----------------
1. `systemClock` - this variable will take the `int` type and represent the system clock, beginning from 0.
2. `timeQuantum`- this variable will take the `int` type and it will hold the Time Quantum given by a command line argument.
3. `numJobs` - this variable will take the `int` type and it will indicate the number of jobs completed by the scheduler.
4. `turnaroundTime` - this variable will take the `int` type and it will hold the average amount of time it takes to complete a process.
5. `avgWaiting` - this variable will take the `int` type and it will hold the average waiting time of each process.
6. `numContext` - this variable will take the `int` type and it will hold the total number of context switches performed.
7. `cpuUtil` - this variable will take the `float` type and it will display the percentage of total time the CPU is running.

Process-specific variables
--------
In this program, we will be using a `process` object.

1. `instr[]` - this will be a list of each instruction given by the file name. This variable will not be inside of the process, but will give the process attributes.
2. 
