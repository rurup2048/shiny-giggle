s = []
n = int(input())
testCases = []
for j in range(n):
    testCases.append(list(map(str,input().split())))
for t in testCases: 
    for k in t:
        if k not in s:
            s.append(k)
        else:
            s.remove(k)
    print(100000-len(s))
