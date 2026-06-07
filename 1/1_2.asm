LDA 8030H   ; Load value from 8030H to A
MOV C, A    ; Save A's value in temporary register C
LDA 8050H   ; Load value from 8050H to A (overwrites original value)
STA 8030H   ; Store new value (from 8050H) back to 8030H
MOV A, C    ; Restore original value from 8030H (saved in C) to A
STA 8050H   ; Store original value (from 8030H) back to 8050H
HLT         ; Halt execution