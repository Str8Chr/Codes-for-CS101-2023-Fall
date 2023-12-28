def hanoi(n, k):
    if k == 3 or n <= 2: print(2 ** n - 1); return
    t = ans = comb = 1
    while comb * (k - 2 + t) // t < n:
        ans, comb, t = ans + 2 ** t * (comb * (k - 2 + t) // t - comb), comb * (k - 2 + t) // t, t + 1
    print(ans + 2 ** t * (n - comb))


for n in range(1, 13):
    hanoi(n, 4)

print(*[1, 3, 5, 9, 13, 17, 25, 33, 41, 49, 65, 81], sep='\n')
