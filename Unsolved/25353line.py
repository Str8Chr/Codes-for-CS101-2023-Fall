# 有 N 名同学从左到右排成一排，第 i 名同学的身高为 hi。现在张老师想改变排队的顺序，他能进行任意多次（包括0次）如下操作：
# 如果两名同学相邻，并且他们的身高之差不超过 D，那么老师就能交换他俩的顺序。
# 请你帮张老师算一算，通过以上操作，字典序最小的所有同学（从左到右）身高序列是什么？
# 输入
# 第一行包含两个正整数 N, D (1<=N<=105, 1<=D<=109)。
# 接下去 N 行，每行一个正整数 hi (1<=hi<=109) 表示从左到右每名同学的身高。
# 输出
# 输出 N 行，第 i 行表示答案中第 i 名同学的身高。


global n, d, situations


def is_neighbor(situation1, situation2):  # 判断两个排列是否相邻
    if situation1 == situation2:
        return True
    diff = [abs(situation1[i] - situation2[i]) for i in range(n)]
    if diff.count(0) != 2:
        return False
    for i in range(n - 1):
        if diff[i] > d:
            return False
    return True


def get_neighbors(situation):  # 获取相邻的排列
    neighbors = []
    for i in range(n - 1):
        if abs(situation[i] - situation[i + 1]) <= d:
            neighbor = situation.copy()
            neighbor[i], neighbor[i + 1] = neighbor[i + 1], neighbor[i]
            if all(
                not is_neighbor(situations[i],neighbor) for i in range(len(situations))):
                neighbors.append(neighbor)
                situations.append(neighbor)
    return neighbors


def get_situations(situation):  # 通过递归获取所有排列
    neighbors = get_neighbors(situation)
    for neighbor in neighbors:
        get_situations(neighbor)


n, d = map(int, input().split())
h = [int(input()) for i in range(n)]
situations = [h]
get_situations(h)
situations.sort()
print('\n'.join(map(str, situations[0])))

# Time Limit Exceeded
# How to improve?
# 1. 通过递归获取所有排列的方法太慢了，可以考虑使用动态规划
# 如何使用动态规划？
