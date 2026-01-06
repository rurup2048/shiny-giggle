numCows = input()
m = input().strip().split()
m.sort()
n = input().strip().split()
n.sort()
if len(m) > len(n):
    m, n = n, m
pos = 0
smallest = 10**9+1
for g in m:
    searchList = n
    while len(searchList) != 1:
        pos = int(len(searchList)/2)
        if int(g) - pos > 0:
            searchList = searchList[0:pos-1]
        else:
            searchList = searchList[pos:-1]
    amount = abs(int(g) - int(n[pos]))
    if amount < smallest:
        smallest = amount
print(smallest)
# 3 4
# 3030 9 100
# 7000 60 401 1000000000
            
# smallest = 10**9+1
# for g in m:
#     if int(g) + n[-1] > 10**9:
#             pass
#     for h in n:
#         amount = abs(int(g) - int(h))
#         if amount < smallest:
#             smallest = amount
# print(str(smallest))