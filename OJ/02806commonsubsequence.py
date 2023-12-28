while True:
    try: s1, s2 = input().split()
    except EOFError: break
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (s1[i - 1] == s2[j - 1]))
    print(dp[-1][-1])
