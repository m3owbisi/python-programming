MVI C, 0AH  ; Load immediate value 0AH (hexadecimal 10) into register C (loop counter)
LXI H, 8059H ; Load immediate value 8059H (hexadecimal 8059) into HL register pair (source address - starts at the end)
LXI D, 805FH ; Load immediate value 805FH (hexadecimal 805F) into DE register pair (destination address - starts at the end)

loop:       ; Label for loop
    MOV A, M    ; Move the value from the memory location pointed to by HL to accumulator (A)
    STAX D      ; Store the value from A into the memory location pointed to by DE (destination)
    DCX H       ; Decrement HL register pair by 1 (move to the previous source memory location)
    DCX D       ; Decrement DE register pair by 1 (move to the previous destination memory location)
    DCR C       ; Decrement register C by 1 (loop counter)
    JNZ loop   ; Jump to loop if C is not zero (continue copying)

HLT           ; Halt execution
