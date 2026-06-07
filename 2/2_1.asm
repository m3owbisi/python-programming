LXI H, 8050H ; Load immediate 8050h into HL register pair
MOV A, M ; Move the value from memory location pointed to by HL to the accumulator (A)
INX H ; Increment the HL register pair by 1 (point to the next memory location)
ADD M ; Add the value from the memory location pointed to by HL to the accumulator (A)
INX H ; Increment the HL register pair by 1 (point to the next memory location)
MOV M, A ; Move the value from the accumulator (A) to the memory location pointed to by HL
MVI A, 00H ; Move immediate value 00h (hexadecimal 0) to the accumulator (A)
ADC A ; Add the Carry flag (C) to the accumulator (A) and the value in A itself
INX H ; Increment the HL register pair by 1 (point to the next memory location)
MOV M, A ; Move the value from the accumulator (A) to the memory location pointed to by HL
HLT ; Halt execution
