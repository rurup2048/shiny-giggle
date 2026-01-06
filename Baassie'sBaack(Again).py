def getSum(x):
    output = 0
    x = list(str(x))
    for i in x:
        output += int(i)
    return output
total = 0
a, b = list(map(int,input().split()))
for i in range(a,b+1):
    turnCap = 10**5
    turn = 0
    isSleep = False
    n = i
    while not isSleep or turn >= turnCap:
        temp = getSum(n**2)
        if temp == n:
            isSleep = True
        else:
            n = temp
        turn += 1
    if isSleep:
        total += 1
print(total)
        