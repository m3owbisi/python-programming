def worst_fit(memory_blocks, processes):
    # Initialize allocation list with -1 (indicating no allocation)
    allocation = [-1] * len(processes)
    
    # Keep track of whether a block has been allocated
    allocated = [False] * len(memory_blocks)
    
    # Iterate through each process to find the largest suitable block
    for i, process in enumerate(processes):
        # Find the index of the largest block that can accommodate the process and is not allocated
        worst_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process and not allocated[j]:
                if worst_idx == -1 or memory_blocks[j] > memory_blocks[worst_idx]:
                    worst_idx = j
        
        # If a suitable block is found, allocate it to the process
        if worst_idx != -1:
            allocation[i] = worst_idx
            allocated[worst_idx] = True  # Mark this block as allocated
    
    return allocation

def print_allocation(strategy, allocation):
    print(f"{strategy} Allocation:")
    for i, block in enumerate(allocation):
        if block != -1:
            print(f"Process {i + 1} -> Block {block + 1}")
        else:
            print(f"Process {i + 1} -> Not Allocated")
    print()

# Given memory blocks and processes
memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# Demonstrate allocations
allocation = worst_fit(memory_blocks, processes)
print_allocation("Worst Fit", allocation)

