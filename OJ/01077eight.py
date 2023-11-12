from collections import defaultdict
swap = {'u': -3, 'd': 3, 'l': -1, 'r': 1}


def is_solvable(l: int):
    l = [int(x) for x in str(l)]
    l.remove(0)
    inversions = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if l[i] > l[j]:
                inversions += 1
    return inversions % 2 ^ 1


def print_steps(q: list, pointer: int):
    if pointer:
        return print_steps(q, q[pointer][2]) + q[pointer][3]
    else:
        return q[pointer][3]


def is_swapable(x_prev: int, x_next: int):
    return 0 <= x_next <= 8 and\
        x_prev % 3 - x_next % 3 in range(-1, 2)


def swap_digit(l: int, x_prev: int, x_next: int):
    x_prev, x_next = 8 - x_prev, 8 - x_next
    return l - int(l / 10 ** x_next) % 10 * 10 ** x_next +\
        int(l / 10 ** x_next) % 10 * 10 ** x_prev


def bfs(x):
    pointer = 0
    direction = ''
    queue = [(x, l, pointer, direction)]
    reached = defaultdict(bool)
    reached[l] = True
    while True:
        x_prev, l_prev, p_prev, d_prev = queue[pointer]
        if l_prev == 123456780:
            return print_steps(queue, p_prev) + d_prev
        for d in 'udlr':
            x_next = x_prev + swap[d]
            if is_swapable(x_prev, x_next):
                l_next = swap_digit(l_prev, x_prev, x_next)
                if not reached[l_next]:
                    reached[l_next] = True
                    queue.append((x_next, l_next, pointer, d))
        pointer += 1


l_raw = input().split()
i = l_raw.index('x')
l_raw[i] = '0'
l = int(''.join(l_raw))
if is_solvable(l):
    print(bfs(i))
else:
    print('unsolvable')
