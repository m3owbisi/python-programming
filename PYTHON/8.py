memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
def best_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)  # Initialize allocation list with -1
    for i, process in enumerate(processes):
        best_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process and (best_index == -1 or memory_blocks[best_index] > memory_blocks[j]):
                best_index = j  # Find smallest block that fits
        if best_index != -1:
            allocation[i] = best_index  # Allocate block to process
            memory_blocks[best_index] -= process  # Reduce block size
    return allocation

def print_allocation(strategy, allocation):
    print(f"{strategy} Allocation:")
    for i, block in enumerate(allocation):
        if block != -1:
            print(f"Process {i + 1} -> Block {block + 1}")
        else:
            print(f"Process {i + 1} -> Not Allocated")
    print()

print_allocation("Best Fit", best_fit(memory_blocks[:], processes))

