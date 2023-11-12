def game(x: list, y: list):
    x0 = y0 = 0
    x1 = y1 = n - 1
    win_x = lose_x = tie = 0
    while x0 <= x1:
        if x[x0] > y[y0]:
            win_x += 1
            x0 += 1
            y0 += 1
        elif x[x1] > y[y1]:
            win_x += 1
            x1 -= 1
            y1 -= 1
        elif x[x0] < y[y1]:
            lose_x += 1
            x0 += 1
            y1 -= 1
        else:
            tie += 1
            x0 += 1
            y1 -= 1
    return win_x, tie, lose_x


while n := int(input()):
    C = sorted(list(map(int, input().split())))
    S = sorted(list(map(int, input().split())))
    print(sum(i * j for i, j in zip((3, 2, 1), game(S, C))),
          sum(i * j for i, j in zip((1, 2, 3), game(C, S))))
