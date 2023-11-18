def solve(start, rank):
    if rank == 1:
        matrix[n // 2][n // 2] = start
        return
    if rank == 2:
        matrix[n // 2 - 1][n // 2 - 1] = start
        matrix[n // 2 - 1][n // 2] = start + 1
        matrix[n // 2][n // 2] = start + 2
        matrix[n // 2][n // 2 - 1] = start + 3
        return
    t = (n - rank) // 2
    matrix[t][t:t + rank] = [start + i for i in range(rank)]
    matrix[n - t - 1][t:t + rank] = [start - 3 - i + 3 * rank for i in range(rank)]
    for r in range(t + 1, n - t - 1):
        matrix[r][t] = start + 4 * rank - 5 - r + t + 1
        matrix[r][t + rank - 1] = start + rank + r - t - 1
    solve(start + 4 * rank - 4, rank - 2)


n = int(input())
matrix = [[0] * n for _ in range(n)]
solve(1, n)
for row in matrix:
    print(*row)