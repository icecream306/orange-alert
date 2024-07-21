function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x3250]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x3222: v3222(0x3250) = CONST 
    0x3223: JUMPI v3222(0x3250), v8

    Begin block 0xd
    prev=[0x0], succ=[0x3253, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x5d2035b) = CONST 
    0x3c: v3c = EQ v37(0x5d2035b), v35
    0x3224: v3224(0x3253) = CONST 
    0x3225: JUMPI v3224(0x3253), v3c

    Begin block 0x3253
    prev=[0xd], succ=[]
    =================================
    0x3254: v3254(0x137) = CONST 
    0x3255: CALLPRIVATE v3254(0x137)

    Begin block 0x41
    prev=[0xd], succ=[0x3256, 0x4c]
    =================================
    0x42: v42(0x6fdde03) = CONST 
    0x47: v47 = EQ v42(0x6fdde03), v35
    0x3226: v3226(0x3256) = CONST 
    0x3227: JUMPI v3226(0x3256), v47

    Begin block 0x3256
    prev=[0x41], succ=[]
    =================================
    0x3257: v3257(0x166) = CONST 
    0x3258: CALLPRIVATE v3257(0x166)

    Begin block 0x4c
    prev=[0x41], succ=[0x3259, 0x57]
    =================================
    0x4d: v4d(0x95ea7b3) = CONST 
    0x52: v52 = EQ v4d(0x95ea7b3), v35
    0x3228: v3228(0x3259) = CONST 
    0x3229: JUMPI v3228(0x3259), v52

    Begin block 0x3259
    prev=[0x4c], succ=[]
    =================================
    0x325a: v325a(0x1f6) = CONST 
    0x325b: CALLPRIVATE v325a(0x1f6)

    Begin block 0x57
    prev=[0x4c], succ=[0x325c, 0x62]
    =================================
    0x58: v58(0x18160ddd) = CONST 
    0x5d: v5d = EQ v58(0x18160ddd), v35
    0x322a: v322a(0x325c) = CONST 
    0x322b: JUMPI v322a(0x325c), v5d

    Begin block 0x325c
    prev=[0x57], succ=[]
    =================================
    0x325d: v325d(0x25b) = CONST 
    0x325e: CALLPRIVATE v325d(0x25b)

    Begin block 0x62
    prev=[0x57], succ=[0x325f, 0x6d]
    =================================
    0x63: v63(0x23b872dd) = CONST 
    0x68: v68 = EQ v63(0x23b872dd), v35
    0x322c: v322c(0x325f) = CONST 
    0x322d: JUMPI v322c(0x325f), v68

    Begin block 0x325f
    prev=[0x62], succ=[]
    =================================
    0x3260: v3260(0x286) = CONST 
    0x3261: CALLPRIVATE v3260(0x286)

    Begin block 0x6d
    prev=[0x62], succ=[0x3262, 0x78]
    =================================
    0x6e: v6e(0x27e235e3) = CONST 
    0x73: v73 = EQ v6e(0x27e235e3), v35
    0x322e: v322e(0x3262) = CONST 
    0x322f: JUMPI v322e(0x3262), v73

    Begin block 0x3262
    prev=[0x6d], succ=[]
    =================================
    0x3263: v3263(0x30b) = CONST 
    0x3264: CALLPRIVATE v3263(0x30b)

    Begin block 0x78
    prev=[0x6d], succ=[0x3265, 0x83]
    =================================
    0x79: v79(0x2853f925) = CONST 
    0x7e: v7e = EQ v79(0x2853f925), v35
    0x3230: v3230(0x3265) = CONST 
    0x3231: JUMPI v3230(0x3265), v7e

    Begin block 0x3265
    prev=[0x78], succ=[]
    =================================
    0x3266: v3266(0x362) = CONST 
    0x3267: CALLPRIVATE v3266(0x362)

    Begin block 0x83
    prev=[0x78], succ=[0x3268, 0x8e]
    =================================
    0x84: v84(0x313ce567) = CONST 
    0x89: v89 = EQ v84(0x313ce567), v35
    0x3232: v3232(0x3268) = CONST 
    0x3233: JUMPI v3232(0x3268), v89

    Begin block 0x3268
    prev=[0x83], succ=[]
    =================================
    0x3269: v3269(0x379) = CONST 
    0x326a: CALLPRIVATE v3269(0x379)

    Begin block 0x8e
    prev=[0x83], succ=[0x326b, 0x99]
    =================================
    0x8f: v8f(0x40c10f19) = CONST 
    0x94: v94 = EQ v8f(0x40c10f19), v35
    0x3234: v3234(0x326b) = CONST 
    0x3235: JUMPI v3234(0x326b), v94

    Begin block 0x326b
    prev=[0x8e], succ=[]
    =================================
    0x326c: v326c(0x3aa) = CONST 
    0x326d: CALLPRIVATE v326c(0x3aa)

    Begin block 0x99
    prev=[0x8e], succ=[0x326e, 0xa4]
    =================================
    0x9a: v9a(0x42966c68) = CONST 
    0x9f: v9f = EQ v9a(0x42966c68), v35
    0x3236: v3236(0x326e) = CONST 
    0x3237: JUMPI v3236(0x326e), v9f

    Begin block 0x326e
    prev=[0x99], succ=[]
    =================================
    0x326f: v326f(0x40f) = CONST 
    0x3270: CALLPRIVATE v326f(0x40f)

    Begin block 0xa4
    prev=[0x99], succ=[0x3271, 0xaf]
    =================================
    0xa5: va5(0x49dcf638) = CONST 
    0xaa: vaa = EQ va5(0x49dcf638), v35
    0x3238: v3238(0x3271) = CONST 
    0x3239: JUMPI v3238(0x3271), vaa

    Begin block 0x3271
    prev=[0xa4], succ=[]
    =================================
    0x3272: v3272(0x43c) = CONST 
    0x3273: CALLPRIVATE v3272(0x43c)

    Begin block 0xaf
    prev=[0xa4], succ=[0x3274, 0xba]
    =================================
    0xb0: vb0(0x66188463) = CONST 
    0xb5: vb5 = EQ vb0(0x66188463), v35
    0x323a: v323a(0x3274) = CONST 
    0x323b: JUMPI v323a(0x3274), vb5

    Begin block 0x3274
    prev=[0xaf], succ=[]
    =================================
    0x3275: v3275(0x4a7) = CONST 
    0x3276: CALLPRIVATE v3275(0x4a7)

    Begin block 0xba
    prev=[0xaf], succ=[0x3277, 0xc5]
    =================================
    0xbb: vbb(0x70a08231) = CONST 
    0xc0: vc0 = EQ vbb(0x70a08231), v35
    0x323c: v323c(0x3277) = CONST 
    0x323d: JUMPI v323c(0x3277), vc0

    Begin block 0x3277
    prev=[0xba], succ=[]
    =================================
    0x3278: v3278(0x50c) = CONST 
    0x3279: CALLPRIVATE v3278(0x50c)

    Begin block 0xc5
    prev=[0xba], succ=[0x327a, 0xd0]
    =================================
    0xc6: vc6(0x7d64bcb4) = CONST 
    0xcb: vcb = EQ vc6(0x7d64bcb4), v35
    0x323e: v323e(0x327a) = CONST 
    0x323f: JUMPI v323e(0x327a), vcb

    Begin block 0x327a
    prev=[0xc5], succ=[]
    =================================
    0x327b: v327b(0x563) = CONST 
    0x327c: CALLPRIVATE v327b(0x563)

    Begin block 0xd0
    prev=[0xc5], succ=[0x327d, 0xdb]
    =================================
    0xd1: vd1(0x8da5cb5b) = CONST 
    0xd6: vd6 = EQ vd1(0x8da5cb5b), v35
    0x3240: v3240(0x327d) = CONST 
    0x3241: JUMPI v3240(0x327d), vd6

    Begin block 0x327d
    prev=[0xd0], succ=[]
    =================================
    0x327e: v327e(0x592) = CONST 
    0x327f: CALLPRIVATE v327e(0x592)

    Begin block 0xdb
    prev=[0xd0], succ=[0x3280, 0xe6]
    =================================
    0xdc: vdc(0x95d89b41) = CONST 
    0xe1: ve1 = EQ vdc(0x95d89b41), v35
    0x3242: v3242(0x3280) = CONST 
    0x3243: JUMPI v3242(0x3280), ve1

    Begin block 0x3280
    prev=[0xdb], succ=[]
    =================================
    0x3281: v3281(0x5e9) = CONST 
    0x3282: CALLPRIVATE v3281(0x5e9)

    Begin block 0xe6
    prev=[0xdb], succ=[0x3283, 0xf1]
    =================================
    0xe7: ve7(0xa9059cbb) = CONST 
    0xec: vec = EQ ve7(0xa9059cbb), v35
    0x3244: v3244(0x3283) = CONST 
    0x3245: JUMPI v3244(0x3283), vec

    Begin block 0x3283
    prev=[0xe6], succ=[]
    =================================
    0x3284: v3284(0x679) = CONST 
    0x3285: CALLPRIVATE v3284(0x679)

    Begin block 0xf1
    prev=[0xe6], succ=[0x3286, 0xfc]
    =================================
    0xf2: vf2(0xbe45fd62) = CONST 
    0xf7: vf7 = EQ vf2(0xbe45fd62), v35
    0x3246: v3246(0x3286) = CONST 
    0x3247: JUMPI v3246(0x3286), vf7

    Begin block 0x3286
    prev=[0xf1], succ=[]
    =================================
    0x3287: v3287(0x6c6) = CONST 
    0x3288: CALLPRIVATE v3287(0x6c6)

    Begin block 0xfc
    prev=[0xf1], succ=[0x3289, 0x107]
    =================================
    0xfd: vfd(0xd73dd623) = CONST 
    0x102: v102 = EQ vfd(0xd73dd623), v35
    0x3248: v3248(0x3289) = CONST 
    0x3249: JUMPI v3248(0x3289), v102

    Begin block 0x3289
    prev=[0xfc], succ=[]
    =================================
    0x328a: v328a(0x759) = CONST 
    0x328b: CALLPRIVATE v328a(0x759)

    Begin block 0x107
    prev=[0xfc], succ=[0x328c, 0x112]
    =================================
    0x108: v108(0xdd62ed3e) = CONST 
    0x10d: v10d = EQ v108(0xdd62ed3e), v35
    0x324a: v324a(0x328c) = CONST 
    0x324b: JUMPI v324a(0x328c), v10d

    Begin block 0x328c
    prev=[0x107], succ=[]
    =================================
    0x328d: v328d(0x7be) = CONST 
    0x328e: CALLPRIVATE v328d(0x7be)

    Begin block 0x112
    prev=[0x107], succ=[0x328f, 0x11d]
    =================================
    0x113: v113(0xf2fde38b) = CONST 
    0x118: v118 = EQ v113(0xf2fde38b), v35
    0x324c: v324c(0x328f) = CONST 
    0x324d: JUMPI v324c(0x328f), v118

    Begin block 0x328f
    prev=[0x112], succ=[]
    =================================
    0x3290: v3290(0x835) = CONST 
    0x3291: CALLPRIVATE v3290(0x835)

    Begin block 0x11d
    prev=[0x112], succ=[0x3250, 0x3292]
    =================================
    0x11e: v11e(0xff6c33e6) = CONST 
    0x123: v123 = EQ v11e(0xff6c33e6), v35
    0x324e: v324e(0x3292) = CONST 
    0x324f: JUMPI v324e(0x3292), v123

    Begin block 0x3250
    prev=[0x0, 0x11d], succ=[]
    =================================
    0x3251: v3251(0x128) = CONST 
    0x3252: CALLPRIVATE v3251(0x128)

    Begin block 0x3292
    prev=[0x11d], succ=[]
    =================================
    0x3293: v3293(0x878) = CONST 
    0x3294: CALLPRIVATE v3293(0x878)

}

function fallback()() public {
    Begin block 0x128
    prev=[], succ=[0x130, 0x134]
    =================================
    0x129: v129 = CALLVALUE 
    0x12b: v12b = ISZERO v129
    0x12c: v12c(0x134) = CONST 
    0x12f: JUMPI v12c(0x134), v12b

    Begin block 0x130
    prev=[0x128], succ=[]
    =================================
    0x130: v130(0x0) = CONST 
    0x133: REVERT v130(0x0), v130(0x0)

    Begin block 0x134
    prev=[0x128], succ=[]
    =================================
    0x136: STOP 

}

function mintingFinished()() public {
    Begin block 0x137
    prev=[], succ=[0x13f, 0x143]
    =================================
    0x138: v138 = CALLVALUE 
    0x13a: v13a = ISZERO v138
    0x13b: v13b(0x143) = CONST 
    0x13e: JUMPI v13b(0x143), v13a

    Begin block 0x13f
    prev=[0x137], succ=[]
    =================================
    0x13f: v13f(0x0) = CONST 
    0x142: REVERT v13f(0x0), v13f(0x0)

    Begin block 0x143
    prev=[0x137], succ=[0x8cf]
    =================================
    0x145: v145(0x14c) = CONST 
    0x148: v148(0x8cf) = CONST 
    0x14b: JUMP v148(0x8cf)

    Begin block 0x8cf
    prev=[0x143], succ=[0x14c]
    =================================
    0x8d0: v8d0(0x0) = CONST 
    0x8d2: v8d2(0x14) = CONST 
    0x8d5: v8d5 = SLOAD v8d0(0x0)
    0x8d7: v8d7(0x100) = CONST 
    0x8da: v8da(0x10000000000000000000000000000000000000000) = EXP v8d7(0x100), v8d2(0x14)
    0x8dc: v8dc = DIV v8d5, v8da(0x10000000000000000000000000000000000000000)
    0x8dd: v8dd(0xff) = CONST 
    0x8df: v8df = AND v8dd(0xff), v8dc
    0x8e1: JUMP v145(0x14c)

    Begin block 0x14c
    prev=[0x8cf], succ=[]
    =================================
    0x14d: v14d(0x40) = CONST 
    0x14f: v14f = MLOAD v14d(0x40)
    0x152: v152 = ISZERO v8df
    0x153: v153 = ISZERO v152
    0x154: v154 = ISZERO v153
    0x155: v155 = ISZERO v154
    0x157: MSTORE v14f, v155
    0x158: v158(0x20) = CONST 
    0x15a: v15a = ADD v158(0x20), v14f
    0x15e: v15e(0x40) = CONST 
    0x160: v160 = MLOAD v15e(0x40)
    0x163: v163(0x20) = SUB v15a, v160
    0x165: RETURN v160, v163(0x20)

}

