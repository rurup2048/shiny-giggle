import math
n, q = list(map(int,input().split()))
# n = 6
# q = 4
# h = [7, 3, 4, 1, 5, 3]
h = list(map(int,input().split()))
testCases = []
for j in range(q):
    testCases.append(list(map(str,input().split())))

for i in range(q):
    # print(h)
    l = testCases[i][0]
    n = testCases[i][1:]
    if l == 'A':
        n = int(n[0])
        temp1 = int((h[n-1]+h[n])/2)
        temp2 = math.ceil((h[n-1]+h[n])/2)
        h[n-1] = temp1
        h[n] = temp2
    else:
        k1 = int(n[0])
        k2 = int(n[1])
        print(sum(h[k1-1:k2]))
    # print('-------------------')
        