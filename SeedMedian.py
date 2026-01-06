endList = []
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        endList.append(i*j)

endList.sort()
pos = len(endList)//2
print(endList[pos])