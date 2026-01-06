n, q = list(map(int,input().split()))
testCases = []
# pots = list('0'*n)
pots = list(map(int,('0'*(n+1))))
for j in range(q):
    testCases.append(list(map(int,input().split())))

for test in testCases:
    s, a, b = test
    if a != b:
        for i in range(a,b+1):
            pots[i] += s
    else:
        pots[a] += s
anc = ''
for p in range(1,len(pots)):
    if p != len(pots)-1:
        anc += str(pots[p]) + ' '
    else:
        anc += str(pots[p])
print(anc)