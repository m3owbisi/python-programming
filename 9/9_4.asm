MVI E, 00H     ; Initialize register E to 0 (quotient)
LHLD 8050H     ; Load low byte (8050H) and high byte (8051H) into HL pair (dividend)
LDA 8052H     ; Load data from memory location 8052H (divisor) to accumulator
MOV B, A       ; Move divisor to register B
MVI C, 08H     ; Move immediate 8H to register C (loop counter, 8 iterations)

loop2: DAD H       ; Add HL pair to itself (shift dividend left by 1 bit)
       MOV A, E    ; Move quotient (initially 0) to accumulator
       RLC          ; Rotate accumulator left through carry flag (shift quotient left by 1 bit)
       MOV E, A    ; Store shifted quotient back to E
       MOV A, H    ; Move high byte of dividend to accumulator
       SUB B        ; Subtract divisor from high byte
       JC loop1      ; Jump to loop1 if carry flag is set (subtraction resulted in borrow)
       MOV H, A    ; Store result of subtraction in high byte of dividend (partial quotient)
       INR E        ; Increment quotient (effectively multiplying by 2)

loop1: DCR C       ; Decrement loop counter
       JNZ loop2    ; Jump to loop2 if counter not zero (continue division loop)

MOV A, E        ; Move final quotient to accumulator
STA 8053H     ; Store quotient in memory location 8053H
MOV A, H        ; Move high byte of dividend (remainder) to accumulator
STA 8054H     ; Store remainder in memory location 8054H
HLT            ; Halt execution
