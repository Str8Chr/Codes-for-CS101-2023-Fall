def search(ordinate, r, n):
    for i in range(n - 1, -1, -1):
        if ordinates[i] - ordinate <= r:
            return i


while True:
    r, n = map(int, input().split())
    if r == n == -1:
        break
    ordinates = list(map(int, input().split()))
    ordinates.sort()
    count = 0
    i = 0
    while i < n:
        count += 1
        j = search(ordinates[i], r, n)
        i = search(ordinates[j], r, n) + 1
    print(count)
