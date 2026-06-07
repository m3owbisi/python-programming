LXI H, 8050H  ; Load immediate 8050H into HL pair (source address)
MOV C, M       ; Move data from memory pointed to by HL to register C (get first byte)
DCR C          ; Decrement C (initialize counter for shifting)

loop1: MOV D, C   ; Move counter (C) to register D (temporary storage)

LXI H, 8051H  ; Load immediate 8051H into HL pair (destination address - start)

loop2: MOV A, M   ; Move data from memory pointed to by HL to accumulator
       INX H      ; Increment HL pair (move to next destination address)
       CMP M       ; Compare current data with next byte in memory
       JNC loop3    ; Jump to loop3 if values are equal (no shift needed)
       MOV B, M     ; Move next byte in memory to register B (store for later)
       MOV M, A     ; Move data from accumulator (current byte) to memory (overwrite next byte)
       DCX H      ; Decrement HL pair (point back to current byte)
       MOV M, B     ; Move stored byte (next byte) to current byte location (effectively shift)
       INX H      ; Increment HL pair (move to next destination address)

loop3: DCR D       ; Decrement counter (D)
       JNZ loop2    ; Jump to loop2 if counter not zero (continue shifting)

DCR C          ; Decrement original counter (C)
JNZ loop1       ; Jump to loop1 if counter not zero (continue processing next byte)

HLT            ; Halt execution
