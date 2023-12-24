k, n = map(int, input().split());
for _ in range(k): x, y = map(int, input().split()); layer = min(x, y, n + 1 - x, n + 1 - y); outside = 4 * (layer - 1) * (n - layer + 1); print(outside + y - layer + 1 if x == layer else outside + n + x - 3 * layer + 2 if y == n + 1 - layer else outside + 3 * n - y - 5 * layer + 4 if x == n + 1 - layer else outside + 4 * n - x - 7 * layer + 5)
