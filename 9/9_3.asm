LXI H, 8050H  ; Load immediate 8050H into HL pair (source address)
MOV E, M       ; Move data from memory pointed to by HL to register E (operand)
MVI D, 00H     ; Move immediate 00H to register D (initialize carry for multiplication)
INX H          ; Increment HL pair (move to next memory location - not used)
MOV A, M       ; Move data from memory pointed to by HL to accumulator (not used)
LXI H, 0000H  ; Load immediate 0000H into HL pair (accumulator for multiplication)
MVI B, 08H     ; Move immediate 08H to register B (loop counter)

loop2: DAD H       ; Add HL pair to itself (effectively multiplying by 2)
       RAL         ; Rotate accumulator left through carry flag (shift operand left)
       JNC loop1    ; Jump to loop1 if carry flag is not set (continue shifting)
       DAD D       ; Add carry flag (D) to HL pair (add operand to partial product)

loop1: DCR B       ; Decrement loop counter B
       JNZ loop2    ; Jump to loop2 if counter not zero (continue multiplication loop)

SHLD 8052H     ; Store low byte (BL) and high byte (BH) of HL in memory location 8052H (store result)
HLT            ; Halt execution
