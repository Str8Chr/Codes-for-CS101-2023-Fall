case = 0
while case := case + 1:
    n, d = map(int, input().split())
    if n == d == 0: break
    intervals = [(x - (d ** 2 - y ** 2) ** 0.5, x + (d ** 2 - y ** 2) ** 0.5) for x, y
                 in (tuple(map(int, input().split())) for _ in range(n)) if y <= d]
    input()
    if len(intervals) < n or d < 0: print('Case {}: -1'.format(case)); continue
    intervals.sort()
    ans, prev = 0, float('-inf')
    for start, end in intervals:
        if end < prev: prev = end
        elif start > prev: ans, prev = ans + 1, end
    print('Case {}: {}'.format(case, ans))
