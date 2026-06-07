def calculate_sstf(requests, head):
    total_movement = 0
    current_position = head
    remaining_requests = requests.copy()
    
    while remaining_requests:
        # Find the request closest to the current head position
        closest_request = min(remaining_requests, key=lambda x: abs(x - current_position))
        # Calculate the movement needed to reach that request
        total_movement += abs(closest_request - current_position)
        # Move the head to the closest request
        current_position = closest_request
        # Remove the serviced request
        remaining_requests.remove(closest_request)
    
    return total_movement

# Example usage
requests = [98, 183, 41, 122, 14]
initial_head = 53

total_movement = calculate_sstf(requests, initial_head)
print("Total Movement of Disk:", total_movement)

