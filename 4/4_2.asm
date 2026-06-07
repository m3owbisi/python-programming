LXI H, 0001H  ; Load immediate value 0001H (hexadecimal 1) into the HL register pair (L gets 00, H gets 01)
DAD H         ; Add the value in register H (01) to the HL pair (add to both L and H)
HLT           ; Halt execution
