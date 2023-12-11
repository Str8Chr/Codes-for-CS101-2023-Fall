while n := int(input()):
    hotels, ans, min_cost = sorted([list(map(int, input().split())) for _ in range(n)]), 0, float('inf')
    for i in range(n):
        if hotels[i][1] < min_cost: min_cost = hotels[i][1]; ans += 1
    print(ans)
