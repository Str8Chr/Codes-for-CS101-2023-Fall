from functools import lru_cache


def overlap(DNA1, DNA2):
    for i in range(len(DNA1) + 1):
        if DNA2.startswith(DNA1[i:]): return len(DNA1) - i


for _ in range(int(input())):
    @lru_cache(maxsize=None)
    def dp(mask, last):
        # mask: bit mask of DNAs used; last: index of last DNA used
        if mask == 0: return lengths[last]
        return min(dp(mask ^ (1 << i), i) + lengths[last] - overlaps[i][last]
                   for i in range(n) if valid[i] and mask & (1 << i))
    n = int(input()); DNAs = tuple(input() for _ in range(n))
    lengths, valid, overlaps = [len(DNA) for DNA in DNAs], [True] * n, [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if DNAs[i] in DNAs[j] and valid[j] and i != j: valid[i] = False; break
    for i in range(n):
        if valid[i]:
            for j in range(n):
                if valid[j] and i != j: overlaps[i][j] = overlap(DNAs[i], DNAs[j])
    all_considered = sum(1 << i for i in range(n) if valid[i])
    print(min(dp(all_considered ^ (1 << i), i) for i in range(n) if valid[i]))
