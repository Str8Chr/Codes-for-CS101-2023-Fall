from math import factorial
a, b, k, n, m = map(int, input().split())
mod = 10007
print(int(pow(a, n, mod) * pow(b, m, mod) % mod * factorial(k) // factorial(n) // factorial(m) % mod))
