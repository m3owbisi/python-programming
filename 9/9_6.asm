MVI C, 0AH     ; Move immediate 0AH to register C (loop counter - 10)
LXI H, 8050H  ; Load immediate 8050H into HL pair (source address)
LXI D, 8070H  ; Load immediate 8070H into DE pair (destination address)

loop1: MOV A, M   ; Move data from memory pointed to by HL to accumulator
       STAX D    ; Store accumulator in memory pointed to by DE
       INX H      ; Increment HL pair (move to next source address)
       INX D      ; Increment DE pair (move to next destination address with a twist)
       DCR C      ; Decrement loop counter
       JNZ loop1    ; Jump to loop1 if counter not zero (continue copying)

HLT            ; Halt execution
