s = int(input())
board = list(map(int, input().split()))
anc = ''
board.sort()
for i in range(s):
    anc += str(board[i])+' '

print(anc.strip())