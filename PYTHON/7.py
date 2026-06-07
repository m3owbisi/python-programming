def first_fit(memory_blocks, processes):
    # Initialize allocation list with -1 (indicating no allocation)
    allocation = [-1] * len(processes)
    
    # Keep track of whether a block has been allocated
    allocated = [False] * len(memory_blocks)
    
    # Iterate through each process to find a suitable block
    for i, process in enumerate(processes):
        for j in range(len(memory_
        blocks)):
            if memory_blocks[j] >= process and not allocated[j]:  # Check if the block is large enough and not already allocated
                allocation[i] = j  # Assign the block to the process
                allocated[j] = True  # Mark this block as allocated
                break  # Move to the next process once allocated
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
allocation = first_fit(memory_blocks, processes)
print_allocation("First Fit", allocation)
            
