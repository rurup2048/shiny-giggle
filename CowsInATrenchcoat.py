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
numAnc = 0
n, k, j = list(map(int,input().split()))
s = list(map(int,input().split()))
for t in range(n**2):
    t2 = base10_to_base2(t)
    t2 = ((n - len(t2)) * '0') + t2
    total = 0
    if list(t2).count('1') <= k:
        pass
    for p in range(len(t2)):
        if t2[p] == '1':
            total += s[p]
    if total == j:
        numAnc += 1 
print(numAnc)
            
        