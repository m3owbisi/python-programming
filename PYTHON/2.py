def calculate_fcfs(requests, head):
    total_movement = 0
    current_position = head
    
    for request in requests:
        total_movement += abs(request - current_position)
        current_position = request
    
    return total_movement

# Example usage
requests = [98, 183, 41, 122, 14]
initial_head = 53

total_movement = calculate_fcfs(requests, initial_head)
print("Total Movement of Disk:", total_movement)