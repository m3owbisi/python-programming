MVI E, 03H  ; Load immediate value 3 into register E
MVI D, 04H  ; Load immediate value 4 into register D
MVI A, 99H  ; Load immediate value 99 (decimal 153) into accumulator A
SUB E       ; Subtract the value in register E (3) from accumulator A
INR A       ; Increment the value in accumulator A by 1 (to handle potential borrow)
ADD D       ; Add the value in register D (4) to accumulator A
DAA          ; Decimal Adjust Accumulator (for BCD correction)
HLT         ; Halt execution
