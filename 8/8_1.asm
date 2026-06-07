LXI H, 8050H  ; Load immediate 8050H into HL pair (initialize pointer to memory location)
MVI C, 00H    ; Move immediate 00H to register C (initialize counter)
MVI B, 00H    ; Move immediate 00H to register B (initialize sum - low byte)
MVI E, 00H    ; Move immediate 00H to register E (initialize sum - high byte)
MVI D, 00H    ; Move immediate 00H to register D (initialize carry flag)

loop1: MOV A, M   ; Move data from memory pointed to by HL to accumulator
       CPI 00H  ; Compare accumulator with immediate 00H (check for zero)
       JZ zero   ; Jump if zero (skip negative numbers)
       ANI 80H  ; Mask accumulator with 80H (check for sign bit)
       JNZ neg   ; Jump if not zero (negative number)
       INR D     ; Increment carry flag (add 1 to carry)
       JMP loop2  ; Jump to loop2 (skip to next iteration)

zero:  INR E     ; Increment register E (add 1 to sum - high byte)
       JMP loop2  ; Jump to loop2

neg:   INR B     ; Increment register B (add 1 to sum - low byte)

loop2: INX H     ; Increment HL pair (move pointer to next memory location)
       INR C     ; Increment counter register C
       MOV A, C   ; Move counter value to accumulator
       CPI 0AH   ; Compare accumulator with immediate 0AH (check for 10 iterations)
       JNZ loop1  ; Jump if not zero (continue loop)

LXI H, 8070H  ; Load immediate 8070H into HL pair (set pointer to output memory)
MOV M, B       ; Move sum - low byte (register B) to memory pointed to by HL
INX H          ; Increment HL pair (move pointer to next memory location)
MOV M, E       ; Move sum - high byte (register E) to memory pointed to by HL
INX H          ; Increment HL pair (move pointer to next memory location)
MOV M, D       ; Move carry flag (register D) to memory pointed to by HL
HLT            ; Halt execution
