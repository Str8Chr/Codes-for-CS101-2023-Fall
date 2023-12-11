from heapq import heapify, heappop


class Process:
    def __init__(self, c, w):
        self.compute = c
        self.write = w

    def __lt__(self, other):
        return self.write > other.write


ans = current = 0
heap = [Process(*map(int, input().split())) for _ in range(int(input()))]
heapify(heap)
while heap:
    process = heappop(heap)
    current += process.compute
    ans = max(ans, current + process.write)
print(ans)
