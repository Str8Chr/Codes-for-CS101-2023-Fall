while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    circle = [i for i in range(1, n + 1)]
    start = 0
    while len(circle) > 1:
        start = (start + m - 1) % len(circle)
        circle.remove(circle[start])
    print(circle[0])