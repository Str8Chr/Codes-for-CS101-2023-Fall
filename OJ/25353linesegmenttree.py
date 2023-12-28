"""
翻不过去的大山，永远都翻不过去
应该先让大山自己排队
"""


# 使用class写一棵线段树
class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.lson = None
        self.rson = None


class SegmentTree:
    def __init__(self, start, end):
        self.root = SegmentTreeNode(start, end, 0)
        self.start = start
        self.end = end

    # 返回修改后的节点的对象。注意对象是浅拷贝，里面存储了一些指针。
    # 改变了子对象的指针之后，需要重新赋值给父对象，不然子对象的子对象就会被释放
    def modify(self, node, pos, value, start=None, end=None):
        if (start is None):
            start, end = self.start, self.end
        if (node is None):
            node = SegmentTreeNode(start, end, value)
        if (start == end):
            node.val = max(node.val, value)
            return node
        mid = (node.start + node.end) // 2
        if pos <= mid:
            node.lson = self.modify(node.lson, pos, value, start, mid)
        else:
            node.rson = self.modify(node.rson, pos, value, mid + 1, end)
        node.val = max(node.val, value)
        return node

    def query(self, node, qstart, qend):
        if ((node is None) or qstart > node.end or qend < node.start):
            return 0
        if (qstart <= node.start and node.end <= qend):
            return node.val
        ret = max(self.query(node.lson, qstart, qend), self.query(node.rson, qstart, qend))
        return ret


N, D = map(int, input().split())
h = [int(input()) for _ in range(N)]
# 求出每个点的层数，用一个线段树维护值域上的层数，这样就可以求出挡在前面的大山的最大的层数了
MAXH = max(h)
layers = SegmentTree(1, MAXH)
members = [[]]  # 存储每一层里面的元素
for hi in h:
    current_layer = max(layers.query(layers.root, 1, hi - D - 1), layers.query(layers.root, hi + D + 1, MAXH)) + 1
    if (current_layer >= len(members)):
        members.append([])
    members[current_layer].append(hi)
    layers.modify(layers.root, hi, current_layer)

# 直接一层层排序、输出即可
for layer in members:
    for _ in sorted(layer):
        print(_)
