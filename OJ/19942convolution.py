def convolution():
    res = [[0] * (n - q + 1) for _ in range(m - p + 1)]
    for i in range(m - p + 1):
        for j in range(n - q + 1):
            for k in range(p):
                for l in range(q):
                    res[i][j] += matrix[i + k][j + l] * kernel[k][l]
    return res


m, n, p, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
kernel = [list(map(int, input().split())) for _ in range(p)]
result = convolution()
for row in result:
    print(*row)
