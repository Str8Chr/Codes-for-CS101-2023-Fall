import heapq as hq


class Node:
    def __init__(self, value, weight):
        self.value, self.weight, self.child, self.code = value, int(weight), None, ''

    def __lt__(self, other): return (self.weight, self.value) < (other.weight, other.value)

    def get_code(self):
        codes[self.value] = self.code
        if self.child is None: return
        for index, child in enumerate(self.child): child.code = self.code + str(index); child.get_code()


heap, tree, codes = [], [], dict()
for _ in range(int(input())): hq.heappush(heap, Node(*input().split()))
while len(heap) > 1:
    tree.extend([hq.heappop(heap), hq.heappop(heap)])
    parent = Node(tree[-2].value + tree[-1].value, tree[-2].weight + tree[-1].weight)
    parent.child = tree[-2:]; hq.heappush(heap, parent)
hq.heappop(heap).get_code()
while True:
    try: string, res = input(), ''
    except EOFError: break
    if string.isdigit():
        while string:
            for node in tree:
                if string.startswith(node.code):
                    string = string[len(node.code):]; res += node.value; break
    else:
        for char in string: res += codes[char]
    print(res)
