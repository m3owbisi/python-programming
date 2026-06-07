LDA 8050H  ; Load the value from memory location 8050H into the accumulator (A)
MOV C, A    ; Move the value from accumulator (A) to register C
LXI H, 8051H  ; Load immediate value 8051H (hexadecimal 8051) into the HL register pair (L gets 80, H gets 51)
SUB A       ; Subtract the value in accumulator (A) from itself (A becomes 0)
MOV B, A    ; Move the value from accumulator (A) (which is now 0) to register B

loop2:       ; Label for loop 2
    ADD M      ; Add the value from the memory location pointed to by HL to the accumulator (A)
    JNC loop1  ; Jump if Not Carry flag is clear (i.e., if the MSB of the value in memory was 0) to loop1
    INR B      ; Increment register B by 1

loop1:       ; Label for loop 1
    INX H      ; Increment the HL register pair by 1 (H increments first)
    DCR C      ; Decrement register C by 1
    JNZ loop2   ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop2
STA 8070H  ; Store the value from the accumulator (A) into memory location 8070H
MOV A, B    ; Move the value from register B to the accumulator (A)
STA 8071H  ; Store the value from the accumulator (A) into memory location 8071H

HLT         ; Halt execution
