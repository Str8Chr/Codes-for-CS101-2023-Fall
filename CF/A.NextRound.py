n, k = map(int, input().split())
a = list(map(int, input().split()))
k_th = a[k - 1]
count = 0
for i in a:
    if i >= k_th and i > 0:
        count += 1
print(count)