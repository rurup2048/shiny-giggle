n, m = map(int, input().split())
 
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
 
max_sum = 0

for c1 in range(m):
    for c2 in range(c1 + 1, m):
        first_max = -float('inf')
        second_max = -float('inf')
 
        for r in range(n):
            pair_sum = grid[r][c1] + grid[r][c2]
            if pair_sum > first_max:
                second_max = first_max
                first_max = pair_sum
            elif pair_sum > second_max:
                second_max = pair_sum
 
        if second_max > -float('inf'):
            max_sum = max(max_sum, first_max + second_max)
 
print(max_sum)

