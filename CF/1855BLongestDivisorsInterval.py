# Given a positive integer n, find the maximum size of an interval [l,r]
# of positive integers such that, for every i in the interval (i.e., l≤i≤r),
# n is a multiple of i.
# Given two integers l≤r, the size of the interval [l,r]is r−l+1
# (i.e., it coincides with the number of integers belonging to the interval).
# Input
# The first line contains a single integer t (1≤t≤104) — the number of test cases.
# The only line of the description of each test case contains one integer n (1≤n≤1018).
# Output
# For each test case, print a single integer: the maximum size of a valid interval.


n = int(input())
for i in range(n):
    x = int(input())
    cnt = 0
    ans = 1
    for j in range(1, 50):
        if x % j == 0:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    print(ans)
# 循环中i 的范围限制到50
