n = int(input())
c = list(map(int, input().split()))
c.sort()

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

total = set()

for b in range(n**2):
    m = 0
    t2 = base10_to_base2(b)
    t2 = ((n - len(t2)) * '0') + t2
    for j in range(len(t2)):
        if t2[j] == '1':
            m += c[j]
    total.add(m)
print(len(total)-1)
#1 2 4 7 9