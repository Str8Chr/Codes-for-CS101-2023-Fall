from collections import defaultdict
import bisect

N,D = map(int,input().split())
info = []
for i in range(N):
    info.append(int(input()))
heights = sorted(list(set(info)))
#高度离散化。
#注意这里用set是因为我们每次只存储当前高度所对应（可能多个）点的层数最大值
ass = {}
l = len(heights)
for i in range(l):
    ass[heights[i]] = i #只是为了方便找到高度h排第几个

tree_l = [-1] * l
tree_r = [-1] * l
#两个树状数组，分别记录从小到大和从大到小第i高的高度点所对应的层数
#这里用了变形的树状数组，不是来处理区间和而是来处理区间最大值
#这种树状数组的有效性依赖于每次修改都会把数改大，否则修改操作需要(logn)^2复杂度
ans = defaultdict(list) #存储分层结果：每层有哪些高度


def low_bit(x):
    return x & (-x)


def update_l(x,y):
    while x <= l:
        tree_l[x-1] = max(y,tree_l[x-1])
        x += low_bit(x)


def update_r(x,y):
    while x <= l:
        tree_r[x-1] = max(y,tree_r[x-1])
        x += low_bit(x)


def get_max_l(x):
    res = -1
    while x:
        res = max(res,tree_l[x-1])
        x -= low_bit(x)
    return res


def get_max_r(x):
    res = -1
    while x:
        res = max(res,tree_r[x-1])
        x -= low_bit(x)
    return res


for h in info: #按照输入的顺序（即队伍顺序）扫描
    index = ass[h]
    left = bisect.bisect_right(heights,h-D-1)
    right = l - bisect.bisect_left(heights,h+D+1)
    storey = 1 + max(get_max_l(left),get_max_r(right))
    #递推关系。分别找到小于h-D与大于h+D的高度所对应层数的最大值
    update_l(index+1,storey)
    update_r(l-index,storey)
    #更新高度h对应的点的层数最大值
    ans[storey].append(h) #加入结果中

for storey in sorted(ans.keys()):
    for h in sorted(ans[storey]):
        print(h)

