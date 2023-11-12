n = int(input())
h = list(map(int, input().split()))
left = [0] * n
right = [0] * n
for i in range(1, n):
    left[i] = max(left[i - 1], h[i - 1])
for i in range(n - 2, -1, -1):
    right[i] = max(right[i + 1], h[i + 1])
ans = 0
for i in range(n):
    ans += max(0, min(left[i], right[i]) - h[i])
print(ans)
