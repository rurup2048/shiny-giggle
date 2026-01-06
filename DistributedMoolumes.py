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

t = int(input())
nx = []
anc = []
for i in range(t):
    line = list(map(int,input().split()))
    nx.append(line)

for c in nx:
    test, r = c
    maxTB = 0
    isPossable = False
    tb = []
    eb = []
    for i in range(2**test):
        t2 = base10_to_base2(i)
        t2 = ((test - len(t2)) * '0') + t2
        b = 0
        e = 0
        ltb = 0
        leb = 0
        for j in range(1,len(t2)+1):
            if t2[j-1] == '0':
                b += 1 
                ltb += j
            else:
                e += 1
                leb += j
        if b > e and leb == ltb:
            isPossable = True
            if b > maxTB:
                maxTB = b
            
    if isPossable:
        print('POSSIBLE')
        if r == 2:
            print(maxTB)
    else:
        print('IMPOSSIBLE')
            