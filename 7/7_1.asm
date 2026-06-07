LXI H, 8050H ; Load immediate value 8050H (hexadecimal 8050) into HL register pair (source address)
LXI D, 8070H ; Load immediate value 8070H (hexadecimal 8070) into DE register pair (destination address)
MVI C, 0AH   ; Load immediate value 0AH (hexadecimal 10) into register C (loop counter)

loop2:       ; Label for loop2 (outer loop)
    MOV A, M    ; Move the value from the memory location pointed to by HL to accumulator (A)
    ANI 01H    ; Perform a bitwise AND operation between A and 01H (hexadecimal 1)
    JNZ loop1   ; Jump to loop1 if the least significant bit (LSB) is 1 (odd value)

    MOV A, M    ; Move the value from the same memory location again (since we didn't jump to loop1)
    STAX D      ; Store the value from A into the memory location pointed to by DE (destination)
    INX D       ; Increment DE register pair by 1 (move to the next destination memory location)

loop1:       ; Label for loop1 (inner loop - not executed for even values)
    INX H       ; Increment HL register pair by 1 (move to the next source memory location)
    DCR C       ; Decrement register C by 1 (loop counter for outer loop)
    JNZ loop2   ; Jump to loop2 if C is not zero (continue outer loop)

HLT           ; Halt execution
