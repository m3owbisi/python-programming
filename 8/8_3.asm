MVI D, 06H    ; Move immediate 06H to register D (exponent)
MVI B, 01H    ; Move immediate 01H to register B (initial value, 2)
loop: SHL B       ; Shift B left by 1 (multiply by 2)
       DCR D       ; Decrement counter D
       JNZ loop    ; Jump to loop if counter D is not zero
HLT           ; Halt execution
