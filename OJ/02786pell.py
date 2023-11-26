from functools import lru_cache
from sys import setrecursionlimit, stdout
setrecursionlimit(1000000)


def solution():
    @lru_cache(maxsize=None)
    def pell(n):
        return n if n <= 2 else (2 * pell(n - 1) % 32767 + pell(n - 2) % 32767) % 32767
    for _ in range(int(input())):
        print(pell(int(input()) % 150))


@lru_cache(maxsize=None)
def pell(n):
    return n if n <= 2 else (2 * pell(n - 1) + pell(n - 2))


def pell_cycle():
    for i in range(3, int(input('Largest Mod: ')) + 1):
        j = 4
        while pell(j) % i != 2 or pell(j - 1) % i != 1:
            j += 1
        stdout.write(f'Mod: {i}, Cycle: {j - 2}\n')


def pell_cycle_bin():
    for i in range(2, int(input('Largest Mod Bin: ')) + 1):
        i = 2 ** i - 1
        j = 4
        while pell(j) % i != 2 or pell(j - 1) % i != 1:
            j += 1
        print(f'Mod: {i}, Cycle: {j - 2}')


def pell_list():
    m = int(input('Mod: '))
    for i in range(1, int(input('Num: ')) + 1):
        print(f'a{i} = {pell(i) % m}')


solution()
