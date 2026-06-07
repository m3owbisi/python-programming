LXI H, 8050H   ; Load immediate value 8050H (hexadecimal 8050) into HL register pair (L gets 80, H gets 50)
MVI B, 05H     ; Load immediate value 05H (hexadecimal 5) into register B (loop counter for loop1)
MVI C, 02H     ; Load immediate value 02H (hexadecimal 2) into register C (value to compare with memory data)

loop1:         ; Label for loop1
    MOV A, M    ; Move the value from memory location pointed to by HL to accumulator (A)
    CMP C       ; Compare the value in A with the value in register C
    JZ loop2    ; Jump to loop2 if accumulator (A) is zero (value in memory is equal to C)
    INX H      ; Increment HL register pair by 1 (move to the next memory location)
    DCR B      ; Decrement register B by 1 (loop counter)
    JNZ loop1   ; Jump to loop1 if B is not zero (continue looping)
    LXI H, 0000H   ; Load immediate value 0000H (hexadecimal 0) into HL register pair
    SHLD 8070H   ; Store the value in HL register pair into memory location 8070H
    JMP loop3    ; Unconditional jump to loop3 (exit)

loop2:         ; Label for loop2
    SHLD 8070H   ; Store the current value in HL register pair into memory location 8070H

loop3:         ; Label for loop3 (used for halting execution)
    HLT         ; Halt execution
