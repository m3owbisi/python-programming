#Banker's Algorithm to find safe sequence
def is_safe(processes, available, max_need, allocation):
    n = len(processes)
    m = len(available)

    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_sequence = []
    work = available[:]

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    found = True
                    break

        if not found:
            print("System is not in a safe state.")
            return False, []

    print("System is in a safe state.")
    print("Safe sequence is:", safe_sequence)
    return True, safe_sequence

# Example usage:
processes = [0, 1, 2, 3, 4]

available = [3, 3, 2]  # Available resources

max_need = [
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3]   # P4
]

allocation = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2]   # P4
]

is_safe(processes, available, max_need, allocation)


