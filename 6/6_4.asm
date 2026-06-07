LXI H, 8050H  ; Load immediate value 8050H (hexadecimal 8050) into the HL register pair (L gets 80, H gets 50)
MOV B, M       ; Move the value from the memory location pointed to by HL to register B
MOV C, M       ; Move the value from the same memory location (8050H) to register C (used for loop control)
MVI A, 00H     ; Load immediate value 00H (hexadecimal 0) into register A (used as an accumulator)

loop:           ; Label for loop
    ADD B        ; Add the value in register B to itself (effectively doubles B)
    DCR C        ; Decrement register C by 1
    JNZ loop     ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop
    INX H        ; Increment the HL register pair by 1 (H increments first)
    MOV M, A      ; Store the value from register A (which is 00H) to the memory location pointed to by HL

HLT            ; Halt execution
