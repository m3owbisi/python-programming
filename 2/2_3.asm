LXI H, 8050H ; Load immediate value 8050H into the HL register pair
MOV A, M     ; Move the value from memory location pointed to by HL to the accumulator (A)
INX H        ; Increment the HL register pair by 1 (point to the next memory location)
SUB M        ; Subtract the value from memory location pointed to by HL from the accumulator (A)
INX H        ; Increment the HL register pair by 1 (point to the next memory location)
MOV M, A     ; Move the value from the accumulator (A) to the memory location pointed to by HL
HLT          ; Halt execution
