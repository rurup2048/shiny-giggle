bl = []
br = []
ul = []
ur = []

for i in range(int(input())):
    a, b, x, y = list(map(int,input().split()))
    bl.append([a,b])
    ur.append([x,y])
    ul.append([a,y])
    br.append([x,b])


    