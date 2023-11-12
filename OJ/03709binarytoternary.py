def ternary(x):
    if x == 0:
        return 0
    return x % 3 + 10 * ternary(x // 3)


def to_binary(x):
    if x == 0:
        return 0
    return x % 10 + 2 * to_binary(x // 10)


for _ in range(int(input())):
    print(ternary(to_binary(int(input()))))
