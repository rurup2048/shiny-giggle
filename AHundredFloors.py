n = int(input())
total = 0 
pos = 0
while total < n:
    pos += 1
    total = 0
    for j in range(1,pos+2):
        total += j//2
print(pos)