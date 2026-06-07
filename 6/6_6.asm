LXI H, 8050H ; Load immediate value 8050H (hexadecimal 8050) into HL register pair (source data)
LXI D, 8060H ; Load immediate value 8060H (hexadecimal 8060) into DE register pair (destination data)
LXI B, 8070H ; Load immediate value 8070H (hexadecimal 8070) into BC register pair (result storage)
STC           ; Set Carry flag
CMC           ; Complement Carry flag (effectively clearing it)

loop:         ; Label for loop

    LDAX D       ; Load the value from memory location pointed to by DE register pair (D) into accumulator (A)
    ADD M        ; Add the value from the memory location pointed to by HL register pair (H) to the accumulator (A)
    DAA          ; Decimal Adjust Accumulator (corrects BCD addition)
    STAX B       ; Store the result from accumulator (A) back into memory location pointed to by BC register pair (B)
    INX H        ; Increment HL register pair by 1 (move to the next source memory location)
    INX D        ; Increment DE register pair by 1 (move to the next destination memory location)
    INX B        ; Increment BC register pair by 1 (move to the next result storage location)
    MOV A, L     ; Move the lower byte of HL register pair (source address) to accumulator (A)
    CPI 06H      ; Compare the value in accumulator (A) with immediate value 06H (hexadecimal 6)
    JNZ loop     ; Jump to loop if the lower byte of HL is not equal to 6 (not the end of data)

HLT           ; Halt execution
