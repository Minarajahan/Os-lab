def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        current_time += process.burst_time
        process.turnaround_time = current_time - process.arrival_time
    return processes