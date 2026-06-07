LDA 8050H  ; Load the value from memory location 8050H into the accumulator (A)
MOV C, A    ; Move the value from accumulator (A) to register C
SUB A       ; Subtract the value in accumulator (A) from itself (A becomes 0)
LXI H, 8051H  ; Load immediate value 8051H (hexadecimal 8051) into the HL register pair (L gets 80, H gets 51)

loop:        ; Label for the loop
    ADD M      ; Add the value from the memory location pointed to by HL to the accumulator (A)
    INX H      ; Increment the HL register pair by 1 (H increments first)
    DCR C      ; Decrement register C by 1
    JNZ loop   ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop
STA 8070H  ; Store the value from the accumulator (A) into memory location 8070H

HLT         ; Halt execution
