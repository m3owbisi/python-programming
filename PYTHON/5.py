# Function to calculate waiting time, start time, finish time, and turnaround time for all processes 
def find_times(n, burst_time, start_time, finish_time, waiting_time, turnaround_time): for i in range(n): 
if i == 0: 
start_time[i] = 0 # Start time of the first process is 0 
else: 
start_time[i] = finish_time[i - 1] # Start time of the current process is the finish time of the previous process 
waiting_time[i] = start_time[i] # Waiting time is the start time since arrival time is 0 
finish_time[i] = start_time[i] + burst_time[i] # Finish time is start time + burst time 
turnaround_time[i] = finish_time[i] # Turnaround time is finish time since arrival time is 0 
# Function to calculate and print average times along with detailed process information 
def find_average_time(processes, n, burst_time): 
start_time = [0] * n 
finish_time = [0] * n 
waiting_time = [0] * n 
turnaround_time = [0] * n 
# Calculate times for each process 
find_times(n, burst_time, start_time, finish_time, waiting_time, turnaround_time) 
# Calculate total waiting time and turnaround time 
total_waiting_time = 0 
total_turnaround_time = 0 
print("Processes Arrival Time Burst Time Start Time Waiting Time Finish Time Turnaround Time") 
for i in range(n): 
total_waiting_time += waiting_time[i] 
total_turnaround_time += turnaround_time[i] 
print(f" {processes[i]} 0 {burst_time[i]} {start_time[i]} {waiting_time[i]} {finish_time[i]} {turnaround_time[i]}") 
# Calculate and print average waiting time and turnaround time print(f"\nAverage waiting time = {total_waiting_time / n:.2f}") print(f"Average turnaround time = {total_turnaround_time / n:.2f}") 
# Main code 
processes = [1, 2, 3, 4, 5] # Process IDs 
burst_time = [10, 5, 8, 6, 2] # Burst times for the processes n = len(processes) 
find_average_time(processes, n, burst_time) 
