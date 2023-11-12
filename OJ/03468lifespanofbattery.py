def lifespan(x: list):
    if (s := sum(x[:-1])) >= x[-1]:
        return (s + x[-1]) / 2
    else:
        return s


while True:
    try:
        input()
    except EOFError:
        break
    print(f'{lifespan(sorted(list(map(int, input().split())))):.1f}')
