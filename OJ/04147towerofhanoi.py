# using recursion to solve the problem of tower of hanoi


def hanoi(n, a, b, c):
    if n == 1:
        print(f'1:{a}->{c}')
    else:
        hanoi(n-1, a, c, b)
        print(f'{n}:{a}->{c}')
        hanoi(n-1, b, a, c)


hanoi(*map(lambda x: x[1] if x[0] else int(x[1]), enumerate(input().split())))