function name()() public {
    Begin block 0x166
    prev=[], succ=[0x16e, 0x172]
    =================================
    0x167: v167 = CALLVALUE 
    0x169: v169 = ISZERO v167
    0x16a: v16a(0x172) = CONST 
    0x16d: JUMPI v16a(0x172), v169

    Begin block 0x16e
    prev=[0x166], succ=[]
    =================================
    0x16e: v16e(0x0) = CONST 
    0x171: REVERT v16e(0x0), v16e(0x0)

    Begin block 0x172
    prev=[0x166], succ=[0x8e2]
    =================================
    0x174: v174(0x17b) = CONST 
    0x177: v177(0x8e2) = CONST 
    0x17a: JUMP v177(0x8e2)

    Begin block 0x8e2
    prev=[0x172], succ=[0x17b]
    =================================
    0x8e3: v8e3(0x60) = CONST 
    0x8e5: v8e5(0x40) = CONST 
    0x8e8: v8e8 = MLOAD v8e5(0x40)
    0x8eb: v8eb = ADD v8e8, v8e5(0x40)
    0x8ec: v8ec(0x40) = CONST 
    0x8ee: MSTORE v8ec(0x40), v8eb
    0x8f0: v8f0(0x8) = CONST 
    0x8f3: MSTORE v8e8, v8f0(0x8)
    0x8f4: v8f4(0x20) = CONST 
    0x8f6: v8f6 = ADD v8f4(0x20), v8e8
    0x8f7: v8f7(0x594f55546f6b656e000000000000000000000000000000000000000000000000) = CONST 
    0x919: MSTORE v8f6, v8f7(0x594f55546f6b656e000000000000000000000000000000000000000000000000)
    0x91e: JUMP v174(0x17b)

    Begin block 0x17b
    prev=[0x8e2], succ=[0x1a0]
    =================================
    0x17c: v17c(0x40) = CONST 
    0x17e: v17e = MLOAD v17c(0x40)
    0x181: v181(0x20) = CONST 
    0x183: v183 = ADD v181(0x20), v17e
    0x186: v186(0x20) = SUB v183, v17e
    0x188: MSTORE v17e, v186(0x20)
    0x18c: v18c(0x8) = MLOAD v8e8
    0x18e: MSTORE v183, v18c(0x8)
    0x18f: v18f(0x20) = CONST 
    0x191: v191 = ADD v18f(0x20), v183
    0x195: v195(0x8) = MLOAD v8e8
    0x197: v197(0x20) = CONST 
    0x199: v199 = ADD v197(0x20), v8e8
    0x19e: v19e(0x0) = CONST 

    Begin block 0x1a0
    prev=[0x17b, 0x1a9], succ=[0x1bb, 0x1a9]
    =================================
    0x1a0_0x0: v1a0_0 = PHI v19e(0x0), v1b4
    0x1a3: v1a3 = LT v1a0_0, v195(0x8)
    0x1a4: v1a4 = ISZERO v1a3
    0x1a5: v1a5(0x1bb) = CONST 
    0x1a8: JUMPI v1a5(0x1bb), v1a4

    Begin block 0x1bb
    prev=[0x1a0], succ=[0x1e8, 0x1cf]
    =================================
    0x1c4: v1c4 = ADD v195(0x8), v191
    0x1c6: v1c6(0x1f) = CONST 
    0x1c8: v1c8(0x8) = AND v1c6(0x1f), v195(0x8)
    0x1ca: v1ca(0x0) = ISZERO v1c8(0x8)
    0x1cb: v1cb(0x1e8) = CONST 
    0x1ce: JUMPI v1cb(0x1e8), v1ca(0x0)

    Begin block 0x1e8
    prev=[0x1bb, 0x1cf], succ=[]
    =================================
    0x1e8_0x1: v1e8_1 = PHI v1c4, v1e5
    0x1ee: v1ee(0x40) = CONST 
    0x1f0: v1f0 = MLOAD v1ee(0x40)
    0x1f3: v1f3 = SUB v1e8_1, v1f0
    0x1f5: RETURN v1f0, v1f3

    Begin block 0x1cf
    prev=[0x1bb], succ=[0x1e8]
    =================================
    0x1d1: v1d1 = SUB v1c4, v1c8(0x8)
    0x1d3: v1d3 = MLOAD v1d1
    0x1d4: v1d4(0x1) = CONST 
    0x1d7: v1d7(0x20) = CONST 
    0x1d9: v1d9(0x18) = SUB v1d7(0x20), v1c8(0x8)
    0x1da: v1da(0x100) = CONST 
    0x1dd: v1dd(0x1000000000000000000000000000000000000000000000000) = EXP v1da(0x100), v1d9(0x18)
    0x1de: v1de(0xffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1dd(0x1000000000000000000000000000000000000000000000000), v1d4(0x1)
    0x1df: v1df(0xffffffffffffffff000000000000000000000000000000000000000000000000) = NOT v1de(0xffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1e0: v1e0 = AND v1df(0xffffffffffffffff000000000000000000000000000000000000000000000000), v1d3
    0x1e2: MSTORE v1d1, v1e0
    0x1e3: v1e3(0x20) = CONST 
    0x1e5: v1e5 = ADD v1e3(0x20), v1d1

    Begin block 0x1a9
    prev=[0x1a0], succ=[0x1a0]
    =================================
    0x1a9_0x0: v1a9_0 = PHI v19e(0x0), v1b4
    0x1ab: v1ab = ADD v199, v1a9_0
    0x1ac: v1ac = MLOAD v1ab
    0x1af: v1af = ADD v191, v1a9_0
    0x1b0: MSTORE v1af, v1ac
    0x1b1: v1b1(0x20) = CONST 
    0x1b4: v1b4 = ADD v1a9_0, v1b1(0x20)
    0x1b7: v1b7(0x1a0) = CONST 
    0x1ba: JUMP v1b7(0x1a0)

}

function approve(address,uint256)() public {
    Begin block 0x1f6
    prev=[], succ=[0x1fe, 0x202]
    =================================
    0x1f7: v1f7 = CALLVALUE 
    0x1f9: v1f9 = ISZERO v1f7
    0x1fa: v1fa(0x202) = CONST 
    0x1fd: JUMPI v1fa(0x202), v1f9

    Begin block 0x1fe
    prev=[0x1f6], succ=[]
    =================================
    0x1fe: v1fe(0x0) = CONST 
    0x201: REVERT v1fe(0x0), v1fe(0x0)

    Begin block 0x202
    prev=[0x1f6], succ=[0x91f]
    =================================
    0x204: v204(0x241) = CONST 
    0x207: v207(0x4) = CONST 
    0x20a: v20a = CALLDATASIZE 
    0x20b: v20b = SUB v20a, v207(0x4)
    0x20d: v20d = ADD v207(0x4), v20b
    0x211: v211 = CALLDATALOAD v207(0x4)
    0x212: v212(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x227: v227 = AND v212(0xffffffffffffffffffffffffffffffffffffffff), v211
    0x229: v229(0x20) = CONST 
    0x22b: v22b(0x24) = ADD v229(0x20), v207(0x4)
    0x231: v231 = CALLDATALOAD v22b(0x24)
    0x233: v233(0x20) = CONST 
    0x235: v235(0x44) = ADD v233(0x20), v22b(0x24)
    0x23d: v23d(0x91f) = CONST 
    0x240: JUMP v23d(0x91f)

    Begin block 0x91f
    prev=[0x202], succ=[0x96b, 0x96f]
    =================================
    0x920: v920(0x0) = CONST 
    0x922: v922(0x3) = CONST 
    0x924: v924(0x0) = CONST 
    0x926: v926 = CALLER 
    0x927: v927(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x93c: v93c = AND v927(0xffffffffffffffffffffffffffffffffffffffff), v926
    0x93d: v93d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x952: v952 = AND v93d(0xffffffffffffffffffffffffffffffffffffffff), v93c
    0x954: MSTORE v924(0x0), v952
    0x955: v955(0x20) = CONST 
    0x957: v957(0x20) = ADD v955(0x20), v924(0x0)
    0x95a: MSTORE v957(0x20), v922(0x3)
    0x95b: v95b(0x20) = CONST 
    0x95d: v95d(0x40) = ADD v95b(0x20), v957(0x20)
    0x95e: v95e(0x0) = CONST 
    0x960: v960 = SHA3 v95e(0x0), v95d(0x40)
    0x961: v961 = SLOAD v960
    0x963: v963 = GT v231, v961
    0x964: v964 = ISZERO v963
    0x965: v965 = ISZERO v964
    0x966: v966 = ISZERO v965
    0x967: v967(0x96f) = CONST 
    0x96a: JUMPI v967(0x96f), v966

    Begin block 0x96b
    prev=[0x91f], succ=[]
    =================================
    0x96b: v96b(0x0) = CONST 
    0x96e: REVERT v96b(0x0), v96b(0x0)

    Begin block 0x96f
    prev=[0x91f], succ=[0x241]
    =================================
    0x971: v971(0x4) = CONST 
    0x973: v973(0x0) = CONST 
    0x975: v975 = CALLER 
    0x976: v976(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x98b: v98b = AND v976(0xffffffffffffffffffffffffffffffffffffffff), v975
    0x98c: v98c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9a1: v9a1 = AND v98c(0xffffffffffffffffffffffffffffffffffffffff), v98b
    0x9a3: MSTORE v973(0x0), v9a1
    0x9a4: v9a4(0x20) = CONST 
    0x9a6: v9a6(0x20) = ADD v9a4(0x20), v973(0x0)
    0x9a9: MSTORE v9a6(0x20), v971(0x4)
    0x9aa: v9aa(0x20) = CONST 
    0x9ac: v9ac(0x40) = ADD v9aa(0x20), v9a6(0x20)
    0x9ad: v9ad(0x0) = CONST 
    0x9af: v9af = SHA3 v9ad(0x0), v9ac(0x40)
    0x9b0: v9b0(0x0) = CONST 
    0x9b3: v9b3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9c8: v9c8 = AND v9b3(0xffffffffffffffffffffffffffffffffffffffff), v227
    0x9c9: v9c9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9de: v9de = AND v9c9(0xffffffffffffffffffffffffffffffffffffffff), v9c8
    0x9e0: MSTORE v9b0(0x0), v9de
    0x9e1: v9e1(0x20) = CONST 
    0x9e3: v9e3(0x20) = ADD v9e1(0x20), v9b0(0x0)
    0x9e6: MSTORE v9e3(0x20), v9af
    0x9e7: v9e7(0x20) = CONST 
    0x9e9: v9e9(0x40) = ADD v9e7(0x20), v9e3(0x20)
    0x9ea: v9ea(0x0) = CONST 
    0x9ec: v9ec = SHA3 v9ea(0x0), v9e9(0x40)
    0x9ef: SSTORE v9ec, v231
    0x9f2: v9f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa07: va07 = AND v9f2(0xffffffffffffffffffffffffffffffffffffffff), v227
    0xa08: va08 = CALLER 
    0xa09: va09(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa1e: va1e = AND va09(0xffffffffffffffffffffffffffffffffffffffff), va08
    0xa1f: va1f(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xa41: va41(0x40) = CONST 
    0xa43: va43 = MLOAD va41(0x40)
    0xa47: MSTORE va43, v231
    0xa48: va48(0x20) = CONST 
    0xa4a: va4a = ADD va48(0x20), va43
    0xa4e: va4e(0x40) = CONST 
    0xa50: va50 = MLOAD va4e(0x40)
    0xa53: va53(0x20) = SUB va4a, va50
    0xa55: LOG3 va50, va53(0x20), va1f(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), va1e, va07
    0xa56: va56(0x1) = CONST 
    0xa5e: JUMP v204(0x241)

    Begin block 0x241
    prev=[0x96f], succ=[]
    =================================
    0x242: v242(0x40) = CONST 
    0x244: v244 = MLOAD v242(0x40)
    0x247: v247(0x0) = ISZERO va56(0x1)
    0x248: v248(0x1) = ISZERO v247(0x0)
    0x249: v249(0x0) = ISZERO v248(0x1)
    0x24a: v24a(0x1) = ISZERO v249(0x0)
    0x24c: MSTORE v244, v24a(0x1)
    0x24d: v24d(0x20) = CONST 
    0x24f: v24f = ADD v24d(0x20), v244
    0x253: v253(0x40) = CONST 
    0x255: v255 = MLOAD v253(0x40)
    0x258: v258(0x20) = SUB v24f, v255
    0x25a: RETURN v255, v258(0x20)

}

function totalSupply()() public {
    Begin block 0x25b
    prev=[], succ=[0x263, 0x267]
    =================================
    0x25c: v25c = CALLVALUE 
    0x25e: v25e = ISZERO v25c
    0x25f: v25f(0x267) = CONST 
    0x262: JUMPI v25f(0x267), v25e

    Begin block 0x263
    prev=[0x25b], succ=[]
    =================================
    0x263: v263(0x0) = CONST 
    0x266: REVERT v263(0x0), v263(0x0)

    Begin block 0x267
    prev=[0x25b], succ=[0xa5f]
    =================================
    0x269: v269(0x270) = CONST 
    0x26c: v26c(0xa5f) = CONST 
    0x26f: JUMP v26c(0xa5f)

    Begin block 0xa5f
    prev=[0x267], succ=[0x270]
    =================================
    0xa60: va60(0x2) = CONST 
    0xa62: va62 = SLOAD va60(0x2)
    0xa64: JUMP v269(0x270)

    Begin block 0x270
    prev=[0xa5f], succ=[]
    =================================
    0x271: v271(0x40) = CONST 
    0x273: v273 = MLOAD v271(0x40)
    0x277: MSTORE v273, va62
    0x278: v278(0x20) = CONST 
    0x27a: v27a = ADD v278(0x20), v273
    0x27e: v27e(0x40) = CONST 
    0x280: v280 = MLOAD v27e(0x40)
    0x283: v283(0x20) = SUB v27a, v280
    0x285: RETURN v280, v283(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x286
    prev=[], succ=[0x28e, 0x292]
    =================================
    0x287: v287 = CALLVALUE 
    0x289: v289 = ISZERO v287
    0x28a: v28a(0x292) = CONST 
    0x28d: JUMPI v28a(0x292), v289

    Begin block 0x28e
    prev=[0x286], succ=[]
    =================================
    0x28e: v28e(0x0) = CONST 
    0x291: REVERT v28e(0x0), v28e(0x0)

    Begin block 0x292
    prev=[0x286], succ=[0xa65]
    =================================
    0x294: v294(0x2f1) = CONST 
    0x297: v297(0x4) = CONST 
    0x29a: v29a = CALLDATASIZE 
    0x29b: v29b = SUB v29a, v297(0x4)
    0x29d: v29d = ADD v297(0x4), v29b
    0x2a1: v2a1 = CALLDATALOAD v297(0x4)
    0x2a2: v2a2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b7: v2b7 = AND v2a2(0xffffffffffffffffffffffffffffffffffffffff), v2a1
    0x2b9: v2b9(0x20) = CONST 
    0x2bb: v2bb(0x24) = ADD v2b9(0x20), v297(0x4)
    0x2c1: v2c1 = CALLDATALOAD v2bb(0x24)
    0x2c2: v2c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d7: v2d7 = AND v2c2(0xffffffffffffffffffffffffffffffffffffffff), v2c1
    0x2d9: v2d9(0x20) = CONST 
    0x2db: v2db(0x44) = ADD v2d9(0x20), v2bb(0x24)
    0x2e1: v2e1 = CALLDATALOAD v2db(0x44)
    0x2e3: v2e3(0x20) = CONST 
    0x2e5: v2e5(0x64) = ADD v2e3(0x20), v2db(0x44)
    0x2ed: v2ed(0xa65) = CONST 
    0x2f0: JUMP v2ed(0xa65)

    Begin block 0xa65
    prev=[0x292], succ=[0xaa1, 0xaa5]
    =================================
    0xa66: va66(0x0) = CONST 
    0xa68: va68(0x60) = CONST 
    0xa6a: va6a(0x0) = CONST 
    0xa6c: va6c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa81: va81(0x0) = AND va6c(0xffffffffffffffffffffffffffffffffffffffff), va6a(0x0)
    0xa83: va83(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa98: va98 = AND va83(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xa99: va99 = EQ va98, va81(0x0)
    0xa9a: va9a = ISZERO va99
    0xa9b: va9b = ISZERO va9a
    0xa9c: va9c = ISZERO va9b
    0xa9d: va9d(0xaa5) = CONST 
    0xaa0: JUMPI va9d(0xaa5), va9c

    Begin block 0xaa1
    prev=[0xa65], succ=[]
    =================================
    0xaa1: vaa1(0x0) = CONST 
    0xaa4: REVERT vaa1(0x0), vaa1(0x0)

    Begin block 0xaa5
    prev=[0xa65], succ=[0xadd, 0xae1]
    =================================
    0xaa6: vaa6(0x0) = CONST 
    0xaa8: vaa8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xabd: vabd(0x0) = AND vaa8(0xffffffffffffffffffffffffffffffffffffffff), vaa6(0x0)
    0xabf: vabf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xad4: vad4 = AND vabf(0xffffffffffffffffffffffffffffffffffffffff), v2d7
    0xad5: vad5 = EQ vad4, vabd(0x0)
    0xad6: vad6 = ISZERO vad5
    0xad7: vad7 = ISZERO vad6
    0xad8: vad8 = ISZERO vad7
    0xad9: vad9(0xae1) = CONST 
    0xadc: JUMPI vad9(0xae1), vad8

    Begin block 0xadd
    prev=[0xaa5], succ=[]
    =================================
    0xadd: vadd(0x0) = CONST 
    0xae0: REVERT vadd(0x0), vadd(0x0)

    Begin block 0xae1
    prev=[0xaa5], succ=[0xb2b, 0xb2f]
    =================================
    0xae2: vae2(0x3) = CONST 
    0xae4: vae4(0x0) = CONST 
    0xae7: vae7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xafc: vafc = AND vae7(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xafd: vafd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb12: vb12 = AND vafd(0xffffffffffffffffffffffffffffffffffffffff), vafc
    0xb14: MSTORE vae4(0x0), vb12
    0xb15: vb15(0x20) = CONST 
    0xb17: vb17(0x20) = ADD vb15(0x20), vae4(0x0)
    0xb1a: MSTORE vb17(0x20), vae2(0x3)
    0xb1b: vb1b(0x20) = CONST 
    0xb1d: vb1d(0x40) = ADD vb1b(0x20), vb17(0x20)
    0xb1e: vb1e(0x0) = CONST 
    0xb20: vb20 = SHA3 vb1e(0x0), vb1d(0x40)
    0xb21: vb21 = SLOAD vb20
    0xb23: vb23 = GT v2e1, vb21
    0xb24: vb24 = ISZERO vb23
    0xb25: vb25 = ISZERO vb24
    0xb26: vb26 = ISZERO vb25
    0xb27: vb27(0xb2f) = CONST 
    0xb2a: JUMPI vb27(0xb2f), vb26

    Begin block 0xb2b
    prev=[0xae1], succ=[]
    =================================
    0xb2b: vb2b(0x0) = CONST 
    0xb2e: REVERT vb2b(0x0), vb2b(0x0)

    Begin block 0xb2f
    prev=[0xae1], succ=[0xbb6, 0xbba]
    =================================
    0xb30: vb30(0x4) = CONST 
    0xb32: vb32(0x0) = CONST 
    0xb35: vb35(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb4a: vb4a = AND vb35(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xb4b: vb4b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb60: vb60 = AND vb4b(0xffffffffffffffffffffffffffffffffffffffff), vb4a
    0xb62: MSTORE vb32(0x0), vb60
    0xb63: vb63(0x20) = CONST 
    0xb65: vb65(0x20) = ADD vb63(0x20), vb32(0x0)
    0xb68: MSTORE vb65(0x20), vb30(0x4)
    0xb69: vb69(0x20) = CONST 
    0xb6b: vb6b(0x40) = ADD vb69(0x20), vb65(0x20)
    0xb6c: vb6c(0x0) = CONST 
    0xb6e: vb6e = SHA3 vb6c(0x0), vb6b(0x40)
    0xb6f: vb6f(0x0) = CONST 
    0xb71: vb71 = CALLER 
    0xb72: vb72(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb87: vb87 = AND vb72(0xffffffffffffffffffffffffffffffffffffffff), vb71
    0xb88: vb88(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb9d: vb9d = AND vb88(0xffffffffffffffffffffffffffffffffffffffff), vb87
    0xb9f: MSTORE vb6f(0x0), vb9d
    0xba0: vba0(0x20) = CONST 
    0xba2: vba2(0x20) = ADD vba0(0x20), vb6f(0x0)
    0xba5: MSTORE vba2(0x20), vb6e
    0xba6: vba6(0x20) = CONST 
    0xba8: vba8(0x40) = ADD vba6(0x20), vba2(0x20)
    0xba9: vba9(0x0) = CONST 
    0xbab: vbab = SHA3 vba9(0x0), vba8(0x40)
    0xbac: vbac = SLOAD vbab
    0xbae: vbae = GT v2e1, vbac
    0xbaf: vbaf = ISZERO vbae
    0xbb0: vbb0 = ISZERO vbaf
    0xbb1: vbb1 = ISZERO vbb0
    0xbb2: vbb2(0xbba) = CONST 
    0xbb5: JUMPI vbb2(0xbba), vbb1

    Begin block 0xbb6
    prev=[0xb2f], succ=[]
    =================================
    0xbb6: vbb6(0x0) = CONST 
    0xbb9: REVERT vbb6(0x0), vbb6(0x0)

    Begin block 0xbba
    prev=[0xb2f], succ=[0xc0c]
    =================================
    0xbbb: vbbb(0xc0c) = CONST 
    0xbbf: vbbf(0x3) = CONST 
    0xbc1: vbc1(0x0) = CONST 
    0xbc4: vbc4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbd9: vbd9 = AND vbc4(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xbda: vbda(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbef: vbef = AND vbda(0xffffffffffffffffffffffffffffffffffffffff), vbd9
    0xbf1: MSTORE vbc1(0x0), vbef
    0xbf2: vbf2(0x20) = CONST 
    0xbf4: vbf4(0x20) = ADD vbf2(0x20), vbc1(0x0)
    0xbf7: MSTORE vbf4(0x20), vbbf(0x3)
    0xbf8: vbf8(0x20) = CONST 
    0xbfa: vbfa(0x40) = ADD vbf8(0x20), vbf4(0x20)
    0xbfb: vbfb(0x0) = CONST 
    0xbfd: vbfd = SHA3 vbfb(0x0), vbfa(0x40)
    0xbfe: vbfe = SLOAD vbfd
    0xbff: vbff(0x31bf) = CONST 
    0xc05: vc05(0xffffffff) = CONST 
    0xc0a: vc0a(0x31bf) = AND vc05(0xffffffff), vbff(0x31bf)
    0xc0b: vc0b_0 = CALLPRIVATE vc0a(0x31bf), v2e1, vbfe, vbbb(0xc0c)

    Begin block 0xc0c
    prev=[0xbba], succ=[0xca1]
    =================================
    0xc0d: vc0d(0x3) = CONST 
    0xc0f: vc0f(0x0) = CONST 
    0xc12: vc12(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc27: vc27 = AND vc12(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xc28: vc28(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc3d: vc3d = AND vc28(0xffffffffffffffffffffffffffffffffffffffff), vc27
    0xc3f: MSTORE vc0f(0x0), vc3d
    0xc40: vc40(0x20) = CONST 
    0xc42: vc42(0x20) = ADD vc40(0x20), vc0f(0x0)
    0xc45: MSTORE vc42(0x20), vc0d(0x3)
    0xc46: vc46(0x20) = CONST 
    0xc48: vc48(0x40) = ADD vc46(0x20), vc42(0x20)
    0xc49: vc49(0x0) = CONST 
    0xc4b: vc4b = SHA3 vc49(0x0), vc48(0x40)
    0xc4e: SSTORE vc4b, vc0b_0
    0xc50: vc50(0xca1) = CONST 
    0xc54: vc54(0x3) = CONST 
    0xc56: vc56(0x0) = CONST 
    0xc59: vc59(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc6e: vc6e = AND vc59(0xffffffffffffffffffffffffffffffffffffffff), v2d7
    0xc6f: vc6f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc84: vc84 = AND vc6f(0xffffffffffffffffffffffffffffffffffffffff), vc6e
    0xc86: MSTORE vc56(0x0), vc84
    0xc87: vc87(0x20) = CONST 
    0xc89: vc89(0x20) = ADD vc87(0x20), vc56(0x0)
    0xc8c: MSTORE vc89(0x20), vc54(0x3)
    0xc8d: vc8d(0x20) = CONST 
    0xc8f: vc8f(0x40) = ADD vc8d(0x20), vc89(0x20)
    0xc90: vc90(0x0) = CONST 
    0xc92: vc92 = SHA3 vc90(0x0), vc8f(0x40)
    0xc93: vc93 = SLOAD vc92
    0xc94: vc94(0x31d8) = CONST 
    0xc9a: vc9a(0xffffffff) = CONST 
    0xc9f: vc9f(0x31d8) = AND vc9a(0xffffffff), vc94(0x31d8)
    0xca0: vca0_0 = CALLPRIVATE vc9f(0x31d8), v2e1, vc93, vc50(0xca1)

    Begin block 0xca1
    prev=[0xc0c], succ=[0xd73]
    =================================
    0xca2: vca2(0x3) = CONST 
    0xca4: vca4(0x0) = CONST 
    0xca7: vca7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcbc: vcbc = AND vca7(0xffffffffffffffffffffffffffffffffffffffff), v2d7
    0xcbd: vcbd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcd2: vcd2 = AND vcbd(0xffffffffffffffffffffffffffffffffffffffff), vcbc
    0xcd4: MSTORE vca4(0x0), vcd2
    0xcd5: vcd5(0x20) = CONST 
    0xcd7: vcd7(0x20) = ADD vcd5(0x20), vca4(0x0)
    0xcda: MSTORE vcd7(0x20), vca2(0x3)
    0xcdb: vcdb(0x20) = CONST 
    0xcdd: vcdd(0x40) = ADD vcdb(0x20), vcd7(0x20)
    0xcde: vcde(0x0) = CONST 
    0xce0: vce0 = SHA3 vcde(0x0), vcdd(0x40)
    0xce3: SSTORE vce0, vca0_0
    0xce5: vce5(0xd73) = CONST 
    0xce9: vce9(0x4) = CONST 
    0xceb: vceb(0x0) = CONST 
    0xcee: vcee(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd03: vd03 = AND vcee(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xd04: vd04(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd19: vd19 = AND vd04(0xffffffffffffffffffffffffffffffffffffffff), vd03
    0xd1b: MSTORE vceb(0x0), vd19
    0xd1c: vd1c(0x20) = CONST 
    0xd1e: vd1e(0x20) = ADD vd1c(0x20), vceb(0x0)
    0xd21: MSTORE vd1e(0x20), vce9(0x4)
    0xd22: vd22(0x20) = CONST 
    0xd24: vd24(0x40) = ADD vd22(0x20), vd1e(0x20)
    0xd25: vd25(0x0) = CONST 
    0xd27: vd27 = SHA3 vd25(0x0), vd24(0x40)
    0xd28: vd28(0x0) = CONST 
    0xd2a: vd2a = CALLER 
    0xd2b: vd2b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd40: vd40 = AND vd2b(0xffffffffffffffffffffffffffffffffffffffff), vd2a
    0xd41: vd41(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd56: vd56 = AND vd41(0xffffffffffffffffffffffffffffffffffffffff), vd40
    0xd58: MSTORE vd28(0x0), vd56
    0xd59: vd59(0x20) = CONST 
    0xd5b: vd5b(0x20) = ADD vd59(0x20), vd28(0x0)
    0xd5e: MSTORE vd5b(0x20), vd27
    0xd5f: vd5f(0x20) = CONST 
    0xd61: vd61(0x40) = ADD vd5f(0x20), vd5b(0x20)
    0xd62: vd62(0x0) = CONST 
    0xd64: vd64 = SHA3 vd62(0x0), vd61(0x40)
    0xd65: vd65 = SLOAD vd64
    0xd66: vd66(0x31bf) = CONST 
    0xd6c: vd6c(0xffffffff) = CONST 
    0xd71: vd71(0x31bf) = AND vd6c(0xffffffff), vd66(0x31bf)
    0xd72: vd72_0 = CALLPRIVATE vd71(0x31bf), v2e1, vd65, vce5(0xd73)

    Begin block 0xd73
    prev=[0xca1], succ=[0xe6f]
    =================================
    0xd74: vd74(0x4) = CONST 
    0xd76: vd76(0x0) = CONST 
    0xd79: vd79(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd8e: vd8e = AND vd79(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xd8f: vd8f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xda4: vda4 = AND vd8f(0xffffffffffffffffffffffffffffffffffffffff), vd8e
    0xda6: MSTORE vd76(0x0), vda4
    0xda7: vda7(0x20) = CONST 
    0xda9: vda9(0x20) = ADD vda7(0x20), vd76(0x0)
    0xdac: MSTORE vda9(0x20), vd74(0x4)
    0xdad: vdad(0x20) = CONST 
    0xdaf: vdaf(0x40) = ADD vdad(0x20), vda9(0x20)
    0xdb0: vdb0(0x0) = CONST 
    0xdb2: vdb2 = SHA3 vdb0(0x0), vdaf(0x40)
    0xdb3: vdb3(0x0) = CONST 
    0xdb5: vdb5 = CALLER 
    0xdb6: vdb6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdcb: vdcb = AND vdb6(0xffffffffffffffffffffffffffffffffffffffff), vdb5
    0xdcc: vdcc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xde1: vde1 = AND vdcc(0xffffffffffffffffffffffffffffffffffffffff), vdcb
    0xde3: MSTORE vdb3(0x0), vde1
    0xde4: vde4(0x20) = CONST 
    0xde6: vde6(0x20) = ADD vde4(0x20), vdb3(0x0)
    0xde9: MSTORE vde6(0x20), vdb2
    0xdea: vdea(0x20) = CONST 
    0xdec: vdec(0x40) = ADD vdea(0x20), vde6(0x20)
    0xded: vded(0x0) = CONST 
    0xdef: vdef = SHA3 vded(0x0), vdec(0x40)
    0xdf2: SSTORE vdef, vd72_0
    0xdf5: vdf5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe0a: ve0a = AND vdf5(0xffffffffffffffffffffffffffffffffffffffff), v2d7
    0xe0c: ve0c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe21: ve21 = AND ve0c(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0xe22: ve22(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16) = CONST 
    0xe45: ve45(0x40) = CONST 
    0xe47: ve47 = MLOAD ve45(0x40)
    0xe4b: MSTORE ve47, v2e1
    0xe4c: ve4c(0x20) = CONST 
    0xe4e: ve4e = ADD ve4c(0x20), ve47
    0xe50: ve50(0x20) = CONST 
    0xe52: ve52 = ADD ve50(0x20), ve4e
    0xe55: ve55(0x40) = SUB ve52, ve47
    0xe57: MSTORE ve4e, ve55(0x40)
    0xe5b: ve5b = MLOAD va68(0x60)
    0xe5d: MSTORE ve52, ve5b
    0xe5e: ve5e(0x20) = CONST 
    0xe60: ve60 = ADD ve5e(0x20), ve52
    0xe64: ve64 = MLOAD va68(0x60)
    0xe66: ve66(0x20) = CONST 
    0xe68: ve68(0x80) = ADD ve66(0x20), va68(0x60)
    0xe6d: ve6d(0x0) = CONST 

    Begin block 0xe6f
    prev=[0xd73, 0xe78], succ=[0xe8a, 0xe78]
    =================================
    0xe6f_0x0: ve6f_0 = PHI ve6d(0x0), ve83
    0xe72: ve72 = LT ve6f_0, ve64
    0xe73: ve73 = ISZERO ve72
    0xe74: ve74(0xe8a) = CONST 
    0xe77: JUMPI ve74(0xe8a), ve73

    Begin block 0xe8a
    prev=[0xe6f], succ=[0xeb7, 0xe9e]
    =================================
    0xe93: ve93 = ADD ve64, ve60
    0xe95: ve95(0x1f) = CONST 
    0xe97: ve97 = AND ve95(0x1f), ve64
    0xe99: ve99 = ISZERO ve97
    0xe9a: ve9a(0xeb7) = CONST 
    0xe9d: JUMPI ve9a(0xeb7), ve99

    Begin block 0xeb7
    prev=[0xe8a, 0xe9e], succ=[0x2f1]
    =================================
    0xeb7_0x1: veb7_1 = PHI ve93, veb4
    0xebe: vebe(0x40) = CONST 
    0xec0: vec0 = MLOAD vebe(0x40)
    0xec3: vec3 = SUB veb7_1, vec0
    0xec5: LOG3 vec0, vec3, ve22(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16), ve21, ve0a
    0xec6: vec6(0x1) = CONST 
    0xed0: JUMP v294(0x2f1)

    Begin block 0x2f1
    prev=[0xeb7], succ=[]
    =================================
    0x2f2: v2f2(0x40) = CONST 
    0x2f4: v2f4 = MLOAD v2f2(0x40)
    0x2f7: v2f7(0x0) = ISZERO vec6(0x1)
    0x2f8: v2f8(0x1) = ISZERO v2f7(0x0)
    0x2f9: v2f9(0x0) = ISZERO v2f8(0x1)
    0x2fa: v2fa(0x1) = ISZERO v2f9(0x0)
    0x2fc: MSTORE v2f4, v2fa(0x1)
    0x2fd: v2fd(0x20) = CONST 
    0x2ff: v2ff = ADD v2fd(0x20), v2f4
    0x303: v303(0x40) = CONST 
    0x305: v305 = MLOAD v303(0x40)
    0x308: v308(0x20) = SUB v2ff, v305
    0x30a: RETURN v305, v308(0x20)

    Begin block 0xe9e
    prev=[0xe8a], succ=[0xeb7]
    =================================
    0xea0: vea0 = SUB ve93, ve97
    0xea2: vea2 = MLOAD vea0
    0xea3: vea3(0x1) = CONST 
    0xea6: vea6(0x20) = CONST 
    0xea8: vea8 = SUB vea6(0x20), ve97
    0xea9: vea9(0x100) = CONST 
    0xeac: veac = EXP vea9(0x100), vea8
    0xead: vead = SUB veac, vea3(0x1)
    0xeae: veae = NOT vead
    0xeaf: veaf = AND veae, vea2
    0xeb1: MSTORE vea0, veaf
    0xeb2: veb2(0x20) = CONST 
    0xeb4: veb4 = ADD veb2(0x20), vea0

    Begin block 0xe78
    prev=[0xe6f], succ=[0xe6f]
    =================================
    0xe78_0x0: ve78_0 = PHI ve6d(0x0), ve83
    0xe7a: ve7a = ADD ve68(0x80), ve78_0
    0xe7b: ve7b = MLOAD ve7a
    0xe7e: ve7e = ADD ve60, ve78_0
    0xe7f: MSTORE ve7e, ve7b
    0xe80: ve80(0x20) = CONST 
    0xe83: ve83 = ADD ve78_0, ve80(0x20)
    0xe86: ve86(0xe6f) = CONST 
    0xe89: JUMP ve86(0xe6f)

}

function balances(address)() public {
    Begin block 0x30b
    prev=[], succ=[0x313, 0x317]
    =================================
    0x30c: v30c = CALLVALUE 
    0x30e: v30e = ISZERO v30c
    0x30f: v30f(0x317) = CONST 
    0x312: JUMPI v30f(0x317), v30e

    Begin block 0x313
    prev=[0x30b], succ=[]
    =================================
    0x313: v313(0x0) = CONST 
    0x316: REVERT v313(0x0), v313(0x0)

    Begin block 0x317
    prev=[0x30b], succ=[0xed1]
    =================================
    0x319: v319(0x34c) = CONST 
    0x31c: v31c(0x4) = CONST 
    0x31f: v31f = CALLDATASIZE 
    0x320: v320 = SUB v31f, v31c(0x4)
    0x322: v322 = ADD v31c(0x4), v320
    0x326: v326 = CALLDATALOAD v31c(0x4)
    0x327: v327(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33c: v33c = AND v327(0xffffffffffffffffffffffffffffffffffffffff), v326
    0x33e: v33e(0x20) = CONST 
    0x340: v340(0x24) = ADD v33e(0x20), v31c(0x4)
    0x348: v348(0xed1) = CONST 
    0x34b: JUMP v348(0xed1)

    Begin block 0xed1
    prev=[0x317], succ=[0x34c]
    =================================
    0xed2: ved2(0x3) = CONST 
    0xed4: ved4(0x20) = CONST 
    0xed6: MSTORE ved4(0x20), ved2(0x3)
    0xed8: ved8(0x0) = CONST 
    0xeda: MSTORE ved8(0x0), v33c
    0xedb: vedb(0x40) = CONST 
    0xedd: vedd(0x0) = CONST 
    0xedf: vedf = SHA3 vedd(0x0), vedb(0x40)
    0xee0: vee0(0x0) = CONST 
    0xee6: vee6 = SLOAD vedf
    0xee8: JUMP v319(0x34c)

    Begin block 0x34c
    prev=[0xed1], succ=[]
    =================================
    0x34d: v34d(0x40) = CONST 
    0x34f: v34f = MLOAD v34d(0x40)
    0x353: MSTORE v34f, vee6
    0x354: v354(0x20) = CONST 
    0x356: v356 = ADD v354(0x20), v34f
    0x35a: v35a(0x40) = CONST 
    0x35c: v35c = MLOAD v35a(0x40)
    0x35f: v35f(0x20) = SUB v356, v35c
    0x361: RETURN v35c, v35f(0x20)

}

function 0x31bf(0x31bfarg0x0, 0x31bfarg0x1, 0x31bfarg0x2) private {
    Begin block 0x31bf
    prev=[], succ=[0x31cc, 0x31cd]
    =================================
    0x31c0: v31c0(0x0) = CONST 
    0x31c4: v31c4 = GT v31bfarg0, v31bfarg1
    0x31c5: v31c5 = ISZERO v31c4
    0x31c6: v31c6 = ISZERO v31c5
    0x31c7: v31c7 = ISZERO v31c6
    0x31c8: v31c8(0x31cd) = CONST 
    0x31cb: JUMPI v31c8(0x31cd), v31c7

    Begin block 0x31cc
    prev=[0x31bf], succ=[]
    =================================
    0x31cc: THROW 

    Begin block 0x31cd
    prev=[0x31bf], succ=[]
    =================================
    0x31d0: v31d0 = SUB v31bfarg1, v31bfarg0
    0x31d7: RETURNPRIVATE v31bfarg2, v31d0

}

function 0x31d8(0x31d8arg0x0, 0x31d8arg0x1, 0x31d8arg0x2) private {
    Begin block 0x31d8
    prev=[], succ=[0x31eb, 0x31ec]
    =================================
    0x31d9: v31d9(0x0) = CONST 
    0x31de: v31de = ADD v31d8arg1, v31d8arg0
    0x31e3: v31e3 = LT v31de, v31d8arg1
    0x31e4: v31e4 = ISZERO v31e3
    0x31e5: v31e5 = ISZERO v31e4
    0x31e6: v31e6 = ISZERO v31e5
    0x31e7: v31e7(0x31ec) = CONST 
    0x31ea: JUMPI v31e7(0x31ec), v31e6

    Begin block 0x31eb
    prev=[0x31d8], succ=[]
    =================================
    0x31eb: THROW 

    Begin block 0x31ec
    prev=[0x31d8], succ=[]
    =================================
    0x31f5: RETURNPRIVATE v31d8arg2, v31de

}

function unfreezeFoundingTeamBalance()() public {
    Begin block 0x362
    prev=[], succ=[0x36a, 0x36e]
    =================================
    0x363: v363 = CALLVALUE 
    0x365: v365 = ISZERO v363
    0x366: v366(0x36e) = CONST 
    0x369: JUMPI v366(0x36e), v365

    Begin block 0x36a
    prev=[0x362], succ=[]
    =================================
    0x36a: v36a(0x0) = CONST 
    0x36d: REVERT v36a(0x0), v36a(0x0)

    Begin block 0x36e
    prev=[0x362], succ=[0xee9B0x36e]
    =================================
    0x370: v370(0x377) = CONST 
    0x373: v373(0xee9) = CONST 
    0x376: JUMP v373(0xee9)

    Begin block 0xee9B0x36e
    prev=[0x36e], succ=[0xf86B0x36e, 0xf42B0x36e]
    =================================
    0xeeaS0x36e: veeaV36e(0x0) = CONST 
    0xeedS0x36e: veedV36e(0x0) = CONST 
    0xef1S0x36e: vef1V36e = SLOAD veedV36e(0x0)
    0xef3S0x36e: vef3V36e(0x100) = CONST 
    0xef6S0x36e: vef6V36e(0x1) = EXP vef3V36e(0x100), veedV36e(0x0)
    0xef8S0x36e: vef8V36e = DIV vef1V36e, vef6V36e(0x1)
    0xef9S0x36e: vef9V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf0eS0x36e: vf0eV36e = AND vef9V36e(0xffffffffffffffffffffffffffffffffffffffff), vef8V36e
    0xf0fS0x36e: vf0fV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf24S0x36e: vf24V36e = AND vf0fV36e(0xffffffffffffffffffffffffffffffffffffffff), vf0eV36e
    0xf25S0x36e: vf25V36e = CALLER 
    0xf26S0x36e: vf26V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf3bS0x36e: vf3bV36e = AND vf26V36e(0xffffffffffffffffffffffffffffffffffffffff), vf25V36e
    0xf3cS0x36e: vf3cV36e = EQ vf3bV36e, vf24V36e
    0xf3eS0x36e: vf3eV36e(0xf86) = CONST 
    0xf41S0x36e: JUMPI vf3eV36e(0xf86), vf3cV36e

    Begin block 0xf86B0x36e
    prev=[0xee9B0x36e, 0xf42B0x36e], succ=[0xf8dB0x36e, 0xf91B0x36e]
    =================================
    0xf86_0x0S0x36e: vf86_0V36e = PHI vf3cV36e, vf85V36e
    0xf87S0x36e: vf87V36e = ISZERO vf86_0V36e
    0xf88S0x36e: vf88V36e = ISZERO vf87V36e
    0xf89S0x36e: vf89V36e(0xf91) = CONST 
    0xf8cS0x36e: JUMPI vf89V36e(0xf91), vf88V36e

    Begin block 0xf8dB0x36e
    prev=[0xf86B0x36e], succ=[]
    =================================
    0xf8dS0x36e: vf8dV36e(0x0) = CONST 
    0xf90S0x36e: REVERT vf8dV36e(0x0), vf8dV36e(0x0)

    Begin block 0xf91B0x36e
    prev=[0xf86B0x36e], succ=[0xfadB0x36e, 0xfb1B0x36e]
    =================================
    0xf92S0x36e: vf92V36e = TIMESTAMP 
    0xf95S0x36e: vf95V36e(0x5c2aad81) = CONST 
    0xf9bS0x36e: vf9bV36e(0xffffffffffffffff) = CONST 
    0xfa4S0x36e: vfa4V36e = AND vf9bV36e(0xffffffffffffffff), vf92V36e
    0xfa5S0x36e: vfa5V36e = LT vfa4V36e, vf95V36e(0x5c2aad81)
    0xfa6S0x36e: vfa6V36e = ISZERO vfa5V36e
    0xfa7S0x36e: vfa7V36e = ISZERO vfa6V36e
    0xfa8S0x36e: vfa8V36e = ISZERO vfa7V36e
    0xfa9S0x36e: vfa9V36e(0xfb1) = CONST 
    0xfacS0x36e: JUMPI vfa9V36e(0xfb1), vfa8V36e

    Begin block 0xfadB0x36e
    prev=[0xf91B0x36e], succ=[]
    =================================
    0xfadS0x36e: vfadV36e(0x0) = CONST 
    0xfb0S0x36e: REVERT vfadV36e(0x0), vfadV36e(0x0)

    Begin block 0xfb1B0x36e
    prev=[0xf91B0x36e], succ=[0xfc8B0x36e, 0x19c8B0x36e]
    =================================
    0xfb2S0x36e: vfb2V36e(0x5e0be101) = CONST 
    0xfb8S0x36e: vfb8V36e(0xffffffffffffffff) = CONST 
    0xfc1S0x36e: vfc1V36e = AND vfb8V36e(0xffffffffffffffff), vf92V36e
    0xfc2S0x36e: vfc2V36e = LT vfc1V36e, vfb2V36e(0x5e0be101)
    0xfc3S0x36e: vfc3V36e = ISZERO vfc2V36e
    0xfc4S0x36e: vfc4V36e(0x19c8) = CONST 
    0xfc7S0x36e: JUMPI vfc4V36e(0x19c8), vfc3V36e

    Begin block 0xfc8B0x36e
    prev=[0xfb1B0x36e], succ=[0x111aB0x36e]
    =================================
    0xfc8S0x36e: vfc8V36e(0x1) = CONST 
    0xfcaS0x36e: vfcaV36e(0x0) = CONST 
    0xfccS0x36e: vfccV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = CONST 
    0xfe1S0x36e: vfe1V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xff6S0x36e: vff6V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND vfe1V36e(0xffffffffffffffffffffffffffffffffffffffff), vfccV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0xff7S0x36e: vff7V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x100cS0x36e: v100cV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND vff7V36e(0xffffffffffffffffffffffffffffffffffffffff), vff6V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x100eS0x36e: MSTORE vfcaV36e(0x0), v100cV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x100fS0x36e: v100fV36e(0x20) = CONST 
    0x1011S0x36e: v1011V36e(0x20) = ADD v100fV36e(0x20), vfcaV36e(0x0)
    0x1014S0x36e: MSTORE v1011V36e(0x20), vfc8V36e(0x1)
    0x1015S0x36e: v1015V36e(0x20) = CONST 
    0x1017S0x36e: v1017V36e(0x40) = ADD v1015V36e(0x20), v1011V36e(0x20)
    0x1018S0x36e: v1018V36e(0x0) = CONST 
    0x101aS0x36e: v101aV36e = SHA3 v1018V36e(0x0), v1017V36e(0x40)
    0x101bS0x36e: v101bV36e(0x0) = CONST 
    0x101dS0x36e: v101dV36e(0x5c2aad81) = CONST 
    0x1022S0x36e: v1022V36e(0xffffffffffffffff) = CONST 
    0x102bS0x36e: v102bV36e(0x5c2aad81) = AND v1022V36e(0xffffffffffffffff), v101dV36e(0x5c2aad81)
    0x102dS0x36e: MSTORE v101bV36e(0x0), v102bV36e(0x5c2aad81)
    0x102eS0x36e: v102eV36e(0x20) = CONST 
    0x1030S0x36e: v1030V36e(0x20) = ADD v102eV36e(0x20), v101bV36e(0x0)
    0x1033S0x36e: MSTORE v1030V36e(0x20), v101aV36e
    0x1034S0x36e: v1034V36e(0x20) = CONST 
    0x1036S0x36e: v1036V36e(0x40) = ADD v1034V36e(0x20), v1030V36e(0x20)
    0x1037S0x36e: v1037V36e(0x0) = CONST 
    0x1039S0x36e: v1039V36e = SHA3 v1037V36e(0x0), v1036V36e(0x40)
    0x103aS0x36e: v103aV36e = SLOAD v1039V36e
    0x103dS0x36e: v103dV36e(0x0) = CONST 
    0x103fS0x36e: v103fV36e(0x1) = CONST 
    0x1041S0x36e: v1041V36e(0x0) = CONST 
    0x1043S0x36e: v1043V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = CONST 
    0x1058S0x36e: v1058V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x106dS0x36e: v106dV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND v1058V36e(0xffffffffffffffffffffffffffffffffffffffff), v1043V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x106eS0x36e: v106eV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1083S0x36e: v1083V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND v106eV36e(0xffffffffffffffffffffffffffffffffffffffff), v106dV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x1085S0x36e: MSTORE v1041V36e(0x0), v1083V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x1086S0x36e: v1086V36e(0x20) = CONST 
    0x1088S0x36e: v1088V36e(0x20) = ADD v1086V36e(0x20), v1041V36e(0x0)
    0x108bS0x36e: MSTORE v1088V36e(0x20), v103fV36e(0x1)
    0x108cS0x36e: v108cV36e(0x20) = CONST 
    0x108eS0x36e: v108eV36e(0x40) = ADD v108cV36e(0x20), v1088V36e(0x20)
    0x108fS0x36e: v108fV36e(0x0) = CONST 
    0x1091S0x36e: v1091V36e = SHA3 v108fV36e(0x0), v108eV36e(0x40)
    0x1092S0x36e: v1092V36e(0x0) = CONST 
    0x1094S0x36e: v1094V36e(0x5c2aad81) = CONST 
    0x1099S0x36e: v1099V36e(0xffffffffffffffff) = CONST 
    0x10a2S0x36e: v10a2V36e(0x5c2aad81) = AND v1099V36e(0xffffffffffffffff), v1094V36e(0x5c2aad81)
    0x10a4S0x36e: MSTORE v1092V36e(0x0), v10a2V36e(0x5c2aad81)
    0x10a5S0x36e: v10a5V36e(0x20) = CONST 
    0x10a7S0x36e: v10a7V36e(0x20) = ADD v10a5V36e(0x20), v1092V36e(0x0)
    0x10aaS0x36e: MSTORE v10a7V36e(0x20), v1091V36e
    0x10abS0x36e: v10abV36e(0x20) = CONST 
    0x10adS0x36e: v10adV36e(0x40) = ADD v10abV36e(0x20), v10a7V36e(0x20)
    0x10aeS0x36e: v10aeV36e(0x0) = CONST 
    0x10b0S0x36e: v10b0V36e = SHA3 v10aeV36e(0x0), v10adV36e(0x40)
    0x10b3S0x36e: SSTORE v10b0V36e, v103dV36e(0x0)
    0x10b5S0x36e: v10b5V36e(0x111a) = CONST 
    0x10b9S0x36e: v10b9V36e(0x3) = CONST 
    0x10bbS0x36e: v10bbV36e(0x0) = CONST 
    0x10bdS0x36e: v10bdV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = CONST 
    0x10d2S0x36e: v10d2V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10e7S0x36e: v10e7V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND v10d2V36e(0xffffffffffffffffffffffffffffffffffffffff), v10bdV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x10e8S0x36e: v10e8V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10fdS0x36e: v10fdV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND v10e8V36e(0xffffffffffffffffffffffffffffffffffffffff), v10e7V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x10ffS0x36e: MSTORE v10bbV36e(0x0), v10fdV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x1100S0x36e: v1100V36e(0x20) = CONST 
    0x1102S0x36e: v1102V36e(0x20) = ADD v1100V36e(0x20), v10bbV36e(0x0)
    0x1105S0x36e: MSTORE v1102V36e(0x20), v10b9V36e(0x3)
    0x1106S0x36e: v1106V36e(0x20) = CONST 
    0x1108S0x36e: v1108V36e(0x40) = ADD v1106V36e(0x20), v1102V36e(0x20)
    0x1109S0x36e: v1109V36e(0x0) = CONST 
    0x110bS0x36e: v110bV36e = SHA3 v1109V36e(0x0), v1108V36e(0x40)
    0x110cS0x36e: v110cV36e = SLOAD v110bV36e
    0x110dS0x36e: v110dV36e(0x31d8) = CONST 
    0x1113S0x36e: v1113V36e(0xffffffff) = CONST 
    0x1118S0x36e: v1118V36e(0x31d8) = AND v1113V36e(0xffffffff), v110dV36e(0x31d8)
    0x1119S0x36e: v1119_0V36e = CALLPRIVATE v1118V36e(0x31d8), v103aV36e, v110cV36e, v10b5V36e(0x111a)

    Begin block 0x111aB0x36e
    prev=[0xfc8B0x36e], succ=[0x12c4B0x36e]
    =================================
    0x111bS0x36e: v111bV36e(0x3) = CONST 
    0x111dS0x36e: v111dV36e(0x0) = CONST 
    0x111fS0x36e: v111fV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = CONST 
    0x1134S0x36e: v1134V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1149S0x36e: v1149V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND v1134V36e(0xffffffffffffffffffffffffffffffffffffffff), v111fV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x114aS0x36e: v114aV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x115fS0x36e: v115fV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370) = AND v114aV36e(0xffffffffffffffffffffffffffffffffffffffff), v1149V36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x1161S0x36e: MSTORE v111dV36e(0x0), v115fV36e(0x3d220cfddc45900c78ff47d3d2f4302a2e994370)
    0x1162S0x36e: v1162V36e(0x20) = CONST 
    0x1164S0x36e: v1164V36e(0x20) = ADD v1162V36e(0x20), v111dV36e(0x0)
    0x1167S0x36e: MSTORE v1164V36e(0x20), v111bV36e(0x3)
    0x1168S0x36e: v1168V36e(0x20) = CONST 
    0x116aS0x36e: v116aV36e(0x40) = ADD v1168V36e(0x20), v1164V36e(0x20)
    0x116bS0x36e: v116bV36e(0x0) = CONST 
    0x116dS0x36e: v116dV36e = SHA3 v116bV36e(0x0), v116aV36e(0x40)
    0x1170S0x36e: SSTORE v116dV36e, v1119_0V36e
    0x1172S0x36e: v1172V36e(0x1) = CONST 
    0x1174S0x36e: v1174V36e(0x0) = CONST 
    0x1176S0x36e: v1176V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x118bS0x36e: v118bV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11a0S0x36e: v11a0V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v118bV36e(0xffffffffffffffffffffffffffffffffffffffff), v1176V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x11a1S0x36e: v11a1V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11b6S0x36e: v11b6V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v11a1V36e(0xffffffffffffffffffffffffffffffffffffffff), v11a0V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x11b8S0x36e: MSTORE v1174V36e(0x0), v11b6V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x11b9S0x36e: v11b9V36e(0x20) = CONST 
    0x11bbS0x36e: v11bbV36e(0x20) = ADD v11b9V36e(0x20), v1174V36e(0x0)
    0x11beS0x36e: MSTORE v11bbV36e(0x20), v1172V36e(0x1)
    0x11bfS0x36e: v11bfV36e(0x20) = CONST 
    0x11c1S0x36e: v11c1V36e(0x40) = ADD v11bfV36e(0x20), v11bbV36e(0x20)
    0x11c2S0x36e: v11c2V36e(0x0) = CONST 
    0x11c4S0x36e: v11c4V36e = SHA3 v11c2V36e(0x0), v11c1V36e(0x40)
    0x11c5S0x36e: v11c5V36e(0x0) = CONST 
    0x11c7S0x36e: v11c7V36e(0x5c2aad81) = CONST 
    0x11ccS0x36e: v11ccV36e(0xffffffffffffffff) = CONST 
    0x11d5S0x36e: v11d5V36e(0x5c2aad81) = AND v11ccV36e(0xffffffffffffffff), v11c7V36e(0x5c2aad81)
    0x11d7S0x36e: MSTORE v11c5V36e(0x0), v11d5V36e(0x5c2aad81)
    0x11d8S0x36e: v11d8V36e(0x20) = CONST 
    0x11daS0x36e: v11daV36e(0x20) = ADD v11d8V36e(0x20), v11c5V36e(0x0)
    0x11ddS0x36e: MSTORE v11daV36e(0x20), v11c4V36e
    0x11deS0x36e: v11deV36e(0x20) = CONST 
    0x11e0S0x36e: v11e0V36e(0x40) = ADD v11deV36e(0x20), v11daV36e(0x20)
    0x11e1S0x36e: v11e1V36e(0x0) = CONST 
    0x11e3S0x36e: v11e3V36e = SHA3 v11e1V36e(0x0), v11e0V36e(0x40)
    0x11e4S0x36e: v11e4V36e = SLOAD v11e3V36e
    0x11e7S0x36e: v11e7V36e(0x0) = CONST 
    0x11e9S0x36e: v11e9V36e(0x1) = CONST 
    0x11ebS0x36e: v11ebV36e(0x0) = CONST 
    0x11edS0x36e: v11edV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1202S0x36e: v1202V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1217S0x36e: v1217V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1202V36e(0xffffffffffffffffffffffffffffffffffffffff), v11edV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1218S0x36e: v1218V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x122dS0x36e: v122dV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1218V36e(0xffffffffffffffffffffffffffffffffffffffff), v1217V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x122fS0x36e: MSTORE v11ebV36e(0x0), v122dV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1230S0x36e: v1230V36e(0x20) = CONST 
    0x1232S0x36e: v1232V36e(0x20) = ADD v1230V36e(0x20), v11ebV36e(0x0)
    0x1235S0x36e: MSTORE v1232V36e(0x20), v11e9V36e(0x1)
    0x1236S0x36e: v1236V36e(0x20) = CONST 
    0x1238S0x36e: v1238V36e(0x40) = ADD v1236V36e(0x20), v1232V36e(0x20)
    0x1239S0x36e: v1239V36e(0x0) = CONST 
    0x123bS0x36e: v123bV36e = SHA3 v1239V36e(0x0), v1238V36e(0x40)
    0x123cS0x36e: v123cV36e(0x0) = CONST 
    0x123eS0x36e: v123eV36e(0x5c2aad81) = CONST 
    0x1243S0x36e: v1243V36e(0xffffffffffffffff) = CONST 
    0x124cS0x36e: v124cV36e(0x5c2aad81) = AND v1243V36e(0xffffffffffffffff), v123eV36e(0x5c2aad81)
    0x124eS0x36e: MSTORE v123cV36e(0x0), v124cV36e(0x5c2aad81)
    0x124fS0x36e: v124fV36e(0x20) = CONST 
    0x1251S0x36e: v1251V36e(0x20) = ADD v124fV36e(0x20), v123cV36e(0x0)
    0x1254S0x36e: MSTORE v1251V36e(0x20), v123bV36e
    0x1255S0x36e: v1255V36e(0x20) = CONST 
    0x1257S0x36e: v1257V36e(0x40) = ADD v1255V36e(0x20), v1251V36e(0x20)
    0x1258S0x36e: v1258V36e(0x0) = CONST 
    0x125aS0x36e: v125aV36e = SHA3 v1258V36e(0x0), v1257V36e(0x40)
    0x125dS0x36e: SSTORE v125aV36e, v11e7V36e(0x0)
    0x125fS0x36e: v125fV36e(0x12c4) = CONST 
    0x1263S0x36e: v1263V36e(0x3) = CONST 
    0x1265S0x36e: v1265V36e(0x0) = CONST 
    0x1267S0x36e: v1267V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x127cS0x36e: v127cV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1291S0x36e: v1291V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v127cV36e(0xffffffffffffffffffffffffffffffffffffffff), v1267V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1292S0x36e: v1292V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12a7S0x36e: v12a7V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1292V36e(0xffffffffffffffffffffffffffffffffffffffff), v1291V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x12a9S0x36e: MSTORE v1265V36e(0x0), v12a7V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x12aaS0x36e: v12aaV36e(0x20) = CONST 
    0x12acS0x36e: v12acV36e(0x20) = ADD v12aaV36e(0x20), v1265V36e(0x0)
    0x12afS0x36e: MSTORE v12acV36e(0x20), v1263V36e(0x3)
    0x12b0S0x36e: v12b0V36e(0x20) = CONST 
    0x12b2S0x36e: v12b2V36e(0x40) = ADD v12b0V36e(0x20), v12acV36e(0x20)
    0x12b3S0x36e: v12b3V36e(0x0) = CONST 
    0x12b5S0x36e: v12b5V36e = SHA3 v12b3V36e(0x0), v12b2V36e(0x40)
    0x12b6S0x36e: v12b6V36e = SLOAD v12b5V36e
    0x12b7S0x36e: v12b7V36e(0x31d8) = CONST 
    0x12bdS0x36e: v12bdV36e(0xffffffff) = CONST 
    0x12c2S0x36e: v12c2V36e(0x31d8) = AND v12bdV36e(0xffffffff), v12b7V36e(0x31d8)
    0x12c3S0x36e: v12c3_0V36e = CALLPRIVATE v12c2V36e(0x31d8), v11e4V36e, v12b6V36e, v125fV36e(0x12c4)

    Begin block 0x12c4B0x36e
    prev=[0x111aB0x36e], succ=[0x146eB0x36e]
    =================================
    0x12c5S0x36e: v12c5V36e(0x3) = CONST 
    0x12c7S0x36e: v12c7V36e(0x0) = CONST 
    0x12c9S0x36e: v12c9V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x12deS0x36e: v12deV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12f3S0x36e: v12f3V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v12deV36e(0xffffffffffffffffffffffffffffffffffffffff), v12c9V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x12f4S0x36e: v12f4V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1309S0x36e: v1309V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v12f4V36e(0xffffffffffffffffffffffffffffffffffffffff), v12f3V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x130bS0x36e: MSTORE v12c7V36e(0x0), v1309V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x130cS0x36e: v130cV36e(0x20) = CONST 
    0x130eS0x36e: v130eV36e(0x20) = ADD v130cV36e(0x20), v12c7V36e(0x0)
    0x1311S0x36e: MSTORE v130eV36e(0x20), v12c5V36e(0x3)
    0x1312S0x36e: v1312V36e(0x20) = CONST 
    0x1314S0x36e: v1314V36e(0x40) = ADD v1312V36e(0x20), v130eV36e(0x20)
    0x1315S0x36e: v1315V36e(0x0) = CONST 
    0x1317S0x36e: v1317V36e = SHA3 v1315V36e(0x0), v1314V36e(0x40)
    0x131aS0x36e: SSTORE v1317V36e, v12c3_0V36e
    0x131cS0x36e: v131cV36e(0x1) = CONST 
    0x131eS0x36e: v131eV36e(0x0) = CONST 
    0x1320S0x36e: v1320V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = CONST 
    0x1335S0x36e: v1335V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x134aS0x36e: v134aV36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v1335V36e(0xffffffffffffffffffffffffffffffffffffffff), v1320V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x134bS0x36e: v134bV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1360S0x36e: v1360V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v134bV36e(0xffffffffffffffffffffffffffffffffffffffff), v134aV36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x1362S0x36e: MSTORE v131eV36e(0x0), v1360V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x1363S0x36e: v1363V36e(0x20) = CONST 
    0x1365S0x36e: v1365V36e(0x20) = ADD v1363V36e(0x20), v131eV36e(0x0)
    0x1368S0x36e: MSTORE v1365V36e(0x20), v131cV36e(0x1)
    0x1369S0x36e: v1369V36e(0x20) = CONST 
    0x136bS0x36e: v136bV36e(0x40) = ADD v1369V36e(0x20), v1365V36e(0x20)
    0x136cS0x36e: v136cV36e(0x0) = CONST 
    0x136eS0x36e: v136eV36e = SHA3 v136cV36e(0x0), v136bV36e(0x40)
    0x136fS0x36e: v136fV36e(0x0) = CONST 
    0x1371S0x36e: v1371V36e(0x5c2aad81) = CONST 
    0x1376S0x36e: v1376V36e(0xffffffffffffffff) = CONST 
    0x137fS0x36e: v137fV36e(0x5c2aad81) = AND v1376V36e(0xffffffffffffffff), v1371V36e(0x5c2aad81)
    0x1381S0x36e: MSTORE v136fV36e(0x0), v137fV36e(0x5c2aad81)
    0x1382S0x36e: v1382V36e(0x20) = CONST 
    0x1384S0x36e: v1384V36e(0x20) = ADD v1382V36e(0x20), v136fV36e(0x0)
    0x1387S0x36e: MSTORE v1384V36e(0x20), v136eV36e
    0x1388S0x36e: v1388V36e(0x20) = CONST 
    0x138aS0x36e: v138aV36e(0x40) = ADD v1388V36e(0x20), v1384V36e(0x20)
    0x138bS0x36e: v138bV36e(0x0) = CONST 
    0x138dS0x36e: v138dV36e = SHA3 v138bV36e(0x0), v138aV36e(0x40)
    0x138eS0x36e: v138eV36e = SLOAD v138dV36e
    0x1391S0x36e: v1391V36e(0x0) = CONST 
    0x1393S0x36e: v1393V36e(0x1) = CONST 
    0x1395S0x36e: v1395V36e(0x0) = CONST 
    0x1397S0x36e: v1397V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = CONST 
    0x13acS0x36e: v13acV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13c1S0x36e: v13c1V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v13acV36e(0xffffffffffffffffffffffffffffffffffffffff), v1397V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x13c2S0x36e: v13c2V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13d7S0x36e: v13d7V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v13c2V36e(0xffffffffffffffffffffffffffffffffffffffff), v13c1V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x13d9S0x36e: MSTORE v1395V36e(0x0), v13d7V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x13daS0x36e: v13daV36e(0x20) = CONST 
    0x13dcS0x36e: v13dcV36e(0x20) = ADD v13daV36e(0x20), v1395V36e(0x0)
    0x13dfS0x36e: MSTORE v13dcV36e(0x20), v1393V36e(0x1)
    0x13e0S0x36e: v13e0V36e(0x20) = CONST 
    0x13e2S0x36e: v13e2V36e(0x40) = ADD v13e0V36e(0x20), v13dcV36e(0x20)
    0x13e3S0x36e: v13e3V36e(0x0) = CONST 
    0x13e5S0x36e: v13e5V36e = SHA3 v13e3V36e(0x0), v13e2V36e(0x40)
    0x13e6S0x36e: v13e6V36e(0x0) = CONST 
    0x13e8S0x36e: v13e8V36e(0x5c2aad81) = CONST 
    0x13edS0x36e: v13edV36e(0xffffffffffffffff) = CONST 
    0x13f6S0x36e: v13f6V36e(0x5c2aad81) = AND v13edV36e(0xffffffffffffffff), v13e8V36e(0x5c2aad81)
    0x13f8S0x36e: MSTORE v13e6V36e(0x0), v13f6V36e(0x5c2aad81)
    0x13f9S0x36e: v13f9V36e(0x20) = CONST 
    0x13fbS0x36e: v13fbV36e(0x20) = ADD v13f9V36e(0x20), v13e6V36e(0x0)
    0x13feS0x36e: MSTORE v13fbV36e(0x20), v13e5V36e
    0x13ffS0x36e: v13ffV36e(0x20) = CONST 
    0x1401S0x36e: v1401V36e(0x40) = ADD v13ffV36e(0x20), v13fbV36e(0x20)
    0x1402S0x36e: v1402V36e(0x0) = CONST 
    0x1404S0x36e: v1404V36e = SHA3 v1402V36e(0x0), v1401V36e(0x40)
    0x1407S0x36e: SSTORE v1404V36e, v1391V36e(0x0)
    0x1409S0x36e: v1409V36e(0x146e) = CONST 
    0x140dS0x36e: v140dV36e(0x3) = CONST 
    0x140fS0x36e: v140fV36e(0x0) = CONST 
    0x1411S0x36e: v1411V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = CONST 
    0x1426S0x36e: v1426V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x143bS0x36e: v143bV36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v1426V36e(0xffffffffffffffffffffffffffffffffffffffff), v1411V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x143cS0x36e: v143cV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1451S0x36e: v1451V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v143cV36e(0xffffffffffffffffffffffffffffffffffffffff), v143bV36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x1453S0x36e: MSTORE v140fV36e(0x0), v1451V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x1454S0x36e: v1454V36e(0x20) = CONST 
    0x1456S0x36e: v1456V36e(0x20) = ADD v1454V36e(0x20), v140fV36e(0x0)
    0x1459S0x36e: MSTORE v1456V36e(0x20), v140dV36e(0x3)
    0x145aS0x36e: v145aV36e(0x20) = CONST 
    0x145cS0x36e: v145cV36e(0x40) = ADD v145aV36e(0x20), v1456V36e(0x20)
    0x145dS0x36e: v145dV36e(0x0) = CONST 
    0x145fS0x36e: v145fV36e = SHA3 v145dV36e(0x0), v145cV36e(0x40)
    0x1460S0x36e: v1460V36e = SLOAD v145fV36e
    0x1461S0x36e: v1461V36e(0x31d8) = CONST 
    0x1467S0x36e: v1467V36e(0xffffffff) = CONST 
    0x146cS0x36e: v146cV36e(0x31d8) = AND v1467V36e(0xffffffff), v1461V36e(0x31d8)
    0x146dS0x36e: v146d_0V36e = CALLPRIVATE v146cV36e(0x31d8), v138eV36e, v1460V36e, v1409V36e(0x146e)

    Begin block 0x146eB0x36e
    prev=[0x12c4B0x36e], succ=[0x1618B0x36e]
    =================================
    0x146fS0x36e: v146fV36e(0x3) = CONST 
    0x1471S0x36e: v1471V36e(0x0) = CONST 
    0x1473S0x36e: v1473V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = CONST 
    0x1488S0x36e: v1488V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x149dS0x36e: v149dV36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v1488V36e(0xffffffffffffffffffffffffffffffffffffffff), v1473V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x149eS0x36e: v149eV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14b3S0x36e: v14b3V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89) = AND v149eV36e(0xffffffffffffffffffffffffffffffffffffffff), v149dV36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x14b5S0x36e: MSTORE v1471V36e(0x0), v14b3V36e(0x41cf7d41adf0d5de82b35143c9bbca68af819a89)
    0x14b6S0x36e: v14b6V36e(0x20) = CONST 
    0x14b8S0x36e: v14b8V36e(0x20) = ADD v14b6V36e(0x20), v1471V36e(0x0)
    0x14bbS0x36e: MSTORE v14b8V36e(0x20), v146fV36e(0x3)
    0x14bcS0x36e: v14bcV36e(0x20) = CONST 
    0x14beS0x36e: v14beV36e(0x40) = ADD v14bcV36e(0x20), v14b8V36e(0x20)
    0x14bfS0x36e: v14bfV36e(0x0) = CONST 
    0x14c1S0x36e: v14c1V36e = SHA3 v14bfV36e(0x0), v14beV36e(0x40)
    0x14c4S0x36e: SSTORE v14c1V36e, v146d_0V36e
    0x14c6S0x36e: v14c6V36e(0x1) = CONST 
    0x14c8S0x36e: v14c8V36e(0x0) = CONST 
    0x14caS0x36e: v14caV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = CONST 
    0x14dfS0x36e: v14dfV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14f4S0x36e: v14f4V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v14dfV36e(0xffffffffffffffffffffffffffffffffffffffff), v14caV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x14f5S0x36e: v14f5V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x150aS0x36e: v150aV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v14f5V36e(0xffffffffffffffffffffffffffffffffffffffff), v14f4V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x150cS0x36e: MSTORE v14c8V36e(0x0), v150aV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x150dS0x36e: v150dV36e(0x20) = CONST 
    0x150fS0x36e: v150fV36e(0x20) = ADD v150dV36e(0x20), v14c8V36e(0x0)
    0x1512S0x36e: MSTORE v150fV36e(0x20), v14c6V36e(0x1)
    0x1513S0x36e: v1513V36e(0x20) = CONST 
    0x1515S0x36e: v1515V36e(0x40) = ADD v1513V36e(0x20), v150fV36e(0x20)
    0x1516S0x36e: v1516V36e(0x0) = CONST 
    0x1518S0x36e: v1518V36e = SHA3 v1516V36e(0x0), v1515V36e(0x40)
    0x1519S0x36e: v1519V36e(0x0) = CONST 
    0x151bS0x36e: v151bV36e(0x5c2aad81) = CONST 
    0x1520S0x36e: v1520V36e(0xffffffffffffffff) = CONST 
    0x1529S0x36e: v1529V36e(0x5c2aad81) = AND v1520V36e(0xffffffffffffffff), v151bV36e(0x5c2aad81)
    0x152bS0x36e: MSTORE v1519V36e(0x0), v1529V36e(0x5c2aad81)
    0x152cS0x36e: v152cV36e(0x20) = CONST 
    0x152eS0x36e: v152eV36e(0x20) = ADD v152cV36e(0x20), v1519V36e(0x0)
    0x1531S0x36e: MSTORE v152eV36e(0x20), v1518V36e
    0x1532S0x36e: v1532V36e(0x20) = CONST 
    0x1534S0x36e: v1534V36e(0x40) = ADD v1532V36e(0x20), v152eV36e(0x20)
    0x1535S0x36e: v1535V36e(0x0) = CONST 
    0x1537S0x36e: v1537V36e = SHA3 v1535V36e(0x0), v1534V36e(0x40)
    0x1538S0x36e: v1538V36e = SLOAD v1537V36e
    0x153bS0x36e: v153bV36e(0x0) = CONST 
    0x153dS0x36e: v153dV36e(0x1) = CONST 
    0x153fS0x36e: v153fV36e(0x0) = CONST 
    0x1541S0x36e: v1541V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = CONST 
    0x1556S0x36e: v1556V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x156bS0x36e: v156bV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v1556V36e(0xffffffffffffffffffffffffffffffffffffffff), v1541V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x156cS0x36e: v156cV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1581S0x36e: v1581V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v156cV36e(0xffffffffffffffffffffffffffffffffffffffff), v156bV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x1583S0x36e: MSTORE v153fV36e(0x0), v1581V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x1584S0x36e: v1584V36e(0x20) = CONST 
    0x1586S0x36e: v1586V36e(0x20) = ADD v1584V36e(0x20), v153fV36e(0x0)
    0x1589S0x36e: MSTORE v1586V36e(0x20), v153dV36e(0x1)
    0x158aS0x36e: v158aV36e(0x20) = CONST 
    0x158cS0x36e: v158cV36e(0x40) = ADD v158aV36e(0x20), v1586V36e(0x20)
    0x158dS0x36e: v158dV36e(0x0) = CONST 
    0x158fS0x36e: v158fV36e = SHA3 v158dV36e(0x0), v158cV36e(0x40)
    0x1590S0x36e: v1590V36e(0x0) = CONST 
    0x1592S0x36e: v1592V36e(0x5c2aad81) = CONST 
    0x1597S0x36e: v1597V36e(0xffffffffffffffff) = CONST 
    0x15a0S0x36e: v15a0V36e(0x5c2aad81) = AND v1597V36e(0xffffffffffffffff), v1592V36e(0x5c2aad81)
    0x15a2S0x36e: MSTORE v1590V36e(0x0), v15a0V36e(0x5c2aad81)
    0x15a3S0x36e: v15a3V36e(0x20) = CONST 
    0x15a5S0x36e: v15a5V36e(0x20) = ADD v15a3V36e(0x20), v1590V36e(0x0)
    0x15a8S0x36e: MSTORE v15a5V36e(0x20), v158fV36e
    0x15a9S0x36e: v15a9V36e(0x20) = CONST 
    0x15abS0x36e: v15abV36e(0x40) = ADD v15a9V36e(0x20), v15a5V36e(0x20)
    0x15acS0x36e: v15acV36e(0x0) = CONST 
    0x15aeS0x36e: v15aeV36e = SHA3 v15acV36e(0x0), v15abV36e(0x40)
    0x15b1S0x36e: SSTORE v15aeV36e, v153bV36e(0x0)
    0x15b3S0x36e: v15b3V36e(0x1618) = CONST 
    0x15b7S0x36e: v15b7V36e(0x3) = CONST 
    0x15b9S0x36e: v15b9V36e(0x0) = CONST 
    0x15bbS0x36e: v15bbV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = CONST 
    0x15d0S0x36e: v15d0V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15e5S0x36e: v15e5V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v15d0V36e(0xffffffffffffffffffffffffffffffffffffffff), v15bbV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x15e6S0x36e: v15e6V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15fbS0x36e: v15fbV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v15e6V36e(0xffffffffffffffffffffffffffffffffffffffff), v15e5V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x15fdS0x36e: MSTORE v15b9V36e(0x0), v15fbV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x15feS0x36e: v15feV36e(0x20) = CONST 
    0x1600S0x36e: v1600V36e(0x20) = ADD v15feV36e(0x20), v15b9V36e(0x0)
    0x1603S0x36e: MSTORE v1600V36e(0x20), v15b7V36e(0x3)
    0x1604S0x36e: v1604V36e(0x20) = CONST 
    0x1606S0x36e: v1606V36e(0x40) = ADD v1604V36e(0x20), v1600V36e(0x20)
    0x1607S0x36e: v1607V36e(0x0) = CONST 
    0x1609S0x36e: v1609V36e = SHA3 v1607V36e(0x0), v1606V36e(0x40)
    0x160aS0x36e: v160aV36e = SLOAD v1609V36e
    0x160bS0x36e: v160bV36e(0x31d8) = CONST 
    0x1611S0x36e: v1611V36e(0xffffffff) = CONST 
    0x1616S0x36e: v1616V36e(0x31d8) = AND v1611V36e(0xffffffff), v160bV36e(0x31d8)
    0x1617S0x36e: v1617_0V36e = CALLPRIVATE v1616V36e(0x31d8), v1538V36e, v160aV36e, v15b3V36e(0x1618)

    Begin block 0x1618B0x36e
    prev=[0x146eB0x36e], succ=[0x17c2B0x36e]
    =================================
    0x1619S0x36e: v1619V36e(0x3) = CONST 
    0x161bS0x36e: v161bV36e(0x0) = CONST 
    0x161dS0x36e: v161dV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = CONST 
    0x1632S0x36e: v1632V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1647S0x36e: v1647V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v1632V36e(0xffffffffffffffffffffffffffffffffffffffff), v161dV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x1648S0x36e: v1648V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x165dS0x36e: v165dV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398) = AND v1648V36e(0xffffffffffffffffffffffffffffffffffffffff), v1647V36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x165fS0x36e: MSTORE v161bV36e(0x0), v165dV36e(0x61c3b0fc6c6ee51df1972c5f8dce4663e573a398)
    0x1660S0x36e: v1660V36e(0x20) = CONST 
    0x1662S0x36e: v1662V36e(0x20) = ADD v1660V36e(0x20), v161bV36e(0x0)
    0x1665S0x36e: MSTORE v1662V36e(0x20), v1619V36e(0x3)
    0x1666S0x36e: v1666V36e(0x20) = CONST 
    0x1668S0x36e: v1668V36e(0x40) = ADD v1666V36e(0x20), v1662V36e(0x20)
    0x1669S0x36e: v1669V36e(0x0) = CONST 
    0x166bS0x36e: v166bV36e = SHA3 v1669V36e(0x0), v1668V36e(0x40)
    0x166eS0x36e: SSTORE v166bV36e, v1617_0V36e
    0x1670S0x36e: v1670V36e(0x1) = CONST 
    0x1672S0x36e: v1672V36e(0x0) = CONST 
    0x1674S0x36e: v1674V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = CONST 
    0x1689S0x36e: v1689V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x169eS0x36e: v169eV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v1689V36e(0xffffffffffffffffffffffffffffffffffffffff), v1674V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x169fS0x36e: v169fV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16b4S0x36e: v16b4V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v169fV36e(0xffffffffffffffffffffffffffffffffffffffff), v169eV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x16b6S0x36e: MSTORE v1672V36e(0x0), v16b4V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x16b7S0x36e: v16b7V36e(0x20) = CONST 
    0x16b9S0x36e: v16b9V36e(0x20) = ADD v16b7V36e(0x20), v1672V36e(0x0)
    0x16bcS0x36e: MSTORE v16b9V36e(0x20), v1670V36e(0x1)
    0x16bdS0x36e: v16bdV36e(0x20) = CONST 
    0x16bfS0x36e: v16bfV36e(0x40) = ADD v16bdV36e(0x20), v16b9V36e(0x20)
    0x16c0S0x36e: v16c0V36e(0x0) = CONST 
    0x16c2S0x36e: v16c2V36e = SHA3 v16c0V36e(0x0), v16bfV36e(0x40)
    0x16c3S0x36e: v16c3V36e(0x0) = CONST 
    0x16c5S0x36e: v16c5V36e(0x5c2aad81) = CONST 
    0x16caS0x36e: v16caV36e(0xffffffffffffffff) = CONST 
    0x16d3S0x36e: v16d3V36e(0x5c2aad81) = AND v16caV36e(0xffffffffffffffff), v16c5V36e(0x5c2aad81)
    0x16d5S0x36e: MSTORE v16c3V36e(0x0), v16d3V36e(0x5c2aad81)
    0x16d6S0x36e: v16d6V36e(0x20) = CONST 
    0x16d8S0x36e: v16d8V36e(0x20) = ADD v16d6V36e(0x20), v16c3V36e(0x0)
    0x16dbS0x36e: MSTORE v16d8V36e(0x20), v16c2V36e
    0x16dcS0x36e: v16dcV36e(0x20) = CONST 
    0x16deS0x36e: v16deV36e(0x40) = ADD v16dcV36e(0x20), v16d8V36e(0x20)
    0x16dfS0x36e: v16dfV36e(0x0) = CONST 
    0x16e1S0x36e: v16e1V36e = SHA3 v16dfV36e(0x0), v16deV36e(0x40)
    0x16e2S0x36e: v16e2V36e = SLOAD v16e1V36e
    0x16e5S0x36e: v16e5V36e(0x0) = CONST 
    0x16e7S0x36e: v16e7V36e(0x1) = CONST 
    0x16e9S0x36e: v16e9V36e(0x0) = CONST 
    0x16ebS0x36e: v16ebV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = CONST 
    0x1700S0x36e: v1700V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1715S0x36e: v1715V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v1700V36e(0xffffffffffffffffffffffffffffffffffffffff), v16ebV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x1716S0x36e: v1716V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x172bS0x36e: v172bV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v1716V36e(0xffffffffffffffffffffffffffffffffffffffff), v1715V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x172dS0x36e: MSTORE v16e9V36e(0x0), v172bV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x172eS0x36e: v172eV36e(0x20) = CONST 
    0x1730S0x36e: v1730V36e(0x20) = ADD v172eV36e(0x20), v16e9V36e(0x0)
    0x1733S0x36e: MSTORE v1730V36e(0x20), v16e7V36e(0x1)
    0x1734S0x36e: v1734V36e(0x20) = CONST 
    0x1736S0x36e: v1736V36e(0x40) = ADD v1734V36e(0x20), v1730V36e(0x20)
    0x1737S0x36e: v1737V36e(0x0) = CONST 
    0x1739S0x36e: v1739V36e = SHA3 v1737V36e(0x0), v1736V36e(0x40)
    0x173aS0x36e: v173aV36e(0x0) = CONST 
    0x173cS0x36e: v173cV36e(0x5c2aad81) = CONST 
    0x1741S0x36e: v1741V36e(0xffffffffffffffff) = CONST 
    0x174aS0x36e: v174aV36e(0x5c2aad81) = AND v1741V36e(0xffffffffffffffff), v173cV36e(0x5c2aad81)
    0x174cS0x36e: MSTORE v173aV36e(0x0), v174aV36e(0x5c2aad81)
    0x174dS0x36e: v174dV36e(0x20) = CONST 
    0x174fS0x36e: v174fV36e(0x20) = ADD v174dV36e(0x20), v173aV36e(0x0)
    0x1752S0x36e: MSTORE v174fV36e(0x20), v1739V36e
    0x1753S0x36e: v1753V36e(0x20) = CONST 
    0x1755S0x36e: v1755V36e(0x40) = ADD v1753V36e(0x20), v174fV36e(0x20)
    0x1756S0x36e: v1756V36e(0x0) = CONST 
    0x1758S0x36e: v1758V36e = SHA3 v1756V36e(0x0), v1755V36e(0x40)
    0x175bS0x36e: SSTORE v1758V36e, v16e5V36e(0x0)
    0x175dS0x36e: v175dV36e(0x17c2) = CONST 
    0x1761S0x36e: v1761V36e(0x3) = CONST 
    0x1763S0x36e: v1763V36e(0x0) = CONST 
    0x1765S0x36e: v1765V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = CONST 
    0x177aS0x36e: v177aV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x178fS0x36e: v178fV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v177aV36e(0xffffffffffffffffffffffffffffffffffffffff), v1765V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x1790S0x36e: v1790V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17a5S0x36e: v17a5V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v1790V36e(0xffffffffffffffffffffffffffffffffffffffff), v178fV36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x17a7S0x36e: MSTORE v1763V36e(0x0), v17a5V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x17a8S0x36e: v17a8V36e(0x20) = CONST 
    0x17aaS0x36e: v17aaV36e(0x20) = ADD v17a8V36e(0x20), v1763V36e(0x0)
    0x17adS0x36e: MSTORE v17aaV36e(0x20), v1761V36e(0x3)
    0x17aeS0x36e: v17aeV36e(0x20) = CONST 
    0x17b0S0x36e: v17b0V36e(0x40) = ADD v17aeV36e(0x20), v17aaV36e(0x20)
    0x17b1S0x36e: v17b1V36e(0x0) = CONST 
    0x17b3S0x36e: v17b3V36e = SHA3 v17b1V36e(0x0), v17b0V36e(0x40)
    0x17b4S0x36e: v17b4V36e = SLOAD v17b3V36e
    0x17b5S0x36e: v17b5V36e(0x31d8) = CONST 
    0x17bbS0x36e: v17bbV36e(0xffffffff) = CONST 
    0x17c0S0x36e: v17c0V36e(0x31d8) = AND v17bbV36e(0xffffffff), v17b5V36e(0x31d8)
    0x17c1S0x36e: v17c1_0V36e = CALLPRIVATE v17c0V36e(0x31d8), v16e2V36e, v17b4V36e, v175dV36e(0x17c2)

    Begin block 0x17c2B0x36e
    prev=[0x1618B0x36e], succ=[0x196cB0x36e]
    =================================
    0x17c3S0x36e: v17c3V36e(0x3) = CONST 
    0x17c5S0x36e: v17c5V36e(0x0) = CONST 
    0x17c7S0x36e: v17c7V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = CONST 
    0x17dcS0x36e: v17dcV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17f1S0x36e: v17f1V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v17dcV36e(0xffffffffffffffffffffffffffffffffffffffff), v17c7V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x17f2S0x36e: v17f2V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1807S0x36e: v1807V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104) = AND v17f2V36e(0xffffffffffffffffffffffffffffffffffffffff), v17f1V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x1809S0x36e: MSTORE v17c5V36e(0x0), v1807V36e(0x51d8cc55d6bfc41676a64fefa6bbac56b61a7104)
    0x180aS0x36e: v180aV36e(0x20) = CONST 
    0x180cS0x36e: v180cV36e(0x20) = ADD v180aV36e(0x20), v17c5V36e(0x0)
    0x180fS0x36e: MSTORE v180cV36e(0x20), v17c3V36e(0x3)
    0x1810S0x36e: v1810V36e(0x20) = CONST 
    0x1812S0x36e: v1812V36e(0x40) = ADD v1810V36e(0x20), v180cV36e(0x20)
    0x1813S0x36e: v1813V36e(0x0) = CONST 
    0x1815S0x36e: v1815V36e = SHA3 v1813V36e(0x0), v1812V36e(0x40)
    0x1818S0x36e: SSTORE v1815V36e, v17c1_0V36e
    0x181aS0x36e: v181aV36e(0x1) = CONST 
    0x181cS0x36e: v181cV36e(0x0) = CONST 
    0x181eS0x36e: v181eV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = CONST 
    0x1833S0x36e: v1833V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1848S0x36e: v1848V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v1833V36e(0xffffffffffffffffffffffffffffffffffffffff), v181eV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x1849S0x36e: v1849V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x185eS0x36e: v185eV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v1849V36e(0xffffffffffffffffffffffffffffffffffffffff), v1848V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x1860S0x36e: MSTORE v181cV36e(0x0), v185eV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x1861S0x36e: v1861V36e(0x20) = CONST 
    0x1863S0x36e: v1863V36e(0x20) = ADD v1861V36e(0x20), v181cV36e(0x0)
    0x1866S0x36e: MSTORE v1863V36e(0x20), v181aV36e(0x1)
    0x1867S0x36e: v1867V36e(0x20) = CONST 
    0x1869S0x36e: v1869V36e(0x40) = ADD v1867V36e(0x20), v1863V36e(0x20)
    0x186aS0x36e: v186aV36e(0x0) = CONST 
    0x186cS0x36e: v186cV36e = SHA3 v186aV36e(0x0), v1869V36e(0x40)
    0x186dS0x36e: v186dV36e(0x0) = CONST 
    0x186fS0x36e: v186fV36e(0x5c2aad81) = CONST 
    0x1874S0x36e: v1874V36e(0xffffffffffffffff) = CONST 
    0x187dS0x36e: v187dV36e(0x5c2aad81) = AND v1874V36e(0xffffffffffffffff), v186fV36e(0x5c2aad81)
    0x187fS0x36e: MSTORE v186dV36e(0x0), v187dV36e(0x5c2aad81)
    0x1880S0x36e: v1880V36e(0x20) = CONST 
    0x1882S0x36e: v1882V36e(0x20) = ADD v1880V36e(0x20), v186dV36e(0x0)
    0x1885S0x36e: MSTORE v1882V36e(0x20), v186cV36e
    0x1886S0x36e: v1886V36e(0x20) = CONST 
    0x1888S0x36e: v1888V36e(0x40) = ADD v1886V36e(0x20), v1882V36e(0x20)
    0x1889S0x36e: v1889V36e(0x0) = CONST 
    0x188bS0x36e: v188bV36e = SHA3 v1889V36e(0x0), v1888V36e(0x40)
    0x188cS0x36e: v188cV36e = SLOAD v188bV36e
    0x188fS0x36e: v188fV36e(0x0) = CONST 
    0x1891S0x36e: v1891V36e(0x1) = CONST 
    0x1893S0x36e: v1893V36e(0x0) = CONST 
    0x1895S0x36e: v1895V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = CONST 
    0x18aaS0x36e: v18aaV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18bfS0x36e: v18bfV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v18aaV36e(0xffffffffffffffffffffffffffffffffffffffff), v1895V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x18c0S0x36e: v18c0V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18d5S0x36e: v18d5V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v18c0V36e(0xffffffffffffffffffffffffffffffffffffffff), v18bfV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x18d7S0x36e: MSTORE v1893V36e(0x0), v18d5V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x18d8S0x36e: v18d8V36e(0x20) = CONST 
    0x18daS0x36e: v18daV36e(0x20) = ADD v18d8V36e(0x20), v1893V36e(0x0)
    0x18ddS0x36e: MSTORE v18daV36e(0x20), v1891V36e(0x1)
    0x18deS0x36e: v18deV36e(0x20) = CONST 
    0x18e0S0x36e: v18e0V36e(0x40) = ADD v18deV36e(0x20), v18daV36e(0x20)
    0x18e1S0x36e: v18e1V36e(0x0) = CONST 
    0x18e3S0x36e: v18e3V36e = SHA3 v18e1V36e(0x0), v18e0V36e(0x40)
    0x18e4S0x36e: v18e4V36e(0x0) = CONST 
    0x18e6S0x36e: v18e6V36e(0x5c2aad81) = CONST 
    0x18ebS0x36e: v18ebV36e(0xffffffffffffffff) = CONST 
    0x18f4S0x36e: v18f4V36e(0x5c2aad81) = AND v18ebV36e(0xffffffffffffffff), v18e6V36e(0x5c2aad81)
    0x18f6S0x36e: MSTORE v18e4V36e(0x0), v18f4V36e(0x5c2aad81)
    0x18f7S0x36e: v18f7V36e(0x20) = CONST 
    0x18f9S0x36e: v18f9V36e(0x20) = ADD v18f7V36e(0x20), v18e4V36e(0x0)
    0x18fcS0x36e: MSTORE v18f9V36e(0x20), v18e3V36e
    0x18fdS0x36e: v18fdV36e(0x20) = CONST 
    0x18ffS0x36e: v18ffV36e(0x40) = ADD v18fdV36e(0x20), v18f9V36e(0x20)
    0x1900S0x36e: v1900V36e(0x0) = CONST 
    0x1902S0x36e: v1902V36e = SHA3 v1900V36e(0x0), v18ffV36e(0x40)
    0x1905S0x36e: SSTORE v1902V36e, v188fV36e(0x0)
    0x1907S0x36e: v1907V36e(0x196c) = CONST 
    0x190bS0x36e: v190bV36e(0x3) = CONST 
    0x190dS0x36e: v190dV36e(0x0) = CONST 
    0x190fS0x36e: v190fV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = CONST 
    0x1924S0x36e: v1924V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1939S0x36e: v1939V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v1924V36e(0xffffffffffffffffffffffffffffffffffffffff), v190fV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x193aS0x36e: v193aV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x194fS0x36e: v194fV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v193aV36e(0xffffffffffffffffffffffffffffffffffffffff), v1939V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x1951S0x36e: MSTORE v190dV36e(0x0), v194fV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x1952S0x36e: v1952V36e(0x20) = CONST 
    0x1954S0x36e: v1954V36e(0x20) = ADD v1952V36e(0x20), v190dV36e(0x0)
    0x1957S0x36e: MSTORE v1954V36e(0x20), v190bV36e(0x3)
    0x1958S0x36e: v1958V36e(0x20) = CONST 
    0x195aS0x36e: v195aV36e(0x40) = ADD v1958V36e(0x20), v1954V36e(0x20)
    0x195bS0x36e: v195bV36e(0x0) = CONST 
    0x195dS0x36e: v195dV36e = SHA3 v195bV36e(0x0), v195aV36e(0x40)
    0x195eS0x36e: v195eV36e = SLOAD v195dV36e
    0x195fS0x36e: v195fV36e(0x31d8) = CONST 
    0x1965S0x36e: v1965V36e(0xffffffff) = CONST 
    0x196aS0x36e: v196aV36e(0x31d8) = AND v1965V36e(0xffffffff), v195fV36e(0x31d8)
    0x196bS0x36e: v196b_0V36e = CALLPRIVATE v196aV36e(0x31d8), v188cV36e, v195eV36e, v1907V36e(0x196c)

    Begin block 0x196cB0x36e
    prev=[0x17c2B0x36e], succ=[0x1d39B0x36e]
    =================================
    0x196dS0x36e: v196dV36e(0x3) = CONST 
    0x196fS0x36e: v196fV36e(0x0) = CONST 
    0x1971S0x36e: v1971V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = CONST 
    0x1986S0x36e: v1986V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x199bS0x36e: v199bV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v1986V36e(0xffffffffffffffffffffffffffffffffffffffff), v1971V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x199cS0x36e: v199cV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19b1S0x36e: v19b1V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047) = AND v199cV36e(0xffffffffffffffffffffffffffffffffffffffff), v199bV36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x19b3S0x36e: MSTORE v196fV36e(0x0), v19b1V36e(0xfbfbf95152fcc8901974d35ab0aef172445b3047)
    0x19b4S0x36e: v19b4V36e(0x20) = CONST 
    0x19b6S0x36e: v19b6V36e(0x20) = ADD v19b4V36e(0x20), v196fV36e(0x0)
    0x19b9S0x36e: MSTORE v19b6V36e(0x20), v196dV36e(0x3)
    0x19baS0x36e: v19baV36e(0x20) = CONST 
    0x19bcS0x36e: v19bcV36e(0x40) = ADD v19baV36e(0x20), v19b6V36e(0x20)
    0x19bdS0x36e: v19bdV36e(0x0) = CONST 
    0x19bfS0x36e: v19bfV36e = SHA3 v19bdV36e(0x0), v19bcV36e(0x40)
    0x19c2S0x36e: SSTORE v19bfV36e, v196b_0V36e
    0x19c4S0x36e: v19c4V36e(0x1d39) = CONST 
    0x19c7S0x36e: JUMP v19c4V36e(0x1d39)

    Begin block 0x1d39B0x36e
    prev=[0x196cB0x36e, 0x1d38B0x36e], succ=[0x377]
    =================================
    0x1d3cS0x36e: JUMP v370(0x377)

    Begin block 0x377
    prev=[0x1d39B0x36e], succ=[]
    =================================
    0x378: STOP 

    Begin block 0x19c8B0x36e
    prev=[0xfb1B0x36e], succ=[0x19dfB0x36e, 0x1b8dB0x36e]
    =================================
    0x19c9S0x36e: v19c9V36e(0x5fee6601) = CONST 
    0x19cfS0x36e: v19cfV36e(0xffffffffffffffff) = CONST 
    0x19d8S0x36e: v19d8V36e = AND v19cfV36e(0xffffffffffffffff), vf92V36e
    0x19d9S0x36e: v19d9V36e = LT v19d8V36e, v19c9V36e(0x5fee6601)
    0x19daS0x36e: v19daV36e = ISZERO v19d9V36e
    0x19dbS0x36e: v19dbV36e(0x1b8d) = CONST 
    0x19deS0x36e: JUMPI v19dbV36e(0x1b8d), v19daV36e

    Begin block 0x19dfB0x36e
    prev=[0x19c8B0x36e], succ=[0x1b31B0x36e]
    =================================
    0x19dfS0x36e: v19dfV36e(0x1) = CONST 
    0x19e1S0x36e: v19e1V36e(0x0) = CONST 
    0x19e3S0x36e: v19e3V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x19f8S0x36e: v19f8V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a0dS0x36e: v1a0dV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v19f8V36e(0xffffffffffffffffffffffffffffffffffffffff), v19e3V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1a0eS0x36e: v1a0eV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a23S0x36e: v1a23V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1a0eV36e(0xffffffffffffffffffffffffffffffffffffffff), v1a0dV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1a25S0x36e: MSTORE v19e1V36e(0x0), v1a23V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1a26S0x36e: v1a26V36e(0x20) = CONST 
    0x1a28S0x36e: v1a28V36e(0x20) = ADD v1a26V36e(0x20), v19e1V36e(0x0)
    0x1a2bS0x36e: MSTORE v1a28V36e(0x20), v19dfV36e(0x1)
    0x1a2cS0x36e: v1a2cV36e(0x20) = CONST 
    0x1a2eS0x36e: v1a2eV36e(0x40) = ADD v1a2cV36e(0x20), v1a28V36e(0x20)
    0x1a2fS0x36e: v1a2fV36e(0x0) = CONST 
    0x1a31S0x36e: v1a31V36e = SHA3 v1a2fV36e(0x0), v1a2eV36e(0x40)
    0x1a32S0x36e: v1a32V36e(0x0) = CONST 
    0x1a34S0x36e: v1a34V36e(0x5e0be101) = CONST 
    0x1a39S0x36e: v1a39V36e(0xffffffffffffffff) = CONST 
    0x1a42S0x36e: v1a42V36e(0x5e0be101) = AND v1a39V36e(0xffffffffffffffff), v1a34V36e(0x5e0be101)
    0x1a44S0x36e: MSTORE v1a32V36e(0x0), v1a42V36e(0x5e0be101)
    0x1a45S0x36e: v1a45V36e(0x20) = CONST 
    0x1a47S0x36e: v1a47V36e(0x20) = ADD v1a45V36e(0x20), v1a32V36e(0x0)
    0x1a4aS0x36e: MSTORE v1a47V36e(0x20), v1a31V36e
    0x1a4bS0x36e: v1a4bV36e(0x20) = CONST 
    0x1a4dS0x36e: v1a4dV36e(0x40) = ADD v1a4bV36e(0x20), v1a47V36e(0x20)
    0x1a4eS0x36e: v1a4eV36e(0x0) = CONST 
    0x1a50S0x36e: v1a50V36e = SHA3 v1a4eV36e(0x0), v1a4dV36e(0x40)
    0x1a51S0x36e: v1a51V36e = SLOAD v1a50V36e
    0x1a54S0x36e: v1a54V36e(0x0) = CONST 
    0x1a56S0x36e: v1a56V36e(0x1) = CONST 
    0x1a58S0x36e: v1a58V36e(0x0) = CONST 
    0x1a5aS0x36e: v1a5aV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1a6fS0x36e: v1a6fV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a84S0x36e: v1a84V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1a6fV36e(0xffffffffffffffffffffffffffffffffffffffff), v1a5aV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1a85S0x36e: v1a85V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a9aS0x36e: v1a9aV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1a85V36e(0xffffffffffffffffffffffffffffffffffffffff), v1a84V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1a9cS0x36e: MSTORE v1a58V36e(0x0), v1a9aV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1a9dS0x36e: v1a9dV36e(0x20) = CONST 
    0x1a9fS0x36e: v1a9fV36e(0x20) = ADD v1a9dV36e(0x20), v1a58V36e(0x0)
    0x1aa2S0x36e: MSTORE v1a9fV36e(0x20), v1a56V36e(0x1)
    0x1aa3S0x36e: v1aa3V36e(0x20) = CONST 
    0x1aa5S0x36e: v1aa5V36e(0x40) = ADD v1aa3V36e(0x20), v1a9fV36e(0x20)
    0x1aa6S0x36e: v1aa6V36e(0x0) = CONST 
    0x1aa8S0x36e: v1aa8V36e = SHA3 v1aa6V36e(0x0), v1aa5V36e(0x40)
    0x1aa9S0x36e: v1aa9V36e(0x0) = CONST 
    0x1aabS0x36e: v1aabV36e(0x5e0be101) = CONST 
    0x1ab0S0x36e: v1ab0V36e(0xffffffffffffffff) = CONST 
    0x1ab9S0x36e: v1ab9V36e(0x5e0be101) = AND v1ab0V36e(0xffffffffffffffff), v1aabV36e(0x5e0be101)
    0x1abbS0x36e: MSTORE v1aa9V36e(0x0), v1ab9V36e(0x5e0be101)
    0x1abcS0x36e: v1abcV36e(0x20) = CONST 
    0x1abeS0x36e: v1abeV36e(0x20) = ADD v1abcV36e(0x20), v1aa9V36e(0x0)
    0x1ac1S0x36e: MSTORE v1abeV36e(0x20), v1aa8V36e
    0x1ac2S0x36e: v1ac2V36e(0x20) = CONST 
    0x1ac4S0x36e: v1ac4V36e(0x40) = ADD v1ac2V36e(0x20), v1abeV36e(0x20)
    0x1ac5S0x36e: v1ac5V36e(0x0) = CONST 
    0x1ac7S0x36e: v1ac7V36e = SHA3 v1ac5V36e(0x0), v1ac4V36e(0x40)
    0x1acaS0x36e: SSTORE v1ac7V36e, v1a54V36e(0x0)
    0x1accS0x36e: v1accV36e(0x1b31) = CONST 
    0x1ad0S0x36e: v1ad0V36e(0x3) = CONST 
    0x1ad2S0x36e: v1ad2V36e(0x0) = CONST 
    0x1ad4S0x36e: v1ad4V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1ae9S0x36e: v1ae9V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1afeS0x36e: v1afeV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1ae9V36e(0xffffffffffffffffffffffffffffffffffffffff), v1ad4V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1affS0x36e: v1affV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b14S0x36e: v1b14V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1affV36e(0xffffffffffffffffffffffffffffffffffffffff), v1afeV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1b16S0x36e: MSTORE v1ad2V36e(0x0), v1b14V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1b17S0x36e: v1b17V36e(0x20) = CONST 
    0x1b19S0x36e: v1b19V36e(0x20) = ADD v1b17V36e(0x20), v1ad2V36e(0x0)
    0x1b1cS0x36e: MSTORE v1b19V36e(0x20), v1ad0V36e(0x3)
    0x1b1dS0x36e: v1b1dV36e(0x20) = CONST 
    0x1b1fS0x36e: v1b1fV36e(0x40) = ADD v1b1dV36e(0x20), v1b19V36e(0x20)
    0x1b20S0x36e: v1b20V36e(0x0) = CONST 
    0x1b22S0x36e: v1b22V36e = SHA3 v1b20V36e(0x0), v1b1fV36e(0x40)
    0x1b23S0x36e: v1b23V36e = SLOAD v1b22V36e
    0x1b24S0x36e: v1b24V36e(0x31d8) = CONST 
    0x1b2aS0x36e: v1b2aV36e(0xffffffff) = CONST 
    0x1b2fS0x36e: v1b2fV36e(0x31d8) = AND v1b2aV36e(0xffffffff), v1b24V36e(0x31d8)
    0x1b30S0x36e: v1b30_0V36e = CALLPRIVATE v1b2fV36e(0x31d8), v1a51V36e, v1b23V36e, v1accV36e(0x1b31)

    Begin block 0x1b31B0x36e
    prev=[0x19dfB0x36e], succ=[0x1d38B0x36e]
    =================================
    0x1b32S0x36e: v1b32V36e(0x3) = CONST 
    0x1b34S0x36e: v1b34V36e(0x0) = CONST 
    0x1b36S0x36e: v1b36V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1b4bS0x36e: v1b4bV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b60S0x36e: v1b60V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1b4bV36e(0xffffffffffffffffffffffffffffffffffffffff), v1b36V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1b61S0x36e: v1b61V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b76S0x36e: v1b76V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1b61V36e(0xffffffffffffffffffffffffffffffffffffffff), v1b60V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1b78S0x36e: MSTORE v1b34V36e(0x0), v1b76V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1b79S0x36e: v1b79V36e(0x20) = CONST 
    0x1b7bS0x36e: v1b7bV36e(0x20) = ADD v1b79V36e(0x20), v1b34V36e(0x0)
    0x1b7eS0x36e: MSTORE v1b7bV36e(0x20), v1b32V36e(0x3)
    0x1b7fS0x36e: v1b7fV36e(0x20) = CONST 
    0x1b81S0x36e: v1b81V36e(0x40) = ADD v1b7fV36e(0x20), v1b7bV36e(0x20)
    0x1b82S0x36e: v1b82V36e(0x0) = CONST 
    0x1b84S0x36e: v1b84V36e = SHA3 v1b82V36e(0x0), v1b81V36e(0x40)
    0x1b87S0x36e: SSTORE v1b84V36e, v1b30_0V36e
    0x1b89S0x36e: v1b89V36e(0x1d38) = CONST 
    0x1b8cS0x36e: JUMP v1b89V36e(0x1d38)

    Begin block 0x1d38B0x36e
    prev=[0x1b31B0x36e, 0x1ce0B0x36e], succ=[0x1d39B0x36e]
    =================================

    Begin block 0x1b8dB0x36e
    prev=[0x19c8B0x36e], succ=[0x1ce0B0x36e]
    =================================
    0x1b8eS0x36e: v1b8eV36e(0x1) = CONST 
    0x1b90S0x36e: v1b90V36e(0x0) = CONST 
    0x1b92S0x36e: v1b92V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1ba7S0x36e: v1ba7V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1bbcS0x36e: v1bbcV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1ba7V36e(0xffffffffffffffffffffffffffffffffffffffff), v1b92V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1bbdS0x36e: v1bbdV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1bd2S0x36e: v1bd2V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1bbdV36e(0xffffffffffffffffffffffffffffffffffffffff), v1bbcV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1bd4S0x36e: MSTORE v1b90V36e(0x0), v1bd2V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1bd5S0x36e: v1bd5V36e(0x20) = CONST 
    0x1bd7S0x36e: v1bd7V36e(0x20) = ADD v1bd5V36e(0x20), v1b90V36e(0x0)
    0x1bdaS0x36e: MSTORE v1bd7V36e(0x20), v1b8eV36e(0x1)
    0x1bdbS0x36e: v1bdbV36e(0x20) = CONST 
    0x1bddS0x36e: v1bddV36e(0x40) = ADD v1bdbV36e(0x20), v1bd7V36e(0x20)
    0x1bdeS0x36e: v1bdeV36e(0x0) = CONST 
    0x1be0S0x36e: v1be0V36e = SHA3 v1bdeV36e(0x0), v1bddV36e(0x40)
    0x1be1S0x36e: v1be1V36e(0x0) = CONST 
    0x1be3S0x36e: v1be3V36e(0x5fee6601) = CONST 
    0x1be8S0x36e: v1be8V36e(0xffffffffffffffff) = CONST 
    0x1bf1S0x36e: v1bf1V36e(0x5fee6601) = AND v1be8V36e(0xffffffffffffffff), v1be3V36e(0x5fee6601)
    0x1bf3S0x36e: MSTORE v1be1V36e(0x0), v1bf1V36e(0x5fee6601)
    0x1bf4S0x36e: v1bf4V36e(0x20) = CONST 
    0x1bf6S0x36e: v1bf6V36e(0x20) = ADD v1bf4V36e(0x20), v1be1V36e(0x0)
    0x1bf9S0x36e: MSTORE v1bf6V36e(0x20), v1be0V36e
    0x1bfaS0x36e: v1bfaV36e(0x20) = CONST 
    0x1bfcS0x36e: v1bfcV36e(0x40) = ADD v1bfaV36e(0x20), v1bf6V36e(0x20)
    0x1bfdS0x36e: v1bfdV36e(0x0) = CONST 
    0x1bffS0x36e: v1bffV36e = SHA3 v1bfdV36e(0x0), v1bfcV36e(0x40)
    0x1c00S0x36e: v1c00V36e = SLOAD v1bffV36e
    0x1c03S0x36e: v1c03V36e(0x0) = CONST 
    0x1c05S0x36e: v1c05V36e(0x1) = CONST 
    0x1c07S0x36e: v1c07V36e(0x0) = CONST 
    0x1c09S0x36e: v1c09V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1c1eS0x36e: v1c1eV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c33S0x36e: v1c33V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1c1eV36e(0xffffffffffffffffffffffffffffffffffffffff), v1c09V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1c34S0x36e: v1c34V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c49S0x36e: v1c49V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1c34V36e(0xffffffffffffffffffffffffffffffffffffffff), v1c33V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1c4bS0x36e: MSTORE v1c07V36e(0x0), v1c49V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1c4cS0x36e: v1c4cV36e(0x20) = CONST 
    0x1c4eS0x36e: v1c4eV36e(0x20) = ADD v1c4cV36e(0x20), v1c07V36e(0x0)
    0x1c51S0x36e: MSTORE v1c4eV36e(0x20), v1c05V36e(0x1)
    0x1c52S0x36e: v1c52V36e(0x20) = CONST 
    0x1c54S0x36e: v1c54V36e(0x40) = ADD v1c52V36e(0x20), v1c4eV36e(0x20)
    0x1c55S0x36e: v1c55V36e(0x0) = CONST 
    0x1c57S0x36e: v1c57V36e = SHA3 v1c55V36e(0x0), v1c54V36e(0x40)
    0x1c58S0x36e: v1c58V36e(0x0) = CONST 
    0x1c5aS0x36e: v1c5aV36e(0x5fee6601) = CONST 
    0x1c5fS0x36e: v1c5fV36e(0xffffffffffffffff) = CONST 
    0x1c68S0x36e: v1c68V36e(0x5fee6601) = AND v1c5fV36e(0xffffffffffffffff), v1c5aV36e(0x5fee6601)
    0x1c6aS0x36e: MSTORE v1c58V36e(0x0), v1c68V36e(0x5fee6601)
    0x1c6bS0x36e: v1c6bV36e(0x20) = CONST 
    0x1c6dS0x36e: v1c6dV36e(0x20) = ADD v1c6bV36e(0x20), v1c58V36e(0x0)
    0x1c70S0x36e: MSTORE v1c6dV36e(0x20), v1c57V36e
    0x1c71S0x36e: v1c71V36e(0x20) = CONST 
    0x1c73S0x36e: v1c73V36e(0x40) = ADD v1c71V36e(0x20), v1c6dV36e(0x20)
    0x1c74S0x36e: v1c74V36e(0x0) = CONST 
    0x1c76S0x36e: v1c76V36e = SHA3 v1c74V36e(0x0), v1c73V36e(0x40)
    0x1c79S0x36e: SSTORE v1c76V36e, v1c03V36e(0x0)
    0x1c7bS0x36e: v1c7bV36e(0x1ce0) = CONST 
    0x1c7fS0x36e: v1c7fV36e(0x3) = CONST 
    0x1c81S0x36e: v1c81V36e(0x0) = CONST 
    0x1c83S0x36e: v1c83V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1c98S0x36e: v1c98V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cadS0x36e: v1cadV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1c98V36e(0xffffffffffffffffffffffffffffffffffffffff), v1c83V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1caeS0x36e: v1caeV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cc3S0x36e: v1cc3V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1caeV36e(0xffffffffffffffffffffffffffffffffffffffff), v1cadV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1cc5S0x36e: MSTORE v1c81V36e(0x0), v1cc3V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1cc6S0x36e: v1cc6V36e(0x20) = CONST 
    0x1cc8S0x36e: v1cc8V36e(0x20) = ADD v1cc6V36e(0x20), v1c81V36e(0x0)
    0x1ccbS0x36e: MSTORE v1cc8V36e(0x20), v1c7fV36e(0x3)
    0x1cccS0x36e: v1cccV36e(0x20) = CONST 
    0x1cceS0x36e: v1cceV36e(0x40) = ADD v1cccV36e(0x20), v1cc8V36e(0x20)
    0x1ccfS0x36e: v1ccfV36e(0x0) = CONST 
    0x1cd1S0x36e: v1cd1V36e = SHA3 v1ccfV36e(0x0), v1cceV36e(0x40)
    0x1cd2S0x36e: v1cd2V36e = SLOAD v1cd1V36e
    0x1cd3S0x36e: v1cd3V36e(0x31d8) = CONST 
    0x1cd9S0x36e: v1cd9V36e(0xffffffff) = CONST 
    0x1cdeS0x36e: v1cdeV36e(0x31d8) = AND v1cd9V36e(0xffffffff), v1cd3V36e(0x31d8)
    0x1cdfS0x36e: v1cdf_0V36e = CALLPRIVATE v1cdeV36e(0x31d8), v1c00V36e, v1cd2V36e, v1c7bV36e(0x1ce0)

    Begin block 0x1ce0B0x36e
    prev=[0x1b8dB0x36e], succ=[0x1d38B0x36e]
    =================================
    0x1ce1S0x36e: v1ce1V36e(0x3) = CONST 
    0x1ce3S0x36e: v1ce3V36e(0x0) = CONST 
    0x1ce5S0x36e: v1ce5V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = CONST 
    0x1cfaS0x36e: v1cfaV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d0fS0x36e: v1d0fV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1cfaV36e(0xffffffffffffffffffffffffffffffffffffffff), v1ce5V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1d10S0x36e: v1d10V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d25S0x36e: v1d25V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97) = AND v1d10V36e(0xffffffffffffffffffffffffffffffffffffffff), v1d0fV36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1d27S0x36e: MSTORE v1ce3V36e(0x0), v1d25V36e(0xcd975ce2903cf9f17d924d96d2bc752c06a3bb97)
    0x1d28S0x36e: v1d28V36e(0x20) = CONST 
    0x1d2aS0x36e: v1d2aV36e(0x20) = ADD v1d28V36e(0x20), v1ce3V36e(0x0)
    0x1d2dS0x36e: MSTORE v1d2aV36e(0x20), v1ce1V36e(0x3)
    0x1d2eS0x36e: v1d2eV36e(0x20) = CONST 
    0x1d30S0x36e: v1d30V36e(0x40) = ADD v1d2eV36e(0x20), v1d2aV36e(0x20)
    0x1d31S0x36e: v1d31V36e(0x0) = CONST 
    0x1d33S0x36e: v1d33V36e = SHA3 v1d31V36e(0x0), v1d30V36e(0x40)
    0x1d36S0x36e: SSTORE v1d33V36e, v1cdf_0V36e

    Begin block 0xf42B0x36e
    prev=[0xee9B0x36e], succ=[0xf86B0x36e]
    =================================
    0xf43S0x36e: vf43V36e(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = CONST 
    0xf58S0x36e: vf58V36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf6dS0x36e: vf6dV36e(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = AND vf58V36e(0xffffffffffffffffffffffffffffffffffffffff), vf43V36e(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0xf6eS0x36e: vf6eV36e = CALLER 
    0xf6fS0x36e: vf6fV36e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf84S0x36e: vf84V36e = AND vf6fV36e(0xffffffffffffffffffffffffffffffffffffffff), vf6eV36e
    0xf85S0x36e: vf85V36e = EQ vf84V36e, vf6dV36e(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)

}

function decimals()() public {
    Begin block 0x379
    prev=[], succ=[0x381, 0x385]
    =================================
    0x37a: v37a = CALLVALUE 
    0x37c: v37c = ISZERO v37a
    0x37d: v37d(0x385) = CONST 
    0x380: JUMPI v37d(0x385), v37c

    Begin block 0x381
    prev=[0x379], succ=[]
    =================================
    0x381: v381(0x0) = CONST 
    0x384: REVERT v381(0x0), v381(0x0)

    Begin block 0x385
    prev=[0x379], succ=[0x1d3d]
    =================================
    0x387: v387(0x38e) = CONST 
    0x38a: v38a(0x1d3d) = CONST 
    0x38d: JUMP v38a(0x1d3d)

    Begin block 0x1d3d
    prev=[0x385], succ=[0x38e]
    =================================
    0x1d3e: v1d3e(0x0) = CONST 
    0x1d40: v1d40(0x12) = CONST 
    0x1d45: JUMP v387(0x38e)

    Begin block 0x38e
    prev=[0x1d3d], succ=[]
    =================================
    0x38f: v38f(0x40) = CONST 
    0x391: v391 = MLOAD v38f(0x40)
    0x394: v394(0xff) = CONST 
    0x396: v396(0x12) = AND v394(0xff), v1d40(0x12)
    0x397: v397(0xff) = CONST 
    0x399: v399(0x12) = AND v397(0xff), v396(0x12)
    0x39b: MSTORE v391, v399(0x12)
    0x39c: v39c(0x20) = CONST 
    0x39e: v39e = ADD v39c(0x20), v391
    0x3a2: v3a2(0x40) = CONST 
    0x3a4: v3a4 = MLOAD v3a2(0x40)
    0x3a7: v3a7(0x20) = SUB v39e, v3a4
    0x3a9: RETURN v3a4, v3a7(0x20)

}

function mint(address,uint256)() public {
    Begin block 0x3aa
    prev=[], succ=[0x3b2, 0x3b6]
    =================================
    0x3ab: v3ab = CALLVALUE 
    0x3ad: v3ad = ISZERO v3ab
    0x3ae: v3ae(0x3b6) = CONST 
    0x3b1: JUMPI v3ae(0x3b6), v3ad

    Begin block 0x3b2
    prev=[0x3aa], succ=[]
    =================================
    0x3b2: v3b2(0x0) = CONST 
    0x3b5: REVERT v3b2(0x0), v3b2(0x0)

    Begin block 0x3b6
    prev=[0x3aa], succ=[0x1d46]
    =================================
    0x3b8: v3b8(0x3f5) = CONST 
    0x3bb: v3bb(0x4) = CONST 
    0x3be: v3be = CALLDATASIZE 
    0x3bf: v3bf = SUB v3be, v3bb(0x4)
    0x3c1: v3c1 = ADD v3bb(0x4), v3bf
    0x3c5: v3c5 = CALLDATALOAD v3bb(0x4)
    0x3c6: v3c6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3db: v3db = AND v3c6(0xffffffffffffffffffffffffffffffffffffffff), v3c5
    0x3dd: v3dd(0x20) = CONST 
    0x3df: v3df(0x24) = ADD v3dd(0x20), v3bb(0x4)
    0x3e5: v3e5 = CALLDATALOAD v3df(0x24)
    0x3e7: v3e7(0x20) = CONST 
    0x3e9: v3e9(0x44) = ADD v3e7(0x20), v3df(0x24)
    0x3f1: v3f1(0x1d46) = CONST 
    0x3f4: JUMP v3f1(0x1d46)

    Begin block 0x1d46
    prev=[0x3b6], succ=[0x1de4, 0x1da0]
    =================================
    0x1d47: v1d47(0x0) = CONST 
    0x1d49: v1d49(0x60) = CONST 
    0x1d4b: v1d4b(0x0) = CONST 
    0x1d4f: v1d4f = SLOAD v1d4b(0x0)
    0x1d51: v1d51(0x100) = CONST 
    0x1d54: v1d54(0x1) = EXP v1d51(0x100), v1d4b(0x0)
    0x1d56: v1d56 = DIV v1d4f, v1d54(0x1)
    0x1d57: v1d57(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d6c: v1d6c = AND v1d57(0xffffffffffffffffffffffffffffffffffffffff), v1d56
    0x1d6d: v1d6d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d82: v1d82 = AND v1d6d(0xffffffffffffffffffffffffffffffffffffffff), v1d6c
    0x1d83: v1d83 = CALLER 
    0x1d84: v1d84(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d99: v1d99 = AND v1d84(0xffffffffffffffffffffffffffffffffffffffff), v1d83
    0x1d9a: v1d9a = EQ v1d99, v1d82
    0x1d9c: v1d9c(0x1de4) = CONST 
    0x1d9f: JUMPI v1d9c(0x1de4), v1d9a

    Begin block 0x1de4
    prev=[0x1d46, 0x1da0], succ=[0x1deb, 0x1def]
    =================================
    0x1de4_0x0: v1de4_0 = PHI v1d9a, v1de3
    0x1de5: v1de5 = ISZERO v1de4_0
    0x1de6: v1de6 = ISZERO v1de5
    0x1de7: v1de7(0x1def) = CONST 
    0x1dea: JUMPI v1de7(0x1def), v1de6

    Begin block 0x1deb
    prev=[0x1de4], succ=[]
    =================================
    0x1deb: v1deb(0x0) = CONST 
    0x1dee: REVERT v1deb(0x0), v1deb(0x0)

    Begin block 0x1def
    prev=[0x1de4], succ=[0x1e07, 0x1e0b]
    =================================
    0x1df0: v1df0(0x0) = CONST 
    0x1df2: v1df2(0x14) = CONST 
    0x1df5: v1df5 = SLOAD v1df0(0x0)
    0x1df7: v1df7(0x100) = CONST 
    0x1dfa: v1dfa(0x10000000000000000000000000000000000000000) = EXP v1df7(0x100), v1df2(0x14)
    0x1dfc: v1dfc = DIV v1df5, v1dfa(0x10000000000000000000000000000000000000000)
    0x1dfd: v1dfd(0xff) = CONST 
    0x1dff: v1dff = AND v1dfd(0xff), v1dfc
    0x1e00: v1e00 = ISZERO v1dff
    0x1e01: v1e01 = ISZERO v1e00
    0x1e02: v1e02 = ISZERO v1e01
    0x1e03: v1e03(0x1e0b) = CONST 
    0x1e06: JUMPI v1e03(0x1e0b), v1e02

    Begin block 0x1e07
    prev=[0x1def], succ=[]
    =================================
    0x1e07: v1e07(0x0) = CONST 
    0x1e0a: REVERT v1e07(0x0), v1e07(0x0)

    Begin block 0x1e0b
    prev=[0x1def], succ=[0x1e43, 0x1e47]
    =================================
    0x1e0c: v1e0c(0x0) = CONST 
    0x1e0e: v1e0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e23: v1e23(0x0) = AND v1e0e(0xffffffffffffffffffffffffffffffffffffffff), v1e0c(0x0)
    0x1e25: v1e25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e3a: v1e3a = AND v1e25(0xffffffffffffffffffffffffffffffffffffffff), v3db
    0x1e3b: v1e3b = EQ v1e3a, v1e23(0x0)
    0x1e3c: v1e3c = ISZERO v1e3b
    0x1e3d: v1e3d = ISZERO v1e3c
    0x1e3e: v1e3e = ISZERO v1e3d
    0x1e3f: v1e3f(0x1e47) = CONST 
    0x1e42: JUMPI v1e3f(0x1e47), v1e3e

    Begin block 0x1e43
    prev=[0x1e0b], succ=[]
    =================================
    0x1e43: v1e43(0x0) = CONST 
    0x1e46: REVERT v1e43(0x0), v1e43(0x0)

    Begin block 0x1e47
    prev=[0x1e0b], succ=[0x1e5c]
    =================================
    0x1e48: v1e48(0x1e5c) = CONST 
    0x1e4c: v1e4c(0x2) = CONST 
    0x1e4e: v1e4e = SLOAD v1e4c(0x2)
    0x1e4f: v1e4f(0x31d8) = CONST 
    0x1e55: v1e55(0xffffffff) = CONST 
    0x1e5a: v1e5a(0x31d8) = AND v1e55(0xffffffff), v1e4f(0x31d8)
    0x1e5b: v1e5b_0 = CALLPRIVATE v1e5a(0x31d8), v3e5, v1e4e, v1e48(0x1e5c)

    Begin block 0x1e5c
    prev=[0x1e47], succ=[0x1eb4]
    =================================
    0x1e5d: v1e5d(0x2) = CONST 
    0x1e61: SSTORE v1e5d(0x2), v1e5b_0
    0x1e63: v1e63(0x1eb4) = CONST 
    0x1e67: v1e67(0x3) = CONST 
    0x1e69: v1e69(0x0) = CONST 
    0x1e6c: v1e6c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e81: v1e81 = AND v1e6c(0xffffffffffffffffffffffffffffffffffffffff), v3db
    0x1e82: v1e82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e97: v1e97 = AND v1e82(0xffffffffffffffffffffffffffffffffffffffff), v1e81
    0x1e99: MSTORE v1e69(0x0), v1e97
    0x1e9a: v1e9a(0x20) = CONST 
    0x1e9c: v1e9c(0x20) = ADD v1e9a(0x20), v1e69(0x0)
    0x1e9f: MSTORE v1e9c(0x20), v1e67(0x3)
    0x1ea0: v1ea0(0x20) = CONST 
    0x1ea2: v1ea2(0x40) = ADD v1ea0(0x20), v1e9c(0x20)
    0x1ea3: v1ea3(0x0) = CONST 
    0x1ea5: v1ea5 = SHA3 v1ea3(0x0), v1ea2(0x40)
    0x1ea6: v1ea6 = SLOAD v1ea5
    0x1ea7: v1ea7(0x31d8) = CONST 
    0x1ead: v1ead(0xffffffff) = CONST 
    0x1eb2: v1eb2(0x31d8) = AND v1ead(0xffffffff), v1ea7(0x31d8)
    0x1eb3: v1eb3_0 = CALLPRIVATE v1eb2(0x31d8), v3e5, v1ea6, v1e63(0x1eb4)

    Begin block 0x1eb4
    prev=[0x1e5c], succ=[0x1fc2]
    =================================
    0x1eb5: v1eb5(0x3) = CONST 
    0x1eb7: v1eb7(0x0) = CONST 
    0x1eba: v1eba(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ecf: v1ecf = AND v1eba(0xffffffffffffffffffffffffffffffffffffffff), v3db
    0x1ed0: v1ed0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ee5: v1ee5 = AND v1ed0(0xffffffffffffffffffffffffffffffffffffffff), v1ecf
    0x1ee7: MSTORE v1eb7(0x0), v1ee5
    0x1ee8: v1ee8(0x20) = CONST 
    0x1eea: v1eea(0x20) = ADD v1ee8(0x20), v1eb7(0x0)
    0x1eed: MSTORE v1eea(0x20), v1eb5(0x3)
    0x1eee: v1eee(0x20) = CONST 
    0x1ef0: v1ef0(0x40) = ADD v1eee(0x20), v1eea(0x20)
    0x1ef1: v1ef1(0x0) = CONST 
    0x1ef3: v1ef3 = SHA3 v1ef1(0x0), v1ef0(0x40)
    0x1ef6: SSTORE v1ef3, v1eb3_0
    0x1ef9: v1ef9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f0e: v1f0e = AND v1ef9(0xffffffffffffffffffffffffffffffffffffffff), v3db
    0x1f0f: v1f0f(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885) = CONST 
    0x1f31: v1f31(0x40) = CONST 
    0x1f33: v1f33 = MLOAD v1f31(0x40)
    0x1f37: MSTORE v1f33, v3e5
    0x1f38: v1f38(0x20) = CONST 
    0x1f3a: v1f3a = ADD v1f38(0x20), v1f33
    0x1f3e: v1f3e(0x40) = CONST 
    0x1f40: v1f40 = MLOAD v1f3e(0x40)
    0x1f43: v1f43(0x20) = SUB v1f3a, v1f40
    0x1f45: LOG2 v1f40, v1f43(0x20), v1f0f(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885), v1f0e
    0x1f47: v1f47(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f5c: v1f5c = AND v1f47(0xffffffffffffffffffffffffffffffffffffffff), v3db
    0x1f5d: v1f5d(0x0) = CONST 
    0x1f5f: v1f5f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f74: v1f74(0x0) = AND v1f5f(0xffffffffffffffffffffffffffffffffffffffff), v1f5d(0x0)
    0x1f75: v1f75(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16) = CONST 
    0x1f98: v1f98(0x40) = CONST 
    0x1f9a: v1f9a = MLOAD v1f98(0x40)
    0x1f9e: MSTORE v1f9a, v3e5
    0x1f9f: v1f9f(0x20) = CONST 
    0x1fa1: v1fa1 = ADD v1f9f(0x20), v1f9a
    0x1fa3: v1fa3(0x20) = CONST 
    0x1fa5: v1fa5 = ADD v1fa3(0x20), v1fa1
    0x1fa8: v1fa8(0x40) = SUB v1fa5, v1f9a
    0x1faa: MSTORE v1fa1, v1fa8(0x40)
    0x1fae: v1fae = MLOAD v1d49(0x60)
    0x1fb0: MSTORE v1fa5, v1fae
    0x1fb1: v1fb1(0x20) = CONST 
    0x1fb3: v1fb3 = ADD v1fb1(0x20), v1fa5
    0x1fb7: v1fb7 = MLOAD v1d49(0x60)
    0x1fb9: v1fb9(0x20) = CONST 
    0x1fbb: v1fbb(0x80) = ADD v1fb9(0x20), v1d49(0x60)
    0x1fc0: v1fc0(0x0) = CONST 

    Begin block 0x1fc2
    prev=[0x1eb4, 0x1fcb], succ=[0x1fdd, 0x1fcb]
    =================================
    0x1fc2_0x0: v1fc2_0 = PHI v1fc0(0x0), v1fd6
    0x1fc5: v1fc5 = LT v1fc2_0, v1fb7
    0x1fc6: v1fc6 = ISZERO v1fc5
    0x1fc7: v1fc7(0x1fdd) = CONST 
    0x1fca: JUMPI v1fc7(0x1fdd), v1fc6

    Begin block 0x1fdd
    prev=[0x1fc2], succ=[0x200a, 0x1ff1]
    =================================
    0x1fe6: v1fe6 = ADD v1fb7, v1fb3
    0x1fe8: v1fe8(0x1f) = CONST 
    0x1fea: v1fea = AND v1fe8(0x1f), v1fb7
    0x1fec: v1fec = ISZERO v1fea
    0x1fed: v1fed(0x200a) = CONST 
    0x1ff0: JUMPI v1fed(0x200a), v1fec

    Begin block 0x200a
    prev=[0x1fdd, 0x1ff1], succ=[0x3f5]
    =================================
    0x200a_0x1: v200a_1 = PHI v1fe6, v2007
    0x2011: v2011(0x40) = CONST 
    0x2013: v2013 = MLOAD v2011(0x40)
    0x2016: v2016 = SUB v200a_1, v2013
    0x2018: LOG3 v2013, v2016, v1f75(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16), v1f74(0x0), v1f5c
    0x2019: v2019(0x1) = CONST 
    0x2022: JUMP v3b8(0x3f5)

    Begin block 0x3f5
    prev=[0x200a], succ=[]
    =================================
    0x3f6: v3f6(0x40) = CONST 
    0x3f8: v3f8 = MLOAD v3f6(0x40)
    0x3fb: v3fb(0x0) = ISZERO v2019(0x1)
    0x3fc: v3fc(0x1) = ISZERO v3fb(0x0)
    0x3fd: v3fd(0x0) = ISZERO v3fc(0x1)
    0x3fe: v3fe(0x1) = ISZERO v3fd(0x0)
    0x400: MSTORE v3f8, v3fe(0x1)
    0x401: v401(0x20) = CONST 
    0x403: v403 = ADD v401(0x20), v3f8
    0x407: v407(0x40) = CONST 
    0x409: v409 = MLOAD v407(0x40)
    0x40c: v40c(0x20) = SUB v403, v409
    0x40e: RETURN v409, v40c(0x20)

    Begin block 0x1ff1
    prev=[0x1fdd], succ=[0x200a]
    =================================
    0x1ff3: v1ff3 = SUB v1fe6, v1fea
    0x1ff5: v1ff5 = MLOAD v1ff3
    0x1ff6: v1ff6(0x1) = CONST 
    0x1ff9: v1ff9(0x20) = CONST 
    0x1ffb: v1ffb = SUB v1ff9(0x20), v1fea
    0x1ffc: v1ffc(0x100) = CONST 
    0x1fff: v1fff = EXP v1ffc(0x100), v1ffb
    0x2000: v2000 = SUB v1fff, v1ff6(0x1)
    0x2001: v2001 = NOT v2000
    0x2002: v2002 = AND v2001, v1ff5
    0x2004: MSTORE v1ff3, v2002
    0x2005: v2005(0x20) = CONST 
    0x2007: v2007 = ADD v2005(0x20), v1ff3

    Begin block 0x1fcb
    prev=[0x1fc2], succ=[0x1fc2]
    =================================
    0x1fcb_0x0: v1fcb_0 = PHI v1fc0(0x0), v1fd6
    0x1fcd: v1fcd = ADD v1fbb(0x80), v1fcb_0
    0x1fce: v1fce = MLOAD v1fcd
    0x1fd1: v1fd1 = ADD v1fb3, v1fcb_0
    0x1fd2: MSTORE v1fd1, v1fce
    0x1fd3: v1fd3(0x20) = CONST 
    0x1fd6: v1fd6 = ADD v1fcb_0, v1fd3(0x20)
    0x1fd9: v1fd9(0x1fc2) = CONST 
    0x1fdc: JUMP v1fd9(0x1fc2)

    Begin block 0x1da0
    prev=[0x1d46], succ=[0x1de4]
    =================================
    0x1da1: v1da1(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = CONST 
    0x1db6: v1db6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1dcb: v1dcb(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = AND v1db6(0xffffffffffffffffffffffffffffffffffffffff), v1da1(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0x1dcc: v1dcc = CALLER 
    0x1dcd: v1dcd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1de2: v1de2 = AND v1dcd(0xffffffffffffffffffffffffffffffffffffffff), v1dcc
    0x1de3: v1de3 = EQ v1de2, v1dcb(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)

}

function burn(uint256)() public {
    Begin block 0x40f
    prev=[], succ=[0x417, 0x41b]
    =================================
    0x410: v410 = CALLVALUE 
    0x412: v412 = ISZERO v410
    0x413: v413(0x41b) = CONST 
    0x416: JUMPI v413(0x41b), v412

    Begin block 0x417
    prev=[0x40f], succ=[]
    =================================
    0x417: v417(0x0) = CONST 
    0x41a: REVERT v417(0x0), v417(0x0)

    Begin block 0x41b
    prev=[0x40f], succ=[0x2023]
    =================================
    0x41d: v41d(0x43a) = CONST 
    0x420: v420(0x4) = CONST 
    0x423: v423 = CALLDATASIZE 
    0x424: v424 = SUB v423, v420(0x4)
    0x426: v426 = ADD v420(0x4), v424
    0x42a: v42a = CALLDATALOAD v420(0x4)
    0x42c: v42c(0x20) = CONST 
    0x42e: v42e(0x24) = ADD v42c(0x20), v420(0x4)
    0x436: v436(0x2023) = CONST 
    0x439: JUMP v436(0x2023)

    Begin block 0x2023
    prev=[0x41b], succ=[0x202e, 0x2032]
    =================================
    0x2024: v2024(0x0) = CONST 
    0x2027: v2027 = GT v42a, v2024(0x0)
    0x2028: v2028 = ISZERO v2027
    0x2029: v2029 = ISZERO v2028
    0x202a: v202a(0x2032) = CONST 
    0x202d: JUMPI v202a(0x2032), v2029

    Begin block 0x202e
    prev=[0x2023], succ=[]
    =================================
    0x202e: v202e(0x0) = CONST 
    0x2031: REVERT v202e(0x0), v202e(0x0)

    Begin block 0x2032
    prev=[0x2023], succ=[0x207c, 0x2080]
    =================================
    0x2033: v2033(0x3) = CONST 
    0x2035: v2035(0x0) = CONST 
    0x2037: v2037 = CALLER 
    0x2038: v2038(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x204d: v204d = AND v2038(0xffffffffffffffffffffffffffffffffffffffff), v2037
    0x204e: v204e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2063: v2063 = AND v204e(0xffffffffffffffffffffffffffffffffffffffff), v204d
    0x2065: MSTORE v2035(0x0), v2063
    0x2066: v2066(0x20) = CONST 
    0x2068: v2068(0x20) = ADD v2066(0x20), v2035(0x0)
    0x206b: MSTORE v2068(0x20), v2033(0x3)
    0x206c: v206c(0x20) = CONST 
    0x206e: v206e(0x40) = ADD v206c(0x20), v2068(0x20)
    0x206f: v206f(0x0) = CONST 
    0x2071: v2071 = SHA3 v206f(0x0), v206e(0x40)
    0x2072: v2072 = SLOAD v2071
    0x2074: v2074 = GT v42a, v2072
    0x2075: v2075 = ISZERO v2074
    0x2076: v2076 = ISZERO v2075
    0x2077: v2077 = ISZERO v2076
    0x2078: v2078(0x2080) = CONST 
    0x207b: JUMPI v2078(0x2080), v2077

    Begin block 0x207c
    prev=[0x2032], succ=[]
    =================================
    0x207c: v207c(0x0) = CONST 
    0x207f: REVERT v207c(0x0), v207c(0x0)

    Begin block 0x2080
    prev=[0x2032], succ=[0x20d2]
    =================================
    0x2081: v2081(0x20d2) = CONST 
    0x2085: v2085(0x3) = CONST 
    0x2087: v2087(0x0) = CONST 
    0x2089: v2089 = CALLER 
    0x208a: v208a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x209f: v209f = AND v208a(0xffffffffffffffffffffffffffffffffffffffff), v2089
    0x20a0: v20a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20b5: v20b5 = AND v20a0(0xffffffffffffffffffffffffffffffffffffffff), v209f
    0x20b7: MSTORE v2087(0x0), v20b5
    0x20b8: v20b8(0x20) = CONST 
    0x20ba: v20ba(0x20) = ADD v20b8(0x20), v2087(0x0)
    0x20bd: MSTORE v20ba(0x20), v2085(0x3)
    0x20be: v20be(0x20) = CONST 
    0x20c0: v20c0(0x40) = ADD v20be(0x20), v20ba(0x20)
    0x20c1: v20c1(0x0) = CONST 
    0x20c3: v20c3 = SHA3 v20c1(0x0), v20c0(0x40)
    0x20c4: v20c4 = SLOAD v20c3
    0x20c5: v20c5(0x31bf) = CONST 
    0x20cb: v20cb(0xffffffff) = CONST 
    0x20d0: v20d0(0x31bf) = AND v20cb(0xffffffff), v20c5(0x31bf)
    0x20d1: v20d1_0 = CALLPRIVATE v20d0(0x31bf), v42a, v20c4, v2081(0x20d2)

    Begin block 0x20d2
    prev=[0x2080], succ=[0x212a]
    =================================
    0x20d3: v20d3(0x3) = CONST 
    0x20d5: v20d5(0x0) = CONST 
    0x20d7: v20d7 = CALLER 
    0x20d8: v20d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20ed: v20ed = AND v20d8(0xffffffffffffffffffffffffffffffffffffffff), v20d7
    0x20ee: v20ee(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2103: v2103 = AND v20ee(0xffffffffffffffffffffffffffffffffffffffff), v20ed
    0x2105: MSTORE v20d5(0x0), v2103
    0x2106: v2106(0x20) = CONST 
    0x2108: v2108(0x20) = ADD v2106(0x20), v20d5(0x0)
    0x210b: MSTORE v2108(0x20), v20d3(0x3)
    0x210c: v210c(0x20) = CONST 
    0x210e: v210e(0x40) = ADD v210c(0x20), v2108(0x20)
    0x210f: v210f(0x0) = CONST 
    0x2111: v2111 = SHA3 v210f(0x0), v210e(0x40)
    0x2114: SSTORE v2111, v20d1_0
    0x2116: v2116(0x212a) = CONST 
    0x211a: v211a(0x2) = CONST 
    0x211c: v211c = SLOAD v211a(0x2)
    0x211d: v211d(0x31bf) = CONST 
    0x2123: v2123(0xffffffff) = CONST 
    0x2128: v2128(0x31bf) = AND v2123(0xffffffff), v211d(0x31bf)
    0x2129: v2129_0 = CALLPRIVATE v2128(0x31bf), v42a, v211c, v2116(0x212a)

    Begin block 0x212a
    prev=[0x20d2], succ=[0x43a]
    =================================
    0x212b: v212b(0x2) = CONST 
    0x212f: SSTORE v212b(0x2), v2129_0
    0x2131: v2131 = CALLER 
    0x2132: v2132(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2147: v2147 = AND v2132(0xffffffffffffffffffffffffffffffffffffffff), v2131
    0x2148: v2148(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0x216a: v216a(0x40) = CONST 
    0x216c: v216c = MLOAD v216a(0x40)
    0x2170: MSTORE v216c, v42a
    0x2171: v2171(0x20) = CONST 
    0x2173: v2173 = ADD v2171(0x20), v216c
    0x2177: v2177(0x40) = CONST 
    0x2179: v2179 = MLOAD v2177(0x40)
    0x217c: v217c(0x20) = SUB v2173, v2179
    0x217e: LOG2 v2179, v217c(0x20), v2148(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), v2147
    0x2180: JUMP v41d(0x43a)

    Begin block 0x43a
    prev=[0x212a], succ=[]
    =================================
    0x43b: STOP 

}

function teamFrozenBalances(address,uint64)() public {
    Begin block 0x43c
    prev=[], succ=[0x444, 0x448]
    =================================
    0x43d: v43d = CALLVALUE 
    0x43f: v43f = ISZERO v43d
    0x440: v440(0x448) = CONST 
    0x443: JUMPI v440(0x448), v43f

    Begin block 0x444
    prev=[0x43c], succ=[]
    =================================
    0x444: v444(0x0) = CONST 
    0x447: REVERT v444(0x0), v444(0x0)

    Begin block 0x448
    prev=[0x43c], succ=[0x2181]
    =================================
    0x44a: v44a(0x491) = CONST 
    0x44d: v44d(0x4) = CONST 
    0x450: v450 = CALLDATASIZE 
    0x451: v451 = SUB v450, v44d(0x4)
    0x453: v453 = ADD v44d(0x4), v451
    0x457: v457 = CALLDATALOAD v44d(0x4)
    0x458: v458(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x46d: v46d = AND v458(0xffffffffffffffffffffffffffffffffffffffff), v457
    0x46f: v46f(0x20) = CONST 
    0x471: v471(0x24) = ADD v46f(0x20), v44d(0x4)
    0x477: v477 = CALLDATALOAD v471(0x24)
    0x478: v478(0xffffffffffffffff) = CONST 
    0x481: v481 = AND v478(0xffffffffffffffff), v477
    0x483: v483(0x20) = CONST 
    0x485: v485(0x44) = ADD v483(0x20), v471(0x24)
    0x48d: v48d(0x2181) = CONST 
    0x490: JUMP v48d(0x2181)

    Begin block 0x2181
    prev=[0x448], succ=[0x491]
    =================================
    0x2182: v2182(0x1) = CONST 
    0x2184: v2184(0x20) = CONST 
    0x2186: MSTORE v2184(0x20), v2182(0x1)
    0x2188: v2188(0x0) = CONST 
    0x218a: MSTORE v2188(0x0), v46d
    0x218b: v218b(0x40) = CONST 
    0x218d: v218d(0x0) = CONST 
    0x218f: v218f = SHA3 v218d(0x0), v218b(0x40)
    0x2190: v2190(0x20) = CONST 
    0x2192: MSTORE v2190(0x20), v218f
    0x2194: v2194(0x0) = CONST 
    0x2196: MSTORE v2194(0x0), v481
    0x2197: v2197(0x40) = CONST 
    0x2199: v2199(0x0) = CONST 
    0x219b: v219b = SHA3 v2199(0x0), v2197(0x40)
    0x219c: v219c(0x0) = CONST 
    0x21a3: v21a3 = SLOAD v219b
    0x21a5: JUMP v44a(0x491)

    Begin block 0x491
    prev=[0x2181], succ=[]
    =================================
    0x492: v492(0x40) = CONST 
    0x494: v494 = MLOAD v492(0x40)
    0x498: MSTORE v494, v21a3
    0x499: v499(0x20) = CONST 
    0x49b: v49b = ADD v499(0x20), v494
    0x49f: v49f(0x40) = CONST 
    0x4a1: v4a1 = MLOAD v49f(0x40)
    0x4a4: v4a4(0x20) = SUB v49b, v4a1
    0x4a6: RETURN v4a1, v4a4(0x20)

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x4a7
    prev=[], succ=[0x4af, 0x4b3]
    =================================
    0x4a8: v4a8 = CALLVALUE 
    0x4aa: v4aa = ISZERO v4a8
    0x4ab: v4ab(0x4b3) = CONST 
    0x4ae: JUMPI v4ab(0x4b3), v4aa

    Begin block 0x4af
    prev=[0x4a7], succ=[]
    =================================
    0x4af: v4af(0x0) = CONST 
    0x4b2: REVERT v4af(0x0), v4af(0x0)

    Begin block 0x4b3
    prev=[0x4a7], succ=[0x21a6]
    =================================
    0x4b5: v4b5(0x4f2) = CONST 
    0x4b8: v4b8(0x4) = CONST 
    0x4bb: v4bb = CALLDATASIZE 
    0x4bc: v4bc = SUB v4bb, v4b8(0x4)
    0x4be: v4be = ADD v4b8(0x4), v4bc
    0x4c2: v4c2 = CALLDATALOAD v4b8(0x4)
    0x4c3: v4c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4d8: v4d8 = AND v4c3(0xffffffffffffffffffffffffffffffffffffffff), v4c2
    0x4da: v4da(0x20) = CONST 
    0x4dc: v4dc(0x24) = ADD v4da(0x20), v4b8(0x4)
    0x4e2: v4e2 = CALLDATALOAD v4dc(0x24)
    0x4e4: v4e4(0x20) = CONST 
    0x4e6: v4e6(0x44) = ADD v4e4(0x20), v4dc(0x24)
    0x4ee: v4ee(0x21a6) = CONST 
    0x4f1: JUMP v4ee(0x21a6)

    Begin block 0x21a6
    prev=[0x4b3], succ=[0x21e1, 0x21e5]
    =================================
    0x21a7: v21a7(0x0) = CONST 
    0x21aa: v21aa(0x0) = CONST 
    0x21ac: v21ac(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21c1: v21c1(0x0) = AND v21ac(0xffffffffffffffffffffffffffffffffffffffff), v21aa(0x0)
    0x21c3: v21c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21d8: v21d8 = AND v21c3(0xffffffffffffffffffffffffffffffffffffffff), v4d8
    0x21d9: v21d9 = EQ v21d8, v21c1(0x0)
    0x21da: v21da = ISZERO v21d9
    0x21db: v21db = ISZERO v21da
    0x21dc: v21dc = ISZERO v21db
    0x21dd: v21dd(0x21e5) = CONST 
    0x21e0: JUMPI v21dd(0x21e5), v21dc

    Begin block 0x21e1
    prev=[0x21a6], succ=[]
    =================================
    0x21e1: v21e1(0x0) = CONST 
    0x21e4: REVERT v21e1(0x0), v21e1(0x0)

    Begin block 0x21e5
    prev=[0x21a6], succ=[0x226d, 0x22f3]
    =================================
    0x21e6: v21e6(0x4) = CONST 
    0x21e8: v21e8(0x0) = CONST 
    0x21ea: v21ea = CALLER 
    0x21eb: v21eb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2200: v2200 = AND v21eb(0xffffffffffffffffffffffffffffffffffffffff), v21ea
    0x2201: v2201(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2216: v2216 = AND v2201(0xffffffffffffffffffffffffffffffffffffffff), v2200
    0x2218: MSTORE v21e8(0x0), v2216
    0x2219: v2219(0x20) = CONST 
    0x221b: v221b(0x20) = ADD v2219(0x20), v21e8(0x0)
    0x221e: MSTORE v221b(0x20), v21e6(0x4)
    0x221f: v221f(0x20) = CONST 
    0x2221: v2221(0x40) = ADD v221f(0x20), v221b(0x20)
    0x2222: v2222(0x0) = CONST 
    0x2224: v2224 = SHA3 v2222(0x0), v2221(0x40)
    0x2225: v2225(0x0) = CONST 
    0x2228: v2228(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x223d: v223d = AND v2228(0xffffffffffffffffffffffffffffffffffffffff), v4d8
    0x223e: v223e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2253: v2253 = AND v223e(0xffffffffffffffffffffffffffffffffffffffff), v223d
    0x2255: MSTORE v2225(0x0), v2253
    0x2256: v2256(0x20) = CONST 
    0x2258: v2258(0x20) = ADD v2256(0x20), v2225(0x0)
    0x225b: MSTORE v2258(0x20), v2224
    0x225c: v225c(0x20) = CONST 
    0x225e: v225e(0x40) = ADD v225c(0x20), v2258(0x20)
    0x225f: v225f(0x0) = CONST 
    0x2261: v2261 = SHA3 v225f(0x0), v225e(0x40)
    0x2262: v2262 = SLOAD v2261
    0x2267: v2267 = GT v4e2, v2262
    0x2268: v2268 = ISZERO v2267
    0x2269: v2269(0x22f3) = CONST 
    0x226c: JUMPI v2269(0x22f3), v2268

    Begin block 0x226d
    prev=[0x21e5], succ=[0x2387]
    =================================
    0x226d: v226d(0x0) = CONST 
    0x226f: v226f(0x4) = CONST 
    0x2271: v2271(0x0) = CONST 
    0x2273: v2273 = CALLER 
    0x2274: v2274(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2289: v2289 = AND v2274(0xffffffffffffffffffffffffffffffffffffffff), v2273
    0x228a: v228a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x229f: v229f = AND v228a(0xffffffffffffffffffffffffffffffffffffffff), v2289
    0x22a1: MSTORE v2271(0x0), v229f
    0x22a2: v22a2(0x20) = CONST 
    0x22a4: v22a4(0x20) = ADD v22a2(0x20), v2271(0x0)
    0x22a7: MSTORE v22a4(0x20), v226f(0x4)
    0x22a8: v22a8(0x20) = CONST 
    0x22aa: v22aa(0x40) = ADD v22a8(0x20), v22a4(0x20)
    0x22ab: v22ab(0x0) = CONST 
    0x22ad: v22ad = SHA3 v22ab(0x0), v22aa(0x40)
    0x22ae: v22ae(0x0) = CONST 
    0x22b1: v22b1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22c6: v22c6 = AND v22b1(0xffffffffffffffffffffffffffffffffffffffff), v4d8
    0x22c7: v22c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22dc: v22dc = AND v22c7(0xffffffffffffffffffffffffffffffffffffffff), v22c6
    0x22de: MSTORE v22ae(0x0), v22dc
    0x22df: v22df(0x20) = CONST 
    0x22e1: v22e1(0x20) = ADD v22df(0x20), v22ae(0x0)
    0x22e4: MSTORE v22e1(0x20), v22ad
    0x22e5: v22e5(0x20) = CONST 
    0x22e7: v22e7(0x40) = ADD v22e5(0x20), v22e1(0x20)
    0x22e8: v22e8(0x0) = CONST 
    0x22ea: v22ea = SHA3 v22e8(0x0), v22e7(0x40)
    0x22ed: SSTORE v22ea, v226d(0x0)
    0x22ef: v22ef(0x2387) = CONST 
    0x22f2: JUMP v22ef(0x2387)

    Begin block 0x2387
    prev=[0x226d, 0x2306], succ=[0x4f2]
    =================================
    0x2389: v2389(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x239e: v239e = AND v2389(0xffffffffffffffffffffffffffffffffffffffff), v4d8
    0x239f: v239f = CALLER 
    0x23a0: v23a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x23b5: v23b5 = AND v23a0(0xffffffffffffffffffffffffffffffffffffffff), v239f
    0x23b6: v23b6(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x23d7: v23d7(0x4) = CONST 
    0x23d9: v23d9(0x0) = CONST 
    0x23db: v23db = CALLER 
    0x23dc: v23dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x23f1: v23f1 = AND v23dc(0xffffffffffffffffffffffffffffffffffffffff), v23db
    0x23f2: v23f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2407: v2407 = AND v23f2(0xffffffffffffffffffffffffffffffffffffffff), v23f1
    0x2409: MSTORE v23d9(0x0), v2407
    0x240a: v240a(0x20) = CONST 
    0x240c: v240c(0x20) = ADD v240a(0x20), v23d9(0x0)
    0x240f: MSTORE v240c(0x20), v23d7(0x4)
    0x2410: v2410(0x20) = CONST 
    0x2412: v2412(0x40) = ADD v2410(0x20), v240c(0x20)
    0x2413: v2413(0x0) = CONST 
    0x2415: v2415 = SHA3 v2413(0x0), v2412(0x40)
    0x2416: v2416(0x0) = CONST 
    0x2419: v2419(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x242e: v242e = AND v2419(0xffffffffffffffffffffffffffffffffffffffff), v4d8
    0x242f: v242f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2444: v2444 = AND v242f(0xffffffffffffffffffffffffffffffffffffffff), v242e
    0x2446: MSTORE v2416(0x0), v2444
    0x2447: v2447(0x20) = CONST 
    0x2449: v2449(0x20) = ADD v2447(0x20), v2416(0x0)
    0x244c: MSTORE v2449(0x20), v2415
    0x244d: v244d(0x20) = CONST 
    0x244f: v244f(0x40) = ADD v244d(0x20), v2449(0x20)
    0x2450: v2450(0x0) = CONST 
    0x2452: v2452 = SHA3 v2450(0x0), v244f(0x40)
    0x2453: v2453 = SLOAD v2452
    0x2454: v2454(0x40) = CONST 
    0x2456: v2456 = MLOAD v2454(0x40)
    0x245a: MSTORE v2456, v2453
    0x245b: v245b(0x20) = CONST 
    0x245d: v245d = ADD v245b(0x20), v2456
    0x2461: v2461(0x40) = CONST 
    0x2463: v2463 = MLOAD v2461(0x40)
    0x2466: v2466(0x20) = SUB v245d, v2463
    0x2468: LOG3 v2463, v2466(0x20), v23b6(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v23b5, v239e
    0x2469: v2469(0x1) = CONST 
    0x2472: JUMP v4b5(0x4f2)

    Begin block 0x4f2
    prev=[0x2387], succ=[]
    =================================
    0x4f3: v4f3(0x40) = CONST 
    0x4f5: v4f5 = MLOAD v4f3(0x40)
    0x4f8: v4f8(0x0) = ISZERO v2469(0x1)
    0x4f9: v4f9(0x1) = ISZERO v4f8(0x0)
    0x4fa: v4fa(0x0) = ISZERO v4f9(0x1)
    0x4fb: v4fb(0x1) = ISZERO v4fa(0x0)
    0x4fd: MSTORE v4f5, v4fb(0x1)
    0x4fe: v4fe(0x20) = CONST 
    0x500: v500 = ADD v4fe(0x20), v4f5
    0x504: v504(0x40) = CONST 
    0x506: v506 = MLOAD v504(0x40)
    0x509: v509(0x20) = SUB v500, v506
    0x50b: RETURN v506, v509(0x20)

    Begin block 0x22f3
    prev=[0x21e5], succ=[0x2306]
    =================================
    0x22f4: v22f4(0x2306) = CONST 
    0x22f9: v22f9(0x31bf) = CONST 
    0x22ff: v22ff(0xffffffff) = CONST 
    0x2304: v2304(0x31bf) = AND v22ff(0xffffffff), v22f9(0x31bf)
    0x2305: v2305_0 = CALLPRIVATE v2304(0x31bf), v4e2, v2262, v22f4(0x2306)

    Begin block 0x2306
    prev=[0x22f3], succ=[0x2387]
    =================================
    0x2307: v2307(0x4) = CONST 
    0x2309: v2309(0x0) = CONST 
    0x230b: v230b = CALLER 
    0x230c: v230c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2321: v2321 = AND v230c(0xffffffffffffffffffffffffffffffffffffffff), v230b
    0x2322: v2322(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2337: v2337 = AND v2322(0xffffffffffffffffffffffffffffffffffffffff), v2321
    0x2339: MSTORE v2309(0x0), v2337
    0x233a: v233a(0x20) = CONST 
    0x233c: v233c(0x20) = ADD v233a(0x20), v2309(0x0)
    0x233f: MSTORE v233c(0x20), v2307(0x4)
    0x2340: v2340(0x20) = CONST 
    0x2342: v2342(0x40) = ADD v2340(0x20), v233c(0x20)
    0x2343: v2343(0x0) = CONST 
    0x2345: v2345 = SHA3 v2343(0x0), v2342(0x40)
    0x2346: v2346(0x0) = CONST 
    0x2349: v2349(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x235e: v235e = AND v2349(0xffffffffffffffffffffffffffffffffffffffff), v4d8
    0x235f: v235f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2374: v2374 = AND v235f(0xffffffffffffffffffffffffffffffffffffffff), v235e
    0x2376: MSTORE v2346(0x0), v2374
    0x2377: v2377(0x20) = CONST 
    0x2379: v2379(0x20) = ADD v2377(0x20), v2346(0x0)
    0x237c: MSTORE v2379(0x20), v2345
    0x237d: v237d(0x20) = CONST 
    0x237f: v237f(0x40) = ADD v237d(0x20), v2379(0x20)
    0x2380: v2380(0x0) = CONST 
    0x2382: v2382 = SHA3 v2380(0x0), v237f(0x40)
    0x2385: SSTORE v2382, v2305_0

}

function balanceOf(address)() public {
    Begin block 0x50c
    prev=[], succ=[0x514, 0x518]
    =================================
    0x50d: v50d = CALLVALUE 
    0x50f: v50f = ISZERO v50d
    0x510: v510(0x518) = CONST 
    0x513: JUMPI v510(0x518), v50f

    Begin block 0x514
    prev=[0x50c], succ=[]
    =================================
    0x514: v514(0x0) = CONST 
    0x517: REVERT v514(0x0), v514(0x0)

    Begin block 0x518
    prev=[0x50c], succ=[0x2473]
    =================================
    0x51a: v51a(0x54d) = CONST 
    0x51d: v51d(0x4) = CONST 
    0x520: v520 = CALLDATASIZE 
    0x521: v521 = SUB v520, v51d(0x4)
    0x523: v523 = ADD v51d(0x4), v521
    0x527: v527 = CALLDATALOAD v51d(0x4)
    0x528: v528(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x53d: v53d = AND v528(0xffffffffffffffffffffffffffffffffffffffff), v527
    0x53f: v53f(0x20) = CONST 
    0x541: v541(0x24) = ADD v53f(0x20), v51d(0x4)
    0x549: v549(0x2473) = CONST 
    0x54c: JUMP v549(0x2473)

    Begin block 0x2473
    prev=[0x518], succ=[0x54d]
    =================================
    0x2474: v2474(0x0) = CONST 
    0x2476: v2476(0x3) = CONST 
    0x2478: v2478(0x0) = CONST 
    0x247b: v247b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2490: v2490 = AND v247b(0xffffffffffffffffffffffffffffffffffffffff), v53d
    0x2491: v2491(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24a6: v24a6 = AND v2491(0xffffffffffffffffffffffffffffffffffffffff), v2490
    0x24a8: MSTORE v2478(0x0), v24a6
    0x24a9: v24a9(0x20) = CONST 
    0x24ab: v24ab(0x20) = ADD v24a9(0x20), v2478(0x0)
    0x24ae: MSTORE v24ab(0x20), v2476(0x3)
    0x24af: v24af(0x20) = CONST 
    0x24b1: v24b1(0x40) = ADD v24af(0x20), v24ab(0x20)
    0x24b2: v24b2(0x0) = CONST 
    0x24b4: v24b4 = SHA3 v24b2(0x0), v24b1(0x40)
    0x24b5: v24b5 = SLOAD v24b4
    0x24bb: JUMP v51a(0x54d)

    Begin block 0x54d
    prev=[0x2473], succ=[]
    =================================
    0x54e: v54e(0x40) = CONST 
    0x550: v550 = MLOAD v54e(0x40)
    0x554: MSTORE v550, v24b5
    0x555: v555(0x20) = CONST 
    0x557: v557 = ADD v555(0x20), v550
    0x55b: v55b(0x40) = CONST 
    0x55d: v55d = MLOAD v55b(0x40)
    0x560: v560(0x20) = SUB v557, v55d
    0x562: RETURN v55d, v560(0x20)

}

function finishMinting()() public {
    Begin block 0x563
    prev=[], succ=[0x56b, 0x56f]
    =================================
    0x564: v564 = CALLVALUE 
    0x566: v566 = ISZERO v564
    0x567: v567(0x56f) = CONST 
    0x56a: JUMPI v567(0x56f), v566

    Begin block 0x56b
    prev=[0x563], succ=[]
    =================================
    0x56b: v56b(0x0) = CONST 
    0x56e: REVERT v56b(0x0), v56b(0x0)

    Begin block 0x56f
    prev=[0x563], succ=[0x24bc]
    =================================
    0x571: v571(0x578) = CONST 
    0x574: v574(0x24bc) = CONST 
    0x577: JUMP v574(0x24bc)

    Begin block 0x24bc
    prev=[0x56f], succ=[0x2558, 0x2514]
    =================================
    0x24bd: v24bd(0x0) = CONST 
    0x24c0: v24c0(0x0) = CONST 
    0x24c3: v24c3 = SLOAD v24bd(0x0)
    0x24c5: v24c5(0x100) = CONST 
    0x24c8: v24c8(0x1) = EXP v24c5(0x100), v24c0(0x0)
    0x24ca: v24ca = DIV v24c3, v24c8(0x1)
    0x24cb: v24cb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24e0: v24e0 = AND v24cb(0xffffffffffffffffffffffffffffffffffffffff), v24ca
    0x24e1: v24e1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24f6: v24f6 = AND v24e1(0xffffffffffffffffffffffffffffffffffffffff), v24e0
    0x24f7: v24f7 = CALLER 
    0x24f8: v24f8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x250d: v250d = AND v24f8(0xffffffffffffffffffffffffffffffffffffffff), v24f7
    0x250e: v250e = EQ v250d, v24f6
    0x2510: v2510(0x2558) = CONST 
    0x2513: JUMPI v2510(0x2558), v250e

    Begin block 0x2558
    prev=[0x24bc, 0x2514], succ=[0x255f, 0x2563]
    =================================
    0x2558_0x0: v2558_0 = PHI v250e, v2557
    0x2559: v2559 = ISZERO v2558_0
    0x255a: v255a = ISZERO v2559
    0x255b: v255b(0x2563) = CONST 
    0x255e: JUMPI v255b(0x2563), v255a

    Begin block 0x255f
    prev=[0x2558], succ=[]
    =================================
    0x255f: v255f(0x0) = CONST 
    0x2562: REVERT v255f(0x0), v255f(0x0)

    Begin block 0x2563
    prev=[0x2558], succ=[0x257b, 0x257f]
    =================================
    0x2564: v2564(0x0) = CONST 
    0x2566: v2566(0x14) = CONST 
    0x2569: v2569 = SLOAD v2564(0x0)
    0x256b: v256b(0x100) = CONST 
    0x256e: v256e(0x10000000000000000000000000000000000000000) = EXP v256b(0x100), v2566(0x14)
    0x2570: v2570 = DIV v2569, v256e(0x10000000000000000000000000000000000000000)
    0x2571: v2571(0xff) = CONST 
    0x2573: v2573 = AND v2571(0xff), v2570
    0x2574: v2574 = ISZERO v2573
    0x2575: v2575 = ISZERO v2574
    0x2576: v2576 = ISZERO v2575
    0x2577: v2577(0x257f) = CONST 
    0x257a: JUMPI v2577(0x257f), v2576

    Begin block 0x257b
    prev=[0x2563], succ=[]
    =================================
    0x257b: v257b(0x0) = CONST 
    0x257e: REVERT v257b(0x0), v257b(0x0)

    Begin block 0x257f
    prev=[0x2563], succ=[0x578]
    =================================
    0x2580: v2580(0x1) = CONST 
    0x2582: v2582(0x0) = CONST 
    0x2584: v2584(0x14) = CONST 
    0x2586: v2586(0x100) = CONST 
    0x2589: v2589(0x10000000000000000000000000000000000000000) = EXP v2586(0x100), v2584(0x14)
    0x258b: v258b = SLOAD v2582(0x0)
    0x258d: v258d(0xff) = CONST 
    0x258f: v258f(0xff0000000000000000000000000000000000000000) = MUL v258d(0xff), v2589(0x10000000000000000000000000000000000000000)
    0x2590: v2590(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v258f(0xff0000000000000000000000000000000000000000)
    0x2591: v2591 = AND v2590(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v258b
    0x2594: v2594(0x0) = ISZERO v2580(0x1)
    0x2595: v2595(0x1) = ISZERO v2594(0x0)
    0x2596: v2596(0x10000000000000000000000000000000000000000) = MUL v2595(0x1), v2589(0x10000000000000000000000000000000000000000)
    0x2597: v2597 = OR v2596(0x10000000000000000000000000000000000000000), v2591
    0x2599: SSTORE v2582(0x0), v2597
    0x259b: v259b(0xae5184fba832cb2b1f702aca6117b8d265eaf03ad33eb133f19dde0f5920fa08) = CONST 
    0x25bc: v25bc(0x40) = CONST 
    0x25be: v25be = MLOAD v25bc(0x40)
    0x25bf: v25bf(0x40) = CONST 
    0x25c1: v25c1 = MLOAD v25bf(0x40)
    0x25c4: v25c4(0x0) = SUB v25be, v25c1
    0x25c6: LOG1 v25c1, v25c4(0x0), v259b(0xae5184fba832cb2b1f702aca6117b8d265eaf03ad33eb133f19dde0f5920fa08)
    0x25c7: v25c7(0x1) = CONST 
    0x25cc: JUMP v571(0x578)

    Begin block 0x578
    prev=[0x257f], succ=[]
    =================================
    0x579: v579(0x40) = CONST 
    0x57b: v57b = MLOAD v579(0x40)
    0x57e: v57e(0x0) = ISZERO v25c7(0x1)
    0x57f: v57f(0x1) = ISZERO v57e(0x0)
    0x580: v580(0x0) = ISZERO v57f(0x1)
    0x581: v581(0x1) = ISZERO v580(0x0)
    0x583: MSTORE v57b, v581(0x1)
    0x584: v584(0x20) = CONST 
    0x586: v586 = ADD v584(0x20), v57b
    0x58a: v58a(0x40) = CONST 
    0x58c: v58c = MLOAD v58a(0x40)
    0x58f: v58f(0x20) = SUB v586, v58c
    0x591: RETURN v58c, v58f(0x20)

    Begin block 0x2514
    prev=[0x24bc], succ=[0x2558]
    =================================
    0x2515: v2515(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = CONST 
    0x252a: v252a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x253f: v253f(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = AND v252a(0xffffffffffffffffffffffffffffffffffffffff), v2515(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0x2540: v2540 = CALLER 
    0x2541: v2541(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2556: v2556 = AND v2541(0xffffffffffffffffffffffffffffffffffffffff), v2540
    0x2557: v2557 = EQ v2556, v253f(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)

}

function owner()() public {
    Begin block 0x592
    prev=[], succ=[0x59a, 0x59e]
    =================================
    0x593: v593 = CALLVALUE 
    0x595: v595 = ISZERO v593
    0x596: v596(0x59e) = CONST 
    0x599: JUMPI v596(0x59e), v595

    Begin block 0x59a
    prev=[0x592], succ=[]
    =================================
    0x59a: v59a(0x0) = CONST 
    0x59d: REVERT v59a(0x0), v59a(0x0)

    Begin block 0x59e
    prev=[0x592], succ=[0x25cd]
    =================================
    0x5a0: v5a0(0x5a7) = CONST 
    0x5a3: v5a3(0x25cd) = CONST 
    0x5a6: JUMP v5a3(0x25cd)

    Begin block 0x25cd
    prev=[0x59e], succ=[0x5a7]
    =================================
    0x25ce: v25ce(0x0) = CONST 
    0x25d2: v25d2 = SLOAD v25ce(0x0)
    0x25d4: v25d4(0x100) = CONST 
    0x25d7: v25d7(0x1) = EXP v25d4(0x100), v25ce(0x0)
    0x25d9: v25d9 = DIV v25d2, v25d7(0x1)
    0x25da: v25da(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25ef: v25ef = AND v25da(0xffffffffffffffffffffffffffffffffffffffff), v25d9
    0x25f1: JUMP v5a0(0x5a7)

    Begin block 0x5a7
    prev=[0x25cd], succ=[]
    =================================
    0x5a8: v5a8(0x40) = CONST 
    0x5aa: v5aa = MLOAD v5a8(0x40)
    0x5ad: v5ad(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5c2: v5c2 = AND v5ad(0xffffffffffffffffffffffffffffffffffffffff), v25ef
    0x5c3: v5c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5d8: v5d8 = AND v5c3(0xffffffffffffffffffffffffffffffffffffffff), v5c2
    0x5da: MSTORE v5aa, v5d8
    0x5db: v5db(0x20) = CONST 
    0x5dd: v5dd = ADD v5db(0x20), v5aa
    0x5e1: v5e1(0x40) = CONST 
    0x5e3: v5e3 = MLOAD v5e1(0x40)
    0x5e6: v5e6(0x20) = SUB v5dd, v5e3
    0x5e8: RETURN v5e3, v5e6(0x20)

}

function symbol()() public {
    Begin block 0x5e9
    prev=[], succ=[0x5f1, 0x5f5]
    =================================
    0x5ea: v5ea = CALLVALUE 
    0x5ec: v5ec = ISZERO v5ea
    0x5ed: v5ed(0x5f5) = CONST 
    0x5f0: JUMPI v5ed(0x5f5), v5ec

    Begin block 0x5f1
    prev=[0x5e9], succ=[]
    =================================
    0x5f1: v5f1(0x0) = CONST 
    0x5f4: REVERT v5f1(0x0), v5f1(0x0)

    Begin block 0x5f5
    prev=[0x5e9], succ=[0x25f2]
    =================================
    0x5f7: v5f7(0x5fe) = CONST 
    0x5fa: v5fa(0x25f2) = CONST 
    0x5fd: JUMP v5fa(0x25f2)

    Begin block 0x25f2
    prev=[0x5f5], succ=[0x5fe]
    =================================
    0x25f3: v25f3(0x60) = CONST 
    0x25f5: v25f5(0x40) = CONST 
    0x25f8: v25f8 = MLOAD v25f5(0x40)
    0x25fb: v25fb = ADD v25f8, v25f5(0x40)
    0x25fc: v25fc(0x40) = CONST 
    0x25fe: MSTORE v25fc(0x40), v25fb
    0x2600: v2600(0x3) = CONST 
    0x2603: MSTORE v25f8, v2600(0x3)
    0x2604: v2604(0x20) = CONST 
    0x2606: v2606 = ADD v2604(0x20), v25f8
    0x2607: v2607(0x594f550000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2629: MSTORE v2606, v2607(0x594f550000000000000000000000000000000000000000000000000000000000)
    0x262e: JUMP v5f7(0x5fe)

    Begin block 0x5fe
    prev=[0x25f2], succ=[0x623]
    =================================
    0x5ff: v5ff(0x40) = CONST 
    0x601: v601 = MLOAD v5ff(0x40)
    0x604: v604(0x20) = CONST 
    0x606: v606 = ADD v604(0x20), v601
    0x609: v609(0x20) = SUB v606, v601
    0x60b: MSTORE v601, v609(0x20)
    0x60f: v60f(0x3) = MLOAD v25f8
    0x611: MSTORE v606, v60f(0x3)
    0x612: v612(0x20) = CONST 
    0x614: v614 = ADD v612(0x20), v606
    0x618: v618(0x3) = MLOAD v25f8
    0x61a: v61a(0x20) = CONST 
    0x61c: v61c = ADD v61a(0x20), v25f8
    0x621: v621(0x0) = CONST 

    Begin block 0x623
    prev=[0x5fe, 0x62c], succ=[0x63e, 0x62c]
    =================================
    0x623_0x0: v623_0 = PHI v621(0x0), v637
    0x626: v626 = LT v623_0, v618(0x3)
    0x627: v627 = ISZERO v626
    0x628: v628(0x63e) = CONST 
    0x62b: JUMPI v628(0x63e), v627

    Begin block 0x63e
    prev=[0x623], succ=[0x66b, 0x652]
    =================================
    0x647: v647 = ADD v618(0x3), v614
    0x649: v649(0x1f) = CONST 
    0x64b: v64b(0x3) = AND v649(0x1f), v618(0x3)
    0x64d: v64d(0x0) = ISZERO v64b(0x3)
    0x64e: v64e(0x66b) = CONST 
    0x651: JUMPI v64e(0x66b), v64d(0x0)

    Begin block 0x66b
    prev=[0x63e, 0x652], succ=[]
    =================================
    0x66b_0x1: v66b_1 = PHI v647, v668
    0x671: v671(0x40) = CONST 
    0x673: v673 = MLOAD v671(0x40)
    0x676: v676 = SUB v66b_1, v673
    0x678: RETURN v673, v676

    Begin block 0x652
    prev=[0x63e], succ=[0x66b]
    =================================
    0x654: v654 = SUB v647, v64b(0x3)
    0x656: v656 = MLOAD v654
    0x657: v657(0x1) = CONST 
    0x65a: v65a(0x20) = CONST 
    0x65c: v65c(0x1d) = SUB v65a(0x20), v64b(0x3)
    0x65d: v65d(0x100) = CONST 
    0x660: v660(0x10000000000000000000000000000000000000000000000000000000000) = EXP v65d(0x100), v65c(0x1d)
    0x661: v661(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v660(0x10000000000000000000000000000000000000000000000000000000000), v657(0x1)
    0x662: v662(0xffffff0000000000000000000000000000000000000000000000000000000000) = NOT v661(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x663: v663 = AND v662(0xffffff0000000000000000000000000000000000000000000000000000000000), v656
    0x665: MSTORE v654, v663
    0x666: v666(0x20) = CONST 
    0x668: v668 = ADD v666(0x20), v654

    Begin block 0x62c
    prev=[0x623], succ=[0x623]
    =================================
    0x62c_0x0: v62c_0 = PHI v621(0x0), v637
    0x62e: v62e = ADD v61c, v62c_0
    0x62f: v62f = MLOAD v62e
    0x632: v632 = ADD v614, v62c_0
    0x633: MSTORE v632, v62f
    0x634: v634(0x20) = CONST 
    0x637: v637 = ADD v62c_0, v634(0x20)
    0x63a: v63a(0x623) = CONST 
    0x63d: JUMP v63a(0x623)

}

function transfer(address,uint256)() public {
    Begin block 0x679
    prev=[], succ=[0x681, 0x685]
    =================================
    0x67a: v67a = CALLVALUE 
    0x67c: v67c = ISZERO v67a
    0x67d: v67d(0x685) = CONST 
    0x680: JUMPI v67d(0x685), v67c

    Begin block 0x681
    prev=[0x679], succ=[]
    =================================
    0x681: v681(0x0) = CONST 
    0x684: REVERT v681(0x0), v681(0x0)

    Begin block 0x685
    prev=[0x679], succ=[0x262f]
    =================================
    0x687: v687(0x6c4) = CONST 
    0x68a: v68a(0x4) = CONST 
    0x68d: v68d = CALLDATASIZE 
    0x68e: v68e = SUB v68d, v68a(0x4)
    0x690: v690 = ADD v68a(0x4), v68e
    0x694: v694 = CALLDATALOAD v68a(0x4)
    0x695: v695(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6aa: v6aa = AND v695(0xffffffffffffffffffffffffffffffffffffffff), v694
    0x6ac: v6ac(0x20) = CONST 
    0x6ae: v6ae(0x24) = ADD v6ac(0x20), v68a(0x4)
    0x6b4: v6b4 = CALLDATALOAD v6ae(0x24)
    0x6b6: v6b6(0x20) = CONST 
    0x6b8: v6b8(0x44) = ADD v6b6(0x20), v6ae(0x24)
    0x6c0: v6c0(0x262f) = CONST 
    0x6c3: JUMP v6c0(0x262f)

    Begin block 0x262f
    prev=[0x685], succ=[0x2669, 0x266d]
    =================================
    0x2630: v2630(0x60) = CONST 
    0x2632: v2632(0x0) = CONST 
    0x2634: v2634(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2649: v2649(0x0) = AND v2634(0xffffffffffffffffffffffffffffffffffffffff), v2632(0x0)
    0x264b: v264b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2660: v2660 = AND v264b(0xffffffffffffffffffffffffffffffffffffffff), v6aa
    0x2661: v2661 = EQ v2660, v2649(0x0)
    0x2662: v2662 = ISZERO v2661
    0x2663: v2663 = ISZERO v2662
    0x2664: v2664 = ISZERO v2663
    0x2665: v2665(0x266d) = CONST 
    0x2668: JUMPI v2665(0x266d), v2664

    Begin block 0x2669
    prev=[0x262f], succ=[]
    =================================
    0x2669: v2669(0x0) = CONST 
    0x266c: REVERT v2669(0x0), v2669(0x0)

    Begin block 0x266d
    prev=[0x262f], succ=[0x26b7, 0x26bb]
    =================================
    0x266f: v266f(0x3) = CONST 
    0x2671: v2671(0x0) = CONST 
    0x2673: v2673 = CALLER 
    0x2674: v2674(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2689: v2689 = AND v2674(0xffffffffffffffffffffffffffffffffffffffff), v2673
    0x268a: v268a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x269f: v269f = AND v268a(0xffffffffffffffffffffffffffffffffffffffff), v2689
    0x26a1: MSTORE v2671(0x0), v269f
    0x26a2: v26a2(0x20) = CONST 
    0x26a4: v26a4(0x20) = ADD v26a2(0x20), v2671(0x0)
    0x26a7: MSTORE v26a4(0x20), v266f(0x3)
    0x26a8: v26a8(0x20) = CONST 
    0x26aa: v26aa(0x40) = ADD v26a8(0x20), v26a4(0x20)
    0x26ab: v26ab(0x0) = CONST 
    0x26ad: v26ad = SHA3 v26ab(0x0), v26aa(0x40)
    0x26ae: v26ae = SLOAD v26ad
    0x26af: v26af = LT v26ae, v6b4
    0x26b0: v26b0 = ISZERO v26af
    0x26b1: v26b1 = ISZERO v26b0
    0x26b2: v26b2 = ISZERO v26b1
    0x26b3: v26b3(0x26bb) = CONST 
    0x26b6: JUMPI v26b3(0x26bb), v26b2

    Begin block 0x26b7
    prev=[0x266d], succ=[]
    =================================
    0x26b7: v26b7(0x0) = CONST 
    0x26ba: REVERT v26b7(0x0), v26b7(0x0)

    Begin block 0x26bb
    prev=[0x266d], succ=[0x270d]
    =================================
    0x26bc: v26bc(0x270d) = CONST 
    0x26c0: v26c0(0x3) = CONST 
    0x26c2: v26c2(0x0) = CONST 
    0x26c4: v26c4 = CALLER 
    0x26c5: v26c5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26da: v26da = AND v26c5(0xffffffffffffffffffffffffffffffffffffffff), v26c4
    0x26db: v26db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26f0: v26f0 = AND v26db(0xffffffffffffffffffffffffffffffffffffffff), v26da
    0x26f2: MSTORE v26c2(0x0), v26f0
    0x26f3: v26f3(0x20) = CONST 
    0x26f5: v26f5(0x20) = ADD v26f3(0x20), v26c2(0x0)
    0x26f8: MSTORE v26f5(0x20), v26c0(0x3)
    0x26f9: v26f9(0x20) = CONST 
    0x26fb: v26fb(0x40) = ADD v26f9(0x20), v26f5(0x20)
    0x26fc: v26fc(0x0) = CONST 
    0x26fe: v26fe = SHA3 v26fc(0x0), v26fb(0x40)
    0x26ff: v26ff = SLOAD v26fe
    0x2700: v2700(0x31bf) = CONST 
    0x2706: v2706(0xffffffff) = CONST 
    0x270b: v270b(0x31bf) = AND v2706(0xffffffff), v2700(0x31bf)
    0x270c: v270c_0 = CALLPRIVATE v270b(0x31bf), v6b4, v26ff, v26bc(0x270d)

    Begin block 0x270d
    prev=[0x26bb], succ=[0x27a2]
    =================================
    0x270e: v270e(0x3) = CONST 
    0x2710: v2710(0x0) = CONST 
    0x2712: v2712 = CALLER 
    0x2713: v2713(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2728: v2728 = AND v2713(0xffffffffffffffffffffffffffffffffffffffff), v2712
    0x2729: v2729(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x273e: v273e = AND v2729(0xffffffffffffffffffffffffffffffffffffffff), v2728
    0x2740: MSTORE v2710(0x0), v273e
    0x2741: v2741(0x20) = CONST 
    0x2743: v2743(0x20) = ADD v2741(0x20), v2710(0x0)
    0x2746: MSTORE v2743(0x20), v270e(0x3)
    0x2747: v2747(0x20) = CONST 
    0x2749: v2749(0x40) = ADD v2747(0x20), v2743(0x20)
    0x274a: v274a(0x0) = CONST 
    0x274c: v274c = SHA3 v274a(0x0), v2749(0x40)
    0x274f: SSTORE v274c, v270c_0
    0x2751: v2751(0x27a2) = CONST 
    0x2755: v2755(0x3) = CONST 
    0x2757: v2757(0x0) = CONST 
    0x275a: v275a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x276f: v276f = AND v275a(0xffffffffffffffffffffffffffffffffffffffff), v6aa
    0x2770: v2770(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2785: v2785 = AND v2770(0xffffffffffffffffffffffffffffffffffffffff), v276f
    0x2787: MSTORE v2757(0x0), v2785
    0x2788: v2788(0x20) = CONST 
    0x278a: v278a(0x20) = ADD v2788(0x20), v2757(0x0)
    0x278d: MSTORE v278a(0x20), v2755(0x3)
    0x278e: v278e(0x20) = CONST 
    0x2790: v2790(0x40) = ADD v278e(0x20), v278a(0x20)
    0x2791: v2791(0x0) = CONST 
    0x2793: v2793 = SHA3 v2791(0x0), v2790(0x40)
    0x2794: v2794 = SLOAD v2793
    0x2795: v2795(0x31d8) = CONST 
    0x279b: v279b(0xffffffff) = CONST 
    0x27a0: v27a0(0x31d8) = AND v279b(0xffffffff), v2795(0x31d8)
    0x27a1: v27a1_0 = CALLPRIVATE v27a0(0x31d8), v6b4, v2794, v2751(0x27a2)

    Begin block 0x27a2
    prev=[0x270d], succ=[0x2861]
    =================================
    0x27a3: v27a3(0x3) = CONST 
    0x27a5: v27a5(0x0) = CONST 
    0x27a8: v27a8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27bd: v27bd = AND v27a8(0xffffffffffffffffffffffffffffffffffffffff), v6aa
    0x27be: v27be(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27d3: v27d3 = AND v27be(0xffffffffffffffffffffffffffffffffffffffff), v27bd
    0x27d5: MSTORE v27a5(0x0), v27d3
    0x27d6: v27d6(0x20) = CONST 
    0x27d8: v27d8(0x20) = ADD v27d6(0x20), v27a5(0x0)
    0x27db: MSTORE v27d8(0x20), v27a3(0x3)
    0x27dc: v27dc(0x20) = CONST 
    0x27de: v27de(0x40) = ADD v27dc(0x20), v27d8(0x20)
    0x27df: v27df(0x0) = CONST 
    0x27e1: v27e1 = SHA3 v27df(0x0), v27de(0x40)
    0x27e4: SSTORE v27e1, v27a1_0
    0x27e7: v27e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27fc: v27fc = AND v27e7(0xffffffffffffffffffffffffffffffffffffffff), v6aa
    0x27fd: v27fd = CALLER 
    0x27fe: v27fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2813: v2813 = AND v27fe(0xffffffffffffffffffffffffffffffffffffffff), v27fd
    0x2814: v2814(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16) = CONST 
    0x2837: v2837(0x40) = CONST 
    0x2839: v2839 = MLOAD v2837(0x40)
    0x283d: MSTORE v2839, v6b4
    0x283e: v283e(0x20) = CONST 
    0x2840: v2840 = ADD v283e(0x20), v2839
    0x2842: v2842(0x20) = CONST 
    0x2844: v2844 = ADD v2842(0x20), v2840
    0x2847: v2847(0x40) = SUB v2844, v2839
    0x2849: MSTORE v2840, v2847(0x40)
    0x284d: v284d = MLOAD v2630(0x60)
    0x284f: MSTORE v2844, v284d
    0x2850: v2850(0x20) = CONST 
    0x2852: v2852 = ADD v2850(0x20), v2844
    0x2856: v2856 = MLOAD v2630(0x60)
    0x2858: v2858(0x20) = CONST 
    0x285a: v285a(0x80) = ADD v2858(0x20), v2630(0x60)
    0x285f: v285f(0x0) = CONST 

    Begin block 0x2861
    prev=[0x27a2, 0x286a], succ=[0x287c, 0x286a]
    =================================
    0x2861_0x0: v2861_0 = PHI v285f(0x0), v2875
    0x2864: v2864 = LT v2861_0, v2856
    0x2865: v2865 = ISZERO v2864
    0x2866: v2866(0x287c) = CONST 
    0x2869: JUMPI v2866(0x287c), v2865

    Begin block 0x287c
    prev=[0x2861], succ=[0x28a9, 0x2890]
    =================================
    0x2885: v2885 = ADD v2856, v2852
    0x2887: v2887(0x1f) = CONST 
    0x2889: v2889 = AND v2887(0x1f), v2856
    0x288b: v288b = ISZERO v2889
    0x288c: v288c(0x28a9) = CONST 
    0x288f: JUMPI v288c(0x28a9), v288b

    Begin block 0x28a9
    prev=[0x287c, 0x2890], succ=[0x6c4]
    =================================
    0x28a9_0x1: v28a9_1 = PHI v2885, v28a6
    0x28b0: v28b0(0x40) = CONST 
    0x28b2: v28b2 = MLOAD v28b0(0x40)
    0x28b5: v28b5 = SUB v28a9_1, v28b2
    0x28b7: LOG3 v28b2, v28b5, v2814(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16), v2813, v27fc
    0x28bb: JUMP v687(0x6c4)

    Begin block 0x6c4
    prev=[0x28a9], succ=[]
    =================================
    0x6c5: STOP 

    Begin block 0x2890
    prev=[0x287c], succ=[0x28a9]
    =================================
    0x2892: v2892 = SUB v2885, v2889
    0x2894: v2894 = MLOAD v2892
    0x2895: v2895(0x1) = CONST 
    0x2898: v2898(0x20) = CONST 
    0x289a: v289a = SUB v2898(0x20), v2889
    0x289b: v289b(0x100) = CONST 
    0x289e: v289e = EXP v289b(0x100), v289a
    0x289f: v289f = SUB v289e, v2895(0x1)
    0x28a0: v28a0 = NOT v289f
    0x28a1: v28a1 = AND v28a0, v2894
    0x28a3: MSTORE v2892, v28a1
    0x28a4: v28a4(0x20) = CONST 
    0x28a6: v28a6 = ADD v28a4(0x20), v2892

    Begin block 0x286a
    prev=[0x2861], succ=[0x2861]
    =================================
    0x286a_0x0: v286a_0 = PHI v285f(0x0), v2875
    0x286c: v286c = ADD v285a(0x80), v286a_0
    0x286d: v286d = MLOAD v286c
    0x2870: v2870 = ADD v2852, v286a_0
    0x2871: MSTORE v2870, v286d
    0x2872: v2872(0x20) = CONST 
    0x2875: v2875 = ADD v286a_0, v2872(0x20)
    0x2878: v2878(0x2861) = CONST 
    0x287b: JUMP v2878(0x2861)

}

function transfer(address,uint256,bytes)() public {
    Begin block 0x6c6
    prev=[], succ=[0x6ce, 0x6d2]
    =================================
    0x6c7: v6c7 = CALLVALUE 
    0x6c9: v6c9 = ISZERO v6c7
    0x6ca: v6ca(0x6d2) = CONST 
    0x6cd: JUMPI v6ca(0x6d2), v6c9

    Begin block 0x6ce
    prev=[0x6c6], succ=[]
    =================================
    0x6ce: v6ce(0x0) = CONST 
    0x6d1: REVERT v6ce(0x0), v6ce(0x0)

    Begin block 0x6d2
    prev=[0x6c6], succ=[0x28bc]
    =================================
    0x6d4: v6d4(0x757) = CONST 
    0x6d7: v6d7(0x4) = CONST 
    0x6da: v6da = CALLDATASIZE 
    0x6db: v6db = SUB v6da, v6d7(0x4)
    0x6dd: v6dd = ADD v6d7(0x4), v6db
    0x6e1: v6e1 = CALLDATALOAD v6d7(0x4)
    0x6e2: v6e2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6f7: v6f7 = AND v6e2(0xffffffffffffffffffffffffffffffffffffffff), v6e1
    0x6f9: v6f9(0x20) = CONST 
    0x6fb: v6fb(0x24) = ADD v6f9(0x20), v6d7(0x4)
    0x701: v701 = CALLDATALOAD v6fb(0x24)
    0x703: v703(0x20) = CONST 
    0x705: v705(0x44) = ADD v703(0x20), v6fb(0x24)
    0x70b: v70b = CALLDATALOAD v705(0x44)
    0x70d: v70d(0x20) = CONST 
    0x70f: v70f(0x64) = ADD v70d(0x20), v705(0x44)
    0x712: v712 = ADD v6d7(0x4), v70b
    0x714: v714 = CALLDATALOAD v712
    0x716: v716(0x20) = CONST 
    0x718: v718 = ADD v716(0x20), v712
    0x71c: v71c(0x1f) = CONST 
    0x71e: v71e = ADD v71c(0x1f), v714
    0x71f: v71f(0x20) = CONST 
    0x723: v723 = DIV v71e, v71f(0x20)
    0x724: v724 = MUL v723, v71f(0x20)
    0x725: v725(0x20) = CONST 
    0x727: v727 = ADD v725(0x20), v724
    0x728: v728(0x40) = CONST 
    0x72a: v72a = MLOAD v728(0x40)
    0x72d: v72d = ADD v72a, v727
    0x72e: v72e(0x40) = CONST 
    0x730: MSTORE v72e(0x40), v72d
    0x738: MSTORE v72a, v714
    0x739: v739(0x20) = CONST 
    0x73b: v73b = ADD v739(0x20), v72a
    0x741: CALLDATACOPY v73b, v718, v714
    0x743: v743 = ADD v73b, v714
    0x753: v753(0x28bc) = CONST 
    0x756: JUMP v753(0x28bc)

    Begin block 0x28bc
    prev=[0x6d2], succ=[0x28f7, 0x28fb]
    =================================
    0x28bd: v28bd(0x0) = CONST 
    0x28c0: v28c0(0x0) = CONST 
    0x28c2: v28c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28d7: v28d7(0x0) = AND v28c2(0xffffffffffffffffffffffffffffffffffffffff), v28c0(0x0)
    0x28d9: v28d9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28ee: v28ee = AND v28d9(0xffffffffffffffffffffffffffffffffffffffff), v6f7
    0x28ef: v28ef = EQ v28ee, v28d7(0x0)
    0x28f0: v28f0 = ISZERO v28ef
    0x28f1: v28f1 = ISZERO v28f0
    0x28f2: v28f2 = ISZERO v28f1
    0x28f3: v28f3(0x28fb) = CONST 
    0x28f6: JUMPI v28f3(0x28fb), v28f2

    Begin block 0x28f7
    prev=[0x28bc], succ=[]
    =================================
    0x28f7: v28f7(0x0) = CONST 
    0x28fa: REVERT v28f7(0x0), v28f7(0x0)

    Begin block 0x28fb
    prev=[0x28bc], succ=[0x2945, 0x2949]
    =================================
    0x28fd: v28fd(0x3) = CONST 
    0x28ff: v28ff(0x0) = CONST 
    0x2901: v2901 = CALLER 
    0x2902: v2902(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2917: v2917 = AND v2902(0xffffffffffffffffffffffffffffffffffffffff), v2901
    0x2918: v2918(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x292d: v292d = AND v2918(0xffffffffffffffffffffffffffffffffffffffff), v2917
    0x292f: MSTORE v28ff(0x0), v292d
    0x2930: v2930(0x20) = CONST 
    0x2932: v2932(0x20) = ADD v2930(0x20), v28ff(0x0)
    0x2935: MSTORE v2932(0x20), v28fd(0x3)
    0x2936: v2936(0x20) = CONST 
    0x2938: v2938(0x40) = ADD v2936(0x20), v2932(0x20)
    0x2939: v2939(0x0) = CONST 
    0x293b: v293b = SHA3 v2939(0x0), v2938(0x40)
    0x293c: v293c = SLOAD v293b
    0x293d: v293d = LT v293c, v701
    0x293e: v293e = ISZERO v293d
    0x293f: v293f = ISZERO v293e
    0x2940: v2940 = ISZERO v293f
    0x2941: v2941(0x2949) = CONST 
    0x2944: JUMPI v2941(0x2949), v2940

    Begin block 0x2945
    prev=[0x28fb], succ=[]
    =================================
    0x2945: v2945(0x0) = CONST 
    0x2948: REVERT v2945(0x0), v2945(0x0)

    Begin block 0x2949
    prev=[0x28fb], succ=[0x299f]
    =================================
    0x294b: v294b = EXTCODESIZE v6f7
    0x294e: v294e(0x299f) = CONST 
    0x2952: v2952(0x3) = CONST 
    0x2954: v2954(0x0) = CONST 
    0x2956: v2956 = CALLER 
    0x2957: v2957(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x296c: v296c = AND v2957(0xffffffffffffffffffffffffffffffffffffffff), v2956
    0x296d: v296d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2982: v2982 = AND v296d(0xffffffffffffffffffffffffffffffffffffffff), v296c
    0x2984: MSTORE v2954(0x0), v2982
    0x2985: v2985(0x20) = CONST 
    0x2987: v2987(0x20) = ADD v2985(0x20), v2954(0x0)
    0x298a: MSTORE v2987(0x20), v2952(0x3)
    0x298b: v298b(0x20) = CONST 
    0x298d: v298d(0x40) = ADD v298b(0x20), v2987(0x20)
    0x298e: v298e(0x0) = CONST 
    0x2990: v2990 = SHA3 v298e(0x0), v298d(0x40)
    0x2991: v2991 = SLOAD v2990
    0x2992: v2992(0x31bf) = CONST 
    0x2998: v2998(0xffffffff) = CONST 
    0x299d: v299d(0x31bf) = AND v2998(0xffffffff), v2992(0x31bf)
    0x299e: v299e_0 = CALLPRIVATE v299d(0x31bf), v701, v2991, v294e(0x299f)

    Begin block 0x299f
    prev=[0x2949], succ=[0x2a34]
    =================================
    0x29a0: v29a0(0x3) = CONST 
    0x29a2: v29a2(0x0) = CONST 
    0x29a4: v29a4 = CALLER 
    0x29a5: v29a5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29ba: v29ba = AND v29a5(0xffffffffffffffffffffffffffffffffffffffff), v29a4
    0x29bb: v29bb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29d0: v29d0 = AND v29bb(0xffffffffffffffffffffffffffffffffffffffff), v29ba
    0x29d2: MSTORE v29a2(0x0), v29d0
    0x29d3: v29d3(0x20) = CONST 
    0x29d5: v29d5(0x20) = ADD v29d3(0x20), v29a2(0x0)
    0x29d8: MSTORE v29d5(0x20), v29a0(0x3)
    0x29d9: v29d9(0x20) = CONST 
    0x29db: v29db(0x40) = ADD v29d9(0x20), v29d5(0x20)
    0x29dc: v29dc(0x0) = CONST 
    0x29de: v29de = SHA3 v29dc(0x0), v29db(0x40)
    0x29e1: SSTORE v29de, v299e_0
    0x29e3: v29e3(0x2a34) = CONST 
    0x29e7: v29e7(0x3) = CONST 
    0x29e9: v29e9(0x0) = CONST 
    0x29ec: v29ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a01: v2a01 = AND v29ec(0xffffffffffffffffffffffffffffffffffffffff), v6f7
    0x2a02: v2a02(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a17: v2a17 = AND v2a02(0xffffffffffffffffffffffffffffffffffffffff), v2a01
    0x2a19: MSTORE v29e9(0x0), v2a17
    0x2a1a: v2a1a(0x20) = CONST 
    0x2a1c: v2a1c(0x20) = ADD v2a1a(0x20), v29e9(0x0)
    0x2a1f: MSTORE v2a1c(0x20), v29e7(0x3)
    0x2a20: v2a20(0x20) = CONST 
    0x2a22: v2a22(0x40) = ADD v2a20(0x20), v2a1c(0x20)
    0x2a23: v2a23(0x0) = CONST 
    0x2a25: v2a25 = SHA3 v2a23(0x0), v2a22(0x40)
    0x2a26: v2a26 = SLOAD v2a25
    0x2a27: v2a27(0x31d8) = CONST 
    0x2a2d: v2a2d(0xffffffff) = CONST 
    0x2a32: v2a32(0x31d8) = AND v2a2d(0xffffffff), v2a27(0x31d8)
    0x2a33: v2a33_0 = CALLPRIVATE v2a32(0x31d8), v701, v2a26, v29e3(0x2a34)

    Begin block 0x2a34
    prev=[0x299f], succ=[0x2bac, 0x2a81]
    =================================
    0x2a35: v2a35(0x3) = CONST 
    0x2a37: v2a37(0x0) = CONST 
    0x2a3a: v2a3a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a4f: v2a4f = AND v2a3a(0xffffffffffffffffffffffffffffffffffffffff), v6f7
    0x2a50: v2a50(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a65: v2a65 = AND v2a50(0xffffffffffffffffffffffffffffffffffffffff), v2a4f
    0x2a67: MSTORE v2a37(0x0), v2a65
    0x2a68: v2a68(0x20) = CONST 
    0x2a6a: v2a6a(0x20) = ADD v2a68(0x20), v2a37(0x0)
    0x2a6d: MSTORE v2a6a(0x20), v2a35(0x3)
    0x2a6e: v2a6e(0x20) = CONST 
    0x2a70: v2a70(0x40) = ADD v2a6e(0x20), v2a6a(0x20)
    0x2a71: v2a71(0x0) = CONST 
    0x2a73: v2a73 = SHA3 v2a71(0x0), v2a70(0x40)
    0x2a76: SSTORE v2a73, v2a33_0
    0x2a78: v2a78(0x0) = CONST 
    0x2a7b: v2a7b = GT v294b, v2a78(0x0)
    0x2a7c: v2a7c = ISZERO v2a7b
    0x2a7d: v2a7d(0x2bac) = CONST 
    0x2a80: JUMPI v2a7d(0x2bac), v2a7c

    Begin block 0x2bac
    prev=[0x2a34, 0x2ba7], succ=[0x2c28]
    =================================
    0x2bae: v2bae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2bc3: v2bc3 = AND v2bae(0xffffffffffffffffffffffffffffffffffffffff), v6f7
    0x2bc4: v2bc4 = CALLER 
    0x2bc5: v2bc5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2bda: v2bda = AND v2bc5(0xffffffffffffffffffffffffffffffffffffffff), v2bc4
    0x2bdb: v2bdb(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16) = CONST 
    0x2bfe: v2bfe(0x40) = CONST 
    0x2c00: v2c00 = MLOAD v2bfe(0x40)
    0x2c04: MSTORE v2c00, v701
    0x2c05: v2c05(0x20) = CONST 
    0x2c07: v2c07 = ADD v2c05(0x20), v2c00
    0x2c09: v2c09(0x20) = CONST 
    0x2c0b: v2c0b = ADD v2c09(0x20), v2c07
    0x2c0e: v2c0e(0x40) = SUB v2c0b, v2c00
    0x2c10: MSTORE v2c07, v2c0e(0x40)
    0x2c14: v2c14 = MLOAD v72a
    0x2c16: MSTORE v2c0b, v2c14
    0x2c17: v2c17(0x20) = CONST 
    0x2c19: v2c19 = ADD v2c17(0x20), v2c0b
    0x2c1d: v2c1d = MLOAD v72a
    0x2c1f: v2c1f(0x20) = CONST 
    0x2c21: v2c21 = ADD v2c1f(0x20), v72a
    0x2c26: v2c26(0x0) = CONST 

    Begin block 0x2c28
    prev=[0x2bac, 0x2c31], succ=[0x2c43, 0x2c31]
    =================================
    0x2c28_0x0: v2c28_0 = PHI v2c26(0x0), v2c3c
    0x2c2b: v2c2b = LT v2c28_0, v2c1d
    0x2c2c: v2c2c = ISZERO v2c2b
    0x2c2d: v2c2d(0x2c43) = CONST 
    0x2c30: JUMPI v2c2d(0x2c43), v2c2c

    Begin block 0x2c43
    prev=[0x2c28], succ=[0x2c70, 0x2c57]
    =================================
    0x2c4c: v2c4c = ADD v2c1d, v2c19
    0x2c4e: v2c4e(0x1f) = CONST 
    0x2c50: v2c50 = AND v2c4e(0x1f), v2c1d
    0x2c52: v2c52 = ISZERO v2c50
    0x2c53: v2c53(0x2c70) = CONST 
    0x2c56: JUMPI v2c53(0x2c70), v2c52

    Begin block 0x2c70
    prev=[0x2c43, 0x2c57], succ=[0x757]
    =================================
    0x2c70_0x1: v2c70_1 = PHI v2c4c, v2c6d
    0x2c77: v2c77(0x40) = CONST 
    0x2c79: v2c79 = MLOAD v2c77(0x40)
    0x2c7c: v2c7c = SUB v2c70_1, v2c79
    0x2c7e: LOG3 v2c79, v2c7c, v2bdb(0xe19260aff97b920c7df27010903aeb9c8d2be5d310a2c67824cf3f15396e4c16), v2bda, v2bc3
    0x2c84: JUMP v6d4(0x757)

    Begin block 0x757
    prev=[0x2c70], succ=[]
    =================================
    0x758: STOP 

    Begin block 0x2c57
    prev=[0x2c43], succ=[0x2c70]
    =================================
    0x2c59: v2c59 = SUB v2c4c, v2c50
    0x2c5b: v2c5b = MLOAD v2c59
    0x2c5c: v2c5c(0x1) = CONST 
    0x2c5f: v2c5f(0x20) = CONST 
    0x2c61: v2c61 = SUB v2c5f(0x20), v2c50
    0x2c62: v2c62(0x100) = CONST 
    0x2c65: v2c65 = EXP v2c62(0x100), v2c61
    0x2c66: v2c66 = SUB v2c65, v2c5c(0x1)
    0x2c67: v2c67 = NOT v2c66
    0x2c68: v2c68 = AND v2c67, v2c5b
    0x2c6a: MSTORE v2c59, v2c68
    0x2c6b: v2c6b(0x20) = CONST 
    0x2c6d: v2c6d = ADD v2c6b(0x20), v2c59

    Begin block 0x2c31
    prev=[0x2c28], succ=[0x2c28]
    =================================
    0x2c31_0x0: v2c31_0 = PHI v2c26(0x0), v2c3c
    0x2c33: v2c33 = ADD v2c21, v2c31_0
    0x2c34: v2c34 = MLOAD v2c33
    0x2c37: v2c37 = ADD v2c19, v2c31_0
    0x2c38: MSTORE v2c37, v2c34
    0x2c39: v2c39(0x20) = CONST 
    0x2c3c: v2c3c = ADD v2c31_0, v2c39(0x20)
    0x2c3f: v2c3f(0x2c28) = CONST 
    0x2c42: JUMP v2c3f(0x2c28)

    Begin block 0x2a81
    prev=[0x2a34], succ=[0x2b2a]
    =================================
    0x2a85: v2a85(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a9a: v2a9a = AND v2a85(0xffffffffffffffffffffffffffffffffffffffff), v6f7
    0x2a9b: v2a9b(0xc0ee0b8a) = CONST 
    0x2aa0: v2aa0 = CALLER 
    0x2aa3: v2aa3(0x40) = CONST 
    0x2aa5: v2aa5 = MLOAD v2aa3(0x40)
    0x2aa7: v2aa7(0xffffffff) = CONST 
    0x2aac: v2aac(0xc0ee0b8a) = AND v2aa7(0xffffffff), v2a9b(0xc0ee0b8a)
    0x2aad: v2aad(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2acb: v2acb(0xc0ee0b8a00000000000000000000000000000000000000000000000000000000) = MUL v2aad(0x100000000000000000000000000000000000000000000000000000000), v2aac(0xc0ee0b8a)
    0x2acd: MSTORE v2aa5, v2acb(0xc0ee0b8a00000000000000000000000000000000000000000000000000000000)
    0x2ace: v2ace(0x4) = CONST 
    0x2ad0: v2ad0 = ADD v2ace(0x4), v2aa5
    0x2ad3: v2ad3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ae8: v2ae8 = AND v2ad3(0xffffffffffffffffffffffffffffffffffffffff), v2aa0
    0x2ae9: v2ae9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2afe: v2afe = AND v2ae9(0xffffffffffffffffffffffffffffffffffffffff), v2ae8
    0x2b00: MSTORE v2ad0, v2afe
    0x2b01: v2b01(0x20) = CONST 
    0x2b03: v2b03 = ADD v2b01(0x20), v2ad0
    0x2b06: MSTORE v2b03, v701
    0x2b07: v2b07(0x20) = CONST 
    0x2b09: v2b09 = ADD v2b07(0x20), v2b03
    0x2b0b: v2b0b(0x20) = CONST 
    0x2b0d: v2b0d = ADD v2b0b(0x20), v2b09
    0x2b10: v2b10(0x60) = SUB v2b0d, v2ad0
    0x2b12: MSTORE v2b09, v2b10(0x60)
    0x2b16: v2b16 = MLOAD v72a
    0x2b18: MSTORE v2b0d, v2b16
    0x2b19: v2b19(0x20) = CONST 
    0x2b1b: v2b1b = ADD v2b19(0x20), v2b0d
    0x2b1f: v2b1f = MLOAD v72a
    0x2b21: v2b21(0x20) = CONST 
    0x2b23: v2b23 = ADD v2b21(0x20), v72a
    0x2b28: v2b28(0x0) = CONST 

    Begin block 0x2b2a
    prev=[0x2a81, 0x2b33], succ=[0x2b45, 0x2b33]
    =================================
    0x2b2a_0x0: v2b2a_0 = PHI v2b28(0x0), v2b3e
    0x2b2d: v2b2d = LT v2b2a_0, v2b1f
    0x2b2e: v2b2e = ISZERO v2b2d
    0x2b2f: v2b2f(0x2b45) = CONST 
    0x2b32: JUMPI v2b2f(0x2b45), v2b2e

    Begin block 0x2b45
    prev=[0x2b2a], succ=[0x2b72, 0x2b59]
    =================================
    0x2b4e: v2b4e = ADD v2b1f, v2b1b
    0x2b50: v2b50(0x1f) = CONST 
    0x2b52: v2b52 = AND v2b50(0x1f), v2b1f
    0x2b54: v2b54 = ISZERO v2b52
    0x2b55: v2b55(0x2b72) = CONST 
    0x2b58: JUMPI v2b55(0x2b72), v2b54

    Begin block 0x2b72
    prev=[0x2b45, 0x2b59], succ=[0x2b8f, 0x2b93]
    =================================
    0x2b72_0x1: v2b72_1 = PHI v2b4e, v2b6f
    0x2b7a: v2b7a(0x0) = CONST 
    0x2b7c: v2b7c(0x40) = CONST 
    0x2b7e: v2b7e = MLOAD v2b7c(0x40)
    0x2b81: v2b81 = SUB v2b72_1, v2b7e
    0x2b83: v2b83(0x0) = CONST 
    0x2b87: v2b87 = EXTCODESIZE v2a9a
    0x2b88: v2b88 = ISZERO v2b87
    0x2b8a: v2b8a = ISZERO v2b88
    0x2b8b: v2b8b(0x2b93) = CONST 
    0x2b8e: JUMPI v2b8b(0x2b93), v2b8a

    Begin block 0x2b8f
    prev=[0x2b72], succ=[]
    =================================
    0x2b8f: v2b8f(0x0) = CONST 
    0x2b92: REVERT v2b8f(0x0), v2b8f(0x0)

    Begin block 0x2b93
    prev=[0x2b72], succ=[0x2b9e, 0x2ba7]
    =================================
    0x2b95: v2b95 = GAS 
    0x2b96: v2b96 = CALL v2b95, v2a9a, v2b83(0x0), v2b7e, v2b81, v2b7e, v2b7a(0x0)
    0x2b97: v2b97 = ISZERO v2b96
    0x2b99: v2b99 = ISZERO v2b97
    0x2b9a: v2b9a(0x2ba7) = CONST 
    0x2b9d: JUMPI v2b9a(0x2ba7), v2b99

    Begin block 0x2b9e
    prev=[0x2b93], succ=[]
    =================================
    0x2b9e: v2b9e = RETURNDATASIZE 
    0x2b9f: v2b9f(0x0) = CONST 
    0x2ba2: RETURNDATACOPY v2b9f(0x0), v2b9f(0x0), v2b9e
    0x2ba3: v2ba3 = RETURNDATASIZE 
    0x2ba4: v2ba4(0x0) = CONST 
    0x2ba6: REVERT v2ba4(0x0), v2ba3

    Begin block 0x2ba7
    prev=[0x2b93], succ=[0x2bac]
    =================================

    Begin block 0x2b59
    prev=[0x2b45], succ=[0x2b72]
    =================================
    0x2b5b: v2b5b = SUB v2b4e, v2b52
    0x2b5d: v2b5d = MLOAD v2b5b
    0x2b5e: v2b5e(0x1) = CONST 
    0x2b61: v2b61(0x20) = CONST 
    0x2b63: v2b63 = SUB v2b61(0x20), v2b52
    0x2b64: v2b64(0x100) = CONST 
    0x2b67: v2b67 = EXP v2b64(0x100), v2b63
    0x2b68: v2b68 = SUB v2b67, v2b5e(0x1)
    0x2b69: v2b69 = NOT v2b68
    0x2b6a: v2b6a = AND v2b69, v2b5d
    0x2b6c: MSTORE v2b5b, v2b6a
    0x2b6d: v2b6d(0x20) = CONST 
    0x2b6f: v2b6f = ADD v2b6d(0x20), v2b5b

    Begin block 0x2b33
    prev=[0x2b2a], succ=[0x2b2a]
    =================================
    0x2b33_0x0: v2b33_0 = PHI v2b28(0x0), v2b3e
    0x2b35: v2b35 = ADD v2b23, v2b33_0
    0x2b36: v2b36 = MLOAD v2b35
    0x2b39: v2b39 = ADD v2b1b, v2b33_0
    0x2b3a: MSTORE v2b39, v2b36
    0x2b3b: v2b3b(0x20) = CONST 
    0x2b3e: v2b3e = ADD v2b33_0, v2b3b(0x20)
    0x2b41: v2b41(0x2b2a) = CONST 
    0x2b44: JUMP v2b41(0x2b2a)

}

function increaseApproval(address,uint256)() public {
    Begin block 0x759
    prev=[], succ=[0x761, 0x765]
    =================================
    0x75a: v75a = CALLVALUE 
    0x75c: v75c = ISZERO v75a
    0x75d: v75d(0x765) = CONST 
    0x760: JUMPI v75d(0x765), v75c

    Begin block 0x761
    prev=[0x759], succ=[]
    =================================
    0x761: v761(0x0) = CONST 
    0x764: REVERT v761(0x0), v761(0x0)

    Begin block 0x765
    prev=[0x759], succ=[0x2c85]
    =================================
    0x767: v767(0x7a4) = CONST 
    0x76a: v76a(0x4) = CONST 
    0x76d: v76d = CALLDATASIZE 
    0x76e: v76e = SUB v76d, v76a(0x4)
    0x770: v770 = ADD v76a(0x4), v76e
    0x774: v774 = CALLDATALOAD v76a(0x4)
    0x775: v775(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x78a: v78a = AND v775(0xffffffffffffffffffffffffffffffffffffffff), v774
    0x78c: v78c(0x20) = CONST 
    0x78e: v78e(0x24) = ADD v78c(0x20), v76a(0x4)
    0x794: v794 = CALLDATALOAD v78e(0x24)
    0x796: v796(0x20) = CONST 
    0x798: v798(0x44) = ADD v796(0x20), v78e(0x24)
    0x7a0: v7a0(0x2c85) = CONST 
    0x7a3: JUMP v7a0(0x2c85)

    Begin block 0x2c85
    prev=[0x765], succ=[0x2cbe, 0x2cc2]
    =================================
    0x2c86: v2c86(0x0) = CONST 
    0x2c89: v2c89(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c9e: v2c9e(0x0) = AND v2c89(0xffffffffffffffffffffffffffffffffffffffff), v2c86(0x0)
    0x2ca0: v2ca0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2cb5: v2cb5 = AND v2ca0(0xffffffffffffffffffffffffffffffffffffffff), v78a
    0x2cb6: v2cb6 = EQ v2cb5, v2c9e(0x0)
    0x2cb7: v2cb7 = ISZERO v2cb6
    0x2cb8: v2cb8 = ISZERO v2cb7
    0x2cb9: v2cb9 = ISZERO v2cb8
    0x2cba: v2cba(0x2cc2) = CONST 
    0x2cbd: JUMPI v2cba(0x2cc2), v2cb9

    Begin block 0x2cbe
    prev=[0x2c85], succ=[]
    =================================
    0x2cbe: v2cbe(0x0) = CONST 
    0x2cc1: REVERT v2cbe(0x0), v2cbe(0x0)

    Begin block 0x2cc2
    prev=[0x2c85], succ=[0x2d0c, 0x2d10]
    =================================
    0x2cc3: v2cc3(0x3) = CONST 
    0x2cc5: v2cc5(0x0) = CONST 
    0x2cc7: v2cc7 = CALLER 
    0x2cc8: v2cc8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2cdd: v2cdd = AND v2cc8(0xffffffffffffffffffffffffffffffffffffffff), v2cc7
    0x2cde: v2cde(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2cf3: v2cf3 = AND v2cde(0xffffffffffffffffffffffffffffffffffffffff), v2cdd
    0x2cf5: MSTORE v2cc5(0x0), v2cf3
    0x2cf6: v2cf6(0x20) = CONST 
    0x2cf8: v2cf8(0x20) = ADD v2cf6(0x20), v2cc5(0x0)
    0x2cfb: MSTORE v2cf8(0x20), v2cc3(0x3)
    0x2cfc: v2cfc(0x20) = CONST 
    0x2cfe: v2cfe(0x40) = ADD v2cfc(0x20), v2cf8(0x20)
    0x2cff: v2cff(0x0) = CONST 
    0x2d01: v2d01 = SHA3 v2cff(0x0), v2cfe(0x40)
    0x2d02: v2d02 = SLOAD v2d01
    0x2d04: v2d04 = GT v794, v2d02
    0x2d05: v2d05 = ISZERO v2d04
    0x2d06: v2d06 = ISZERO v2d05
    0x2d07: v2d07 = ISZERO v2d06
    0x2d08: v2d08(0x2d10) = CONST 
    0x2d0b: JUMPI v2d08(0x2d10), v2d07

    Begin block 0x2d0c
    prev=[0x2cc2], succ=[]
    =================================
    0x2d0c: v2d0c(0x0) = CONST 
    0x2d0f: REVERT v2d0c(0x0), v2d0c(0x0)

    Begin block 0x2d10
    prev=[0x2cc2], succ=[0x2d9f]
    =================================
    0x2d11: v2d11(0x2d9f) = CONST 
    0x2d15: v2d15(0x4) = CONST 
    0x2d17: v2d17(0x0) = CONST 
    0x2d19: v2d19 = CALLER 
    0x2d1a: v2d1a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d2f: v2d2f = AND v2d1a(0xffffffffffffffffffffffffffffffffffffffff), v2d19
    0x2d30: v2d30(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d45: v2d45 = AND v2d30(0xffffffffffffffffffffffffffffffffffffffff), v2d2f
    0x2d47: MSTORE v2d17(0x0), v2d45
    0x2d48: v2d48(0x20) = CONST 
    0x2d4a: v2d4a(0x20) = ADD v2d48(0x20), v2d17(0x0)
    0x2d4d: MSTORE v2d4a(0x20), v2d15(0x4)
    0x2d4e: v2d4e(0x20) = CONST 
    0x2d50: v2d50(0x40) = ADD v2d4e(0x20), v2d4a(0x20)
    0x2d51: v2d51(0x0) = CONST 
    0x2d53: v2d53 = SHA3 v2d51(0x0), v2d50(0x40)
    0x2d54: v2d54(0x0) = CONST 
    0x2d57: v2d57(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d6c: v2d6c = AND v2d57(0xffffffffffffffffffffffffffffffffffffffff), v78a
    0x2d6d: v2d6d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d82: v2d82 = AND v2d6d(0xffffffffffffffffffffffffffffffffffffffff), v2d6c
    0x2d84: MSTORE v2d54(0x0), v2d82
    0x2d85: v2d85(0x20) = CONST 
    0x2d87: v2d87(0x20) = ADD v2d85(0x20), v2d54(0x0)
    0x2d8a: MSTORE v2d87(0x20), v2d53
    0x2d8b: v2d8b(0x20) = CONST 
    0x2d8d: v2d8d(0x40) = ADD v2d8b(0x20), v2d87(0x20)
    0x2d8e: v2d8e(0x0) = CONST 
    0x2d90: v2d90 = SHA3 v2d8e(0x0), v2d8d(0x40)
    0x2d91: v2d91 = SLOAD v2d90
    0x2d92: v2d92(0x31d8) = CONST 
    0x2d98: v2d98(0xffffffff) = CONST 
    0x2d9d: v2d9d(0x31d8) = AND v2d98(0xffffffff), v2d92(0x31d8)
    0x2d9e: v2d9e_0 = CALLPRIVATE v2d9d(0x31d8), v794, v2d91, v2d11(0x2d9f)

    Begin block 0x2d9f
    prev=[0x2d10], succ=[0x7a4]
    =================================
    0x2da0: v2da0(0x4) = CONST 
    0x2da2: v2da2(0x0) = CONST 
    0x2da4: v2da4 = CALLER 
    0x2da5: v2da5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2dba: v2dba = AND v2da5(0xffffffffffffffffffffffffffffffffffffffff), v2da4
    0x2dbb: v2dbb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2dd0: v2dd0 = AND v2dbb(0xffffffffffffffffffffffffffffffffffffffff), v2dba
    0x2dd2: MSTORE v2da2(0x0), v2dd0
    0x2dd3: v2dd3(0x20) = CONST 
    0x2dd5: v2dd5(0x20) = ADD v2dd3(0x20), v2da2(0x0)
    0x2dd8: MSTORE v2dd5(0x20), v2da0(0x4)
    0x2dd9: v2dd9(0x20) = CONST 
    0x2ddb: v2ddb(0x40) = ADD v2dd9(0x20), v2dd5(0x20)
    0x2ddc: v2ddc(0x0) = CONST 
    0x2dde: v2dde = SHA3 v2ddc(0x0), v2ddb(0x40)
    0x2ddf: v2ddf(0x0) = CONST 
    0x2de2: v2de2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2df7: v2df7 = AND v2de2(0xffffffffffffffffffffffffffffffffffffffff), v78a
    0x2df8: v2df8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e0d: v2e0d = AND v2df8(0xffffffffffffffffffffffffffffffffffffffff), v2df7
    0x2e0f: MSTORE v2ddf(0x0), v2e0d
    0x2e10: v2e10(0x20) = CONST 
    0x2e12: v2e12(0x20) = ADD v2e10(0x20), v2ddf(0x0)
    0x2e15: MSTORE v2e12(0x20), v2dde
    0x2e16: v2e16(0x20) = CONST 
    0x2e18: v2e18(0x40) = ADD v2e16(0x20), v2e12(0x20)
    0x2e19: v2e19(0x0) = CONST 
    0x2e1b: v2e1b = SHA3 v2e19(0x0), v2e18(0x40)
    0x2e1e: SSTORE v2e1b, v2d9e_0
    0x2e21: v2e21(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e36: v2e36 = AND v2e21(0xffffffffffffffffffffffffffffffffffffffff), v78a
    0x2e37: v2e37 = CALLER 
    0x2e38: v2e38(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e4d: v2e4d = AND v2e38(0xffffffffffffffffffffffffffffffffffffffff), v2e37
    0x2e4e: v2e4e(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x2e6f: v2e6f(0x4) = CONST 
    0x2e71: v2e71(0x0) = CONST 
    0x2e73: v2e73 = CALLER 
    0x2e74: v2e74(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e89: v2e89 = AND v2e74(0xffffffffffffffffffffffffffffffffffffffff), v2e73
    0x2e8a: v2e8a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e9f: v2e9f = AND v2e8a(0xffffffffffffffffffffffffffffffffffffffff), v2e89
    0x2ea1: MSTORE v2e71(0x0), v2e9f
    0x2ea2: v2ea2(0x20) = CONST 
    0x2ea4: v2ea4(0x20) = ADD v2ea2(0x20), v2e71(0x0)
    0x2ea7: MSTORE v2ea4(0x20), v2e6f(0x4)
    0x2ea8: v2ea8(0x20) = CONST 
    0x2eaa: v2eaa(0x40) = ADD v2ea8(0x20), v2ea4(0x20)
    0x2eab: v2eab(0x0) = CONST 
    0x2ead: v2ead = SHA3 v2eab(0x0), v2eaa(0x40)
    0x2eae: v2eae(0x0) = CONST 
    0x2eb1: v2eb1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ec6: v2ec6 = AND v2eb1(0xffffffffffffffffffffffffffffffffffffffff), v78a
    0x2ec7: v2ec7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2edc: v2edc = AND v2ec7(0xffffffffffffffffffffffffffffffffffffffff), v2ec6
    0x2ede: MSTORE v2eae(0x0), v2edc
    0x2edf: v2edf(0x20) = CONST 
    0x2ee1: v2ee1(0x20) = ADD v2edf(0x20), v2eae(0x0)
    0x2ee4: MSTORE v2ee1(0x20), v2ead
    0x2ee5: v2ee5(0x20) = CONST 
    0x2ee7: v2ee7(0x40) = ADD v2ee5(0x20), v2ee1(0x20)
    0x2ee8: v2ee8(0x0) = CONST 
    0x2eea: v2eea = SHA3 v2ee8(0x0), v2ee7(0x40)
    0x2eeb: v2eeb = SLOAD v2eea
    0x2eec: v2eec(0x40) = CONST 
    0x2eee: v2eee = MLOAD v2eec(0x40)
    0x2ef2: MSTORE v2eee, v2eeb
    0x2ef3: v2ef3(0x20) = CONST 
    0x2ef5: v2ef5 = ADD v2ef3(0x20), v2eee
    0x2ef9: v2ef9(0x40) = CONST 
    0x2efb: v2efb = MLOAD v2ef9(0x40)
    0x2efe: v2efe(0x20) = SUB v2ef5, v2efb
    0x2f00: LOG3 v2efb, v2efe(0x20), v2e4e(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v2e4d, v2e36
    0x2f01: v2f01(0x1) = CONST 
    0x2f09: JUMP v767(0x7a4)

    Begin block 0x7a4
    prev=[0x2d9f], succ=[]
    =================================
    0x7a5: v7a5(0x40) = CONST 
    0x7a7: v7a7 = MLOAD v7a5(0x40)
    0x7aa: v7aa(0x0) = ISZERO v2f01(0x1)
    0x7ab: v7ab(0x1) = ISZERO v7aa(0x0)
    0x7ac: v7ac(0x0) = ISZERO v7ab(0x1)
    0x7ad: v7ad(0x1) = ISZERO v7ac(0x0)
    0x7af: MSTORE v7a7, v7ad(0x1)
    0x7b0: v7b0(0x20) = CONST 
    0x7b2: v7b2 = ADD v7b0(0x20), v7a7
    0x7b6: v7b6(0x40) = CONST 
    0x7b8: v7b8 = MLOAD v7b6(0x40)
    0x7bb: v7bb(0x20) = SUB v7b2, v7b8
    0x7bd: RETURN v7b8, v7bb(0x20)

}

function allowance(address,address)() public {
    Begin block 0x7be
    prev=[], succ=[0x7c6, 0x7ca]
    =================================
    0x7bf: v7bf = CALLVALUE 
    0x7c1: v7c1 = ISZERO v7bf
    0x7c2: v7c2(0x7ca) = CONST 
    0x7c5: JUMPI v7c2(0x7ca), v7c1

    Begin block 0x7c6
    prev=[0x7be], succ=[]
    =================================
    0x7c6: v7c6(0x0) = CONST 
    0x7c9: REVERT v7c6(0x0), v7c6(0x0)

    Begin block 0x7ca
    prev=[0x7be], succ=[0x2f0a]
    =================================
    0x7cc: v7cc(0x81f) = CONST 
    0x7cf: v7cf(0x4) = CONST 
    0x7d2: v7d2 = CALLDATASIZE 
    0x7d3: v7d3 = SUB v7d2, v7cf(0x4)
    0x7d5: v7d5 = ADD v7cf(0x4), v7d3
    0x7d9: v7d9 = CALLDATALOAD v7cf(0x4)
    0x7da: v7da(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7ef: v7ef = AND v7da(0xffffffffffffffffffffffffffffffffffffffff), v7d9
    0x7f1: v7f1(0x20) = CONST 
    0x7f3: v7f3(0x24) = ADD v7f1(0x20), v7cf(0x4)
    0x7f9: v7f9 = CALLDATALOAD v7f3(0x24)
    0x7fa: v7fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x80f: v80f = AND v7fa(0xffffffffffffffffffffffffffffffffffffffff), v7f9
    0x811: v811(0x20) = CONST 
    0x813: v813(0x44) = ADD v811(0x20), v7f3(0x24)
    0x81b: v81b(0x2f0a) = CONST 
    0x81e: JUMP v81b(0x2f0a)

    Begin block 0x2f0a
    prev=[0x7ca], succ=[0x2f43, 0x2f47]
    =================================
    0x2f0b: v2f0b(0x0) = CONST 
    0x2f0e: v2f0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f23: v2f23(0x0) = AND v2f0e(0xffffffffffffffffffffffffffffffffffffffff), v2f0b(0x0)
    0x2f25: v2f25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f3a: v2f3a = AND v2f25(0xffffffffffffffffffffffffffffffffffffffff), v7ef
    0x2f3b: v2f3b = EQ v2f3a, v2f23(0x0)
    0x2f3c: v2f3c = ISZERO v2f3b
    0x2f3d: v2f3d = ISZERO v2f3c
    0x2f3e: v2f3e = ISZERO v2f3d
    0x2f3f: v2f3f(0x2f47) = CONST 
    0x2f42: JUMPI v2f3f(0x2f47), v2f3e

    Begin block 0x2f43
    prev=[0x2f0a], succ=[]
    =================================
    0x2f43: v2f43(0x0) = CONST 
    0x2f46: REVERT v2f43(0x0), v2f43(0x0)

    Begin block 0x2f47
    prev=[0x2f0a], succ=[0x2f7f, 0x2f83]
    =================================
    0x2f48: v2f48(0x0) = CONST 
    0x2f4a: v2f4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f5f: v2f5f(0x0) = AND v2f4a(0xffffffffffffffffffffffffffffffffffffffff), v2f48(0x0)
    0x2f61: v2f61(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f76: v2f76 = AND v2f61(0xffffffffffffffffffffffffffffffffffffffff), v80f
    0x2f77: v2f77 = EQ v2f76, v2f5f(0x0)
    0x2f78: v2f78 = ISZERO v2f77
    0x2f79: v2f79 = ISZERO v2f78
    0x2f7a: v2f7a = ISZERO v2f79
    0x2f7b: v2f7b(0x2f83) = CONST 
    0x2f7e: JUMPI v2f7b(0x2f83), v2f7a

    Begin block 0x2f7f
    prev=[0x2f47], succ=[]
    =================================
    0x2f7f: v2f7f(0x0) = CONST 
    0x2f82: REVERT v2f7f(0x0), v2f7f(0x0)

    Begin block 0x2f83
    prev=[0x2f47], succ=[0x81f]
    =================================
    0x2f84: v2f84(0x4) = CONST 
    0x2f86: v2f86(0x0) = CONST 
    0x2f89: v2f89(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f9e: v2f9e = AND v2f89(0xffffffffffffffffffffffffffffffffffffffff), v7ef
    0x2f9f: v2f9f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fb4: v2fb4 = AND v2f9f(0xffffffffffffffffffffffffffffffffffffffff), v2f9e
    0x2fb6: MSTORE v2f86(0x0), v2fb4
    0x2fb7: v2fb7(0x20) = CONST 
    0x2fb9: v2fb9(0x20) = ADD v2fb7(0x20), v2f86(0x0)
    0x2fbc: MSTORE v2fb9(0x20), v2f84(0x4)
    0x2fbd: v2fbd(0x20) = CONST 
    0x2fbf: v2fbf(0x40) = ADD v2fbd(0x20), v2fb9(0x20)
    0x2fc0: v2fc0(0x0) = CONST 
    0x2fc2: v2fc2 = SHA3 v2fc0(0x0), v2fbf(0x40)
    0x2fc3: v2fc3(0x0) = CONST 
    0x2fc6: v2fc6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fdb: v2fdb = AND v2fc6(0xffffffffffffffffffffffffffffffffffffffff), v80f
    0x2fdc: v2fdc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ff1: v2ff1 = AND v2fdc(0xffffffffffffffffffffffffffffffffffffffff), v2fdb
    0x2ff3: MSTORE v2fc3(0x0), v2ff1
    0x2ff4: v2ff4(0x20) = CONST 
    0x2ff6: v2ff6(0x20) = ADD v2ff4(0x20), v2fc3(0x0)
    0x2ff9: MSTORE v2ff6(0x20), v2fc2
    0x2ffa: v2ffa(0x20) = CONST 
    0x2ffc: v2ffc(0x40) = ADD v2ffa(0x20), v2ff6(0x20)
    0x2ffd: v2ffd(0x0) = CONST 
    0x2fff: v2fff = SHA3 v2ffd(0x0), v2ffc(0x40)
    0x3000: v3000 = SLOAD v2fff
    0x3007: JUMP v7cc(0x81f)

    Begin block 0x81f
    prev=[0x2f83], succ=[]
    =================================
    0x820: v820(0x40) = CONST 
    0x822: v822 = MLOAD v820(0x40)
    0x826: MSTORE v822, v3000
    0x827: v827(0x20) = CONST 
    0x829: v829 = ADD v827(0x20), v822
    0x82d: v82d(0x40) = CONST 
    0x82f: v82f = MLOAD v82d(0x40)
    0x832: v832(0x20) = SUB v829, v82f
    0x834: RETURN v82f, v832(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x835
    prev=[], succ=[0x83d, 0x841]
    =================================
    0x836: v836 = CALLVALUE 
    0x838: v838 = ISZERO v836
    0x839: v839(0x841) = CONST 
    0x83c: JUMPI v839(0x841), v838

    Begin block 0x83d
    prev=[0x835], succ=[]
    =================================
    0x83d: v83d(0x0) = CONST 
    0x840: REVERT v83d(0x0), v83d(0x0)

    Begin block 0x841
    prev=[0x835], succ=[0x3008]
    =================================
    0x843: v843(0x876) = CONST 
    0x846: v846(0x4) = CONST 
    0x849: v849 = CALLDATASIZE 
    0x84a: v84a = SUB v849, v846(0x4)
    0x84c: v84c = ADD v846(0x4), v84a
    0x850: v850 = CALLDATALOAD v846(0x4)
    0x851: v851(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x866: v866 = AND v851(0xffffffffffffffffffffffffffffffffffffffff), v850
    0x868: v868(0x20) = CONST 
    0x86a: v86a(0x24) = ADD v868(0x20), v846(0x4)
    0x872: v872(0x3008) = CONST 
    0x875: JUMP v872(0x3008)

    Begin block 0x3008
    prev=[0x841], succ=[0x30a2, 0x305e]
    =================================
    0x3009: v3009(0x0) = CONST 
    0x300d: v300d = SLOAD v3009(0x0)
    0x300f: v300f(0x100) = CONST 
    0x3012: v3012(0x1) = EXP v300f(0x100), v3009(0x0)
    0x3014: v3014 = DIV v300d, v3012(0x1)
    0x3015: v3015(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x302a: v302a = AND v3015(0xffffffffffffffffffffffffffffffffffffffff), v3014
    0x302b: v302b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3040: v3040 = AND v302b(0xffffffffffffffffffffffffffffffffffffffff), v302a
    0x3041: v3041 = CALLER 
    0x3042: v3042(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3057: v3057 = AND v3042(0xffffffffffffffffffffffffffffffffffffffff), v3041
    0x3058: v3058 = EQ v3057, v3040
    0x305a: v305a(0x30a2) = CONST 
    0x305d: JUMPI v305a(0x30a2), v3058

    Begin block 0x30a2
    prev=[0x3008, 0x305e], succ=[0x30a9, 0x30ad]
    =================================
    0x30a2_0x0: v30a2_0 = PHI v3058, v30a1
    0x30a3: v30a3 = ISZERO v30a2_0
    0x30a4: v30a4 = ISZERO v30a3
    0x30a5: v30a5(0x30ad) = CONST 
    0x30a8: JUMPI v30a5(0x30ad), v30a4

    Begin block 0x30a9
    prev=[0x30a2], succ=[]
    =================================
    0x30a9: v30a9(0x0) = CONST 
    0x30ac: REVERT v30a9(0x0), v30a9(0x0)

    Begin block 0x30ad
    prev=[0x30a2], succ=[0x30e5, 0x30e9]
    =================================
    0x30ae: v30ae(0x0) = CONST 
    0x30b0: v30b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x30c5: v30c5(0x0) = AND v30b0(0xffffffffffffffffffffffffffffffffffffffff), v30ae(0x0)
    0x30c7: v30c7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x30dc: v30dc = AND v30c7(0xffffffffffffffffffffffffffffffffffffffff), v866
    0x30dd: v30dd = EQ v30dc, v30c5(0x0)
    0x30de: v30de = ISZERO v30dd
    0x30df: v30df = ISZERO v30de
    0x30e0: v30e0 = ISZERO v30df
    0x30e1: v30e1(0x30e9) = CONST 
    0x30e4: JUMPI v30e1(0x30e9), v30e0

    Begin block 0x30e5
    prev=[0x30ad], succ=[]
    =================================
    0x30e5: v30e5(0x0) = CONST 
    0x30e8: REVERT v30e5(0x0), v30e5(0x0)

    Begin block 0x30e9
    prev=[0x30ad], succ=[0x876]
    =================================
    0x30eb: v30eb(0x0) = CONST 
    0x30ee: v30ee(0x100) = CONST 
    0x30f1: v30f1(0x1) = EXP v30ee(0x100), v30eb(0x0)
    0x30f3: v30f3 = SLOAD v30eb(0x0)
    0x30f5: v30f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x310a: v310a(0xffffffffffffffffffffffffffffffffffffffff) = MUL v30f5(0xffffffffffffffffffffffffffffffffffffffff), v30f1(0x1)
    0x310b: v310b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v310a(0xffffffffffffffffffffffffffffffffffffffff)
    0x310c: v310c = AND v310b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v30f3
    0x310f: v310f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3124: v3124 = AND v310f(0xffffffffffffffffffffffffffffffffffffffff), v866
    0x3125: v3125 = MUL v3124, v30f1(0x1)
    0x3126: v3126 = OR v3125, v310c
    0x3128: SSTORE v30eb(0x0), v3126
    0x312a: v312a(0x0) = CONST 
    0x312e: v312e = SLOAD v312a(0x0)
    0x3130: v3130(0x100) = CONST 
    0x3133: v3133(0x1) = EXP v3130(0x100), v312a(0x0)
    0x3135: v3135 = DIV v312e, v3133(0x1)
    0x3136: v3136(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x314b: v314b = AND v3136(0xffffffffffffffffffffffffffffffffffffffff), v3135
    0x314c: v314c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3161: v3161 = AND v314c(0xffffffffffffffffffffffffffffffffffffffff), v314b
    0x3162: v3162 = CALLER 
    0x3163: v3163(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3178: v3178 = AND v3163(0xffffffffffffffffffffffffffffffffffffffff), v3162
    0x3179: v3179(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x319a: v319a(0x40) = CONST 
    0x319c: v319c = MLOAD v319a(0x40)
    0x319d: v319d(0x40) = CONST 
    0x319f: v319f = MLOAD v319d(0x40)
    0x31a2: v31a2(0x0) = SUB v319c, v319f
    0x31a4: LOG3 v319f, v31a2(0x0), v3179(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v3178, v3161
    0x31a6: JUMP v843(0x876)

    Begin block 0x876
    prev=[0x30e9], succ=[]
    =================================
    0x877: STOP 

    Begin block 0x305e
    prev=[0x3008], succ=[0x30a2]
    =================================
    0x305f: v305f(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = CONST 
    0x3074: v3074(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3089: v3089(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = AND v3074(0xffffffffffffffffffffffffffffffffffffffff), v305f(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0x308a: v308a = CALLER 
    0x308b: v308b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x30a0: v30a0 = AND v308b(0xffffffffffffffffffffffffffffffffffffffff), v308a
    0x30a1: v30a1 = EQ v30a0, v3089(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)

}

function TOKEN_OWNER()() public {
    Begin block 0x878
    prev=[], succ=[0x880, 0x884]
    =================================
    0x879: v879 = CALLVALUE 
    0x87b: v87b = ISZERO v879
    0x87c: v87c(0x884) = CONST 
    0x87f: JUMPI v87c(0x884), v87b

    Begin block 0x880
    prev=[0x878], succ=[]
    =================================
    0x880: v880(0x0) = CONST 
    0x883: REVERT v880(0x0), v880(0x0)

    Begin block 0x884
    prev=[0x878], succ=[0x31a7]
    =================================
    0x886: v886(0x88d) = CONST 
    0x889: v889(0x31a7) = CONST 
    0x88c: JUMP v889(0x31a7)

    Begin block 0x31a7
    prev=[0x884], succ=[0x88d]
    =================================
    0x31a8: v31a8(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = CONST 
    0x31be: JUMP v886(0x88d)

    Begin block 0x88d
    prev=[0x31a7], succ=[]
    =================================
    0x88e: v88e(0x40) = CONST 
    0x890: v890 = MLOAD v88e(0x40)
    0x893: v893(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8a8: v8a8(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = AND v893(0xffffffffffffffffffffffffffffffffffffffff), v31a8(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0x8a9: v8a9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8be: v8be(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8) = AND v8a9(0xffffffffffffffffffffffffffffffffffffffff), v8a8(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0x8c0: MSTORE v890, v8be(0x57cdd07287f668ec4d58f3e362b4fcc2bc54f5b8)
    0x8c1: v8c1(0x20) = CONST 
    0x8c3: v8c3 = ADD v8c1(0x20), v890
    0x8c7: v8c7(0x40) = CONST 
    0x8c9: v8c9 = MLOAD v8c7(0x40)
    0x8cc: v8cc(0x20) = SUB v8c3, v8c9
    0x8ce: RETURN v8c9, v8cc(0x20)

}

