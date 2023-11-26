d = int(input())
n = int(input())
matrix = [[0 for _ in range(1025)] for _ in range(1025)]
for _ in range(n):
    x, y, i = map(int, input().split())
    for r in range(max(0, x-d), min(1025, x+d+1)):
        for c in range(max(0, y-d), min(1025, y+d+1)):
            matrix[r][c] += i
max_value = 0
max_point = 0
for r in range(1025):
    for c in range(1025):
        if matrix[r][c] > max_value:
            max_value = matrix[r][c]
            max_point = 1
        elif matrix[r][c] == max_value:
            max_point += 1
print(max_point, max_value)
