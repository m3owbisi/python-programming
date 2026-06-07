LHLD 8050H    ; Load the 16-bit value from memory locations 8050H (L) and 8051H (H) into the HL register pair
LDA 8052H     ; Load the value from memory location 8052H into the accumulator (A)
MOV C, A       ; Move the value from accumulator (A) to register C
LXI D, 0000H   ; Load immediate value 0000H (hexadecimal 0) into the DE register pair (D gets 00, E gets 00)

loop1:
    MOV A, L      ; Move the value from register L to the accumulator (A)
    SUB C        ; Subtract the value in register C from the accumulator (A)
    MOV L, A      ; Move the result back to register L
    JNC loop2     ; Jump to loop2 if no carry occurred (i.e., subtraction didn't result in a negative value)
    DCR H        ; Decrement register H by 1 (borrow from the higher byte)
loop2:
    INX D        ; Increment the DE register pair by 1 (D increments first)
    MOV A, H      ; Move the value from register H to the accumulator (A)
    CPI 00H      ; Compare the value in the accumulator (A) with 00H
    JNZ loop1     ; Jump to loop1 if A is not zero
    MOV A, L      ; Move the value from register L to the accumulator (A)
    CMP C        ; Compare the value in the accumulator (A) with the value in register C
    JNC loop1     ; Jump to loop1 if A is still greater than or equal to C
SHLD 8072H     ; Store the HL pair (both L and H) into memory locations 8072H (L) and 8073H (H)
XCHG           ; Exchange the values in HL and DE register pairs
SHLD 8070H     ; Store the DE pair (now holding a modified value) into memory locations 8070H (L) and 8071H (H)
HLT            ; Halt execution
