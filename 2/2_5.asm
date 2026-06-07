LDA 8050H ; Load the value from memory location 8050H into the accumulator (A)
CMA       ; Complement the accumulator (A) - Invert all bits (0 becomes 1, 1 becomes 0)
STA 8051H ; Store the complemented value from the accumulator (A) into memory location 8051H
HLT       ; Halt execution
