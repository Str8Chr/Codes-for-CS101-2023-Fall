m, n = map(int, input().split())
woods = ([[1] * (n + 2)] +
         [[1] + list(map(int, input().split())) + [1] for _ in range(m)] +
         [[1] * (n + 2)])
heights = [0] * (n + 2)
ans = 0
for i in range(1, m + 1):
    stack = [0]
    for j in range(1, n + 2):
        heights[j] = (heights[j] + (woods[i][j] ^ 1)) * (woods[i][j] ^ 1)
        while len(stack) > 1 and heights[stack[-1]] > heights[j]:
            ans = max(ans, heights[stack.pop()] * (j - stack[-1] - 1))
        stack.append(j)
print(ans)
