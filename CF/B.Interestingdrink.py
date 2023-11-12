import bisect
n = int(input())
*prices, = map(int, input().split())
prices.sort()
q = int(input())
budgets = [int(input()) for _ in range(q)]
for budget in budgets:
    print(bisect.bisect_right(prices, budget))