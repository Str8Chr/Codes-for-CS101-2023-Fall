l, m = map(int, input().split())
lis = [1] * (l + 1)
for i in range(m):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        lis[j] = 0
print(sum(lis))
