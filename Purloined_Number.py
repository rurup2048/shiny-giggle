n = int(input())
x = input().split()
x.sort()
end = -1
if not int(x[0]) in [1,2]:
    print(str(end))
else:
    for i in range(1,n+1):
        if i != int(x[i-1]):
            end = i
            break
    print(str(end))