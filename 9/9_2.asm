LXI H, 805DH  ; Load 805DH into HL pair (source address)
LXI D, 8059H  ; Load 8059H into DE pair (destination address)

loop: MOV A, M   ; Move data from memory pointed to by HL to accumulator
       STAX D    ; Store accumulator in memory pointed to by DE
       INX D      ; Increment DE pair (next destination)
       INX H      ; Increment HL pair (next source)
       MOV A, L    ; Move low byte of HL pair to accumulator
       CPI 0FH     ; Compare accumulator with 0FH (check for 16 bytes)
       JNZ loop    ; Jump to loop if not 16 bytes copied

HLT            ; Halt execution
