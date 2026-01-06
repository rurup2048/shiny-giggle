'''
7
*..*..*
.*.***.
..****.
.******
..***..
.*.*.*.
*..*..*
'''
n = int(input())
board = ''
total = 0
for i in range(n):
    board += str(input())
# print(list(board).count('*'))
for spiderSize in range((n//2)+1):
    total = 0
    for loc in board:
        isSpider = True
        for dirs in [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]:
            for s in range(spiderSize):
                print(board[(s*dirs[0])+(s*spiderSize*dirs[1])])
                print((s*dirs[0])+(s*spiderSize*dirs[1]))
                if board[(s*dirs[0])+(s*spiderSize*dirs[1])] != '*':
                    print(spiderSize)
                    isSpider = False
        if isSpider:
            total += 1
    print(total)
                    
    