import math


def IsPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
if n < 6 or n % 2 == 1:
    print('Error!')
else:
    results = []
    for i in range(3, n // 2 + 1, 2):
        if IsPrime(i) and IsPrime(n - i):
            results.append((i, n - i))
    for result in results:
        print(f'{n}={result[0]}+{result[1]}')
