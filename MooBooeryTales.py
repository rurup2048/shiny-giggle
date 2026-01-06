n, m, k = list(map(int,input().split()))
testCases = []
storys = {}
for j in range(n):
    testCases.append(list(map(str,input().split())))

for test in range(len(testCases)):
    hasPassed = True
    tc = testCases[test]
    for t in tc:
        for l in range(1,k+1):
            if test-l >= 0:
                if t in testCases[test-l]:
                    hasPassed = False
    if hasPassed:
        print('MOO')
    else:
        print('BOO')
            