LDA 8050H  ; Load the value from memory location 8050H into the accumulator (A)
CMA       ; Complement the accumulator (A) - Invert all bits (0 becomes 1, 1 becomes 0)
ADI 01H   ; Add immediate value 01H to the accumulator (A) with Carry flag (C) considered
STA 8051H  ; Store the value from the accumulator (A) into memory location 8051H
HLT       ; Halt execution
