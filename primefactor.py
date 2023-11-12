# primefactor.py
# 2023/9/5
# version 1.0
# 本程序用于求一个数的所有质因数

import time


def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factor(n, m):
    for i in range(m + 1, n + 1):
        if n % i == 0 and prime(i):
            prmfctr.append(i)
            prime_factor(int(n / i), i)
            break


def times(i, n):
    count = 0
    while n % i == 0:
        count += 1
        n /= i
    return count


while True:
    try:
        n = int(input('请输入一个正整数:'))
    except ValueError:
        break
    start = time.time()
    prmfctr = []
    # 给出n的所有质因数
    prime_factor(n, 1)
    for i in prmfctr:
        print(i, '^', times(i, n), sep='', end='')
        if i != prmfctr[-1]:
            print('*', end='')
    end = time.time()
    print('\n用时', end - start, '秒')
