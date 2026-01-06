'''
4
==
2 11
4 2
2 3
--
2 8
4 2
2 3
--
2 14
4 2
2 3
--
3 1
1 1
1 1
1 1
'''
for i in range(int(input())):
    maxTotal = 0
    minTotal = 0
    n, a  = list(map(int,input().split()))
    maxX = 0
    maxY = 0
    targetHit = False
    for j in range(n):
        w, h = list(map(int,input().split()))
        if w  > maxX:
            minTotal += (w-maxX)*h
            maxX = w
            if h  > maxY:
                maxY = h
        elif h  > maxY:
            minTotal += (h-maxY)*w
            maxY = h
            if w  > maxX:
                maxX = w
        maxTotal += w * h
    # print(maxTotal > a)
    # print(minTotal < a)
    # print(maxTotal)
    # print(minTotal)
    if maxTotal >= a and minTotal < a:
        print('YES')
    else:
        print('NO')
