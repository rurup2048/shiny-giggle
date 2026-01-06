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

n,k = list(map(int,input().split()))
currLoc = 1
endTotal = 0
smallestTotal = 2**n
for i in range(2**n):
    i2 = base10_to_base2(i)
    total = 1
    numMoves = 0
    isOver = False
    for j in i2:       
        if isOver:
            pass
        if j == '1':
            total *= k
        else:
            total += 1
        if total == n:
            isOver = True
        numMoves += 1
    if numMoves < smallestTotal and isOver:
        smallestTotal = numMoves
print(str(smallestTotal))