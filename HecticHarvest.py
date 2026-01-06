def maxPot():
    pos = None
    amnt = 0
    for j in range(len(fields)):
        if fields[j][1] > amnt:
            amnt = fields[j][0]
            pos = j

    return pos
def calalateRot():
    t = 0
    for k in range(len(fields)):
        t += fields[k][1]
    return t

n = int(input())
totalRot = 0
fields = []
for h in range(n):
    fields.append(list(map(int,input().split())))
    

potLoc = maxPot()
timer = fields[potLoc][0]
while len(fields) > 0:
    totalRot += calalateRot()
    timer -= 1
    if timer == 0:
        fields.pop(potLoc)
        if len(fields) > 0:
            potLoc = maxPot()
            timer = fields[potLoc][0]
    
print(totalRot)
'''
order: timer -> check -> rot
r1 3 1+2
r2 5 +2
r3 7 +2
r4 9 +2
r5 11 +2

rot : rotAmount
3 2
2 1
'''
        
    



