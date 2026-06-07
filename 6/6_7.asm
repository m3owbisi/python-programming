LXI H, 8050H  ; Load immediate value 8050H (hexadecimal 8050) into HL register pair (L gets 80, H gets 50)
LXI B, 8060H  ; Load immediate value 8060H (hexadecimal 8060) into BC register pair (B gets 80, C gets 60)
LXI D, 8070H  ; Load immediate value 8070H (hexadecimal 8070) into DE register pair (D gets 80, E gets 70)

loop:         ; Label for loop
    LDAX B      ; Load the value from memory location pointed to by BC register pair (B) into accumulator (A)
    ADD M       ; Add the value from the memory location pointed to by HL register pair (H) to the accumulator (A)
    STAX D      ; Store the result from accumulator (A) into memory location pointed to by DE register pair (D)
    INX H       ; Increment HL register pair by 1 (move to the next source memory location)
    INX B       ; Increment BC register pair by 1 (move to the next intermediate memory location)
    INX D       ; Increment DE register pair by 1 (move to the next destination memory location)
    MOV A, L    ; Move the lower byte of HL register pair (source address) to accumulator (A)
    CPI 0AH     ; Compare the value in accumulator (A) with immediate value 0AH (hexadecimal 10)
    JNZ loop    ; Jump to loop if the lower byte of HL is not equal to 10 (not the end of data)

HLT           ; Halt execution
