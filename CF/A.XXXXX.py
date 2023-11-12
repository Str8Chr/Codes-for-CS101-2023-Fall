for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) % x != 0:
        print(n)
        continue
    for i in range((n + 1) // 2):
        if a[i] % x != 0 or a[n - i - 1] % x != 0:
            print(n - i - 1)
            break
    else:
        print(-1)
