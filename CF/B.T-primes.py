def euler(x):
    is_prime = [True] * (x + 1)
    is_prime[1] = False
    primes = []
    for i in range(2, x + 1):
        if is_prime[i]:
            primes.append(i)
        for j in primes:
            if i * j > x:
                break
            is_prime[i * j] = False
            if i % j == 0:
                break
    return is_prime


input()
*nums, = map(int, input().split())
max_num = max(nums)
is_prime = euler(int(max_num ** 0.5) + 1)
for num in nums:
    if (sq := num ** 0.5) == int(sq) and is_prime[int(sq)]:
        print('YES')
    else:
        print('NO')
