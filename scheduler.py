pid = 1
process_exec_time = 5
process_burst = 10

sysclock = 0
while True:
    if sysclock >= process_exec_time:
        process_burst -= 1

    sysclock += 1
    if process_burst == 0:
        break

print = 'Process ' + repr(pid) + ' has been terminated.'
print = 'Finishing at system time: ' + repr(sysclock)
    
