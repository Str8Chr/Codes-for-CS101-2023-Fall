from functools import reduce
for _ in range(int(input())):
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n // 2 - abs(i - n // 2)):
            rotate = map(ord, (matrix[i][j], matrix[j][n - i - 1],matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i]))
            result = reduce(lambda x, y: (x[0] + y, max(x[1], y)), rotate, (0, 0))
            cnt += result[1] * 4 - result[0]
    print(cnt)