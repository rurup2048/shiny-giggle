mn = list(map(int,input().split()))
m, n = mn[0], mn[1]
g = list(map(int,input().split()))
h = list(map(int,input().split()))
# mn = list(map(int,'3 4'.split()))
# m, n = mn[0], mn[1]
# g = list(map(int,'3030 9 100'.split()))
# h = list(map(int,'7000 60 401 1000000000'.split()))
allHeights = []
for x in g:
    allHeights.append(int(str(x)+'0'))
for y in h:
    allHeights.append(int(str(y)+'1'))
allHeights.sort()
minHeight = 10**10
for i in range(1, m+n):
    if (str(allHeights[i])[-1] =='0' and str(allHeights[i-1])[-1] == '1') or (str(allHeights[i])[-1] == '1' and str(allHeights[i-1])[-1]=='0'):
        currentHeight = int(str(allHeights[i])[0:-1])-int(str(allHeights[i-1])[0:-1])
        minHeight = min(currentHeight, minHeight)
print(minHeight)