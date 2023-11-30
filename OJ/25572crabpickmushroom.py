sides = (((1, 0), (-1, 0)), ((0, 1), (0, -1)))
fronts = ((((0, 1), (1, 1)), ((0, -1), (1, -1))), (((1, 0), (1, 1)), ((-1, 0), (-1, 1))))


def dfs(r, c):
    res = False
    for dr, dc in sides[di]:
        if matrix[r + dr + (dr == 1)][c + dc + (dc == 1)] == 1:
            continue
        if matrix[r + dr + (dr == 1)][c + dc + (dc == 1)] == 9:
            return True
        matrix[r + dr + (dr == 1)][c + dc + (dc == 1)] = 1
        res |= dfs(r + dr, c + dc)
    for front in fronts[di]:
        if any(matrix[r + dr][c + dc] == 1 for dr, dc in front):
            continue
        if (matrix[r + front[0][0]][c + front[0][1]] == 9 or
                matrix[r + front[1][0]][c + front[1][1]] == 9):
            return True
        matrix[r + front[0][0]][c + front[0][1]] = matrix[r + front[1][0]][c + front[1][1]] = 1
        res |= dfs(r + front[0][0], c + front[0][1])
    return res


n = int(input())
matrix = [[1] * (n + 2)] +\
         [[1] + list(map(int, input().split())) + [1] for _ in range(n)] +\
         [[1] * (n + 2)]
crab = (0, 0)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == 5:
            crab = (i, j)
            di = matrix[i][j + 1] == 5
            # direction, 1: right, 0: down
            matrix[i][j] = 1
            matrix[i + (di ^ 1)][j + di] = 1
            break
    else:
        continue
    break
print(('no', 'yes')[dfs(crab[0], crab[1])])
