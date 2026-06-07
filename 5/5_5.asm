LDA 8050H  ; Load the value from memory location 8050H into the accumulator (A)
MOV C, A    ; Move the value from accumulator (A) to register C
MVI B, 00H  ; Load immediate value 00H (hexadecimal 0) into register B (used as a counter)
LXI H, 8051H  ; Load immediate value 8051H (hexadecimal 8051) into the HL register pair (L gets 80, H gets 51)

loop1:       ; Label for loop 1
    MOV A, M    ; Move the value from the memory location pointed to by HL to the accumulator (A)
    ANI 80H    ; Perform a bitwise AND operation between A and 80H (hexadecimal 128)
    JZ loop2   ; Jump if Zero flag is set (i.e., if the result of ANI is 0) to loop2
    INR B      ; Increment register B by 1

loop2:       ; Label for loop 2
    INX H      ; Increment the HL register pair by 1 (H increments first)
    DCR C      ; Decrement register C by 1
    JNZ loop1   ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop1
MOV A, B    ; Move the value from register B to the accumulator (A)
STA 8070H  ; Store the value from the accumulator (A) into memory location 8070H

HLT         ; Halt execution
