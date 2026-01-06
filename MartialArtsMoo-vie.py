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

def isValid(t,s,isb):
    tenemys = enemys
    aura = 0
    stamia = s
    isVal = True
    loc = 0
    for i in t:
        if len(tenemys) == 0:
            break
        if i == '0':
            if stamia < tenemys[loc]:
                isVal = False
            else:
                stamia -= tenemys[loc]
                tenemys.pop(loc)
                loc += 1
                loc = loc % len(tenemys)
        elif i == '1':
            loc += 1
            loc = loc % len(tenemys)
        elif i == '2':
            tenemys.pop(loc)
        elif i == '3':
            if aura > 0:
                aura -= 1
                stamia += tenemys[loc]
                tenemys.pop(loc)
                loc += 1
                loc = loc % len(tenemys)
            else:
                isVal = False
        print('-----------')
        print('isb:\t'+str(isb))
        print('tenemys:\t'+str(tenemys))
        print('aura:\t'+str(aura))
        print('loc:\t'+str(loc))
        print('isVal:\t'+str(isVal))
        print('i:\t'+str(i))
        print('================')
        
    if isb:
        return isVal
    else:
        return aura
# s, n = list(map(int,input().split()))
# enemys = list(map(int,input().split()))
s, n = [100,5]
enemys = [125, 20, 250, 200, 150]
maxAura = 0
for i in range(4**n):
    i4 = base10_to_base4(i)
    i4 = ((n - len(i4)) * '0') + i4
    if isValid(i4, s, True):
        if isValid(i4, s, False) > maxAura:
            maxAura = isValid(i4, s, False)
print(maxAura)