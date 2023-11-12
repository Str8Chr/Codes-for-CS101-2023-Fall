n = int(input())
coins = sorted(map(int, input().split()), reverse=True)
s = 0
t = sum(coins) / 2
for i in range(n):
    s += coins[i]
    if s > t:
        print(i + 1)
        break
