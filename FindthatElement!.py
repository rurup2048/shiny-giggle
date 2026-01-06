n, q = list(map(int,input().split()))
lst = list(map(int,input().split()))
for i in range(q):
    temp = int(input())
    print(lst.index(temp)+1)