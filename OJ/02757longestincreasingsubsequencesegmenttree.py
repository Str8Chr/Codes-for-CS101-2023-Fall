# using segment tree to solve the LIS problem
def update(index: int, value: int) -> None:
    while index <= n:
        tree[index] = max(tree[index], value)
        index += index & -index


def query(index: int) -> int:
    ans = 0
    while index:
        ans = max(ans, tree[index])
        index -= index & -index
    return ans


n = int(input())
*seq, = map(int, input().split())
tree = [0] * (n + 1)
indexSorted = sorted(range(n), key=lambda i: (seq[i], -i))

for i in indexSorted:
    update(i + 1, query(i) + 1)
print(query(n))
