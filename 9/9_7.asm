MVI C, 00H     ; Move immediate 00H to register C (initialize to zero)
LXI H, 8060H  ; Load immediate 8060H into HL pair (source address)
MOV A, M       ; Move data from memory pointed to by HL to accumulator (load number)
MVI E, 01H     ; Move immediate 01H to register E (constant value 1)

loop1: SUB E      ; Subtract 1 from accumulator (check for sign)
       INR E       ; Increment E (restore subtracted value for next iteration)
       INR E       ; Increment E again (effectively add 2)
       INR C       ; Increment counter C
       CPI 00H     ; Compare accumulator with 0 (check for overflow)
       JNZ loop1    ; Jump to loop1 if overflow occurred (number was negative)
MOV A, C       ; Move counter (absolute value) to accumulator
STA 8061H     ; Store absolute value in memory location 8061H
HLT            ; Halt execution
