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

n  = int(input())
f = list(map(int,input().split()))
f.sort()
mostHay = 0
for h in range(2**n):
    h2 = base10_to_base2(h)
    h2 = ((n - len(h2)) * '0') + h2
    isLegal = True
    temp = [0]
    for i in range(len(h2)):
        if h2[i] == '1':
            if abs(f[i] - temp[-1]) >= 10:
                temp.append(f[i])
    if mostHay < sum(temp):
        mostHay = sum(temp)
print(mostHay)