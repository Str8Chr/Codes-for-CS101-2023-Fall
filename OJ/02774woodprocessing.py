def max_length():
    left, right = 1, max(logs)
    while left <= right:
        mid = (left + right) // 2
        pieces = sum(log // mid for log in logs)
        if pieces >= k: left = mid + 1
        else: right = mid - 1
    return right


n, k = map(int, input().split())
logs = [int(input()) for _ in range(n)]
print(max_length())
