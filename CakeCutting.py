t = int(input())
testCases = []
for i in range(t):
    testCases.append([])
    testCases[i].append(list(map(int, input().split())))
    testCases[i].append([])
    for j in range(testCases[i][0][0]):
        testCases[i][1].append(list(map(int, input().split())))

for test in testCases:
    r,c,h,v =  test[0]
    board = test[1]
    isPossable = True
    
    Rcase = []
    for row in range(r):
        # print(board[r-1])
        temp = sum(board[r-1])
        Rcase.append(temp)
    
    Ccase = []
    for col in range(c):
        temp = 0
        for row in range(r):
            temp += board[row][col]
        Ccase.append(temp)
    # print('R:\t',Rcase)
    # print('C:\t',Ccase)
    
    pos = 0
    while pos != len(Rcase):
        if sum(Rcase[:pos]) == sum(Rcase[pos:]):
            break
        pos += 1
    if pos == len(Rcase):
        isPossable = False
    
    if isPossable:
        pos = 0
        while pos != len(Ccase):
            if sum(Ccase[:pos]) == sum(Ccase[pos:]):
                break
            pos += 1
        if pos == len(Rcase):
            isPossable = False
    
    
    if isPossable:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
    
    
            
            
    
# r,c,h,v = list(map(int, input().split()))
