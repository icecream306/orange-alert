function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xf, 0xb]
    =================================
    0xa: JUMPI v8(0xf), v7

    Begin block 0xf
    prev=[0x0], succ=[0x18, 0xe6]
    =================================
    0xe1: JUMPI ve0(0xe6), v14

    Begin block 0x18
    prev=[0xf], succ=[0xe9, 0x28]
    =================================
    0x1a: v1a = CALLDATALOAD v18(0x0)
    0x1d: v1d = SHR v1b(0xe0), v1a
    0xe3: JUMPI ve2(0xe9), v24

    Begin block 0xe9
    prev=[0x18], succ=[]
    =================================
    0xeb: CALLPRIVATE vea(0x37)

    Begin block 0x28
    prev=[0x18], succ=[0xe6, 0xec]
    =================================
    0xe5: JUMPI ve4(0xec), v2e

    Begin block 0xe6
    prev=[0xf, 0x28], succ=[]
    =================================
    0xe8: CALLPRIVATE ve7(0x32)

    Begin block 0xec
    prev=[0x28], succ=[]
    =================================
    0xee: CALLPRIVATE ved(0x3f)

    Begin block 0xb
    prev=[0x0], succ=[]
    =================================
    0xe: REVERT vb(0x0), vb(0x0)

}

function fallback()() public {
    Begin block 0x32
    prev=[], succ=[]
    =================================
    0x36: REVERT v33(0x0), v33(0x0)

}

function begin()() public {
    Begin block 0x37
    prev=[], succ=[0x5b]
    =================================
    0x3c: JUMP v3a(0x5b)

    Begin block 0x5b
    prev=[0x37], succ=[0x6e]
    =================================
    0x62: JUMP v60(0x6e)

    Begin block 0x6e
    prev=[0x5b, 0x96], succ=[0x82]
    =================================
    0x6e_0x0: v6e_0 = PHI v5e(0x0), va3
    0x74: SSTORE v70(0x0), v6e_0
    0x7e: JUMP v7c(0x82)

    Begin block 0x82
    prev=[0x6e], succ=[0x96]
    =================================
    0x88: SSTORE v84(0x0), v7b
    0x92: JUMP v90(0x96)

    Begin block 0x96
    prev=[0x82], succ=[0x6e]
    =================================
    0x9c: SSTORE v98(0x0), v8f
    0xa6: JUMP va4(0x6e)

}

function retrieve()() public {
    Begin block 0x3f
    prev=[], succ=[0x65]
    =================================
    0x44: JUMP v42(0x65)

    Begin block 0x65
    prev=[0x3f], succ=[0x45]
    =================================
    0x69: v69 = SLOAD v66(0x0)
    0x6d: JUMP v40(0x45)

    Begin block 0x45
    prev=[0x65], succ=[]
    =================================
    0x5a: RETURN v55, v58(0x20)

}

