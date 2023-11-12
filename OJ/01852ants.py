for _ in range(int(input())):
    l, n = map(int, input().split())
    ants = list(map(int, input().split()))
    min_time = max_time = 0
    for ant in ants:
        min_time = max(min_time, min(ant, l - ant))
        max_time = max(max_time, max(ant, l - ant))
    print(min_time, max_time)