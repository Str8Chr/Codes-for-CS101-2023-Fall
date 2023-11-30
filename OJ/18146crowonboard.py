def crow_misunderstood():  # misunderstood the problem
    def is_valid_sum(index, m, summ=0, dep=0):
        if dep == m:
            return floor <= summ <= ceil
        for i in range(index, k):
            if is_valid_sum(i + 1, m, summ + nest[i], dep + 1):
                return True
        return False

    n, k = map(int, input().split())
    *nest, = map(int, input().split())
    s = sum(nest)
    if 8 * n < s:
        print('NO')
    else:
        floor = s - 4 * n
        ceil = s / 2
        for i in range(1, k + 1):
            if is_valid_sum(0, i):
                print('YES')
                break
        else:
            print('NO')


from collections import Counter
n, k, *nest = *map(int, input().split()), *map(int, input().split())
fourSeatNeeded, nest = sum(map(lambda x: x // 4, nest)), Counter(map(lambda x: x % 4, nest))
twoSeat, fourSeat, fourSeatNeeded = n * 2, max(0, n - fourSeatNeeded), max(0, fourSeatNeeded - n)
nest[1], nest[2] = nest[1] + nest[3], nest[2] + nest[3] + fourSeatNeeded * 2
nest[2], twoSeat = max(0, nest[2] - fourSeat - twoSeat), max(0, fourSeat + twoSeat - nest[2])
print('YES' if twoSeat + fourSeat >= nest[1] + nest[2] * 2 else 'NO')
