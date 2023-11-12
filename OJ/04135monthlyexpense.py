n, m = map(int, input().split())
expense = [int(input()) for _ in range(n)]
l, r = max(expense), sum(expense)
while l < r:
    mid = (l + r) // 2
    cnt, tmp = 1, 0
    for i in expense:
        if tmp + i > mid:
            cnt += 1
            tmp = i
        else:
            tmp += i
    if cnt > m:
        l = mid + 1
    else:
        r = mid
print(l)