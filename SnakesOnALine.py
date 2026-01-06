def pot(loc):
    total = 0
    for j in snakes:
        sPos = j[0]
        ePos = j[1]
        if sPos <= loc and loc <= ePos:
            total += 1
    return total

n = int(input())
snakes = []
smallest = 10**10
largest = 0
total = 0
locs = []
for s in range(n):
    snakes.append(list(map(int,input().split())))
    locs.append(snakes[s][0])
    locs.append(snakes[s][1])
    if snakes[s][0] <= smallest:
        smallest = snakes[s][0]
    if snakes[s][1] >= largest:
        largest = snakes[s][1]
        
# i = [[7, 11],[2, 4],[13, 15],[4, 6],[10, 14]]
# i.sort()
# print(i)
locs.sort()
locs.reverse()
while snakes != []:
    maxPot = 0
    maxpos = 0
    for i in locs:
        if pot(i) > maxPot:
            maxPot = pot(i)
            maxpos = i
    tempLocs = []
    for j in range(len(snakes)-1,-1,-1):
        if snakes[j][0] <= maxpos and maxpos <= snakes[j][1]:
            snakes.pop(j)
    total += 1
print(total)

