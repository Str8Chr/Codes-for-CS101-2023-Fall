print('NO' if (l := [list(map(int, input().split())) for _ in range(int(input()))]) and any(sum([l[i][j] for i in range(len(l))]) for j in range(3)) else 'YES')
