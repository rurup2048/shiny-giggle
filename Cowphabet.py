'''
[('A', 'B', 'C'), 
 ('A', 'C', 'B'), 
 ('B', 'A', 'C'), 
 ('B', 'C', 'A'), 
 ('C', 'A', 'B'), 
 ('C', 'B', 'A')]'''
output = ''
abcs = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
from itertools import permutations
n, k = list(map(int,input().split()))
temp = list(permutations(abcs[:n]))
for i in temp[k-1]:
    output += i
print(output.strip())