testCases = [[[5, 4], [4, 1, 9, 2, 7]], [[4, 3], [2, 7, 6, 5]]]
t = 2
t = int(input())
for thing in range(t):
    testCases.append([0,0])
    testCases[thing][0] = list(map(int,input().split()))
    testCases[thing][1] = list(map(int,input().split()))
for test in range(t):
    n, d = testCases[test][0]
    an = testCases[test][1]
    sLoc = n-1
    eLoc = sLoc -1
    isFound = False
    # while (not isFound) or sLoc != 0: 
    while sLoc != 0 and not isFound:
        # print('s:'+str(sLoc)+'->'+str(an[sLoc]))
        # print('e:'+str(eLoc)+'->'+str(an[eLoc]))
        # print('-------------')
        i = an[sLoc]
        j = an[eLoc]
        if i - j == d:
            isFound = True
        if eLoc == 0:
            sLoc -= 1
            eLoc = sLoc-1
        else:
            eLoc -= 1
    if isFound:
        print('YES')
    else:
        print('NO')