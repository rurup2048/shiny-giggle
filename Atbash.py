note = str(input())
output = ''
for n in note:
    output += chr((91-ord(n))+64)
print(output)