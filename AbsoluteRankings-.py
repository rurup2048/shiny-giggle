n, k = list(map(int,input().split()))
a = list(map(int,input().split()))

s = 0
e = 1
diffs = []
while s != n-1:
    i = a[s]
    j = a[e]
    diffs.append(abs(i-j))
    if e == n-1:
        s += 1
        e = s+1
    else:
        e += 1
diffs.sort()
print(diffs[k-1])