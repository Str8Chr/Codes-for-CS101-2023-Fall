for _ in range(int(input())):
    n = int(input())
    altitudes = list(map(int, input().split()))
    altitudes.sort()
    l, r = (n - 2) // 2, (n - 1) // 2
    while l >= 0 and r < n - 1:
        if altitudes[l] != altitudes[l + 1]:
            print((n - l - 1) * (l + 1))
            break
        if altitudes[r] != altitudes[r + 1]:
            print((n - r - 1) * (r + 1))
            break
        l -= 1
        r += 1
    else:
        print(n // 2)