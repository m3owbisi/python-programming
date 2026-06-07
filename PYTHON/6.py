# Function to calculate waiting time, start time, finish time, and turnaround time for all processes using SJF 
def find_sjf_times(processes, n, burst_time, start_time, finish_time, waiting_time, turnaround_time): 
# Sort processes by burst time since arrival time is 0 
processes_burst = list(zip(processes, burst_time)) 
processes_burst.sort(key=lambda x: x[1]) 
sorted_processes = [process for process, burst in processes_burst] sorted_burst_time = [burst for process, burst in processes_burst] 
for i in range(n): 
if i == 0: 
start_time[i] = 0 # Start time of the first process is 0 
else: 
start_time[i] = finish_time[i - 1] # Start time of the current process is the finish time of the previous process 
waiting_time[i] = start_time[i] # Waiting time is the start time since arrival time is 0 
finish_time[i] = start_time[i] + sorted_burst_time[i] # Finish time is start time + burst time 
turnaround_time[i] = finish_time[i] # Turnaround time is finish time since arrival time is 0 
return sorted_processes, sorted_burst_time 
# Function to calculate and print average times along with detailed process information 
def find_average_time(processes, n, burst_time): 
start_time = [0] * n 
finish_time = [0] * n 
waiting_time = [0] * n 
turnaround_time = [0] * n 
# Calculate times for each process using SJF 
sorted_processes, sorted_burst_time = find_sjf_times(processes, n, burst_time, start_time, finish_time, waiting_time, turnaround_time) 
# Calculate total waiting time and turnaround time 
total_waiting_time = 0 
total_turnaround_time = 0 
print("Original Processes Sorted Processes Arrival Time Burst Time Start Time Waiting Time Finish Time Turnaround Time") 
for i in range(n): 
total_waiting_time += waiting_time[i] 
total_turnaround_time += turnaround_time[i] 
print(f" {processes[i]} {sorted_processes[i]} 0 {sorted_burst_time[i]} {start_time[i]} {waiting_time[i]} {finish_time[i]} {turnaround_time[i]}") 
# Calculate and print average waiting time and turnaround time print(f"\nAverage waiting time = {total_waiting_time / n:.2f}") print(f"Average turnaround time = {total_turnaround_time / n:.2f}") 
# Main code 
processes = [1, 2, 3, 4, 5] # Process IDs 
burst_time = [6, 2, 8, 3, 4] # Burst times for the processes n = len(processes) 
find_average_time(processes, n, burst_time)
