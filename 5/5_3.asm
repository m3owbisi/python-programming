LDA 8050H ; Load the value from memory location 8050H into the accumulator (A)
MOV E, A  ; Move the value from accumulator (A) to register E
MVI D, 00H ; Load immediate value 00H (hexadecimal 0) into register D

LDA 8051H ; Load the value from memory location 8051H into the accumulator (A)
MOV C, A  ; Move the value from accumulator (A) to register C

LXI H, 0000H ; Load immediate value 0000H (hexadecimal 0) into the HL register pair (L gets 00, H gets 00)

loop:       ; Label for the loop
    DAD D      ; Double Add with D (add the value in D to both L and H of the HL pair)
    DCR C      ; Decrement register C by 1
    JNZ loop   ; Jump if Not Zero flag is clear (i.e., if C is not yet zero) to loop
SHLD 8052H  ; Store the HL pair (both L and H) into memory location 8052H

HLT         ; Halt execution
