def base10_to_base3(q):
    if q == 0:
        return "0"  

    result = ""
    while q > 0:
        remainder = q % 3
        result = str(remainder) + result
        q //= 3

    return result

amount = 0
n, s = list(map(str,input().split()))
n = int(n)
t = ['C','O','W']
for i in range((3**n)):
    n3 = base10_to_base3(i)
    n3 = ((n - len(n3)) * '0') + n3
    temp = ''
    for j in range(len(s)):
        temp += str(t.index(s[j]))
    if not temp in n3:
        amount += 1
print(str(amount))
        
        