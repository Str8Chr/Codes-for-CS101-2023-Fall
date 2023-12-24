k, n = map(int, input().split())
if k == 3 or n <= 2: print(2 ** n - 1); exit()
t = ans = comb = 1
while comb * (k - 2 + t) // t < n:
    ans, comb, t = ans + 2 ** t * (comb * (k - 2 + t) // t - comb), comb * (k - 2 + t) // t, t + 1
print(ans + 2 ** t * (n - comb))
