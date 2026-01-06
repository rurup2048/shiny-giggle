def base10_to_base2(q):
    base = 2
    if q == 0:
        return "0"  

    result = ""
    while q > 0:
        remainder = q % base
        result = str(remainder) + result
        q //= base

    return result
board = ''
for i in range(6):
     line = str(input())
     # line = str(map(str,input()))
     board = board + line
# board = 'MOOMOOOMOOMOOOMOOMMOOMOOO..O..O..O..'
# board = 'OOOOMMOOOOMMOOMMOOOOMMOOMMOOOOMMOOOO'
numMissing = 0
total = 0
thing = ['M', 'O']
for j in board:
    if j == '.':
        numMissing += 1
for i in range(2**numMissing):
    t2 = base10_to_base2(i)
    t2 = ((numMissing - len(t2)) * '0') + t2
    tBoard = list(board)
    isCom = True
    pos = 0
    for k in range(len(tBoard)):
        if tBoard[k] == '.':
            tBoard[k] = thing[int(t2[pos])]
            pos += 1
    for l in range(6):
        a1 = tBoard[l*6:(l*6)+6]
        a2 = [tBoard[l], tBoard[l+6], tBoard[l+12], tBoard[l+18],tBoard[l+24],tBoard[l+30]]
        a1.sort()
        a2.sort()
        # print(str(a1)+'<-a1 == a2-> '+str(a2),end=' ')
        if a1 != ['M','M','O','O','O','O'] or a2 != ['M','M','O','O','O','O']:
            isCom = False
            # print('f')
        else:
            # print('s')
            pass
    if isCom:
        # print(t2)
        # print(tBoard[0:6])
        # print(tBoard[6:12])
        # print(tBoard[12:18])
        # print(tBoard[18:24])
        # print(tBoard[24:30])
        # print(tBoard[30:36])
        # print('-----------')
        total += 1
print(total)
        