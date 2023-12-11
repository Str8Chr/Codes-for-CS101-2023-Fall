def prime_list(x):
    prime = [True] * (x + 1)
    for i in range(2, x):
        if prime[i]:
            for j in range(2, x // i + 1):
                prime[j * i] = False
    return prime


m, n = map(int, input().split())
grades = [list(map(int, input().split())) for _ in range(m)]
prime = prime_list(int(max(max(i) for i in grades) ** 0.5))
for i in grades:
    a = (sum(map(
        lambda x: x * (int(x ** 0.5) == x ** 0.5 and prime[int(x ** 0.5)]), i))
         / len(i))
    print(0 if a == 0 else f'{a:.2f}')
