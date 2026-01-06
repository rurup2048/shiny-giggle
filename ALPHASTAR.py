n = int(input())
word = input()
output = []
for i in range(n):
    for j in range(i+1,n+1):
        temp = word[i:j]
        print(temp)
        if temp[0]< temp[-1]:
            output.append(temp)
print(len(output))