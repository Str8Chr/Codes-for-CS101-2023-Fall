def get_step(dis):
    cnt = 0
    prev = 0
    for rock in rocks:
        if rock - prev < dis:
            cnt += 1
        else:
            prev = rock
    return cnt


l, n, m = map(int, input().split())
rocks = [int(input()) for _ in range(n)]
rocks.sort()
rocks.append(l)
left = 0
right = l
while left < right:
    mid = (left + right + 1) // 2
    if get_step(mid) <= m:
        left = mid
    else:
        right = mid - 1
print(left)