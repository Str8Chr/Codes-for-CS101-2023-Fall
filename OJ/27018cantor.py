def update(index: int, delta: int) -> None:
    while index <= n:
        bit_tree[index] += delta
        index += index & -index


def query(index: int) -> int:
    ans = 0
    while index:
        ans += bit_tree[index]
        index -= index & -index
    return ans


n = int(input())
permutation = tuple(map(int, input().split()))
factorial = [1] * (n + 1)
bit_tree = [0] * (n + 1)
res = 1
for i in range(1, n + 1):
    factorial[i] = factorial[i - 1] * i % 998244353
for i in range(n):
    res += factorial[n - i - 1] * \
           (permutation[i] - query(permutation[i]) - 1) % 998244353
    update(permutation[i], 1)
print(res % 998244353)
