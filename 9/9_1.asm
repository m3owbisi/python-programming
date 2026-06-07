LXI H, 900EH  ; Load immediate 900EH into HL pair (source address)
LXI D, 9012H  ; Load immediate 9012H into DE pair (destination address - start)

loop1: MOV A, M   ; Move data from memory pointed to by HL to accumulator
       STAX D    ; Store accumulator in memory pointed to by DE
       DCX D      ; Decrement DE pair (move destination pointer)
       DCX H      ; Decrement HL pair (move source pointer)
       MOV A, L    ; Move low byte of HL pair to accumulator
       CPI 08H   ; Compare accumulator with 8 (check for 8 bytes copied)
       JNZ loop1  ; Jump to loop1 if not 8 bytes copied

INX H           ; Increment HL pair (move source pointer to next block)
LXI D, 9500H  ; Load immediate 9500H into DE pair (new destination address)

loop2: LDAX D    ; Load data from memory pointed to by DE to accumulator
       MOV M, A   ; Move accumulator to memory pointed to by HL (copy data)
       INX D      ; Increment DE pair (move destination pointer)
       INX H      ; Increment HL pair (move source pointer)
       MOV A, E    ; Move high byte of DE pair to accumulator
       CPI 04H   ; Compare accumulator with 4 (check for 4 blocks copied)
       JNZ loop2  ; Jump to loop2 if not 4 blocks copied

HLT            ; Halt execution
