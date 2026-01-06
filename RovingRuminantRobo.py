import math

n = int(input())
c = list(str(input()))
def getDiff(a,b):
    temp = 0
    for i in range(len(n)):
        if a[n] != b[a]:
            temp += 1
    return temp
def calulatePos(l,loc=[0,0]):
    #         [X,Y]
    tempLoc = loc
    for t in range(len(l)):
        if   l[t] == 'U':
            tempLoc[1] += 1
        elif l[t] == 'D':
            tempLoc[1] -= 1
        elif l[t] == 'R':
            tempLoc[0] += 1
        elif l[t] == 'L':
            tempLoc[0] -= 1
    return tempLoc
    
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
#           [X,Y]
targetLoc = calulatePos(c)
smallestDiff = math.inf
for b in range(n**4):
    t2 = base10_to_base4(b)
    t2 = ((n - len(t2)) * '0') + t2
    test = ''
    for i in range(len(t2)):
        if   t2[i] == '0':
            test += 'U'
        elif t2[i] == '1':
            test += 'D'
        elif t2[i] == '2':
            test += 'R'
        elif t2[i] == '3':
            test += 'L'
    tempTest = calulatePos(list(test),targetLoc)
    if tempTest == [0,0]:
        if getDiff(tempTest,targetLoc) < smallestDiff:
            smallestDiff = getDiff(tempTest,targetLoc)
if smallestDiff == math.inf:
    print('-1')
else:
    print(smallestDiff)
    