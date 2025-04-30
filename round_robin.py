def round_robin(processes, quantum):
    """Round Robin (preemptive)"""
    current_time = 0
    queue = processes.copy()
    completed = 0
    n = len(queue)
    
    # Initialize total times
    total_waiting_time = 0
    total_turnaround_time = 0
    total_completion_time = 0
    
    while completed < n:
        # Flag to check if any process was executed in this round
        executed_this_round = False
        
        for process in queue:
            if process.remaining_time > 0 and process.arrival_time <= current_time:
                executed_this_round = True  # A process is being executed
                if process.remaining_time > quantum:
                    current_time += quantum
                    process.remaining_time -= quantum
                else:
                    current_time += process.remaining_time
                    process.waiting_time = current_time - process.arrival_time - process.burst_time
                    process.turnaround_time = current_time - process.arrival_time
                    process.remaining_time = 0
                    completed += 1
                    # Calculate completion time
                    process.completion_time = current_time
                    
                    # Update total times
                    total_waiting_time += process.waiting_time
                    total_turnaround_time += process.turnaround_time
                    total_completion_time += process.completion_time

                    # Debug output
                    print(f"Process {process.pid} completed at time {current_time}")

        # Increment current time if no processes were executed
        if not executed_this_round:
            current_time += 1
    
    # Calculate average times
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    avg_completion_time = total_completion_time / n
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Completion Time: {avg_completion_time:.2f}")

    return processes
