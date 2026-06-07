LDA 8050H ; Load the value from memory location 8050H into the accumulator (A)
ANI F0H   ; Mask the lower nibble of the accumulator (A) with F0H (sets lower 4 bits to 0)
RRC        ; Rotate the contents of accumulator (A) to the right by one bit (Carry flag receives the LSB)
RRC        ; Perform right rotation again
RRC        ; Perform right rotation again
RRC        ; Perform right rotation again (total of four right rotations)
STA 8061H  ; Store the value from the accumulator (A) into memory location 8061H
LDA 8050H ; Load the value from memory location 8050H again into the accumulator (A)
ANI 0FH   ; Mask the upper nibble of the accumulator (A) with 0FH (sets upper 4 bits to 0)
STA 8060H  ; Store the value from the accumulator (A) into memory location 8060H
HLT        ; Halt execution
