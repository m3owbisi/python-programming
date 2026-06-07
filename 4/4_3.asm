MVI B, 00H  ; Load immediate value 00H (hexadecimal 0) into register B
MVI D, 06H  ; Load immediate value 06H (hexadecimal 6) into register D
MVI E, 08H  ; Load immediate value 08H (hexadecimal 8) into register E
MOV A, D    ; Move the value from register D (06H) to the accumulator (A)

loop2:        ; Label for loop 2
    RAR        ; Rotate the contents of accumulator (A) to the right by one bit (Carry flag receives the LSB)
    JNC loop1  ; Jump if Not Carry flag is clear (i.e., if the LSB of A was 0) to loop1
    INR B      ; Increment register B by 1

loop1:        ; Label for loop 1
    DCR E      ; Decrement register E by 1
    JNZ loop2  ; Jump if Not Zero flag is clear (i.e., if E is not yet zero) to loop2

HLT         ; Halt execution
