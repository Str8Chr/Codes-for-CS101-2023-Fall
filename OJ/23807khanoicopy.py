from functools import lru_cache
@lru_cache(maxsize=None)
def cal(k, n): return 2 ** n - 1 if k == 3 or n <= 2 else min(2 * cal(k, x) + cal(k - 1, n - x) for x in range(1, n))
print(cal(*map(int, input().split())))