# 将正整数n 表示成一系列正整数之和，n=n1+n2+…+nk, 其中n1>=n2>=…>=nk>=1 ，k>=1 。
# 正整数n 的这种表示称为正整数n 的划分。


# def seg(n, k):  # N划分成K个正整数之和的划分数目
#     if k == 1:
#         return 1
#     if n < k:
#         return 0
#     if n == k:
#         return 1
#     return seg(n - 1, k - 1) + seg(n - k, k)
#
#
# def seg2(n, k):  # N划分成若干个不同正整数之和的划分数目
#     if n == 1:
#         return 1
#     if k == 1:
#         return 0
#     if n < k:
#         return seg2(n, n)
#     if n == k:
#         return 1 + seg2(n, n - 1)
#     return seg2(n - k, k - 1) + seg2(n, k - 1)
#
#
# def seg3(n, k):  # N划分成若干个奇正整数之和的划分数目
#     if k % 2 == 0:
#         return seg3(n, k - 1)
#     if n < k:
#         return seg3(n, n)
#     if k == 1:
#         return 1
#     if n == k:
#         return 1 + seg3(n, n - 2)
#     return seg3(n - k, k) + seg3(n, k - 2)
#
#
# while True:
#     try:
#         n, k = map(int, input().split())
#         print(seg(n, k))
#         print(seg2(n, n))
#         print(seg3(n, n), end='')
#     except BaseException:
#         break

# Time Limit Exceeded
# 递归的时间复杂度太高了，需要用动态规划来解决

# 动态规划

def seg(n, k):  # N划分成K个正整数之和的划分数目
    if n < k:
        return 0
    if n == k:
        return 1
    dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = 1
    for i in range(2, n + 1):
        for j in range(2, min(i + 1, k + 1)):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    return dp[n][k]


def seg_diff(n, k):  # N划分成若干个不同正整数之和的划分数目
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    for j in range(1, k + 1):
        dp[1][j] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            if i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = 1 + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - j][j - 1] + dp[i][j - 1]
    return dp[n][k]


def seg_odd(n, k):  # N划分成若干个奇正整数之和的划分数目
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = 1
    for j in range(1, k + 1):
        dp[1][j] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            if j % 2 == 0:
                dp[i][j] = dp[i][j - 1]
            elif i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = 1 + dp[i][j - 2]
            else:
                dp[i][j] = dp[i - j][j] + dp[i][j - 2]
    return dp[n][k]


while True:
    try:
        n, k = map(int, input().split())
        print(seg(n, k))
        print(seg_diff(n, n))
        print(seg_odd(n, n))
    except:
        break
