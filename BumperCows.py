'''
3 135
0 180 90
-1 1 -1
'''
total = 0
n, t = list(map(int,input().split()))
curPos = list(map(int,input().split()))
curDir = list(map(int,input().split()))
for i in range(n):
    if curPos[i] == 360:
        curPos[i] = 0
    if curPos[i] == 0:
        curPos[i] = 360
for turn in range(t):
    for i in range(n):
        curPos[i] += curDir[i]
        if curPos[i] == 360:
            curPos[i] = 0
        if curPos[i] == 0:
            curPos[i] = 360
    for i in range(n):
        if curPos.count(curPos[i]) > 1:
            curDir[i] *= -1
            total += 0.5
print(int(total))