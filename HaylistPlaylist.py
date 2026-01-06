n = int(input())
s = list(map(int,input().split()))
longest = 0
sLoc = 0
eLoc = 1
while sLoc != n:
    temp = []
    for i in range(sLoc,eLoc):
        temp.append(s[i])
        if len(temp) == len(set(temp)):
            if len(temp) > longest:
                longest = len(temp)
    if eLoc == n:
        sLoc += 1
        eLoc = sLoc+1
    else:
        eLoc += 1
print(longest)