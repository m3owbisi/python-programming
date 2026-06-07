MVI D, 06H    ; Move immediate 06H to register D (initialize counter)
MVI B, 00H    ; Move immediate 00H to register B (initialize result)
MVI C, 01H    ; Move immediate 01H to register C (operand)
MOV A, B       ; Move B (result) to accumulator
loop: ADD B      ; Add B (result) to itself (effectively multiplying by 2)
       MOV B, C    ; Move operand (01H) to B (result)
       MOV C, A    ; Move previous result (after addition) to C
       DCR D       ; Decrement counter D
       JNZ loop    ; Jump to loop if counter D is not zero
HLT           ; Halt execution
