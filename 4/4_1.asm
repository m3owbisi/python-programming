MVI C, FEH  ; Load immediate value FEH (hexadecimal FE) into register C
MOV A, C    ; Move the value from register C to the accumulator (A)
RAR         ; Rotate the contents of accumulator (A) to the right by one bit (Carry flag receives the LSB, MSB remains unchanged)
RAR         ; Perform right rotation again
RAR         ; Perform right rotation again
RAR         ; Perform right rotation again (total of four right rotations)
MOV C, A    ; Move the rotated value from the accumulator (A) back to register C
HLT         ; Halt execution
