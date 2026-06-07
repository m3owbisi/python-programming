LXI H, 8050H ; Load immediate value 8050H (hexadecimal 8050) into HL register pair (source/destination address)
MOV C, M     ; Move the value from the memory location pointed to by HL into register C (loop counter)

loop1:         ; Label for loop1
    INX H      ; Increment HL register pair by 1 (move to the next memory location)
    MOV A, M    ; Move the value from the current memory location pointed to by HL to accumulator (A)
    ORA A      ; Perform a bitwise OR operation between A and itself (effectively checking for zero)
    JPO loop2   ; Jump to loop2 if the Parity Flag (PF) is 1 (value is even)
    ORI 80H     ; Set the most significant bit (MSB) of A to 1 (making the value negative)

loop2:         ; Label for loop2
    MOV M, A    ; Store the modified value from A back into the memory location pointed to by HL
    DCR C       ; Decrement register C by 1 (loop counter)
    JNZ loop1   ; Jump to loop1 if C is not zero (continue processing more bytes)

HLT           ; Halt execution
