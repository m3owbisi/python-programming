LXI SP, 8421H  ; Initialize stack pointer (not directly relevant to factorial calculation)
LDA 8050H     ; Load data from memory location 8050H to accumulator (number for factorial)
CPI 02H        ; Compare accumulator with 2 (check if value is less than 2)
JC loop1       ; Jump to loop1 if carry flag is set (value < 2)
MVI D, 00H     ; Move immediate 00H to D (initialize carry for multiplication)
MOV E, A       ; Move data from accumulator to E (preserve original value)
DCR A          ; Decrement accumulator (get the value for factorial)
MOV C, A       ; Move data from accumulator to C (operand for factorial calculation)
CALL FACTO    ; Call subroutine FACTO to calculate factorial
XCHG           ; Exchange registers B and C (result in B, operand in C)
SHLD 8051H     ; Store the low byte (BL) and high byte (BH) of B in memory location 8051H
JMP loop2      ; Jump to loop2 (program termination)

loop1: LXI H, 0001H ; Load immediate 01H into HL pair (set result to 1 for numbers < 2)
SHLD 8051H     ; Store the low byte (01H) and high byte (00H) of HL in memory location 8051H
loop2: HLT        ; Halt execution (program ends)
