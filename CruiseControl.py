n, d = list(map(int,input().split()))
minNum = d
spdList = []
for i in range(n):
    f, s = list(map(int,input().split()))
    temp = (d-f)/s
    spdList.append(s)
    if temp < minNum:
        minNum = temp
print(8/3)
minNum = d/max(spdList)
x = 20
if len(str(minNum)) > x:
    print(str(minNum)[:x])
else:
    print(minNum)
