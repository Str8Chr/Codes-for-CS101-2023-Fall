n, m = map(int, input().split())
s = [int(i) for i in input().split()]
s.sort()
delta = []
for i in range(n - 1):
    delta.append(s[i + 1] - s[i])
delta.sort(reverse=True)
print(sum(delta[m - 1:]))
