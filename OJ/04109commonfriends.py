for i in range(int(input())):
    n, m, k = map(int, input().split()); friends = [set() for _ in range(n + 1)]
    for _ in range(m): a, b = map(int, input().split()); friends[a].add(b); friends[b].add(a)
    print("Case %d:" % (i + 1))
    for _ in range(k): a, b = map(int, input().split()); print(len(friends[a] & friends[b]))