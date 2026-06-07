LXI H, 8050H  ; Load immediate 8050H into HL pair (source address)
MOV B, M       ; Move data from memory pointed to by HL to register B (load byte)
MOV A, B       ; Move byte from B to accumulator (duplicate for processing)
ANI 0FH       ; Mask accumulator with 0FH (keep only lower 4 bits)
INX H          ; Increment HL pair (move to next memory location)
MOV M, A       ; Store lower nibble (masked accumulator) in memory pointed to by HL
MOV A, B       ; Move byte from B to accumulator again (restore original value)
ANI F0H       ; Mask accumulator with F0H (keep only upper 4 bits)
RRC            ; Rotate accumulator right by 1 bit (shift upper nibble right)
RRC            ; Rotate accumulator right by 1 bit again (shift upper nibble right again)
RRC            ; Rotate accumulator right by 1 bit again (shift upper nibble right again)
RRC            ; Rotate accumulator right by 1 bit again (shift upper nibble right again)
INX H          ; Increment HL pair again (move to next memory location for upper nibble)
MOV M, A       ; Store upper nibble (shifted accumulator) in memory pointed to by HL
HLT            ; Halt execution
