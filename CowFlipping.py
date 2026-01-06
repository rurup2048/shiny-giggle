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

def shift(x):
    for i in range(len(cows)):
        if i % x == 0:
            if tempCow[i] == 'R':
                tempCow[i] = 'L'
            else:
                tempCow[i] = 'R'
    

n  = int(input())
cows = list(str(input()))
leastMoves = -9999999999999999999999999999999999999999
for h in range(2**n):
    tempCow = cows
    moves = 0
    h2 = base10_to_base2(h)
    h2 = ((n - len(h2)) * '0') + h2
    for c in range(1,len(h2)):
        if h2[c] == '1':
            shift(c)
            moves += 1
    print(tempCow)
    if tempCow == list('R'*n) or tempCow == list('L'*n):
        print('1')
        if leastMoves > moves:
            print('2')
            leastMoves = moves
print(leastMoves)

