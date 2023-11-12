n, m = map(int, input().split())
developers = [(int(x), int(y)) for (x, y)
              in (input().split() for _ in range(n))]
valid_ranges = [0] * n  # valid start point for each developer
for i in range(n):
    valid_ranges[i] = (max(0, developers[i][0] - developers[i][1] + 1),
                       min(m - developers[i][1], developers[i][0]),
                       developers[i][1])
min_start = 0
ans = 0
valid_developers = [True] * n
while True:
    min_end = m + 1
    for i in range(n):
        if valid_developers[i]:
            if (x := min_start <= valid_ranges[i][1]) and \
                    max(valid_ranges[i][0], min_start) + developers[i][1] \
                    < min_end:
                    min_end = max(valid_ranges[i][0], min_start) + developers[i][1]
                    current_developer = i
            valid_developers[i] = x
    if min_end == m + 1:
        break
    ans += 1
    min_start = min_end
    valid_developers[current_developer] = False
print(ans)
