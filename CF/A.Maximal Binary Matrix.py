def put_ones_in(k, l):  # k is the number of ones, l is the length of the matrix
    if k == 0:
        return
    elif k >= 2 * l - 1:
        for i in range(l):
            matrix[n - l][n - l + i] = matrix[n - l + i][n - l] = 1
        put_ones_in(k - 2 * l + 1, l - 1)
    elif k % 2 == 0:
        for i in range(k // 2):
            matrix[n - l][n - l + i] = matrix[n - l + i][n - l] = 1
        matrix[n - l + 1][n - l + 1] = 1
    else:
        for i in range((k + 1) // 2):
            matrix[n - l][n - l + i] = matrix[n - l + i][n - l] = 1


n, k = map(int, input().split())
if k > n * n:
    print(-1)
    exit()
matrix = [[0] * n for _ in range(n)]
put_ones_in(k, n)
for row in matrix:
    print(*row)