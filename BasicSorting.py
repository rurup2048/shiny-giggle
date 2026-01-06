n = int(input())
ls = list(map(int,input().split()))
ls.sort()
output = ''
for i in ls:
    output += str(i)+' '
print(output.strip())