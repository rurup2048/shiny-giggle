def overlap_finder(first: tuple[int, int], second: tuple[int, int], dupe: list[int]) -> tuple[float, float]:
    if first == second:
        dupe[0] += 1
        return (0.0, -1.0)
    if second[1] >= first[1]:
        return (0.0, -1.0)
    else:
        diff = (second[0] - first[0]) / (first[1] - second[1])
    time_at_intersection = (diff * first[1]) + first[0]

    return (diff, time_at_intersection)

def main():
    n = int(input())
    duplicates = 0
    dupe = [0]
    horse = []

    positions = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    for i in range(n):
        horse.append((positions[i], speeds[i]))
    horse.sort()
    horsey_speed_time = []
    for i in range(n):
        for j in range(i + 1, n):
            check = overlap_finder(horse[i], horse[j], dupe)
            if check != (0.0, -1.0):
                horsey_speed_time.append(check)
    freq = {}

    for item in horsey_speed_time:
        freq[item] = freq.get(item, 0) + 1

    if freq: 
        duplicates = max(freq.values())
    total_count = duplicates + dupe[0]
    val = max(1, total_count)

    print(val)

if __name__ == "__main__":
    main()