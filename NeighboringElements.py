h, w = list(map(int,input().split()))
boardCount = []
total = 0
for row in range(h):
    board = list(map(int,input().split()))
    boardCount.append(board[1])
    boardCount.append(board[-2])
    for spaceLoc in range(1,w-1):
        boardCount.append(board[spaceLoc-1] + board[spaceLoc+1])
print(boardCount.count(int(input())))
    