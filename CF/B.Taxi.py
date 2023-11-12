from collections import Counter, defaultdict


input()
groups = Counter(map(int, input().split()))
groups = defaultdict(lambda: 0, groups)
ans = groups[4] + groups[3] + (groups[2] + 1) // 2
volume = ans * 4 - groups[4] * 4 - groups[3] * 3 - groups[2] * 2
if (x := (groups[1] - volume + 3) // 4) > 0:
    ans += x
print(ans)