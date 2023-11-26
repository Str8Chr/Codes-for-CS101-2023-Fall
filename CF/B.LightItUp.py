n, m = map(int, input().split())
a = [0] + list(map(int, input().split())) + [m]
light = [0] * (n + 2)
for i in range(1, n + 2):
    light[i] = light[i - 1] + (1 - (-1) ** i) * (a[i] - a[i - 1]) // 2
ans = light[n + 1]
for i in range(1, n + 2):
    if a[i] - a[i - 1] > 1:
        ans = max(ans, light[i - 1] + m - light[n + 1] + light[i] - a[i - 1] - 1)
print(ans)
