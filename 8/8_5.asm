FACTO: LXI H, 0000H ; Initialize HL pair to 0 (accumulator for multiplication)
MOV B, C       ; Move operand from C to B (register for multiplication)
loop: DAD D        ; Add D (carry) to HL pair (repeated addition for multiplication)
      DCR B        ; Decrement B (multiplier)
      JNZ loop      ; Jump to loop if B is not zero (continue multiplication)
XCHG           ; Exchange registers B and C (result in B, operand in C)
DCR C          ; Decrement operand (C) (move to next number for factorial)
CNZ FACTO     ; Conditional jump to FACTO if C is not zero (calculate factorial for next number)
RET            ; Return from subroutine
