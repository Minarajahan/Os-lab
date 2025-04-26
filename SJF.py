def sjf(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    completed = 0
    while completed < len(processes):
        ready = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        if not ready:
            current_time += 1
            continue
        shortest = min(ready, key=lambda x: x.burst_time)
        shortest.waiting_time = current_time - shortest.arrival_time
        current_time += shortest.burst_time
        shortest.turnaround_time = current_time - shortest.arrival_time
        shortest.remaining_time = 0
        completed += 1
    return processes