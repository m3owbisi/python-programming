LDA 8050H ; Load the value from memory location 8050H into the accumulator (A)
MOV C, A  ; Move the value from accumulator (A) to register C (used for loop control)
XRA A     ; Perform a bitwise Exclusive OR (XOR) operation between A and itself (A becomes 0)

LXI H, 8051H ; Load immediate value 8051H (hexadecimal 8051) into the HL register pair (L gets 80, H gets 51)

loop1:       ; Label for loop 1
    CMP M      ; Compare the value in accumulator (A) (which is now 0) with the value from the memory location pointed to by HL
    JNC loop2  ; Jump if Not Carry flag is clear (i.e., if the memory value is less than or equal to 0) to loop2
    MOV A, M   ; Move the value from memory location pointed to by HL to the accumulator (A)

loop2:       ; Label for loop 2
    INX H      ; Increment the HL register pair by 1 (H increments first)
    DCR C      ; Decrement register C by 1
    JNZ loop1   ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop1
STA 8070H  ; Store the value from the accumulator (A) into memory location 8070H

HLT         ; Halt execution
