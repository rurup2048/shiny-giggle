def base10_to_base4(q):
    base = 4
    if q == 0:
        return "0"  

    result = ""
    while q > 0:
        remainder = q % base
        result = str(remainder) + result
        q //= base

    return result
# def moveList(i):
    
x, y = list(map(int,input().split()))
i = 0
isDone = False
while i+i*i <= 10**9:
    t4 = base10_to_base4(i)
    tx = 0
    ty = 0
    j = 1
    moves = ''
    for t in t4:
        if t == '0':
            tx -= j
            moves += 'L'
        elif t == '1':
            tx += j
            moves += 'R'
        elif t == '2':
            ty += j
            moves += 'U'
        else:
            ty -= j
            moves += 'D'
        j *= 2
    if x == tx and y == ty:
        print(moves)
        isDone = True
        break
    i += 1
if not isDone:
    print('IMPOSSIBLE')
    