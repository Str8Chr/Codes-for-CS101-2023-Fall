month = [31,28,31,30,31,30,31,31,30,31,30,31]
for _ in range(int(input())):
    m1, d1, n, m2, d2 = map(int, input().split())
    if m1 == m2:
        delta = d2 - d1
    else:
        delta = month[m1 - 1] - d1 + d2
        for i in range(m1 + 1, m2):
            delta += month[i - 1]
    print(n * 2 ** delta)