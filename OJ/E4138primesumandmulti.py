def is_prime(x):
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True


mul = []
for i in range(2, (n := int(input()))//2 + 1):
    if is_prime(i) and is_prime(n - i):
        mul.append(i * (n - i))
print(max(mul))