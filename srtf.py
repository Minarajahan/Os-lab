def srtf(processes):
    """Shortest Remaining Time First (preemptive)"""
    current_time = 0
    completed = 0
    n = len(processes)
    total_waiting_time = 0  # To track total waiting time
    total_turnaround_time = 0  # To track total turnaround time
    total_completion_time = 0  # To track total completion time

    while completed < n:
        ready = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        if not ready:
            current_time += 1  # Increment time if no process is ready
            continue
        
        # Select the process with the shortest remaining time
        shortest = min(ready, key=lambda x: x.remaining_time)
        shortest.remaining_time -= 1
        current_time += 1

        # If the process is finished
        if shortest.remaining_time == 0:
            shortest.turnaround_time = current_time - shortest.arrival_time
            shortest.waiting_time = shortest.turnaround_time - shortest.burst_time
            shortest.completion_time = current_time  # Track completion time
            completed += 1

            # Update total times
            total_waiting_time += shortest.waiting_time
            total_turnaround_time += shortest.turnaround_time
            total_completion_time += shortest.completion_time  # Update total completion time

            # Debug output
            print(f"Process {shortest.pid} completed at time {current_time}")
    
    # Calculate average times
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    avg_completion_time = total_completion_time / n
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Completion Time: {avg_completion_time:.2f}")
    
    return processes


