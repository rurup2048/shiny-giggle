t = int(input())
ancrs = []
for i in range(t):
    c, n = list(map(int, input().split()))
    s = list(map(int, input().split()))
    isPossable = True
    if sum(s)%n != 0:
        isPossable = False
        
    
    if isPossable:
        ancrs.append('YES')
    else:
        ancrs.append('NO')
for i in range(t):
    print(ancrs[i])
        