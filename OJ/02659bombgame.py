from collections import defaultdict


a, b, k = map(int, input().split())
bombs = [tuple(map(int, input().split())) for _ in range(k)]
possible = defaultdict(lambda: 0)
impossible = []
cnt = 0
for r, s, p, t in bombs:
    radius = p // 2
    bombing_range = ((nr, ns)
                     for dr in range(-radius, radius + 1) for ds in range(-radius, radius + 1)
                     if 1 <= (nr := r + dr) <= a and 1 <= (ns := s + ds) <= b)
    if t:
        for nr, ns in bombing_range:
            if possible[(nr, ns)] == cnt:
                possible[(nr, ns)] += 1
        cnt += 1
    else:
        for nr, ns in bombing_range:
            impossible.append((nr, ns))
for nr, ns in impossible:
    possible.pop((nr, ns), None)
print(list(possible.values()).count(cnt))