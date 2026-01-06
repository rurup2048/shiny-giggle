b, r = list(map(int,input().split()))
g = list(map(int,input().split()))
m = list(map(int,input().split()))
score = 0
targetLocs = []
for i in range(r):
    targetLocs.append(sum(m[:i+1])+b)
for j in range(r):
    score += abs(targetLocs[j]-g[j])
print(score-b)