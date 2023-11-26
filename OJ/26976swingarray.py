n, *a = int(input()), *map(int, input().split())
b = [a[i + 1] - a[i] for i in range(n - 1)]
res = 1 + (b[0] != 0)
for i in range(1, n - 1):
    if b[i] * b[i - 1] < 0:
        res += 1
    else:
        b[i] += b[i - 1]
print(res)
