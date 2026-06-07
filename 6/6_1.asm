MVI B, 09H  ; Load immediate value 09H (hexadecimal 9) into register B (used for loop control)

start:        ; Label for the starting point
    LXI H, 8050H ; Load immediate value 8050H (hexadecimal 8050) into the HL register pair (L gets 80, H gets 50)
    MVI C, 09H  ; Load immediate value 09H (hexadecimal 9) into register C (used for loop control)

loop1:       ; Label for loop 1
    MOV A, M      ; Move the value from the memory location pointed to by HL to the accumulator (A)
    INX H        ; Increment the HL register pair by 1 (H increments first)
    CMP M        ; Compare the value in accumulator (A) with the value from the next memory location pointed to by HL
    JC loop2     ; Jump if Carry flag is set (i.e., if the next memory value is less than the current value) to loop2
    JZ loop2     ; Jump if Zero flag is set (i.e., if the next memory value is equal to the current value) to loop2
    MOV D, M      ; Move the value from the next memory location to register D (temporary storage)
    MOV M, A      ; Move the current value (from A) to the current memory location pointed to by HL (overwriting it)
    DCX H        ; Decrement the HL register pair by 1 (H decrements first, effectively going back one memory location)
    MOV M, D      ; Move the value from register D (which was the next memory value) to the previous memory location
    INX H        ; Increment the HL register pair by 1 (H increments first, pointing to the next memory location again)

loop2:       ; Label for loop 2
    DCR C        ; Decrement register C by 1
    JNZ loop1   ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop1
    DCR B        ; Decrement register B by 1
    JNZ start    ; Jump if Not Zero flag is clear (i.e., if B is not yet zero) to start

HLT         ; Halt execution
