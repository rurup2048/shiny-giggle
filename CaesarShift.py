abcs = list('abcdefghijklmnopqrstuvwxyz')
output = ''
text = input()
shift = int(input())
for i in text:
    output += abcs[(abcs.index(i)+shift)%26]
print(output)