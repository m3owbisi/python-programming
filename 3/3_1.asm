LDA 8051H  ; Load the value from memory location 8051H into the accumulator (A)
RLC        ; Rotate the contents of accumulator (A) to the left by one bit (carry bit receives the MSB)
RLC        ; Perform left rotation again
RLC        ; Perform left rotation again
RLC        ; Perform left rotation again (total of four left rotations)
ANI F0H   ; Mask the lower nibble of the accumulator (A) with F0H (sets lower 4 bits to 0)
MOV C, A   ; Move the masked value from the accumulator (A) to register C
LDA 8050H  ; Load the value from memory location 8050H into the accumulator (A)
ADD C      ; Add the value from register C (masked value from 8051H) to the accumulator (A)
STA 8060H  ; Store the sum from the accumulator (A) into memory location 8060H
HLT        ; Halt execution
