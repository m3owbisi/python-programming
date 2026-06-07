LHLD 8050H  ; Load the contents of memory locations 8050H and 8051H into the HL pair (L gets 8050H, H gets 8051H)
XCHG       ; Exchange the contents of the accumulator (A) and the register E
LHLD 8052H  ; Load the contents of memory locations 8052H and 8053H into the HL pair (L gets 8052H, H gets 8053H)
MOV A, E    ; Move the value from register E to the accumulator (A)
SUB L       ; Subtract the value from register L from the accumulator (A)
MOV L, A    ; Move the result from the accumulator (A) back to register L
MOV A, D    ; Move the value from register D to the accumulator (A)
SBB H       ; Subtract the value from register H and the Borrow flag (B) from the accumulator (A)
MOV H, A    ; Move the result from the accumulator (A) back to register H
SHLD 8054H  ; Store the contents of the HL pair (H gets stored first) into memory locations 8054H and 8055H
HLT         ; Halt execution
