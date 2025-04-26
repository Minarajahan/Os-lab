# class Process:
#     def __init__(self, pid, arrival_time, burst_time):
#         self.pid = pid
#         self.arrival_time = arrival_time
#         self.burst_time = burst_time
#         self.waiting_time = 0
#         self.turnaround_time = 0
#         self.remaining_time = burst_time  # for SJF

# def read_processes_from_file(filename):
#     processes = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if len(parts) == 3:
#                 pid, arrival, burst = map(int, parts)
#                 processes.append(Process(pid, arrival, burst))
#     return processes

# def fcfs(processes):
#     processes.sort(key=lambda x: x.arrival_time)
#     current_time = 0

#     for process in processes:
#         if current_time < process.arrival_time:
#             current_time = process.arrival_time
#         process.waiting_time = current_time - process.arrival_time
#         current_time += process.burst_time
#         process.turnaround_time = process.waiting_time + process.burst_time

#     return processes

# def sjf(processes):
#     current_time = 0
#     completed = 0
#     n = len(processes)

#     while completed < n:
#         ready = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
#         if not ready:
#             current_time += 1
#             continue

#         shortest = min(ready, key=lambda x: x.burst_time)
#         shortest.waiting_time = current_time - shortest.arrival_time
#         current_time += shortest.burst_time
#         shortest.turnaround_time = current_time - shortest.arrival_time
#         shortest.remaining_time = 0
#         completed += 1

#     return processes

# def print_results(title, processes):
#     print(f"\n{title} Results:")
#     print("PID\tArrival\tBurst\tWaiting\tTurnaround")
#     for p in processes:
#         print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}")


# if __name__ == "__main__":
#     original_processes = read_processes_from_file("processes.txt")


#     fcfs_processes = [Process(p.pid, p.arrival_time, p.burst_time) for p in original_processes]
#     fcfs_result = fcfs(fcfs_processes)
#     print_results("FCFS", fcfs_result)


#     sjf_processes = [Process(p.pid, p.arrival_time, p.burst_time) for p in original_processes]
#     sjf_result = sjf(sjf_processes)
#     print_results("SJF", sjf_result)
# ////////////////