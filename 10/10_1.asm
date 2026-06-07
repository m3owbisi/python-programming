LHLD 8050H  ; Load the 16-bit value from memory location 8050H into the HL register pair
XCHG        ; Exchange the contents of the H and L registers
LHLD 8052H  ; Load the 16-bit value from memory location 8052H into the HL register pair
MOV A, L    ; Move the low byte of the HL register pair (L) to the accumulator (A)
ADD E       ; Add the value in register E to the accumulator (A)
DAA          ; Decimal Adjust Accumulator (for BCD addition)
STA 8060H  ; Store the result (now a BCD number) in memory location 8060H
MOV A, H    ; Move the high byte of the HL register pair (H) to the accumulator (A)
ADC D       ; Add the value in register D with Carry (ADC) to the accumulator (A)
DAA          ; Decimal Adjust Accumulator (again, for BCD addition)
STA 8061H  ; Store the result (now a BCD number) in memory location 8061H
HLT         ; Halt execution
